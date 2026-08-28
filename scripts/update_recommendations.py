#!/usr/bin/env python3
"""
Semantic Model Recommender & Comparative Delta Evaluator (LLM + Web Search Grounding)
Queries OpenRouter models with online web search grounding to analyze the latest
state of AI models, benchmark rankings, and pricing compared to Anthropic tiers,
and performs a non-destructive, minimal-diff update against the active claude-threepio script.
"""

import os
import sys
import json
import re
import urllib.request
from datetime import datetime, timezone

OPENROUTER_MODELS_URL = "https://openrouter.ai/api/v1/models"
OPENROUTER_CHAT_URL = "https://openrouter.ai/api/v1/chat/completions"

def info(msg): print(f"\033[1;34m[INFO]\033[0m {msg}", file=sys.stderr)
def success(msg): print(f"\033[1;32m[SUCCESS]\033[0m {msg}", file=sys.stderr)
def warn(msg): print(f"\033[1;33m[WARN]\033[0m {msg}", file=sys.stderr)
def error(msg): print(f"\033[1;31m[ERROR]\033[0m {msg}", file=sys.stderr)

def get_api_key():
    key = os.environ.get("OPENROUTER_API_KEY")
    if key:
        return key.strip()
    
    env_path = os.path.expanduser("~/.claude-threepio/.env")
    if os.path.exists(env_path):
        try:
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("OPENROUTER_API_KEY="):
                        return line.split("=", 1)[1].strip()
        except Exception:
            pass
    return None

def extract_current_tiers(setup_path="claude-threepio"):
    if not os.path.exists(setup_path):
        return []
    with open(setup_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    tiers = []
    tier_matches = re.finditer(
        r'\{\s*"tier_name":\s*"([^"]+)",\s*"tier_label":\s*"([^"]+)",\s*"claude_name":\s*"([^"]+)",\s*"options":\s*\[(.*?)\](?:,\s*"ollama_options":\s*(ollama_opts\(\[.*?\]\)))?,?\s*\}',
        content,
        re.DOTALL
    )
    for m in tier_matches:
        tname, tlabel, cname, opt_text, ollama_block = m.groups()
        opts = []
        for line in opt_text.strip().split("\n"):
            om = re.search(r'get_model_entry\(catalog,\s*"([^"]+)",\s*"([^"]+)",\s*"([^"]+)",\s*"([^"]+)",\s*(True|False)(?:,\s*is_recommended=(True|False))?\)', line)
            if om:
                opts.append({
                    "id": om.group(1),
                    "name": om.group(2),
                    "price_str": om.group(3),
                    "ctx_str": om.group(4),
                    "supports1m": om.group(5) == "True",
                    "is_recommended": om.group(6) == "True" if om.group(6) else False
                })
        tiers.append({
            "tier_name": tname,
            "tier_label": tlabel,
            "claude_name": cname,
            "options": opts,
            "ollama_block": ollama_block
        })
    return tiers

def fetch_openrouter_catalog():
    info("Fetching full model catalog from OpenRouter API...")
    req = urllib.request.Request(
        OPENROUTER_MODELS_URL,
        headers={"User-Agent": "Claude-OpenRouter-Recommender/1.2.0"}
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode()).get("data", [])
            success(f"Retrieved {len(data)} total models from OpenRouter.")
            return data
    except Exception as e:
        error(f"Failed to fetch OpenRouter catalog: {e}")
        return []

def build_compact_catalog(models):
    catalog_map = {}
    compact_list = []
    for m in models:
        mid = m.get("id", "")
        p_in = float(m.get("pricing", {}).get("prompt", 0)) * 1_000_000
        p_out = float(m.get("pricing", {}).get("completion", 0)) * 1_000_000
        ctx = int(m.get("context_length", 0))
        name = m.get("name", mid)
        desc = m.get("description", "")[:160]

        if p_in == 0 and p_out == 0 and "free" not in mid:
            continue

        entry = {
            "id": mid,
            "name": name,
            "p_in": p_in,
            "p_out": p_out,
            "price_str": f"${p_in:.2f}/${p_out:.2f}",
            "ctx": ctx,
            "ctx_str": f"{ctx // 1_000_000}M Context" if ctx >= 1_000_000 else f"{ctx // 1_000}k Context",
            "supports1m": ctx >= 900_000,
            "desc": desc
        }
        catalog_map[mid] = entry
        compact_list.append({
            "id": mid,
            "name": name,
            "price_in_1m": round(p_in, 2),
            "price_out_1m": round(p_out, 2),
            "context_k": ctx // 1000,
            "desc": desc
        })
    return catalog_map, compact_list

def perform_llm_comparative_analysis(api_key, current_tiers, catalog_map, compact_catalog, today_str):
    info("Querying LLM agent with online web search plugin for comparative delta evaluation...")

    preferred_candidates = [
        "perplexity/sonar-pro-search",
        "perplexity/sonar",
        "openai/gpt-5-mini",
        "openai/gpt-4o-mini",
        "google/gemini-3.7-flash",
        "google/gemini-3.5-flash",
        "anthropic/claude-3.5-haiku",
        "deepseek/deepseek-chat"
    ]

    custom_model = os.environ.get("REASONING_MODEL")
    if custom_model:
        models_to_try = [custom_model]
    else:
        models_to_try = [m for m in preferred_candidates if m in catalog_map]
        if not models_to_try:
            models_to_try = preferred_candidates

    system_prompt = f"""You are an elite AI systems and LLM infrastructure architect conducting a scheduled comparative evaluation of inference models on OpenRouter for integration into the 'claude-threepio' proxy.

You are provided with:
1. THE CURRENTLY ACTIVE TIER CONFIGURATION from claude-threepio (the exact active options and ordering per tier).
2. THE LIVE OPENROUTER MODEL CATALOG (with current token pricing and context lengths).

================================================================================
CRITICAL MINIMAL-DIFF CONSTRAINTS & NON-DESTRUCTIVE RULES:
================================================================================
1. STRICT PRESERVATION OF ORDER:
   - The ordering of existing models within each tier MUST be strictly preserved.
   - NEVER shuffle, re-sort, or reorder retained models.
2. STRICT PRESERVATION OF TEXT & NAMES:
   - DO NOT rewrite descriptions, alter display names, or tweak wording for existing models.
   - All existing model names and curated descriptions in claude-threepio must remain untouched.
3. PRECISE DELTA ACTIONS ONLY:
   Your job is ONLY to perform four specific types of changes:
   a) PRICE & CONTEXT SYNC: Update pricing ($In/$Out per 1M) and context window if OpenRouter catalog rates have changed for existing models.
   b) ADDITIONS: Add newly released or high-impact models present in the provided OpenRouter catalog that represent a clear architectural or cost advantage. New models will be appended to the tier. Provide a concise, multi-bullet technical description formatted to match the codebase style.
   c) REMOVALS: Remove a model ONLY if it is discontinued, broken, deprecated on OpenRouter, or clearly obsolete.
   d) RECOMMENDATION SHIFT: Designate exactly 1 model per tier as 'is_recommended': true based on benchmark/price-to-performance leadership.
4. ABSOLUTELY NO HALLUCINATIONS:
   - Every model ID MUST exist in the provided OpenRouter catalog list.
   - NEVER invent non-existent model slugs, unreleased version numbers, or hypothetical variants.
5. ZERO ARBITRARY CHANGES:
   - Do NOT generate cosmetic changes or gratuitous diffs. Keep changesets minimal, clean, and surgical.

Anthropic Target Aliases:
- Opus Tier (claude-opus-4): Heavyweight reasoning, math, complex system architecture. Reference: Claude 3.7 / 4 Opus ($15/$75).
- Sonnet Tier (claude-sonnet-4-5): Fast agentic coding workhorse, tool calling, SWE-bench leader. Reference: Claude 3.5 / 3.7 Sonnet ($3/$15).
- Haiku Tier (claude-3-haiku-20240307): Maximum economy, high throughput, subagent routing (<$0.30/M).
- Fable Tier (claude-fable-5): Ultra-heavyweight multi-step agent runtime loops.
- Mythos Tier (claude-mythos-1): Frontier & experimental flagships.

JSON Format Schema:
{{
  "executive_summary": "High-level summary of industry shifts, newly released models, and benchmark progress...",
  "web_search_grounding": [
    "Grounding point 1 with benchmark citations (LiveBench, SWE-bench, Arena Elo)...",
    "Grounding point 2..."
  ],
  "tier_comparisons": [
    {{
      "tier_name": "opus",
      "tier_label": "OPUS TIER (Heavyweight Reasoning & Complex Architecture)",
      "claude_name": "claude-opus-4",
      "current_recommended": "exact_current_model_id",
      "proposed_recommended": "exact_proposed_model_id",
      "recommended_change_summary": "Why the primary recommendation shifted or was maintained...",
      "delta_analysis": "In-depth analysis of capability changes, pricing differences, and benchmark comparisons for this tier...",
      "swaps_and_changes": [
        {{
          "action": "SYNC" or "ADD" or "REMOVE" or "RETAIN",
          "current_model": "Old Model Name (or None if new)",
          "proposed_model": "New Model Name & ID",
          "price_comparison": "$X.XX/$Y.YY vs $A.AA/$B.BB (Z% delta)",
          "benchmark_justification": "Why this change is justified..."
        }}
      ],
      "price_syncs": [
        {{
          "id": "exact_existing_model_id",
          "new_price": "$0.50/$1.00",
          "new_context": "1M Context"
        }}
      ],
      "removals": [
        {{
          "id": "exact_model_id_to_remove",
          "rationale": "Why removed"
        }}
      ],
      "additions": [
        {{
          "id": "exact_catalog_model_id",
          "name": "Clean Display Name",
          "is_recommended": false,
          "supports1m": true,
          "price_str": "$X.XX/$Y.YY",
          "ctx_str": "1M Context",
          "rationale": "Why added to tier",
          "description": "Provider's model description summary.\n\n• 1M Context Window: Capacity...\n• Architecture: Details...\n• Recommended Tier Match: Purpose..."
        }}
      ],
      "retained_model_ids_in_order": [
        "exact_model_id_1",
        "exact_model_id_2"
      ]
    }}
  ]
}}
"""

    user_prompt = f"""Current Date: {today_str}

CURRENT ACTIVE CLAUDE-THREEPIO CONFIGURATION:
{json.dumps(current_tiers, indent=2)}

AVAILABLE LIVE OPENROUTER CATALOG:
{json.dumps(compact_catalog[:220], indent=1)}

Please perform web search on recent benchmarks and releases, conduct the non-destructive comparative delta analysis against the active configuration, and return the structured JSON strictly following the schema and minimal-diff constraints."""

    for model_name in models_to_try:
        info(f"Attempting comparative evaluation with model: {model_name}...")
        plugins = [{"id": "web"}] if not model_name.startswith("perplexity/") else []
        payload = {
            "model": model_name,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": 0.2
        }
        if plugins:
            payload["plugins"] = plugins

        req = urllib.request.Request(
            OPENROUTER_CHAT_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://github.com/axiomantic/claude-threepio",
                "X-Title": "claude-threepio Comparative Evaluator"
            }
        )

        try:
            with urllib.request.urlopen(req, timeout=95) as resp:
                data = json.loads(resp.read().decode())
                content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
                
                json_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", content, re.DOTALL)
                if json_match:
                    raw_json = json_match.group(1)
                else:
                    raw_json = content.strip()
                
                parsed = json.loads(raw_json)
                success(f"Successfully received comparative recommendations using {model_name}.")
                return parsed
        except urllib.error.HTTPError as he:
            err_body = he.read().decode("utf-8", errors="ignore")
            warn(f"Model {model_name} HTTP Error {he.code}: {err_body}")
        except Exception as e:
            warn(f"Model {model_name} failed: {e}")

    error("All candidate models failed to return a valid comparative evaluation.")
    return None

def generate_comparative_markdown_report(analysis_result, current_tiers, catalog_map, today_str):
    lines = [
        f"# 🤖 Weekly Model Recommendations & Comparative Delta Analysis",
        f"**Generated on:** {today_str} UTC  ",
        f"**Evaluation Engine:** LLM Agent with Live Web Search Grounding  ",
        f"**Source Data:** Live [OpenRouter Model Catalog](https://openrouter.ai/models)\n",
        "---",
        "## 📑 Executive Summary\n",
        analysis_result.get("executive_summary", "Comparative evaluation completed."),
        "\n### 🌐 Web Search Findings & Benchmark Grounding\n"
    ]

    for g in analysis_result.get("web_search_grounding", []):
        lines.append(f"- {g}")
    lines.append("")

    lines.append("---")
    lines.append("## 📊 Tier-by-Tier Comparative Delta Analysis\n")

    for tc in analysis_result.get("tier_comparisons", []):
        tname = tc.get("tier_name", "")
        tlabel = tc.get("tier_label", tname.upper())
        cname = tc.get("claude_name", "")
        curr_rec = tc.get("current_recommended", "N/A")
        prop_rec = tc.get("proposed_recommended", "N/A")
        rec_sum = tc.get("recommended_change_summary", "")
        delta_analysis = tc.get("delta_analysis", "")

        lines.append(f"### 🏷️ {tlabel} (`{cname}`)")
        lines.append(f"- **Current Recommended (in `claude-threepio`):** `{curr_rec}`")
        lines.append(f"- **Proposed Recommended:** **`{prop_rec}`**")
        if rec_sum:
            lines.append(f"- **Recommendation Shift Rationale:** {rec_sum}\n")
        if delta_analysis:
            lines.append(f"*{delta_analysis}*\n")

        # Swaps / adjustments table
        swaps = tc.get("swaps_and_changes", [])
        if swaps:
            lines.append("#### 🔄 Lineup Adjustments & Benchmark Rationale")
            lines.append("| Action | Previous Model | Proposed Model | Price Delta | Benchmark & Engineering Justification |")
            lines.append("| :--- | :--- | :--- | :--- | :--- |")
            for s in swaps:
                action = s.get("action", "SYNC")
                c_mod = s.get("current_model", "-")
                p_mod = s.get("proposed_model", "-")
                p_cmp = s.get("price_comparison", "-")
                b_just = s.get("benchmark_justification", "-")
                lines.append(f"| **{action}** | {c_mod} | `{p_mod}` | {p_cmp} | {b_just} |")
            lines.append("")

        # Additions table
        adds = tc.get("additions", [])
        if adds:
            lines.append("#### ➕ Newly Added Models")
            lines.append("| Model ID | Display Name | Live Price ($In / $Out) | Context | Status | Link | Rationale |")
            lines.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
            for opt in adds:
                mid = opt.get("id", "")
                name = opt.get("name", mid)
                is_rec = opt.get("is_recommended", False)
                rat = opt.get("rationale", "")
                cat_item = catalog_map.get(mid)
                price_str = cat_item["price_str"] if cat_item else opt.get("price_str", "$1.00/$3.00")
                ctx_str = cat_item["ctx_str"] if cat_item else opt.get("ctx_str", "1M Context")
                badge = "**⭐ Recommended**" if is_rec else "Alternative"
                link_str = f"[`{mid}`](https://openrouter.ai/{mid})"
                lines.append(f"| {link_str} | {name} | **{price_str}** | {ctx_str} | {badge} | [View](https://openrouter.ai/{mid}) | {rat} |")
            lines.append("")

        lines.append("\n---\n")

    lines.append("## 💡 Maintainer Action Items")
    lines.append("- [ ] Review proposed model additions, removals, and pricing syncs above.")
    lines.append("- [ ] Verify context window requirements (1M context preserved for agentic flows).")
    lines.append("- [ ] Merge this PR to update the default curated recommendations in `claude-threepio`.")

    return "\n".join(lines)

def format_python_description(mid, raw_desc):
    """Format description into multi-line Python tuple syntax matching claude-threepio style."""
    lines = [l.strip() for l in raw_desc.strip().split("\n") if l.strip()]
    if not lines:
        return f'    "{mid}": (\n        "High-performance AI model available via OpenRouter."\n    ),'
    
    intro_parts = []
    bullet_parts = []
    for l in lines:
        if l.startswith("•") or l.startswith("- ") or l.startswith("* "):
            bullet_text = l.lstrip("•-* ").strip()
            bullet_parts.append(f'• {bullet_text}')
        else:
            intro_parts.append(l)
    
    intro_str = " ".join(intro_parts)
    clean_intro = intro_str.replace('\\', '\\\\').replace('"', '\\"')
    
    out = [f'    "{mid}": (']
    if bullet_parts:
        out.append(f'        "{clean_intro}\\n\\n"')
        for i, b in enumerate(bullet_parts):
            clean_b = b.replace('\\', '\\\\').replace('"', '\\"')
            nl = '\\n' if i < len(bullet_parts) - 1 else ''
            out.append(f'        "{clean_b}{nl}"')
    else:
        out.append(f'        "{clean_intro}"')
    out.append('    ),')
    return "\n".join(out)

def apply_comparative_recommendations(analysis_result, catalog_map, today_str, setup_path="claude-threepio"):
    """
    Surgically apply recommendations to claude-threepio:
    - Retains exact model order in all tiers
    - Preserves existing display names and text descriptions verbatim
    - Updates pricing and context in-place when changed
    - Appends additions cleanly
    - Drops only explicitly removed models
    """
    if not os.path.exists(setup_path):
        warn(f"{setup_path} not found.")
        return

    info(f"Applying surgical non-destructive updates to {setup_path}...")
    with open(setup_path, "r", encoding="utf-8") as f:
        content = f.read()

    tier_comps = analysis_result.get("tier_comparisons", [])
    tier_map = {tc.get("tier_name"): tc for tc in tier_comps if tc.get("tier_name")}

    # 1. Update options in each tier non-destructively
    tier_pattern = re.compile(
        r'(\{\s*"tier_name":\s*"([^"]+)",\s*"tier_label":\s*"[^"]+",\s*"claude_name":\s*"[^"]+",\s*"options":\s*\[)(.*?)(\](?:,\s*"ollama_options":\s*ollama_opts\(\[.*?\]\))?\s*\})',
        re.DOTALL
    )

    def update_tier_block(match):
        header = match.group(1)
        tname = match.group(2)
        opt_text = match.group(3)
        footer = match.group(4)

        tc = tier_map.get(tname)
        if not tc:
            return match.group(0)

        removals = {r.get("id") for r in tc.get("removals", []) if r.get("id")}
        proposed_rec = tc.get("proposed_recommended")
        price_syncs = {p.get("id"): p for p in tc.get("price_syncs", []) if p.get("id")}

        # Process existing lines preserving exact order
        new_opt_lines = []
        for line in opt_text.split("\n"):
            if not line.strip():
                continue
            om = re.search(r'get_model_entry\(catalog,\s*"([^"]+)",\s*"([^"]+)",\s*"([^"]+)",\s*"([^"]+)",\s*(True|False)(?:,\s*is_recommended=(True|False))?\)', line)
            if not om:
                new_opt_lines.append(line)
                continue

            mid = om.group(1)
            name = om.group(2)
            old_price = om.group(3)
            old_ctx = om.group(4)
            old_supp1m = om.group(5)
            was_rec = (om.group(6) == "True") if om.group(6) else False

            # If removed, drop this line
            if mid in removals:
                continue

            # Determine updated pricing/context if available in catalog or price syncs
            cat_item = catalog_map.get(mid)
            new_price = old_price
            new_ctx = old_ctx
            new_supp1m = old_supp1m

            if cat_item:
                new_price = cat_item["price_str"]
                new_ctx = cat_item["ctx_str"]
                new_supp1m = "True" if cat_item["supports1m"] else "False"
            elif mid in price_syncs:
                new_price = price_syncs[mid].get("new_price", old_price)
                new_ctx = price_syncs[mid].get("new_context", old_ctx)

            is_rec = (mid == proposed_rec) if proposed_rec else was_rec
            rec_arg = ", is_recommended=True" if is_rec else ""

            # Check if any value changed
            if (new_price == old_price and new_ctx == old_ctx and 
                new_supp1m == old_supp1m and is_rec == was_rec):
                new_opt_lines.append(line)
            else:
                new_opt_lines.append(f'                get_model_entry(catalog, "{mid}", "{name}", "{new_price}", "{new_ctx}", {new_supp1m}{rec_arg}),')

        # Append new additions to the end of the options list
        for add in tc.get("additions", []):
            mid = add.get("id")
            if not mid or mid in removals:
                continue
            # Avoid duplicate if already in options
            if any(f'"{mid}"' in l for l in new_opt_lines):
                continue
            name = add.get("name", mid)
            cat_item = catalog_map.get(mid)
            p_str = add.get("price_str") or (cat_item["price_str"] if cat_item else "$1.00/$3.00")
            c_str = add.get("ctx_str") or (cat_item["ctx_str"] if cat_item else "1M Context")
            supp1m = "True" if (add.get("supports1m") or (cat_item and cat_item["supports1m"])) else "False"
            is_rec = (mid == proposed_rec) or add.get("is_recommended", False)
            rec_arg = ", is_recommended=True" if is_rec else ""
            new_opt_lines.append(f'                get_model_entry(catalog, "{mid}", "{name}", "{p_str}", "{c_str}", {supp1m}{rec_arg}),')

        return header + "\n" + "\n".join(new_opt_lines) + "\n            " + footer

    content = tier_pattern.sub(update_tier_block, content)

    # 2. Append new descriptions to CURATED_DESCRIPTIONS without touching existing entries
    new_desc_entries = []
    for tc in tier_comps:
        for add in tc.get("additions", []):
            mid = add.get("id")
            desc = add.get("description", "").strip()
            if mid and desc and f'"{mid}":' not in content:
                formatted = format_python_description(mid, desc)
                new_desc_entries.append(formatted)

    if new_desc_entries:
        desc_block_match = re.search(r'(CURATED_DESCRIPTIONS\s*=\s*\{.*?)(\n\}[ \t]*\n\ndef get_model_entry)', content, re.DOTALL)
        if desc_block_match:
            insert_text = "\n" + "\n".join(new_desc_entries)
            content = content[:desc_block_match.start(2)] + insert_text + content[desc_block_match.start(2):]

    # 3. Append new entries to FRIENDLY_NAMES if needed
    new_friendly_entries = []
    for tc in tier_comps:
        for add in tc.get("additions", []):
            mid = add.get("id")
            name = add.get("name", mid)
            cat_item = catalog_map.get(mid)
            p_str = add.get("price_str") or (cat_item["price_str"] if cat_item else "$1.00/$3.00")
            if mid and f'"{mid}":' not in content:
                new_friendly_entries.append(f'        "{mid}": ("{name}", "{p_str}"),')

    if new_friendly_entries:
        fn_match = re.search(r'(FRIENDLY_NAMES\s*=\s*\{.*?)(\n\s*\}\n\s*def get_tier_name)', content, re.DOTALL)
        if fn_match:
            insert_fn = "\n" + "\n".join(new_friendly_entries)
            content = content[:fn_match.start(2)] + insert_fn + content[fn_match.start(2):]

    # 4. Update MODELS_LAST_REVISITED
    content = re.sub(
        r'^MODELS_LAST_REVISITED\s*=\s*"[^"]+"',
        f'MODELS_LAST_REVISITED = "{today_str}"',
        content,
        flags=re.MULTILINE
    )

    with open(setup_path, "w", encoding="utf-8") as f:
        f.write(content)
    success(f"Successfully applied non-destructive updates to {setup_path} with zero arbitrary diff noise.")

def main():
    apply_mode = "--apply" in sys.argv
    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    api_key = get_api_key()
    if not api_key:
        warn("No OPENROUTER_API_KEY found. Live LLM comparative analysis requires an API key.")
        sys.exit(1)

    current_tiers = extract_current_tiers("claude-threepio")
    info(f"Extracted {len(current_tiers)} active tiers from claude-threepio for comparative baseline.")

    catalog = fetch_openrouter_catalog()
    if not catalog:
        sys.exit(1)

    catalog_map, compact_catalog = build_compact_catalog(catalog)

    analysis_result = perform_llm_comparative_analysis(api_key, current_tiers, catalog_map, compact_catalog, today_str)
    if not analysis_result:
        error("Could not obtain valid comparative analysis from LLM.")
        sys.exit(1)

    report_md = generate_comparative_markdown_report(analysis_result, current_tiers, catalog_map, today_str)
    report_file = "MODEL_RECOMMENDATIONS_REPORT.md"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report_md)
    success(f"Wrote comprehensive comparative evaluation report to {report_file}")

    if apply_mode:
        apply_comparative_recommendations(analysis_result, catalog_map, today_str, "claude-threepio")

if __name__ == "__main__":
    main()
