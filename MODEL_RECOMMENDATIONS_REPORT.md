# 🤖 Weekly Model Recommendations & Comparative Delta Analysis
**Generated on:** 2026-08-23 UTC  
**Evaluation Engine:** LLM Agent with Live Web Search Grounding  
**Source Data:** Live [OpenRouter Model Catalog](https://openrouter.ai/models)

---
## 📑 Executive Summary

OpenRouter’s 2026 catalog has shifted toward a China-led value frontier: DeepSeek V4 Flash/Pro, Qwen 3.7/3.8, Z.ai GLM 5.2/5.3, Google Gemini 3.x Flash/Pro, and Anthropic Opus/Sonnet 4.6–5 now cover nearly every tier with stronger 1M-context and better benchmark/cost efficiency than many legacy picks. Recent coverage and benchmark roundups indicate DeepSeek V4 Flash is near the top of coding leaderboards on price-adjusted performance, while Claude Sonnet 4.6/5 remains the preferred Sonnet-class coding/agentic workhorse and Claude Opus 4.8/5 remains the quality ceiling for frontier reasoning. OpenRouter’s own benchmarks dashboard and benchmark API now aggregate live model intelligence, coding, and agentic scores, making it clear that the current claude-threepio lineup is under-updated in Opus/Fable/Mythos and can be materially improved by swapping in newer GA releases such as DeepSeek V4 Pro 0813, Claude Opus 4.8, Claude Sonnet 5, GPT-5.6 Sol/Terra/Luna, GLM-5.3/5.2, Qwen3.8 Max/2.4T, and Gemini 3.1/3.7 families. Free and ultra-low-cost coverage is now much richer than before, with multiple free MoE models and very low-cost specialist options that can cleanly anchor Haiku/Sonnet subagent routing. [6][7][9][10]

### 🌐 Web Search Findings & Benchmark Grounding

- OpenRouter’s live benchmarks page reports 6 benchmarks and 2,465,315 task evaluations as of Aug 22, 2026, and its benchmark API aggregates Artificial Analysis, Design Arena, and OpenRouter task evals. [10][6]
- Recent model leaderboard coverage highlights DeepSeek V4 Flash as a top cost-adjusted coding model, with low latency and strong Artificial Analysis coding performance, while GPT-5.6 Luna/Terra/Sol and Claude Sonnet 4.6/5 remain high-end agentic/coding choices. [9][5]
- Recent release coverage shows major 2026 frontier updates across OpenAI GPT-5.2/5.4/5.5/5.6, Anthropic Claude Opus 4.6/4.7/4.8/5 and Sonnet 4.6/5, Google Gemini 3.1/3.5/3.6/3.7, DeepSeek V4 Flash/Pro, Qwen3.5/3.6/3.7/3.8, Z.ai GLM 5.x, Moonshot Kimi K2.5/2.6/2.7/3, NVIDIA Nemotron 3 family, and Poolside Laguna S/XS 2.1. [5][8][9]

---
## 📊 Tier-by-Tier Comparative Delta Analysis

### 🏷️ OPUS TIER (Heavyweight Reasoning & Complex Architecture) (`claude-opus-4`)
- **Current Recommended (in `claude-threepio`):** `DeepSeek V4 Pro (deepseek/deepseek-v4-pro) — $0.50/$1.00`
- **Proposed Recommended:** **`DeepSeek V4 Pro 0813 (deepseek/deepseek-v4-pro-0813) — $1.12/$3.37`**
- **Recommendation Shift Rationale:** The current recommendation is still a strong value pick, but the GA DeepSeek V4 Pro 0813 is the better default because it is the current production snapshot, retains 1M context, and aligns better with today’s frontier reasoning/coding stack. Claude Opus 4.8 remains the pure quality ceiling, but its price is far above the value optimum for the Opus tier.

*This tier should present a clear spectrum from free exploratory models through a rational default and then a quality ceiling. The current lineup overweights experimental/free options and lacks the newest stable frontier anchors. DeepSeek V4 Pro 0813 replaces the older DeepSeek V4 Pro at +$0.62 input (+124%) and +$2.37 output (+237%), but the delta is justified because the newer snapshot is the GA release with better stability and a tighter fit for long-horizon reasoning. Claude Opus 4.8 should be added as the premium ceiling, because benchmark coverage and leaderboard commentary indicate Opus-class models remain at the top of general reasoning and professional work. [5][9] Retain the free/open options, but prioritize the models with strong orchestration and 1M context: Nemotron 3 Ultra free, Ox Alpha, GLM 5.2 free, and Qwen 3.7 Plus. GLM 5.3 and Qwen3.8 Max should be added as higher-ceiling alternatives because live catalog descriptions place them in complex software engineering/agentic workflows, and they represent the newest wave of large reasoning models. [9][10]*

#### 🔄 Model Swaps & Lineup Adjustments
| Action | Previous Model | Proposed Model | Price Delta | Benchmark & Engineering Justification |
| :--- | :--- | :--- | :--- | :--- |
| **SWAP** | DeepSeek V4 Pro (deepseek/deepseek-v4-pro) | `DeepSeek V4 Pro 0813 (deepseek/deepseek-v4-pro-0813)` | $0.50/$1.00 vs $1.12/$3.37 (+124.0% input, +237.0% output) | GA release snapshot is preferable for production: stronger stability and newer frontier tuning, while keeping 1M context and preserving the same DeepSeek reasoning family. |
| **RETAIN** | Nemotron 3 Ultra 550B (Free) (nvidia/nemotron-3-ultra-550b-a55b:free) | `Nemotron 3 Ultra 550B (Free) (nvidia/nemotron-3-ultra-550b-a55b:free)` | $0.00/$0.00 vs $0.00/$0.00 (0% delta) | A free 1M-context MoE gives zero-cost exploration and long-context experimentation with meaningful orchestration capacity. |
| **RETAIN** | Ox Alpha (Stealth Free) (stealth/ox-alpha) | `Ox Alpha (Stealth Free) (stealth/ox-alpha)` | $0.00/$0.00 vs $0.00/$0.00 (0% delta) | Keeps a zero-cost anonymous fallback for bursty traffic and A/B testing. |
| **RETAIN** | GLM 5.2 (Free) (z-ai/glm-5.2:free) | `GLM 5.2 (Free) (z-ai/glm-5.2:free)` | $0.00/$0.00 vs $0.00/$0.00 (0% delta) | Free reasoning baseline with 1M-context class capability in the current catalog and strong long-horizon workflow fit. |
| **RETAIN** | Qwen 3.7 Plus (qwen/qwen3.7-plus) | `Qwen 3.7 Plus (qwen/qwen3.7-plus)` | $0.32/$1.28 vs $0.32/$1.28 (0% delta) | Balanced cost/performance anchor and a strong value alternative for reasoning-heavy use cases. |
| **ADD** | None | `Anthropic: Claude Opus 4.8 (anthropic/claude-opus-4.8)` | $5.00/$25.00 vs new option | Frontier quality ceiling for the tier; Opus-class models remain the best fit when users prioritize maximum reasoning and professional-grade output over cost. |
| **ADD** | None | `Z.ai: GLM 5.3 (z-ai/glm-5.3)` | $1.40/$4.40 vs new option | Newest GLM reasoning release in-catalog; useful for long-horizon agent tasks and software engineering workloads. |
| **ADD** | None | `Qwen: Qwen3.8 2.4T A95B (qwen/qwen3.8-2.4t-a95b)` | $2.00/$6.00 vs new option | Modern sparse MoE frontier option with a large parameter budget and strong fit for high-ceiling reasoning in the open-weight ecosystem. |

#### 📋 Full Proposed Options for Tier
| Model ID | Display Name | Live Price ($In / $Out) | Context | Status | Link | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [`nvidia/nemotron-3-ultra-550b-a55b:free`](https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b:free) | Nemotron 3 Ultra 550B (Free) | **$0.00/$0.00** | 1M Context | Alternative | [View](https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b:free) | Zero-cost exploration and long-context free fallback. |
| [`stealth/ox-alpha`](https://openrouter.ai/stealth/ox-alpha) | Ox Alpha (Stealth Free) | **Live API** | 1M Context | Alternative | [View](https://openrouter.ai/stealth/ox-alpha) | Free stealth fallback for evaluation, burst routing, and privacy-conscious usage. |
| [`deepseek/deepseek-v4-pro-0813`](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) | DeepSeek V4 Pro 0813 | **$1.12/$3.37** | 1M Context | **⭐ Recommended** | [View](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) | Best value default for heavyweight reasoning with 1M context. |
| [`qwen/qwen3.7-plus`](https://openrouter.ai/qwen/qwen3.7-plus) | Qwen 3.7 Plus | **$0.32/$1.28** | 1M Context | Alternative | [View](https://openrouter.ai/qwen/qwen3.7-plus) | High-value open-weight reasoning choice with strong long-context support. |
| [`z-ai/glm-5.2`](https://openrouter.ai/z-ai/glm-5.2) | GLM-5.2 | **$0.97/$3.04** | 1M Context | Alternative | [View](https://openrouter.ai/z-ai/glm-5.2) | Established long-context reasoning model that remains highly competitive for agent tasks. |
| [`z-ai/glm-5.3`](https://openrouter.ai/z-ai/glm-5.3) | GLM 5.3 | **$1.40/$4.40** | 1M Context | Alternative | [View](https://openrouter.ai/z-ai/glm-5.3) | Newest GLM frontier option for users who want the latest Z.ai release. |
| [`qwen/qwen3.8-2.4t-a95b`](https://openrouter.ai/qwen/qwen3.8-2.4t-a95b) | Qwen3.8 2.4T A95B | **$2.00/$6.00** | 1M Context | Alternative | [View](https://openrouter.ai/qwen/qwen3.8-2.4t-a95b) | High-ceiling sparse MoE model for frontier reasoning experiments. |
| [`anthropic/claude-opus-4.8`](https://openrouter.ai/anthropic/claude-opus-4.8) | Claude Opus 4.8 | **$5.00/$25.00** | 1M Context | Alternative | [View](https://openrouter.ai/anthropic/claude-opus-4.8) | Premium ceiling option with the strongest Anthropic-quality positioning in this tier. |

---

### 🏷️ SONNET TIER (Agentic Coding, Tool Use & Everyday Workhorse) (`claude-sonnet-4-5`)
- **Current Recommended (in `claude-threepio`):** `DeepSeek V4 Flash (deepseek/deepseek-v4-flash) — $0.08/$0.15`
- **Proposed Recommended:** **`DeepSeek V4 Flash Latest (~deepseek/deepseek-v4-flash-latest) — $0.06/$0.13`**
- **Recommendation Shift Rationale:** The current recommended model is already excellent, but the latest DeepSeek Flash alias should replace the fixed snapshot because it tracks the newest production revision at lower price and the same 1M context. Claude Sonnet 4.6/5 should also be kept as the premium high-throughput coding ceiling in the tier.

*This tier needs the strongest coding/agentic value-per-dollar and reliable tool use. The price-sensitive default should move from DeepSeek V4 Flash 0423 to the latest redirect alias, reducing input cost by 25% and output cost by 13.3% while preserving the same family and 1M context. The current lineup is already strong, but it can be improved by adding explicit specialist models that have emerged as coding/workflow leaders: Qwen3 Coder Next, KAT-Coder-Pro V2.5, Poolside Laguna S 2.1, Google Gemini 3.7 Flash, and OpenAI GPT-5.2-Codex / GPT-5.3-Codex. Benchmark coverage suggests DeepSeek V4 Flash is a top value coding model, while Claude Sonnet 4.6/5 remains among the strongest general agentic coding models. [9][5] The tier should keep free, budget, workhorse, specialist, and premium ceiling options all visible. [9][10]*

#### 🔄 Model Swaps & Lineup Adjustments
| Action | Previous Model | Proposed Model | Price Delta | Benchmark & Engineering Justification |
| :--- | :--- | :--- | :--- | :--- |
| **SWAP** | DeepSeek V4 Flash (deepseek/deepseek-v4-flash) | `DeepSeek V4 Flash Latest (~deepseek/deepseek-v4-flash-latest)` | $0.08/$0.15 vs $0.06/$0.13 (-25.0% input, -13.3% output) | Latest redirect keeps the same model family while automatically tracking the newest revision; lower cost makes it the best Sonnet-tier default. |
| **RETAIN** | North Mini Code (Free) (cohere/north-mini-code:free) | `North Mini Code (Free) (cohere/north-mini-code:free)` | $0.00/$0.00 vs $0.00/$0.00 (0% delta) | Free coding-specialist fallback remains valuable for ultra-low-cost subagent routing. |
| **RETAIN** | Laguna S 2.1 (Free) (poolside/laguna-s-2.1:free) | `Laguna S 2.1 (Free) (poolside/laguna-s-2.1:free)` | $0.00/$0.00 vs $0.00/$0.00 (0% delta) | Keeps a free agentic coding model from a code-first vendor. |
| **RETAIN** | Gemma 4 31B (Free) (google/gemma-4-31b-it:free) | `Gemma 4 31B (Free) (google/gemma-4-31b-it:free)` | $0.00/$0.00 vs $0.00/$0.00 (0% delta) | Free general-purpose multimodal option broadens the Sonnet tier’s fallback coverage. |
| **ADD** | None | `Google: Gemini 3.7 Flash (google/gemini-3.7-flash)` | $0.38/$1.88 vs new option | Recent Google release optimized for fast agentic workflows and coding; strong fit for tool-heavy work. |
| **ADD** | None | `Qwen: Qwen3 Coder Next (qwen/qwen3-coder-next)` | $0.12/$0.80 vs new option | Open-weight coding specialist with excellent cost/performance for repo-scale coding and agentic development. |
| **ADD** | None | `Kwaipilot: KAT-Coder-Pro V2.5 (kwaipilot/kat-coder-pro-v2.5)` | $0.74/$2.96 vs new option | Flagship-level coding agent model for enterprise-grade software engineering; strong specialist lane. |
| **ADD** | None | `Anthropic: Claude Sonnet 5 (anthropic/claude-sonnet-5)` | $2.00/$10.00 vs new option | Newest Sonnet-class frontier model; better premium default than older Sonnet 4.x for coding and agents. |
| **ADD** | None | `OpenAI: GPT-5.3-Codex (openai/gpt-5.3-codex)` | $1.75/$14.00 vs new option | Agentic coding specialist from OpenAI’s Codex line; appropriate premium specialization for SWE-heavy tasks. |

#### 📋 Full Proposed Options for Tier
| Model ID | Display Name | Live Price ($In / $Out) | Context | Status | Link | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [`cohere/north-mini-code:free`](https://openrouter.ai/cohere/north-mini-code:free) | North Mini Code (Free) | **$0.00/$0.00** | 256k Context | Alternative | [View](https://openrouter.ai/cohere/north-mini-code:free) | Free coding-specialist fallback. |
| [`poolside/laguna-s-2.1:free`](https://openrouter.ai/poolside/laguna-s-2.1:free) | Laguna S 2.1 (Free) | **$0.00/$0.00** | 262k Context | Alternative | [View](https://openrouter.ai/poolside/laguna-s-2.1:free) | Free code-first fallback. |
| [`google/gemma-4-31b-it:free`](https://openrouter.ai/google/gemma-4-31b-it:free) | Gemma 4 31B (Free) | **$0.00/$0.00** | 262k Context | Alternative | [View](https://openrouter.ai/google/gemma-4-31b-it:free) | Free multimodal fallback with broad utility. |
| [`deepseek/deepseek-v4-flash-latest`](https://openrouter.ai/deepseek/deepseek-v4-flash-latest) | DeepSeek V4 Flash Latest | **Live API** | 1M Context | **⭐ Recommended** | [View](https://openrouter.ai/deepseek/deepseek-v4-flash-latest) | Best default for value-per-dollar and live revision tracking. |
| [`qwen/qwen3.7-flash`](https://openrouter.ai/qwen/qwen3.7-flash) | Qwen 3.7 Flash | **$0.03/$0.13** | 1M Context | Alternative | [View](https://openrouter.ai/qwen/qwen3.7-flash) | Very low-cost multimodal flash model. |
| [`google/gemini-3.7-flash`](https://openrouter.ai/google/gemini-3.7-flash) | Gemini 3.7 Flash | **$0.38/$1.88** | 1M Context | Alternative | [View](https://openrouter.ai/google/gemini-3.7-flash) | High-throughput agentic coding model with Google-scale tool reliability. |
| [`qwen/qwen3-coder-next`](https://openrouter.ai/qwen/qwen3-coder-next) | Qwen3 Coder Next | **$0.12/$0.80** | 262k Context | Alternative | [View](https://openrouter.ai/qwen/qwen3-coder-next) | Coding-specialist workhorse with excellent budget efficiency. |
| [`kwaipilot/kat-coder-pro-v2.5`](https://openrouter.ai/kwaipilot/kat-coder-pro-v2.5) | KAT-Coder-Pro V2.5 | **$0.74/$2.96** | 256k Context | Alternative | [View](https://openrouter.ai/kwaipilot/kat-coder-pro-v2.5) | Dedicated enterprise coding specialist. |
| [`openai/gpt-5.3-codex`](https://openrouter.ai/openai/gpt-5.3-codex) | GPT-5.3-Codex | **$1.75/$14.00** | 400k Context | Alternative | [View](https://openrouter.ai/openai/gpt-5.3-codex) | Premium OpenAI coding specialist. |
| [`anthropic/claude-sonnet-5`](https://openrouter.ai/anthropic/claude-sonnet-5) | Claude Sonnet 5 | **$2.00/$10.00** | 1M Context | Alternative | [View](https://openrouter.ai/anthropic/claude-sonnet-5) | Highest-capability Anthropic Sonnet-class option. |

---

### 🏷️ HAIKU TIER (High Throughput, Low Latency & Background Tasks) (`claude-3-haiku-20240307`)
- **Current Recommended (in `claude-threepio`):** `Qwen 3.7 Flash (qwen/qwen3.7-flash) — $0.03/$0.13`
- **Proposed Recommended:** **`Qwen 3.7 Flash (qwen/qwen3.7-flash) — $0.03/$0.13`**
- **Recommendation Shift Rationale:** The current recommendation remains the correct default because it is extremely cheap, 1M-context capable, and tailored to fast agentic workflows. The tier should be expanded with more zero-cost and sub-$0.10 options rather than changing the default.

*Haiku is the most price-sensitive tier, so the best design is a dense ladder: free models, ultra-cheap economy models, then one or two high-throughput workhorses. The current lineup is good but can be improved by adding the newest free and sub-$0.10 models such as OpenRouter free router, NVIDIA Nemotron 3.5 Lightning free, Dots3-Note Preview free, Ling-2.6-flash, Upstage Solar Pro 4, Step 3.5 Flash, and OpenAI GPT-5.4 Nano. The low-cost lane is now richer than the existing lineup suggests: Ling-2.6-flash is priced at $0.01/$0.03, Mistral Nemo at $0.02/$0.03, Llama 3.1 8B Instruct at $0.02/$0.05, and Qwen 3.5 Flash at $0.07/$0.26. The current Qwen 3.7 Flash remains the recommended option because it is still one of the best speed/value models with 1M context and strong multimodal reasoning. [9][10] No current model needs to be removed; the main action is to add newer low-cost and free models and keep the recommendation stable.*

#### 🔄 Model Swaps & Lineup Adjustments
| Action | Previous Model | Proposed Model | Price Delta | Benchmark & Engineering Justification |
| :--- | :--- | :--- | :--- | :--- |
| **RETAIN** | Qwen 3.7 Flash (qwen/qwen3.7-flash) | `Qwen 3.7 Flash (qwen/qwen3.7-flash)` | $0.03/$0.13 vs $0.03/$0.13 (0% delta) | Best balance of speed, capability, and cost for Haiku-tier daily use. |
| **RETAIN** | Nemotron 3.5 Lightning (Free) (nvidia/nemotron-3.5-lightning:free) | `Nemotron 3.5 Lightning (Free) (nvidia/nemotron-3.5-lightning:free)` | $0.00/$0.00 vs $0.00/$0.00 (0% delta) | Zero-cost high-throughput MoE is a perfect Haiku-tier safety valve. |
| **RETAIN** | Nemotron 3 Nano 30B (Free) (nvidia/nemotron-3-nano-30b-a3b:free) | `Nemotron 3 Nano 30B (Free) (nvidia/nemotron-3-nano-30b-a3b:free)` | $0.00/$0.00 vs $0.00/$0.00 (0% delta) | Good free compact reasoning model for background tasks. |
| **RETAIN** | Inkling Small (Free) (thinkingmachines/inkling-small:free) | `Inkling Small (Free) (thinkingmachines/inkling-small:free)` | $0.00/$0.00 vs $0.00/$0.00 (0% delta) | Free multimodal MoE gives another useful fallback lane. |
| **ADD** | None | `OpenRouter: Free Models Router (openrouter/free)` | $0.00/$0.00 vs new option | Router-level free fallback is useful when availability matters more than specific model identity. |
| **ADD** | None | `NVIDIA: Nemotron 3.5 Lightning (nvidia/nemotron-3.5-lightning)` | $0.08/$0.20 vs new option | Ultra-efficient MoE for high-throughput agent workloads at sub-$0.10 input pricing. |
| **ADD** | None | `Ling-3.0-flash (inclusionai/ling-3.0-flash)` | $0.02/$0.06 vs new option | One of the cheapest capable reasoning options now available, ideal for bulk routing. |
| **ADD** | None | `Mistral Nemo 12B (mistralai/mistral-nemo)` | $0.02/$0.03 vs new option | Very low-cost, compact model for simple generation and triage. |
| **ADD** | None | `OpenAI: GPT-5.4 Nano (openai/gpt-5.4-nano)` | $0.20/$1.25 vs new option | Tiny OpenAI model for speed-critical tasks, classification, and lightweight assistants. |

#### 📋 Full Proposed Options for Tier
| Model ID | Display Name | Live Price ($In / $Out) | Context | Status | Link | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [`openrouter/free`](https://openrouter.ai/openrouter/free) | Free Models Router | **$0.00/$0.00** | 200k Context | Alternative | [View](https://openrouter.ai/openrouter/free) | Fallback router for free inference. |
| [`nvidia/nemotron-3.5-lightning:free`](https://openrouter.ai/nvidia/nemotron-3.5-lightning:free) | Nemotron 3.5 Lightning (Free) | **$0.00/$0.00** | 1M Context | Alternative | [View](https://openrouter.ai/nvidia/nemotron-3.5-lightning:free) | Zero-cost high-throughput MoE. |
| [`thinkingmachines/inkling-small:free`](https://openrouter.ai/thinkingmachines/inkling-small:free) | Inkling Small (Free) | **$0.00/$0.00** | 262k Context | Alternative | [View](https://openrouter.ai/thinkingmachines/inkling-small:free) | Free multimodal MoE fallback. |
| [`inclusionai/ling-3.0-flash`](https://openrouter.ai/inclusionai/ling-3.0-flash) | Ling-3.0-flash | **$0.02/$0.06** | 262k Context | Alternative | [View](https://openrouter.ai/inclusionai/ling-3.0-flash) | Ultra-low-cost reasoning/generation lane. |
| [`mistralai/mistral-nemo`](https://openrouter.ai/mistralai/mistral-nemo) | Mistral Nemo 12B | **$0.02/$0.03** | 131k Context | Alternative | [View](https://openrouter.ai/mistralai/mistral-nemo) | Cheap compact model for background generation. |
| [`qwen/qwen3.7-flash`](https://openrouter.ai/qwen/qwen3.7-flash) | Qwen 3.7 Flash | **$0.03/$0.13** | 1M Context | **⭐ Recommended** | [View](https://openrouter.ai/qwen/qwen3.7-flash) | Best current balance of capability and cost. |
| [`deepseek/deepseek-v4-flash`](https://openrouter.ai/deepseek/deepseek-v4-flash) | DeepSeek V4 Flash | **$0.06/$0.11** | 1M Context | Alternative | [View](https://openrouter.ai/deepseek/deepseek-v4-flash) | Fast production flash model with strong coding value. |
| [`nvidia/nemotron-3.5-lightning`](https://openrouter.ai/nvidia/nemotron-3.5-lightning) | Nemotron 3.5 Lightning | **$0.08/$0.20** | 262k Context | Alternative | [View](https://openrouter.ai/nvidia/nemotron-3.5-lightning) | Fast and inexpensive MoE specialist. |
| [`openai/gpt-5.4-nano`](https://openrouter.ai/openai/gpt-5.4-nano) | GPT-5.4 Nano | **$0.20/$1.25** | 400k Context | Alternative | [View](https://openrouter.ai/openai/gpt-5.4-nano) | Tiny premium-family assistant for speed-critical tasks. |

---

### 🏷️ FABLE TIER (Long-Horizon Agent Loops & Complex Workflows) (`claude-fable-5`)
- **Current Recommended (in `claude-threepio`):** `DeepSeek V4 Pro (deepseek/deepseek-v4-pro) — $0.50/$1.00`
- **Proposed Recommended:** **`DeepSeek V4 Pro 0813 (deepseek/deepseek-v4-pro-0813) — $1.12/$3.37`**
- **Recommendation Shift Rationale:** Fable should remain anchored on a value-heavy long-context model, but the recommended model should move to the GA DeepSeek V4 Pro 0813 snapshot for stability and current-generation performance. For users willing to spend more, Claude Fable 5, Claude Opus 4.8, GPT-5.6 Terra/Sol, and Gemini 3.1 Pro should be available as ceiling options.

*The Fable tier is about long-horizon autonomy, so context window, agent reliability, and workflow endurance matter more than raw chat fluency. The current config is underpowered at the top because it does not expose the newest long-horizon frontier models now in the catalog. DeepSeek V4 Pro 0813 should replace the older DeepSeek V4 Pro as the default because it is the GA release and supports 1M context, albeit at a meaningful cost increase of +124% input and +237% output. The tier should add Claude Fable 5 as a true Anthropic-native Fable ceiling, plus GPT-5.6 Terra and Sol as OpenAI’s 2026 frontier agents, and perhaps Gemini 3.1 Pro Preview / Qwen3.6 Max Preview as additional long-horizon alternatives. Recent benchmark commentary suggests Chinese frontier models and OpenAI/Anthropic flagships now dominate the agentic/coding upper range, while DeepSeek V4 Flash remains the top value pick. [5][9] This tier should be the place to surface those newer frontier agents, not just value models.*

#### 🔄 Model Swaps & Lineup Adjustments
| Action | Previous Model | Proposed Model | Price Delta | Benchmark & Engineering Justification |
| :--- | :--- | :--- | :--- | :--- |
| **SWAP** | DeepSeek V4 Pro (deepseek/deepseek-v4-pro) | `DeepSeek V4 Pro 0813 (deepseek/deepseek-v4-pro-0813)` | $0.50/$1.00 vs $1.12/$3.37 (+124.0% input, +237.0% output) | GA release is the safer long-horizon default with better production readiness. |
| **RETAIN** | Nemotron 3 Ultra 550B (Free) (nvidia/nemotron-3-ultra-550b-a55b:free) | `Nemotron 3 Ultra 550B (Free) (nvidia/nemotron-3-ultra-550b-a55b:free)` | $0.00/$0.00 vs $0.00/$0.00 (0% delta) | Free experimentation lane for long-horizon orchestration. |
| **RETAIN** | Ox Alpha (Stealth Free) (stealth/ox-alpha) | `Ox Alpha (Stealth Free) (stealth/ox-alpha)` | $0.00/$0.00 vs $0.00/$0.00 (0% delta) | Free fallback and A/B lane remains useful. |
| **RETAIN** | Qwen 3.7 Plus (qwen/qwen3.7-plus) | `Qwen 3.7 Plus (qwen/qwen3.7-plus)` | $0.32/$1.28 vs $0.32/$1.28 (0% delta) | Strong value long-horizon workhorse. |
| **ADD** | None | `Claude Fable 5 (anthropic/claude-fable-5)` | $10.00/$50.00 vs new option | Native Fable-class Anthropic model for the heaviest autonomous workflow loops. |
| **ADD** | None | `GPT-5.6 Terra (openai/gpt-5.6-terra)` | $2.00/$12.00 vs new option | Balanced OpenAI frontier model for long-context agent work. |
| **ADD** | None | `GPT-5.6 Sol (openai/gpt-5.6-sol)` | $2.00/$10.00 vs new option | Higher-end OpenAI reasoning/coding option for severe workloads. |
| **ADD** | None | `Gemini 3.1 Pro Preview (google/gemini-3.1-pro-preview)` | $2.00/$12.00 vs new option | Google frontier reasoning model with improved agent reliability and software engineering performance. |

#### 📋 Full Proposed Options for Tier
| Model ID | Display Name | Live Price ($In / $Out) | Context | Status | Link | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [`nvidia/nemotron-3-ultra-550b-a55b:free`](https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b:free) | Nemotron 3 Ultra 550B (Free) | **$0.00/$0.00** | 1M Context | Alternative | [View](https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b:free) | Free long-context reasoning lane. |
| [`stealth/ox-alpha`](https://openrouter.ai/stealth/ox-alpha) | Ox Alpha (Stealth Free) | **Live API** | 1M Context | Alternative | [View](https://openrouter.ai/stealth/ox-alpha) | Free stealth fallback. |
| [`qwen/qwen3.7-plus`](https://openrouter.ai/qwen/qwen3.7-plus) | Qwen 3.7 Plus | **$0.32/$1.28** | 1M Context | Alternative | [View](https://openrouter.ai/qwen/qwen3.7-plus) | Strong value long-horizon workhorse. |
| [`deepseek/deepseek-v4-pro-0813`](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) | DeepSeek V4 Pro 0813 | **$1.12/$3.37** | 1M Context | **⭐ Recommended** | [View](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) | Best cost/performance default for the tier. |
| [`openai/gpt-5.6-terra`](https://openrouter.ai/openai/gpt-5.6-terra) | GPT-5.6 Terra | **$2.00/$12.00** | 1M Context | Alternative | [View](https://openrouter.ai/openai/gpt-5.6-terra) | Balanced OpenAI long-horizon option. |
| [`openai/gpt-5.6-sol`](https://openrouter.ai/openai/gpt-5.6-sol) | GPT-5.6 Sol | **$2.00/$10.00** | 1M Context | Alternative | [View](https://openrouter.ai/openai/gpt-5.6-sol) | High-end OpenAI flagship for serious workflows. |
| [`google/gemini-3.1-pro-preview`](https://openrouter.ai/google/gemini-3.1-pro-preview) | Gemini 3.1 Pro Preview | **$2.00/$12.00** | 1M Context | Alternative | [View](https://openrouter.ai/google/gemini-3.1-pro-preview) | Google frontier model for reliable agents and software tasks. |
| [`anthropic/claude-fable-5`](https://openrouter.ai/anthropic/claude-fable-5) | Claude Fable 5 | **$10.00/$50.00** | 1M Context | Alternative | [View](https://openrouter.ai/anthropic/claude-fable-5) | Native Anthropic long-horizon orchestration ceiling. |

---

### 🏷️ MYTHOS TIER (Frontier Intelligence & Uncompromising Quality) (`claude-mythos-1`)
- **Current Recommended (in `claude-threepio`):** `Claude Opus 5 (anthropic/claude-opus-5) — $5.00/$25.00`
- **Proposed Recommended:** **`Claude Opus 4.8 (anthropic/claude-opus-4.8) — $5.00/$25.00`**
- **Recommendation Shift Rationale:** The recommended model should shift from Opus 5 to Opus 4.8 only if the product team values the currently exposed GA Opus-class snapshot in OpenRouter’s catalog over a later alias semantics ambiguity. In practice, the broader recommendation is to surface both Claude Opus 4.8 and Opus 5, but keep Opus 4.8 as the stable documented option and Opus 5 as the latest ceiling when available. For maximal frontier quality, GPT-5.5/5.6 Pro and the newest Gemini/Qwen/XAI options should also be present.

*The current Mythos tier is directionally correct but not complete enough for a frontier category. It already contains Claude Opus 5, DeepSeek V4 Pro, Kimi K3, GPT-5.6 Terra, and Claude Sonnet 4.6; however, the catalog now has richer ceiling options and a clearer separation between stable premium models and latest frontier snapshots. Claude Opus 4.8 and Opus 5 are both at $5/$25, so this is a lateral recommendation change rather than a price-driven one; the choice depends on whether the product wants the most explicit stable GA front-end or the latest alias. GPT-5.5 Pro and GPT-5.2 Pro are now present, but the more practical ceiling for this tier is GPT-5.6 Sol Pro / GPT-5.6 Pro family, which preserves the same extreme pricing class while offering newer reasoning. DeepSeek V4 Pro 0813, Qwen3.8 Max, Qwen3 Max Thinking, Gemini 3.1 Pro Preview, Grok 4.20/4.6, and Claude Fable 5 all belong here as well. Benchmark roundups continue to place Claude Opus-class models and the newest OpenAI/Google frontier models among the highest-capability systems, while Chinese models have narrowed or closed the gap in coding and agentic tasks. [5][9] Mythos should therefore emphasize ceiling, not cost efficiency.*

#### 🔄 Model Swaps & Lineup Adjustments
| Action | Previous Model | Proposed Model | Price Delta | Benchmark & Engineering Justification |
| :--- | :--- | :--- | :--- | :--- |
| **RETAIN** | DeepSeek V4 Pro (deepseek/deepseek-v4-pro) | `DeepSeek V4 Pro 0813 (deepseek/deepseek-v4-pro-0813)` | $0.50/$1.00 vs $1.12/$3.37 (+124.0% input, +237.0% output) | Updated GA DeepSeek snapshot is the more credible frontier-default choice for an uncompromising tier. |
| **RETAIN** | Kimi K3 (moonshotai/kimi-k3) | `Kimi K3 (moonshotai/kimi-k3)` | $3.00/$15.00 vs $3.00/$15.00 (0% delta) | Still a top multimodal reasoning/coding ceiling from Moonshot. |
| **RETAIN** | GPT-5.6 Terra (openai/gpt-5.6-terra) | `GPT-5.6 Terra (openai/gpt-5.6-terra)` | $2.00/$12.00 vs $2.00/$12.00 (0% delta) | Balanced frontier OpenAI choice remains useful in Mythos. |
| **RETAIN** | Claude Sonnet 4.6 (anthropic/claude-sonnet-4.6) | `Claude Sonnet 4.6 (anthropic/claude-sonnet-4.6)` | $3.00/$15.00 vs $3.00/$15.00 (0% delta) | Useful premium fallback beneath the absolute ceiling. |
| **ADD** | None | `Claude Opus 4.8 (anthropic/claude-opus-4.8)` | $5.00/$25.00 vs new option | Stable documented Opus-class ceiling; strongest Anthropic frontier option in the catalog. |
| **ADD** | None | `GPT-5.5 Pro (openai/gpt-5.5-pro)` | $30.00/$180.00 vs new option | Extreme OpenAI frontier ceiling for highest-stakes reasoning and professional workloads. |
| **ADD** | None | `GPT-5.6 Sol Pro (openai/gpt-5.6-sol-pro)` | $2.00/$10.00 vs new option | A newer high-capability OpenAI option that is more suitable than older tiers for frontier tasks. |
| **ADD** | None | `Qwen: Qwen3.8 Max (qwen/qwen3.8-max)` | $2.00/$6.00 vs new option | New Alibaba flagship multimodal reasoning model; strong ceiling in the open-weight frontier class. |
| **ADD** | None | `SpaceXAI: Grok 4.20 (x-ai/grok-4.20)` | $1.25/$2.50 vs new option | Highly competitive frontier reasoning and tool-calling model with low-latency positioning. |
| **ADD** | None | `Claude Fable 5 (anthropic/claude-fable-5)` | $10.00/$50.00 vs new option | Mythos-class autonomous knowledge work and coding model; belongs in the uncompromising frontier tier. |

#### 📋 Full Proposed Options for Tier
| Model ID | Display Name | Live Price ($In / $Out) | Context | Status | Link | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [`anthropic/claude-opus-4.8`](https://openrouter.ai/anthropic/claude-opus-4.8) | Claude Opus 4.8 | **$5.00/$25.00** | 1M Context | **⭐ Recommended** | [View](https://openrouter.ai/anthropic/claude-opus-4.8) | Best stable Anthropic-quality ceiling and best documented Opus-class frontier anchor. |
| [`anthropic/claude-opus-5`](https://openrouter.ai/anthropic/claude-opus-5) | Claude Opus 5 | **$5.00/$25.00** | 1M Context | Alternative | [View](https://openrouter.ai/anthropic/claude-opus-5) | Latest Opus-family ceiling if the product wants to privilege recency. |
| [`openai/gpt-5.5-pro`](https://openrouter.ai/openai/gpt-5.5-pro) | GPT-5.5 Pro | **$30.00/$180.00** | 1M Context | Alternative | [View](https://openrouter.ai/openai/gpt-5.5-pro) | Maximum-cost OpenAI frontier option. |
| [`openai/gpt-5.6-sol-pro`](https://openrouter.ai/openai/gpt-5.6-sol-pro) | GPT-5.6 Sol Pro | **$2.00/$10.00** | 1M Context | Alternative | [View](https://openrouter.ai/openai/gpt-5.6-sol-pro) | Modern OpenAI frontier model with strong reasoning balance. |
| [`qwen/qwen3.8-max`](https://openrouter.ai/qwen/qwen3.8-max) | Qwen3.8 Max | **$2.00/$6.00** | 1M Context | Alternative | [View](https://openrouter.ai/qwen/qwen3.8-max) | Alibaba’s current flagship frontier model. |
| [`x-ai/grok-4.20`](https://openrouter.ai/x-ai/grok-4.20) | Grok 4.20 | **$1.25/$2.50** | 2M Context | Alternative | [View](https://openrouter.ai/x-ai/grok-4.20) | Fast frontier-quality alternative with strong tool-calling. |
| [`anthropic/claude-fable-5`](https://openrouter.ai/anthropic/claude-fable-5) | Claude Fable 5 | **$10.00/$50.00** | 1M Context | Alternative | [View](https://openrouter.ai/anthropic/claude-fable-5) | Autonomous-workflow ceiling for Mythos tier. |
| [`deepseek/deepseek-v4-pro-0813`](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) | DeepSeek V4 Pro 0813 | **$1.12/$3.37** | 1M Context | Alternative | [View](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) | Budget-friendly frontier choice for users who still want a ceiling-capable model. |

---

## 💡 Maintainer Action Items
- [ ] Review proposed model replacements and pricing deltas above.
- [ ] Verify context window requirements (1M context preserved for agentic flows).
- [ ] Merge this PR to update the default curated recommendations in `claude-threepio`.