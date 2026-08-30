# 🤖 Weekly Model Recommendations & Comparative Delta Analysis
**Generated on:** 2026-08-30 UTC  
**Evaluation Engine:** LLM Agent with Live Web Search Grounding  
**Source Data:** Live [OpenRouter Model Catalog](https://openrouter.ai/models)

---
## 📑 Executive Summary

The current claude-threepio configuration remains broadly well-aligned with today’s OpenRouter landscape: DeepSeek V4 Flash and Qwen 3.7 Flash are still excellent value anchors, and there are no 404/unavailable models to purge. The only meaningful deltas are (1) catalog price/context differences for DeepSeek V4 Pro and Flash vs the static strings in your config, and (2) major new frontier offerings such as Claude Sonnet 5 and Qwen3.8 Max; however, because your tiers already have strong coverage and Anthropic’s newer models are not yet the claude-threepio targets, the safest minimal-diff approach is to keep all existing recommendations unchanged and only synchronize pricing where it is clearly stale.

### 🌐 Web Search Findings & Benchmark Grounding

- Qwen3.8 Max is a newly GA frontier model (August 2026) that sits around #16/146 on coding, with 67.7% SWE-bench Pro and strong Terminal-Bench 2.1 scores, but remains clearly behind Anthropic’s Fable 5 and Opus 4.8 on core SWE benchmarks, making it competitive but not an obvious tier re-anchor for claude-threepio.[1][2][6]
- DeepSeek V4 Pro 0813 is a GA update of the V4 Pro line with improved performance on multi-agent and tool-heavy benchmarks like Terminal-Bench 2.1 and Toolathlon, but OpenRouter exposes this as a separate model ID deepseek/deepseek-v4-pro-0813 at a slightly lower per-token price than the older V4 Pro 0423 route, which remains available.[14]
- Claude Sonnet 5 significantly outperforms Sonnet 4.6 on coding and multi-agent benchmarks (e.g., ~63.2% vs ~58.1% on SWE-bench Pro), at lower Anthropic list pricing (~$2/$10 vs $3/$15), but your OpenRouter catalog entry lists only claude-sonnet-5 at its native ID rather than as a drop-in replacement for claude-sonnet-4-5; given claude-threepio’s explicit claude_name targets, switching recommendations to Sonnet 5 would be a policy-level change rather than a simple catalog sync.[7][8][11][13]

---
## 📊 Tier-by-Tier Comparative Delta Analysis

### 🏷️ OPUS TIER (Heavyweight Reasoning & Complex Architecture) (`claude-opus-4`)
- **Current Recommended (in `claude-threepio`):** `deepseek/deepseek-v4-pro`
- **Proposed Recommended:** **`deepseek/deepseek-v4-pro`**
*The Opus tier already mixes a very strong value frontier reasoner (DeepSeek V4 Pro), top open MoE options (Nemotron 3 Ultra, GLM 5.3 Flash, Qwen 3.7 Plus), and commercial flagships (GPT-5.6 Terra, Kimi K3, Claude Sonnet 4.6). Recent releases like Qwen3.8 Max and GPT-5.5/5.4 are strong but do not clearly dominate this mix on cost-adjusted SWE-bench/agentic metrics given published results, and Anthropic’s own Opus 4.7/4.8 and Opus 5 exist in the catalog but would be overkill for an Opus-4-targeted proxy. The only concrete deviations between your config and the live catalog in this tier are the static price/context strings for DeepSeek V4 Pro and DeepSeek V3.2, which should be synchronized; no ID swaps or recommendation changes are required for a minimal-diff update.*

#### 🔄 Lineup Adjustments & Benchmark Rationale
| Action | Previous Model | Proposed Model | Price Delta | Benchmark & Engineering Justification |
| :--- | :--- | :--- | :--- | :--- |
| **SYNC** | DeepSeek V4 Pro | `deepseek/deepseek-v4-pro` | $0.87/$1.74 vs $0.51/$1.02 (~41% / ~41% cheaper than current string) | OpenRouter now lists deepseek/deepseek-v4-pro (0423) at $0.51 in / $1.02 out per 1M with a 1,048k context window, while the active config still shows $0.87/$1.74; updating the displayed pricing keeps claude-threepio’s cost hints accurate without changing the model route or its role as the Opus tier’s recommended heavy reasoner.[deepseek/deepseek-v4-pro] |
| **SYNC** | DeepSeek V3.2 (MoE) | `deepseek/deepseek-v3.2` | $0.27/$0.40 vs $0.26/$0.38 (~4% / ~5% cheaper than current string) | The catalog lists deepseek/deepseek-v3.2 at $0.26 in / $0.38 out with 163k context, slightly below the $0.27/$0.40 recorded in your config; syncing this ensures your tier UI reflects current OpenRouter pricing while keeping the same mid-cost MoE reasoning option.[deepseek/deepseek-v3.2] |


---

### 🏷️ SONNET TIER (Agentic Coding, Tool Use & Everyday Workhorse) (`claude-sonnet-4-5`)
- **Current Recommended (in `claude-threepio`):** `deepseek/deepseek-v4-flash`
- **Proposed Recommended:** **`deepseek/deepseek-v4-flash`**
*The Sonnet tier is framed around fast, agentic coding and everyday workhorse usage, and today’s option set already includes some of the strongest high-throughput coders: DeepSeek V4 Flash, Qwen 3.7 Flash, Poolside Laguna S 2.1 (free), Qwen coding variants, and Codestral 2508. New releases like Claude Sonnet 5 and Qwen3.8 Max do advance the frontier for agentic coding, but they would represent policy-level shifts (toward Anthropic frontier or 2.4T MoE options) rather than incremental updates, and their higher list prices are not yet reflected as preferred defaults in your schema. Within the minimal-diff constraints, the only necessary changes here are to align DeepSeek V4 Flash’s displayed pricing and context with the OpenRouter catalog.*

#### 🔄 Lineup Adjustments & Benchmark Rationale
| Action | Previous Model | Proposed Model | Price Delta | Benchmark & Engineering Justification |
| :--- | :--- | :--- | :--- | :--- |
| **SYNC** | DeepSeek V4 Flash | `deepseek/deepseek-v4-flash` | $0.09/$0.18 vs $0.08/$0.16 (~11% / ~11% cheaper than current string) | OpenRouter lists deepseek/deepseek-v4-flash (0423) at $0.08 in / $0.16 out per 1M with a 1,048k context window, while your tier still shows $0.09/$0.18; syncing that price improves cost transparency for the Sonnet workhorse recommendation without altering routing or model behavior.[deepseek/deepseek-v4-flash] |


---

### 🏷️ HAIKU TIER (High Throughput, Low Latency & Background Tasks) (`claude-3-haiku-20240307`)
- **Current Recommended (in `claude-threepio`):** `qwen/qwen3.7-flash`
- **Proposed Recommended:** **`qwen/qwen3.7-flash`**
*The Haiku tier is optimized for maximum economy and throughput. Qwen 3.7 Flash remains an extremely competitive low-cost, high-context multimodal flash model at $0.03/$0.13 with a 1M context, and the rest of the tier includes a good spread of free and cheap small/medium models (Nemotron 3.5 Lightning free, Inkling Small free, Gemma 4 31B free, Ling 3.0 Flash, Nova Micro, Llama 3.1 8B, Mistral Nemo and Ministral 8B). New catalog entries like Mistral Small 4, Solar Pro 4, Qwen 3.6 Flash, and Seed 1.6 Flash are attractive, but your current Haiku options already span similar price/performance points and modalities. There are no price or context mismatches between the live catalog and the configuration for any Haiku-tier IDs, so this tier is already optimal under minimal-diff rules.*

✅ **All models up-to-date.** No changes proposed for this tier.


---

### 🏷️ FABLE TIER (Long-Horizon Agent Loops & Complex Workflows) (`claude-fable-5`)
- **Current Recommended (in `claude-threepio`):** `deepseek/deepseek-v4-pro`
- **Proposed Recommended:** **`deepseek/deepseek-v4-pro`**
*Fable is positioned as an ultra-heavyweight, long-horizon agent tier. You already include DeepSeek V4 Pro, Nemotron 3 Ultra (free), GLM 5.3 Flash, Qwen 3.7 Plus, Kimi K3, GPT-5.6 Terra, and Claude Sonnet 4.6 — a mix that spans cheap MoE agents, free large MoE, and paid frontier models. Although the catalog now includes Claude Fable 5 and newer OpenAI/Qwen flagships, those are Mythos-class or general frontier models and not required for a minimal-diff refresh. As with the Opus tier, the only concrete discrepancy is DeepSeek V4 Pro’s stale pricing; syncing this keeps your Fable tier cost surface accurate without changing the recommended route.*

#### 🔄 Lineup Adjustments & Benchmark Rationale
| Action | Previous Model | Proposed Model | Price Delta | Benchmark & Engineering Justification |
| :--- | :--- | :--- | :--- | :--- |
| **SYNC** | DeepSeek V4 Pro | `deepseek/deepseek-v4-pro` | $0.87/$1.74 vs $0.51/$1.02 (~41% / ~41% cheaper than current string) | Synchronizing DeepSeek V4 Pro’s price/context with the catalog in the Fable tier ensures consistent representation across tiers and reflects its current excellent cost-to-capability ratio for long-horizon agent loops.[deepseek/deepseek-v4-pro] |


---

### 🏷️ MYTHOS TIER (Frontier Intelligence & Uncompromising Quality) (`claude-mythos-1`)
- **Current Recommended (in `claude-threepio`):** `anthropic/claude-opus-5`
- **Proposed Recommended:** **`anthropic/claude-opus-5`**
*The Mythos tier is already anchored on Claude Opus 5 at $5/$25 with a 1M context window, which aligns with OpenRouter’s latest catalog entry and remains an industry-leading frontier reasoning model. The rest of the tier mirrors the Fable/Opus mixes (Nemotron 3 Ultra free, GLM 5.3 Flash, DeepSeek V4 Pro, Kimi K3, GPT-5.6 Terra, Claude Sonnet 4.6) and provides a broad spectrum of frontier and near-frontier options. While new models like Qwen3.8 Max and GPT-5.5 Pro are competitive on frontier benchmarks, your existing Mythos options already cover multiple vendor families at similar or better effective pricing; adding them would expand the list without a clear deficit to fix. All Mythos-tier IDs and their prices already match the live catalog, so no changes are necessary.*

✅ **All models up-to-date.** No changes proposed for this tier.


---

## 💡 Maintainer Action Items
- [ ] Review proposed model additions, removals, and pricing syncs above.
- [ ] Verify context window requirements (1M context preserved for agentic flows).
- [ ] Merge this PR to update the default curated recommendations in `claude-threepio`.