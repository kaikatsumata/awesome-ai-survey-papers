# Awesome AI Survey Papers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**Languages:** [日本語](README.md) · **English**

> A curated collection of high-quality **survey, review, and overview papers** from top AI conferences, journals, and arXiv. It is designed as a fast starting point for finding authoritative review papers across AI research.

**955 survey papers** across 30 fields, with 122 companion repositories. Last updated 2026-06-07.

Each item uses the format `[title](paper URL) — *venue year* · 📈 citations — note — [`companion repo`](github) ⭐stars🟢freshness · [project](page)`.

Legend: 📈 citation count (Semantic Scholar) · ⭐ GitHub stars · freshness 🟢 updated within 6 months / 🟡 within 18 months / 🔴 older. Survey companion repositories may still be valuable for coverage and authority even when stale.

> 📑 Full metadata, statistics, and collection methodology are available in [`docs/research-notes.md`](docs/research-notes.md) (Japanese).

## Table of Contents

- [🧠 Large Language Models (LLM)](#-large-language-models-llm) (82)
- [🎨 Generative AI and Diffusion Models](#-generative-ai-and-diffusion-models) (30)
- [🖼️ Multimodal and Vision-Language AI](#-multimodal-and-vision-language-ai) (22)
- [💬 Natural Language Processing (NLP)](#-natural-language-processing-nlp) (79)
- [🔊 Speech and Signal Processing](#-speech-and-signal-processing) (24)
- [👁️ Computer Vision (CV)](#-computer-vision-cv) (108)
- [📈 Machine Learning (General)](#-machine-learning-general) (101)
- [📐 Learning Theory](#-learning-theory) (18)
- [🎮 Reinforcement Learning (RL)](#-reinforcement-learning-rl) (34)
- [🤖 Robotics and Embodied AI](#-robotics-and-embodied-ai) (22)
- [👥 Multi-Agent Systems](#-multi-agent-systems) (21)
- [🕸️ Graph Neural Networks (GNN)](#-graph-neural-networks-gnn) (33)
- [🔗 Knowledge Representation and Knowledge Graphs](#-knowledge-representation-and-knowledge-graphs) (30)
- [🎯 Causal Inference](#-causal-inference) (15)
- [⏱️ Time Series and Spatio-Temporal AI](#-time-series-and-spatio-temporal-ai) (20)
- [⛏️ Data Mining](#-data-mining) (29)
- [🗄️ Databases and Data Management](#-databases-and-data-management) (17)
- [🔍 Information Retrieval (IR)](#-information-retrieval-ir) (17)
- [🛒 Recommender Systems](#-recommender-systems) (21)
- [🌐 Web and Social Computing](#-web-and-social-computing) (21)
- [🛡️ Trustworthy AI (Fairness, XAI, and Safety)](#-trustworthy-ai-fairness-xai-and-safety) (31)
- [📡 Federated Learning](#-federated-learning) (19)
- [🖐️ HCI and Human-AI Interaction](#-hci-and-human-ai-interaction) (18)
- [🧬 Evolutionary Computation](#-evolutionary-computation) (13)
- [🔢 Theoretical Computer Science](#-theoretical-computer-science) (18)
- [🔬 AI for Science](#-ai-for-science) (20)
- [🌟 Artificial Intelligence (General)](#-artificial-intelligence-general) (15)
- [🧩 Neural Network Foundations](#-neural-network-foundations) (30)
- [🏭 Applications and Cross-Domain AI](#-applications-and-cross-domain-ai) (29)
- [📊 Data-Centric AI and Evaluation](#-data-centric-ai-and-evaluation) (18)

## 🧠 Large Language Models (LLM)

### Code LLM

- [Large Language Models for Software Engineering: A Systematic Literature Review](https://arxiv.org/abs/2308.10620) — *ACM TOSEM 2023* · 📈996 — A systematic literature review on code LLM, summarizing key methods, datasets, applications, and research directions.
- [A Survey on Large Language Models for Code Generation](https://arxiv.org/abs/2406.00515) — *arXiv 2024* · 📈948 — A comprehensive survey on code LLM, with emphasis on benchmarks, evaluation, and representative methods. — [`huybery/Awesome-Code-LLM`](https://github.com/huybery/Awesome-Code-LLM) ⭐1284🔴
- [Unifying the Perspectives of NLP and Software Engineering: A Survey on Language Models for Code](https://arxiv.org/abs/2311.07989) — *TMLR 2023* · 📈113 — A comprehensive survey on code LLM, organizing major methods, taxonomies, and design choices. — [`codefuse-ai/Awesome-Code-LLM`](https://github.com/codefuse-ai/Awesome-Code-LLM) ⭐3376🟢

### Code Reasoning

- [Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence in LLMs](https://arxiv.org/abs/2502.19411) — *arXiv 2025* · 📈50 — A survey on code reasoning, organizing major methods, taxonomies, and design choices.

### Compression / Quantization

- [A Survey on Model Compression for Large Language Models](https://arxiv.org/abs/2308.07633) — *TACL 2023* · 📈446 — A survey on compression and quantization, organizing major methods, taxonomies, and design choices.
- [Efficient Large Language Models: A Survey](https://arxiv.org/abs/2312.03863) — *TMLR 2023* · 📈232 — A comprehensive survey on compression and quantization, organizing major methods, taxonomies, and design choices. — [`AIoT-MLSys-Lab/Efficient-LLMs-Survey`](https://github.com/AIoT-MLSys-Lab/Efficient-LLMs-Survey) ⭐1260🟡
- [The Efficiency Spectrum of Large Language Models: An Algorithmic Survey](https://arxiv.org/abs/2312.00678) — *arXiv 2023* · 📈38 — A survey on compression and quantization, surveying major methods, techniques, and algorithmic choices.

### Context Engineering

- [A Survey of Context Engineering for Large Language Models](https://arxiv.org/abs/2507.13334) — *arXiv 2025* · 📈105 — A comprehensive survey on context engineering, organizing major methods, taxonomies, and design choices. — [`Meirtz/Awesome-Context-Engineering`](https://github.com/Meirtz/Awesome-Context-Engineering) ⭐3172🟢

### Continual Learning

- [Towards Lifelong Learning of Large Language Models: A Survey](https://arxiv.org/abs/2406.06391) — *ACM Computing Surveys 2024* · 📈94 — A survey on continual learning, organizing major methods, taxonomies, and design choices.

### Data Agents

- [A Survey of Data Agents: Emerging Paradigm or Overstated Hype?](https://arxiv.org/abs/2510.23587) — *arXiv 2025* · 📈26 — A survey on data agents, summarizing key methods, datasets, applications, and research directions. — [`HKUSTDial/awesome-data-agents`](https://github.com/HKUSTDial/awesome-data-agents) ⭐573🟢

### Diffusion Language Models

- [A Survey on Diffusion Language Models](https://arxiv.org/abs/2508.10875) — *arXiv 2025* · 📈64 — A recent survey on diffusion language models, summarizing key methods, datasets, applications, and research directions. — [`VILA-Lab/Awesome-DLMs`](https://github.com/VILA-Lab/Awesome-DLMs) ⭐1077🟢

### Efficient Inference / KV Cache

- [A Survey on Efficient Inference for Large Language Models](https://arxiv.org/abs/2404.14294) — *arXiv 2024* · 📈230 — A survey on efficient inference and KV cache, with comparative analysis of representative methods and systems.
- [LLM Inference Unveiled: Survey and Roofline Model Insights](https://arxiv.org/abs/2402.16363) — *arXiv 2024* · 📈185 — A survey on efficient inference and KV cache, summarizing key methods, datasets, applications, and research directions.
- [Towards Efficient Generative LLM Serving: A Survey from Algorithms to Systems](https://arxiv.org/abs/2312.15234) — *ACM Computing Surveys 2023* · 📈156 — A survey on efficient inference and KV cache, surveying major methods, techniques, and algorithmic choices.

### Efficient Reasoning

- [Stop Overthinking: A Survey on Efficient Reasoning for Large Language Models](https://arxiv.org/abs/2503.16419) — *arXiv 2025* · 📈392 — A comprehensive survey on efficient reasoning, organizing major methods, taxonomies, and design choices. — [`Eclipsess/Awesome-Efficient-Reasoning-LLMs`](https://github.com/Eclipsess/Awesome-Efficient-Reasoning-LLMs) ⭐770🟢
- [A Survey of Efficient Reasoning for Large Reasoning Models: Language, Multimodality, and Beyond](https://arxiv.org/abs/2503.21614) — *arXiv 2025* · 📈131 — A survey on efficient reasoning, organizing major methods, taxonomies, and design choices. — [`XiaoYee/Awesome_Efficient_LRM_Reasoning`](https://github.com/XiaoYee/Awesome_Efficient_LRM_Reasoning) ⭐354🟢

### Emergent Abilities / Scaling

- [Emergent Abilities in Large Language Models: A Survey](https://arxiv.org/abs/2503.05788) — *arXiv 2025* · 📈50 — A survey on emergent abilities and scaling, organizing major methods, taxonomies, and design choices.

### GUI Agents

- [Large Language Model-Brained GUI Agents: A Survey](https://arxiv.org/abs/2411.18279) — *arXiv 2024* · 📈171 — A comprehensive survey on GUI agents, organizing major methods, taxonomies, and design choices. — [`vyokky/LLM-Brained-GUI-Agents-Survey`](https://github.com/vyokky/LLM-Brained-GUI-Agents-Survey) ⭐230🟡

### GraphRAG

- [A Survey of Graph Retrieval-Augmented Generation for Customized Large Language Models](https://arxiv.org/abs/2501.13958) — *arXiv 2025* · 📈109 — A comprehensive survey on graphrag, organizing major methods, taxonomies, and design choices. — [`DEEP-PolyU/Awesome-GraphRAG`](https://github.com/DEEP-PolyU/Awesome-GraphRAG) ⭐2437🟢

### Hallucination

- [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://arxiv.org/abs/2311.05232) — *ACM TOIS 2023* · 📈2959 — A standard comprehensive survey on hallucination, covering methods, challenges, and future research directions. — [`LuckyyySTA/Awesome-LLM-hallucination`](https://github.com/LuckyyySTA/Awesome-LLM-hallucination) ⭐335🔴
- [Siren's Song in the AI Ocean: A Survey on Hallucination in Large Language Models](https://arxiv.org/abs/2309.01219) — *arXiv 2023* · 📈1014 — A survey on hallucination, organizing major methods, taxonomies, and design choices. — [`HillZhang1999/llm-hallucination-survey`](https://github.com/HillZhang1999/llm-hallucination-survey) ⭐1085🟡
- [A Comprehensive Survey of Hallucination Mitigation Techniques in Large Language Models](https://arxiv.org/abs/2401.01313) — *arXiv 2024* · 📈450 — A comprehensive survey on hallucination, with comparative analysis of representative methods and systems.

### In-Context Learning

- [A Survey on In-context Learning](https://arxiv.org/abs/2301.00234) — *EMNLP 2023* · 📈1046 — A standard comprehensive survey on in-context learning, organizing major methods, taxonomies, and design choices. — [`EgoAlpha/prompt-in-context-learning`](https://github.com/EgoAlpha/prompt-in-context-learning) ⭐2240🟢

### In-Context Learning Theory

- [The Mystery of In-Context Learning: A Comprehensive Survey on Interpretation and Analysis](https://arxiv.org/abs/2311.00237) — *EMNLP 2023* · 📈46 — A comprehensive comprehensive survey on in-context learning theory, covering theoretical foundations, methods, and implications.

### Instruction Tuning

- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) — *NeurIPS 2022* · 📈21402 — The InstructGPT paper that established instruction-following language-model training with human feedback.
- [Instruction Tuning for Large Language Models: A Survey](https://arxiv.org/abs/2308.10792) — *arXiv 2023* · 📈878 — A standard survey on instruction tuning, covering core methods, applications, and research trends. — [`xiaoya-li/Instruction-Tuning-Survey`](https://github.com/xiaoya-li/Instruction-Tuning-Survey) ⭐232🟡

### KV Cache Compression

- [KV Cache Compression for Inference Efficiency in LLMs: A Review](https://arxiv.org/abs/2508.06297) — *arXiv preprint 2025* · 📈7 — A review on KV cache compression, summarizing key methods, datasets, applications, and research directions.

### Knowledge & Dataset Distillation for LLMs

- [Knowledge Distillation and Dataset Distillation of Large Language Models: Emerging Trends, Challenges, and Future Directions](https://arxiv.org/abs/2504.14772) — *arXiv preprint 2025* · 📈40 — A comprehensive key reference on knowledge & dataset distillation for llms, surveying major methods, techniques, and algorithmic choices.

### Knowledge Distillation

- [A Survey on Knowledge Distillation of Large Language Models](https://arxiv.org/abs/2402.13116) — *arXiv 2024* · 📈330 — A comprehensive survey on knowledge distillation, organizing major methods, taxonomies, and design choices. — [`Tebmer/Awesome-Knowledge-Distillation-of-LLMs`](https://github.com/Tebmer/Awesome-Knowledge-Distillation-of-LLMs) ⭐1284🟡

### Knowledge Editing

- [Editing Large Language Models: Problems, Methods, and Opportunities](https://arxiv.org/abs/2305.13172) — *EMNLP 2023* · 📈455 — A key reference on knowledge editing, covering methods, challenges, and future research directions. — [`zjunlp/KnowledgeEditingPapers`](https://github.com/zjunlp/KnowledgeEditingPapers) ⭐1231🟡
- [Knowledge Editing for Large Language Models: A Survey](https://arxiv.org/abs/2310.16218) — *ACM Computing Surveys 2023* · 📈253 — A standard survey on knowledge editing, with emphasis on benchmarks, evaluation, and representative methods.
- [A Comprehensive Study of Knowledge Editing for Large Language Models](https://arxiv.org/abs/2401.01286) — *arXiv 2024* · 📈161 — A key reference on knowledge editing, organizing major methods, taxonomies, and design choices. — [`zjunlp/EasyEdit`](https://github.com/zjunlp/EasyEdit) ⭐2839🟢

### Knowledge Mechanisms

- [Knowledge Mechanisms in Large Language Models: A Survey and Perspective](https://arxiv.org/abs/2407.15017) — *EMNLP Findings 2024* · 📈69 — A survey on knowledge mechanisms, summarizing key methods, datasets, applications, and research directions. — [`zjunlp/KnowledgeEditingPapers`](https://github.com/zjunlp/KnowledgeEditingPapers) ⭐1231🟡

### LLM Agents

- [A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432) — *Frontiers of Computer Science 2023* · 📈3020 — A standard survey on LLM agents, with emphasis on benchmarks, evaluation, and representative methods. — [`Paitesanshi/LLM-Agent-Survey`](https://github.com/Paitesanshi/LLM-Agent-Survey) ⭐2901🟡
- [The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/abs/2309.07864) — *arXiv 2023* · 📈1776 — A comprehensive survey on LLM agents, summarizing key methods, datasets, applications, and research directions. — [`WooooDyy/LLM-Agent-Paper-List`](https://github.com/WooooDyy/LLM-Agent-Paper-List) ⭐8143🟡
- [ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate](https://arxiv.org/abs/2308.07201) — *ICLR 2024* · 📈928 — A key reference on LLM agents, with emphasis on benchmarks, evaluation, and representative methods. — [`thunlp/ChatEval`](https://github.com/thunlp/ChatEval) ⭐335🔴

### LLM Evaluation

- [A Survey on Evaluation of Large Language Models](https://arxiv.org/abs/2307.03109) — *ACM TIST 2023* · 📈3406 — A standard survey on LLM evaluation, with emphasis on benchmarks, evaluation, and representative methods. — [`MLGroupJLU/LLM-eval-survey`](https://github.com/MLGroupJLU/LLM-eval-survey) ⭐1600🟢
- [Evaluating Large Language Models: A Comprehensive Survey](https://arxiv.org/abs/2310.19736) — *arXiv 2023* · 📈311 — A comprehensive comprehensive survey on LLM evaluation, with emphasis on benchmarks, evaluation, and representative methods. — [`tjunlp-lab/Awesome-LLMs-Evaluation-Papers`](https://github.com/tjunlp-lab/Awesome-LLMs-Evaluation-Papers) ⭐803🔴

### LLM General

- [A Survey of Large Language Models](https://arxiv.org/abs/2303.18223) — *arXiv 2023* · 📈4522 — A comprehensive, large-scale survey of LLM pretraining, adaptation, usage, and evaluation. — [`RUCAIBox/LLMSurvey`](https://github.com/RUCAIBox/LLMSurvey) ⭐12171🟡
- [A Comprehensive Overview of Large Language Models](https://arxiv.org/abs/2307.06435) — *arXiv 2023* · 📈1667 — An overview on large language models, organizing major methods, taxonomies, and design choices.
- [Large Language Models: A Survey](https://arxiv.org/abs/2402.06196) — *arXiv 2024* · 📈975 — A survey on large language models, with emphasis on benchmarks, evaluation, and representative methods.
- [Datasets for Large Language Models: A Comprehensive Survey](https://arxiv.org/abs/2402.18041) — *arXiv 2024* · 📈133 — A comprehensive comprehensive survey on large language models, with emphasis on benchmarks, evaluation, and representative methods.

### LLM Unlearning

- [A Comprehensive Survey of Machine Unlearning Techniques for Large Language Models](https://arxiv.org/abs/2503.01854) — *arXiv 2025* · 📈29 — A comprehensive comprehensive survey on LLM unlearning, organizing major methods, taxonomies, and design choices.

### Long Context

- [Advancing Transformer Architecture in Long-Context LLMs: A Comprehensive Survey](https://arxiv.org/abs/2311.12351) — *arXiv 2023* · 📈121 — A comprehensive comprehensive survey on long context, organizing major methods, taxonomies, and design choices. — [`Strivin0311/long-llms-learning`](https://github.com/Strivin0311/long-llms-learning) ⭐274🔴
- [Beyond the Limits: A Survey of Techniques to Extend the Context Length in Large Language Models](https://arxiv.org/abs/2402.02244) — *IJCAI 2024* · 📈103 — A survey on long context, organizing major methods, taxonomies, and design choices.
- [The What, Why, and How of Context Length Extension Techniques in Large Language Models](https://arxiv.org/abs/2401.07872) — *arXiv 2024* · 📈47 — A comprehensive key reference on long context, with emphasis on benchmarks, evaluation, and representative methods.

### Long Context Modeling

- [A Comprehensive Survey on Long Context Language Modeling](https://arxiv.org/abs/2503.17407) — *arXiv 2025* · 📈111 — A comprehensive comprehensive survey on long context modeling, with emphasis on benchmarks, evaluation, and representative methods. — [`Xnhyacinth/Awesome-LLM-Long-Context-Modeling`](https://github.com/Xnhyacinth/Awesome-LLM-Long-Context-Modeling) ⭐2113🟢

### Mathematical Reasoning

- [A Survey on Large Language Models for Mathematical Reasoning](https://arxiv.org/abs/2506.08446) — *arXiv 2025* · 📈47 — A survey on mathematical reasoning, organizing major methods, taxonomies, and design choices.

### Mechanistic Interpretability

- [A Survey on Sparse Autoencoders: Interpreting the Internal Mechanisms of Large Language Models](https://arxiv.org/abs/2503.05613) — *arXiv 2025* · 📈54 — A survey on mechanistic interpretability, organizing major methods, taxonomies, and design choices.

### Mixture-of-Experts

- [A Survey on Mixture of Experts in Large Language Models](https://arxiv.org/abs/2407.06204) — *IEEE TKDE 2024* · 📈314 — A survey on mixture-of-experts, covering core methods, applications, and research trends. — [`withinmiaov/A-Survey-on-Mixture-of-Experts-in-LLMs`](https://github.com/withinmiaov/A-Survey-on-Mixture-of-Experts-in-LLMs) ⭐504🟢

### Multilingual LLM

- [A Survey on Multilingual Large Language Models: Corpora, Alignment, and Bias](https://arxiv.org/abs/2404.00929) — *arXiv 2024* · 📈127 — A survey on multilingual LLM, organizing major methods, taxonomies, and design choices.

### Parameter-Efficient Fine-Tuning

- [Parameter-Efficient Fine-Tuning for Large Models: A Comprehensive Survey](https://arxiv.org/abs/2403.14608) — *TMLR 2024* · 📈938 — A comprehensive comprehensive survey on parameter-efficient fine-tuning, organizing major methods, taxonomies, and design choices.
- [Parameter-Efficient Fine-Tuning Methods for Pretrained Language Models: A Critical Review and Assessment](https://arxiv.org/abs/2312.12148) — *arXiv 2023* · 📈344 — A review on parameter-efficient fine-tuning, with emphasis on benchmarks, evaluation, and representative methods.
- [Scaling Down to Scale Up: A Guide to Parameter-Efficient Fine-Tuning](https://arxiv.org/abs/2303.15647) — *arXiv 2023* · 📈276 — A key reference on parameter-efficient fine-tuning, with comparative analysis of representative methods and systems.
- [A Survey on LoRA of Large Language Models](https://arxiv.org/abs/2407.11046) — *Frontiers of Computer Science 2024* · 📈147 — A survey on parameter-efficient fine-tuning, covering core methods, applications, and research trends. — [`ZJU-LLMs/Awesome-LoRAs`](https://github.com/ZJU-LLMs/Awesome-LoRAs) ⭐271🔴

### Persona / Role-Play

- [Two Tales of Persona in LLMs: A Survey of Role-Playing and Personalization](https://arxiv.org/abs/2406.01171) — *arXiv 2024* · 📈258 — A survey on persona and role-play, organizing major methods, taxonomies, and design choices.

### Personal LLM Agents

- [Personal LLM Agents: Insights and Survey about the Capability, Efficiency and Security](https://arxiv.org/abs/2401.05459) — *arXiv 2024* · 📈342 — A survey on personal LLM agents, organizing major methods, taxonomies, and design choices. — [`MobileLLM/Personal_LLM_Agents_Survey`](https://github.com/MobileLLM/Personal_LLM_Agents_Survey) ⭐430🔴

### RL for Deep Research Agents

- [Reinforcement Learning Foundations for Deep Research Systems: A Survey](https://arxiv.org/abs/2509.06733) — *arXiv preprint 2025* · 📈8 — A survey on RL for deep research agents, organizing major methods, taxonomies, and design choices.

### RL for LLMs

- [Reinforcement Learning Meets Large Language Models: A Survey of Advancements and Applications Across the LLM Lifecycle](https://arxiv.org/abs/2509.16679) — *arXiv preprint 2025* · 📈23 — A survey on RL for llms, summarizing key methods, datasets, applications, and research directions.

### RL for Reasoning

- [A Survey of Reinforcement Learning for Large Reasoning Models](https://arxiv.org/abs/2509.08827) — *arXiv 2025* · 📈140 — A comprehensive survey on RL for reasoning, organizing major methods, taxonomies, and design choices.

### RLHF / Alignment

- [Safe RLHF: Safe Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2310.12773) — *ICLR 2024* · 📈707 — A key reference on RLHF and alignment, surveying major methods, techniques, and algorithmic choices.
- [AI Alignment: A Comprehensive Survey](https://arxiv.org/abs/2310.19852) — *arXiv 2023* · 📈353 — A comprehensive comprehensive survey on RLHF and alignment, organizing major methods, taxonomies, and design choices. — [`PKU-Alignment/AlignmentSurvey`](https://github.com/PKU-Alignment/AlignmentSurvey) ⭐137🔴 · [project](https://alignmentsurvey.com)
- [Large Language Model Alignment: A Survey](https://arxiv.org/abs/2309.15025) — *arXiv 2023* · 📈316 — A survey on RLHF and alignment, with emphasis on benchmarks, evaluation, and representative methods.
- [Secrets of RLHF in Large Language Models Part I: PPO](https://arxiv.org/abs/2307.04964) — *arXiv 2023* · 📈275 — A key reference on RLHF and alignment, summarizing key methods, datasets, applications, and research directions.

### Reasoning / Chain-of-Thought

- [Towards Reasoning in Large Language Models: A Survey](https://arxiv.org/abs/2212.10403) — *ACL Findings 2022* · 📈898 — A survey on reasoning and chain-of-thought, with emphasis on benchmarks, evaluation, and representative methods.
- [Navigate through Enigmatic Labyrinth: A Survey of Chain of Thought Reasoning](https://arxiv.org/abs/2309.15402) — *ACL 2024* · 📈258 — A survey on reasoning and chain-of-thought, covering methods, challenges, and future research directions. — [`Zoeyyao27/CoT-Igniting-Agent`](https://github.com/Zoeyyao27/CoT-Igniting-Agent) ⭐365🔴
- [LLM Post-Training: A Deep Dive into Reasoning Large Language Models](https://arxiv.org/abs/2502.21321) — *arXiv 2025* · 📈102 — A key reference on reasoning and chain-of-thought, summarizing key methods, datasets, applications, and research directions.

### Retrieval-Augmented Generation

- [A Survey on RAG Meeting LLMs: Towards Retrieval-Augmented Large Language Models](https://arxiv.org/abs/2405.06211) — *KDD 2024* · 📈879 — A survey on retrieval-augmented generation, covering core methods, applications, and research trends.
- [Retrieval-Augmented Generation for AI-Generated Content: A Survey](https://arxiv.org/abs/2402.19473) — *arXiv 2024* · 📈596 — A comprehensive survey on retrieval-augmented generation, covering core methods, applications, and research trends. — [`hymie122/RAG-Survey`](https://github.com/hymie122/RAG-Survey) ⭐1788🔴

### Role-Play

- [The Oscars of AI Theater: A Survey on Role-Playing with Language Models](https://arxiv.org/abs/2407.11484) — *arXiv 2024* · 📈56 — A comprehensive survey on role-play, organizing major methods, taxonomies, and design choices.

### Safety / Jailbreak

- [Trustworthy LLMs: A Survey and Guideline for Evaluating Large Language Models' Alignment](https://arxiv.org/abs/2308.05374) — *arXiv 2023* · 📈542 — A survey on safety and jailbreak, with emphasis on benchmarks, evaluation, and representative methods.
- [Jailbreak Attacks and Defenses Against Large Language Models: A Survey](https://arxiv.org/abs/2407.04295) — *arXiv 2024* · 📈275 — A survey on safety and jailbreak, organizing major methods, taxonomies, and design choices.
- [Attacks, Defenses and Evaluations for LLM Conversation Safety: A Survey](https://arxiv.org/abs/2402.09283) — *NAACL 2024* · 📈160 — A survey on safety and jailbreak, with emphasis on benchmarks, evaluation, and representative methods. — [`niconi19/LLM-Conversation-Safety`](https://github.com/niconi19/LLM-Conversation-Safety) ⭐111🔴

### Self-Correction

- [Automatically Correcting Large Language Models: Surveying the landscape of diverse self-correction strategies](https://arxiv.org/abs/2308.03188) — *TACL 2023* · 📈285 — A survey on self-correction, organizing major methods, taxonomies, and design choices.

### Small Language Models

- [A Comprehensive Survey of Small Language Models in the Era of Large Language Models](https://arxiv.org/abs/2411.03350) — *arXiv 2024* · 📈193 — A comprehensive comprehensive survey on small language models, covering core methods, applications, and research trends.
- [A Survey of Small Language Models](https://arxiv.org/abs/2410.20011) — *arXiv 2024* · 📈49 — A survey on small language models, organizing major methods, taxonomies, and design choices.

### Speculative Decoding

- [Closer Look at Efficient Inference Methods: A Survey of Speculative Decoding](https://arxiv.org/abs/2411.13157) — *arXiv preprint 2024* · 📈7 — A comprehensive survey on speculative decoding, organizing major methods, taxonomies, and design choices.

### Test-Time Compute

- [A Survey of Test-Time Compute: From Intuitive Inference to Deliberate Reasoning](https://arxiv.org/abs/2501.02497) — *arXiv 2025* · 📈19 — A survey on test-time compute, organizing major methods, taxonomies, and design choices.

### Text Watermarking

- [A Survey of Text Watermarking in the Era of Large Language Models](https://arxiv.org/abs/2312.07913) — *arXiv 2023* · 📈167 — A survey on text watermarking, with emphasis on benchmarks, evaluation, and representative methods.

### Theory of Mind

- [A Survey of Theory of Mind in Large Language Models: Evaluations, Representations, and Safety Risks](https://arxiv.org/abs/2502.06470) — *arXiv 2025* · 📈7 — A survey on theory of mind, with emphasis on benchmarks, evaluation, and representative methods.

### Tool Use

- [Tool Learning with Foundation Models](https://arxiv.org/abs/2304.08354) — *ACM Computing Surveys 2023* · 📈399 — A standard comprehensive key reference on tool use, organizing major methods, taxonomies, and design choices. — [`OpenBMB/BMTools`](https://github.com/OpenBMB/BMTools) ⭐2773🔴
- [What Are Tools Anyway? A Survey from the Language Model Perspective](https://arxiv.org/abs/2403.15452) — *COLM 2024* · 📈64 — A survey on tool use, summarizing key methods, datasets, applications, and research directions.

## 🎨 Generative AI and Diffusion Models

### 3D Generation

- [Generative AI meets 3D: A Survey on Text-to-3D in AIGC Era](https://arxiv.org/abs/2305.06131) — *arXiv 2023* · 📈102 — A survey on 3D generation, organizing major methods, taxonomies, and design choices.
- [Advances in 3D Generation: A Survey](https://arxiv.org/abs/2401.17807) — *arXiv 2024* · 📈91 — A survey on 3D generation, covering core methods, applications, and research trends.

### 4D Generation

- [Advances in 4D Generation: A Survey](https://arxiv.org/abs/2503.14501) — *arXiv 2025* · 📈0 — A comprehensive survey on 4D generation, covering core methods, applications, and research trends.

### AIGC General

- [A Comprehensive Survey of AI-Generated Content (AIGC): A History of Generative AI from GAN to ChatGPT](https://arxiv.org/abs/2303.04226) — *arXiv 2023* · 📈798 — A comprehensive survey on AIGC general, summarizing key methods, datasets, applications, and research directions.

### Audio / Music Generation

- [Sparks of Large Audio Models: A Survey and Outlook](https://arxiv.org/abs/2308.12792) — *arXiv 2023* · 📈63 — A comprehensive survey on audio and music generation, summarizing key methods, datasets, applications, and research directions. — [`EmulationAI/awesome-large-audio-models`](https://github.com/EmulationAI/awesome-large-audio-models) ⭐732🟢

### Autoregressive Visual Generation

- [Autoregressive Models in Vision: A Survey](https://arxiv.org/abs/2411.05902) — *TMLR 2024* · 📈51 — A survey on autoregressive visual generation, organizing major methods, taxonomies, and design choices. — [`ChaofanTao/Autoregressive-Models-in-Vision-Survey`](https://github.com/ChaofanTao/Autoregressive-Models-in-Vision-Survey) ⭐796🟢

### Concept Erasure

- [A Comprehensive Survey on Concept Erasure in Text-to-Image Diffusion Models](https://arxiv.org/abs/2502.14896) — *arXiv 2025* · 📈9 — A comprehensive survey on concept erasure, organizing major methods, taxonomies, and design choices.

### Controllable Generation

- [Controllable Generation with Text-to-Image Diffusion Models: A Survey](https://arxiv.org/abs/2403.04279) — *IEEE TPAMI 2024* · 📈94 — A survey on controllable generation, organizing major methods, taxonomies, and design choices. — [`PRIV-Creation/Awesome-Controllable-T2I-Diffusion-Models`](https://github.com/PRIV-Creation/Awesome-Controllable-T2I-Diffusion-Models) ⭐1113🟡

### Diffusion Acceleration

- [Efficient Diffusion Models: A Comprehensive Survey from Principles to Practices](https://arxiv.org/abs/2410.11795) — *TMLR 2024* · 📈53 — A comprehensive survey on diffusion acceleration, summarizing key methods, datasets, applications, and research directions. — [`AIoT-MLSys-Lab/Efficient-Diffusion-Model-Survey`](https://github.com/AIoT-MLSys-Lab/Efficient-Diffusion-Model-Survey) ⭐184🟢

### Diffusion Distillation

- [A Survey on Pre-Trained Diffusion Model Distillations](https://arxiv.org/abs/2502.08364) — *arXiv 2025* · 📈5 — A survey on diffusion distillation, organizing major methods, taxonomies, and design choices.

### Diffusion Theory

- [Score-based Diffusion Models via Stochastic Differential Equations -- a Technical Tutorial](https://arxiv.org/abs/2402.07487) — *arXiv 2024* · 📈50 — A tutorial survey on diffusion theory, covering theoretical foundations, methods, and implications.

### Efficient Diffusion

- [Efficient Diffusion Models: A Survey](https://arxiv.org/abs/2502.06805) — *TMLR 2025* · 📈41 — A survey on efficient diffusion, organizing major methods, taxonomies, and design choices. — [`AIoT-MLSys-Lab/Efficient-Diffusion-Model-Survey`](https://github.com/AIoT-MLSys-Lab/Efficient-Diffusion-Model-Survey) ⭐184🟢

### GAN

- [NIPS 2016 Tutorial: Generative Adversarial Networks](https://arxiv.org/abs/1701.00160) — *NIPS Tutorial 2016* · 📈1811 — A highly cited standard tutorial survey on GAN, covering theoretical foundations, methods, and implications.
- [A Review on Generative Adversarial Networks: Algorithms, Theory, and Applications](https://arxiv.org/abs/2001.06937) — *IEEE TKDE 2020* · 📈1108 — A standard comprehensive review on GAN, covering core methods, applications, and research trends.
- [Generative Adversarial Networks: Challenges, Solutions, and Future Directions](https://arxiv.org/abs/2005.00065) — *ACM Computing Surveys 2021* · 📈452 — A standard key reference on GAN, covering methods, challenges, and future research directions.
- [Generative Adversarial Networks in Computer Vision: A Survey and Taxonomy](https://arxiv.org/abs/1906.01529) — *ACM Computing Surveys 2021* · 📈92 — A highly cited comprehensive survey on GAN, covering core methods, applications, and research trends.

### Human Motion Generation

- [Human Motion Generation: A Survey](https://arxiv.org/abs/2307.10894) — *IEEE TPAMI 2023* · 📈136 — A survey on human motion generation, summarizing key methods, datasets, applications, and research directions.

### Image Editing

- [Diffusion Model-Based Image Editing: A Survey](https://arxiv.org/abs/2402.17525) — *IEEE TPAMI 2024* · 📈265 — A survey on image editing, organizing major methods, taxonomies, and design choices. — [`SiatMMLab/Awesome-Diffusion-Model-Based-Image-Editing-Methods`](https://github.com/SiatMMLab/Awesome-Diffusion-Model-Based-Image-Editing-Methods) ⭐713🟡
- [A Survey of Multimodal-Guided Image Editing with Text-to-Image Diffusion Models](https://arxiv.org/abs/2406.14555) — *arXiv 2024* · 📈63 — A survey on image editing, summarizing key methods, datasets, applications, and research directions.

### Music Generation

- [Vision-to-Music Generation: A Survey](https://arxiv.org/abs/2503.21254) — *ISMIR 2025* · 📈5 — A survey on music generation, with emphasis on benchmarks, evaluation, and representative methods. — [`wzk1015/Awesome-Vision-to-Music-Generation`](https://github.com/wzk1015/Awesome-Vision-to-Music-Generation) ⭐124🟡

### Normalizing Flow

- [Normalizing Flows: An Introduction and Review of Current Methods](https://arxiv.org/abs/1908.09257) — *IEEE TPAMI 2019* · 📈58 — A standard recent review on normalizing flow, organizing major methods, taxonomies, and design choices.

### Personalization

- [A Survey on Personalized Content Synthesis with Diffusion Models](https://arxiv.org/abs/2405.05538) — *arXiv 2024* · 📈38 — A survey on personalization, organizing major methods, taxonomies, and design choices.

### Text-to-Image

- [RenAIssance: A Survey into AI Text-to-Image Generation in the Era of Large Model](https://arxiv.org/abs/2309.00810) — *IEEE TPAMI 2023* · 📈79 — A comprehensive survey on text-to-image, summarizing key methods, datasets, applications, and research directions.

### Text-to-Video

- [A Survey on Video Diffusion Models](https://arxiv.org/abs/2310.10647) — *ACM Computing Surveys 2023* · 📈278 — A standard survey on text-to-video, organizing major methods, taxonomies, and design choices. — [`ChenHsing/Awesome-Video-Diffusion-Models`](https://github.com/ChenHsing/Awesome-Video-Diffusion-Models) ⭐2293🟢
- [Sora as a World Model? A Complete Survey on Text-to-Video Generation](https://arxiv.org/abs/2403.05131) — *arXiv 2024* · 📈72 — A survey on text-to-video, organizing major methods, taxonomies, and design choices.
- [Video Diffusion Models: A Survey](https://arxiv.org/abs/2405.03150) — *TMLR 2024* · 📈45 — A survey on text-to-video, organizing major methods, taxonomies, and design choices. — [`ndrwmlnk/Awesome-Video-Diffusion-Models`](https://github.com/ndrwmlnk/Awesome-Video-Diffusion-Models) ⭐56🟡

### VAE

- [An Introduction to Variational Autoencoders](https://arxiv.org/abs/1906.02691) — *Foundations and Trends in ML 2019* · 📈3048 — A standard comprehensive key reference on VAE, covering theoretical foundations, methods, and implications.

### Video Editing

- [Diffusion Model-Based Video Editing: A Survey](https://arxiv.org/abs/2407.07111) — *arXiv 2024* · 📈51 — A survey on video editing, covering theoretical foundations, methods, and implications.

### Video Generation

- [Controllable Video Generation: A Survey](https://arxiv.org/abs/2507.16869) — *arXiv 2025* · 📈64 — A comprehensive survey on video generation, organizing major methods, taxonomies, and design choices. — [`mayuelala/Awesome-Controllable-Video-Generation`](https://github.com/mayuelala/Awesome-Controllable-Video-Generation) ⭐741🟢

### World Models

- [Simulating the Real World: A Unified Survey of Multimodal Generative Models](https://arxiv.org/abs/2503.04641) — *IEEE TPAMI 2025* · 📈16 — A survey on world models, summarizing key methods, datasets, applications, and research directions. — [`ALEEEHU/World-Simulator`](https://github.com/ALEEEHU/World-Simulator) ⭐378🟢

## 🖼️ Multimodal and Vision-Language AI

### 3D-LLM

- [When LLMs step into the 3D World: A Survey and Meta-Analysis of 3D Tasks via Multi-modal Large Language Models](https://arxiv.org/abs/2405.10255) — *arXiv 2024* · 📈39 — A comprehensive systematic review and meta-analysis on 3D-LLM, organizing major methods, taxonomies, and design choices. — [`ActiveVisionLab/Awesome-LLM-3D`](https://github.com/ActiveVisionLab/Awesome-LLM-3D) ⭐2217🟢

### Audio-Visual

- [Deep Audio-Visual Learning: A Survey](https://arxiv.org/abs/2001.04758) — *International Journal of Automation and Computing 2020* · 📈191 — A standard survey on audio-visual, organizing major methods, taxonomies, and design choices.

### Autonomous Driving

- [A Survey on Multimodal Large Language Models for Autonomous Driving](https://arxiv.org/abs/2311.12320) — *WACV 2024* · 📈516 — A survey on autonomous driving, covering methods, challenges, and future research directions. — [`IrohXu/Awesome-Multimodal-LLM-Autonomous-Driving`](https://github.com/IrohXu/Awesome-Multimodal-LLM-Autonomous-Driving) ⭐311🔴

### Document AI

- [Document AI: Benchmarks, Models and Applications](https://arxiv.org/abs/2111.08609) — *arXiv 2021* · 📈97 — A benchmarking reference on document AI, with emphasis on benchmarks, evaluation, and representative methods.

### Embodied Multimodal

- [A Survey on Vision-Language-Action Models for Embodied AI](https://arxiv.org/abs/2405.14093) — *arXiv 2024* · 📈268 — A survey on embodied multimodal, organizing major methods, taxonomies, and design choices.
- [Agent AI: Surveying the Horizons of Multimodal Interaction](https://arxiv.org/abs/2401.03568) — *arXiv 2024* · 📈251 — A survey on embodied multimodal, summarizing key methods, datasets, applications, and research directions.

### Label-Free VLM Adaptation

- [Adapting Vision-Language Models Without Labels: A Comprehensive Survey](https://arxiv.org/abs/2508.05547) — *arXiv preprint 2025* · 📈6 — A comprehensive survey on label-free VLM adaptation, organizing major methods, taxonomies, and design choices. — [`tim-learn/Awesome-LabelFree-VLMs`](https://github.com/tim-learn/Awesome-LabelFree-VLMs) ⭐91🟢

### Mathematical Reasoning

- [A Survey of Mathematical Reasoning in the Era of Multimodal Large Language Model: Benchmark, Method & Challenges](https://arxiv.org/abs/2412.11936) — *ACL Findings 2024* · 📈58 — A survey on mathematical reasoning, with emphasis on benchmarks, evaluation, and representative methods.

### Mechanistic Interpretability

- [A Survey on Mechanistic Interpretability for Multi-Modal Foundation Models](https://arxiv.org/abs/2502.17516) — *arXiv 2025* · 📈34 — A survey on mechanistic interpretability, organizing major methods, taxonomies, and design choices.

### Multimodal Agents

- [Large Multimodal Agents: A Survey](https://arxiv.org/abs/2402.15116) — *arXiv 2024* · 📈111 — A comprehensive survey on multimodal agents, organizing major methods, taxonomies, and design choices. — [`jun0wanan/awesome-large-multimodal-agents`](https://github.com/jun0wanan/awesome-large-multimodal-agents) ⭐491🔴

### Multimodal Hallucination

- [Hallucination of Multimodal Large Language Models: A Survey](https://arxiv.org/abs/2404.18930) — *arXiv 2024* · 📈392 — A survey on multimodal hallucination, with emphasis on benchmarks, evaluation, and representative methods.

### Multimodal LLM

- [A Survey on Multimodal Large Language Models](https://arxiv.org/abs/2306.13549) — *National Science Review 2023* · 📈1390 — A standard survey on multimodal LLM, with emphasis on benchmarks, evaluation, and representative methods. — [`BradyFU/Awesome-Multimodal-Large-Language-Models`](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models) ⭐17868🟢
- [MM-LLMs: Recent Advances in MultiModal Large Language Models](https://arxiv.org/abs/2401.13601) — *ACL Findings 2024* · 📈425 — A key reference on multimodal LLM, organizing major methods, taxonomies, and design choices. — [project](https://mm-llms.github.io)

### Multimodal RAG

- [Ask in Any Modality: A Comprehensive Survey on Multimodal Retrieval-Augmented Generation](https://arxiv.org/abs/2502.08826) — *ACL Findings 2025* · 📈51 — A comprehensive comprehensive survey on multimodal RAG, organizing major methods, taxonomies, and design choices.
- [A Survey of Multimodal Retrieval-Augmented Generation](https://arxiv.org/abs/2504.08748) — *arXiv 2025* · 📈43 — A survey on multimodal RAG, surveying major methods, techniques, and algorithmic choices.

### Multimodal Reasoning

- [Multimodal Chain-of-Thought Reasoning: A Comprehensive Survey](https://arxiv.org/abs/2503.12605) — *arXiv 2025* · 📈179 — A comprehensive comprehensive survey on multimodal reasoning, organizing major methods, taxonomies, and design choices. — [`yaotingwangofficial/Awesome-MCoT`](https://github.com/yaotingwangofficial/Awesome-MCoT) ⭐1005🟢
- [Perception, Reason, Think, and Plan: A Survey on Large Multimodal Reasoning Models](https://arxiv.org/abs/2505.04921) — *arXiv 2025* · 📈73 — A comprehensive survey on multimodal reasoning, organizing major methods, taxonomies, and design choices.

### Prompt Engineering

- [A Systematic Survey of Prompt Engineering on Vision-Language Foundation Models](https://arxiv.org/abs/2307.12980) — *arXiv 2023* — A comprehensive survey on prompt engineering, organizing major methods, taxonomies, and design choices. — [`JindongGu/Awesome-Prompting-on-Vision-Language-Model`](https://github.com/JindongGu/Awesome-Prompting-on-Vision-Language-Model) ⭐510🟡

### Unified Multimodal Models

- [Unified Multimodal Understanding and Generation Models: Advances, Challenges, and Opportunities](https://arxiv.org/abs/2505.02567) — *arXiv 2025* · 📈63 — A key reference on unified multimodal models, covering methods, challenges, and future research directions. — [`AIDC-AI/Awesome-Unified-Multimodal-Models`](https://github.com/AIDC-AI/Awesome-Unified-Multimodal-Models) ⭐1278🟢

### Video LLM

- [Video Understanding with Large Language Models: A Survey](https://arxiv.org/abs/2312.17432) — *arXiv 2023* · 📈257 — A survey on video LLM, organizing major methods, taxonomies, and design choices.

### Video-Language

- [Video-Language Understanding: A Survey from Model Architecture, Model Training, and Data Perspectives](https://arxiv.org/abs/2406.05615) — *ACL Findings 2024* · 📈42 — A survey on video-language, organizing major methods, taxonomies, and design choices.

### Vision-Language Pretraining

- [Vision-Language Pre-training: Basics, Recent Advances, and Future Trends](https://arxiv.org/abs/2210.09263) — *Foundations and Trends in CV 2022* · 📈216 — A comprehensive key reference on vision-language pretraining, surveying major methods, techniques, and algorithmic choices.

## 💬 Natural Language Processing (NLP)

### Adversarial Attacks (NLP)

- [Adversarial Attacks on Deep Learning Models in Natural Language Processing: A Survey](https://arxiv.org/abs/1901.06796) — *ACM TIST 2019* · 📈57 — A standard comprehensive survey on adversarial attacks (NLP), organizing major methods, taxonomies, and design choices.
- [A Survey of Adversarial Defences and Robustness in NLP](https://arxiv.org/abs/2203.06414) — *ACM Computing Surveys 2022* · 📈36 — A survey on adversarial attacks (NLP), organizing major methods, taxonomies, and design choices.
- [Adversarial Attacks and Defense on Texts: A Survey](https://arxiv.org/abs/2005.14108) — *arXiv 2020* · 📈24 — A survey on adversarial attacks (NLP), organizing major methods, taxonomies, and design choices.

### Argument Mining

- [Large Language Models in Argument Mining: A Survey](https://arxiv.org/abs/2506.16383) — *arXiv 2025* · 📈14 — A survey on argument mining, organizing major methods, taxonomies, and design choices.

### Biomedical NLP

- [SECNLP: A Survey of Embeddings in Clinical Natural Language Processing](https://arxiv.org/abs/1903.01039) — *Journal of Biomedical Informatics 2019* · 📈95 — A survey on biomedical NLP, organizing major methods, taxonomies, and design choices.

### Code-switching

- [A Survey of Code-switched Speech and Language Processing](https://arxiv.org/abs/1904.00784) — *arXiv 2019* · 📈155 — A survey on code-switching, organizing major methods, taxonomies, and design choices.
- [The Decades Progress on Code-Switching Research in NLP: A Systematic Survey on Trends and Challenges](https://arxiv.org/abs/2212.09660) — *ACL Findings 2023* · 📈62 — A comprehensive survey on code-switching, covering methods, challenges, and future research directions.

### Computational Morphology

- [Recent advancements in computational morphology: A comprehensive survey](https://arxiv.org/abs/2406.05424) — *arXiv 2024* · 📈5 — A comprehensive comprehensive survey on computational morphology, organizing major methods, taxonomies, and design choices.

### Coreference Resolution

- [A Neural Entity Coreference Resolution Review](https://arxiv.org/abs/1910.09329) — *Expert Systems with Applications 2019* · 📈43 — A review on coreference resolution, with emphasis on benchmarks, evaluation, and representative methods.
- [Coreference Resolution for the Biomedical Domain: A Survey](https://arxiv.org/abs/2109.12424) — *arXiv 2021* · 📈20 — A survey on coreference resolution, organizing major methods, taxonomies, and design choices.

### Cross-lingual Transfer

- [Transfer Learning for Multi-lingual Tasks -- a Survey](https://arxiv.org/abs/2110.02052) — *arXiv 2021* · 📈6 — A survey on cross-lingual transfer, organizing major methods, taxonomies, and design choices.

### Data Augmentation (NLP)

- [A Survey of Data Augmentation Approaches for NLP](https://arxiv.org/abs/2105.03075) — *Findings of ACL 2021* · 📈980 — A standard comprehensive survey on data augmentation (NLP), organizing major methods, taxonomies, and design choices.

### Data-to-Text Generation

- [Innovations in Neural Data-to-text Generation: A Survey](https://arxiv.org/abs/2207.12571) — *arXiv 2022* · 📈12 — A survey on data-to-text generation, organizing major methods, taxonomies, and design choices.

### Deep Learning for NLP (Overview)

- [A Survey of the Usages of Deep Learning in Natural Language Processing](https://arxiv.org/abs/1807.10854) — *IEEE TNNLS 2021* · 📈12 — A highly cited survey on deep learning for NLP (overview), covering core methods, applications, and research trends.

### Dialogue State Tracking

- ["Do you follow me?": A Survey of Recent Approaches in Dialogue State Tracking](https://arxiv.org/abs/2207.14627) — *SIGDIAL 2022* · 📈36 — A recent survey on dialogue state tracking, organizing major methods, taxonomies, and design choices.

### Dialogue Systems

- [A Survey on Dialogue Systems: Recent Advances and New Frontiers](https://arxiv.org/abs/1711.01731) — *ACM SIGKDD Explorations 2017* · 📈766 — A standard survey on dialogue systems, summarizing key methods, datasets, applications, and research directions.
- [Recent Advances in Deep Learning Based Dialogue Systems: A Systematic Survey](https://arxiv.org/abs/2105.04387) — *Artificial Intelligence Review 2021* · 📈342 — A comprehensive survey on dialogue systems, organizing major methods, taxonomies, and design choices.
- [A Short Survey of Pre-trained Language Models for Conversational AI - A New Age in NLP](https://arxiv.org/abs/2104.10810) — *ACSW 2020* · 📈82 — A survey on dialogue systems, organizing major methods, taxonomies, and design choices.

### Discourse Parsing

- [A Survey of Implicit Discourse Relation Recognition](https://arxiv.org/abs/2203.02982) — *ACM Computing Surveys 2022* · 📈34 — A comprehensive survey on discourse parsing, organizing major methods, taxonomies, and design choices.

### Empathetic Dialogue

- [Empathetic Conversational Systems: A Review of Current Advances, Gaps, and Opportunities](https://arxiv.org/abs/2206.05017) — *IEEE Transactions on Affective Computing 2022* · 📈52 — A review on empathetic dialogue, summarizing key methods, datasets, applications, and research directions.

### Evaluation & Benchmarks

- [A Survey of Evaluation Metrics Used for NLG Systems](https://arxiv.org/abs/2008.12009) — *ACM Computing Surveys 2020* · 📈330 — A survey on evaluation & benchmarks, with emphasis on benchmarks, evaluation, and representative methods.
- [Survey on Factuality in Large Language Models: Knowledge, Retrieval and Domain-Specificity](https://arxiv.org/abs/2310.07521) — *arXiv 2023* · 📈286 — A survey on evaluation & benchmarks, organizing major methods, taxonomies, and design choices.

### Explainability (NLP)

- [A Survey of the State of Explainable AI for Natural Language Processing](https://arxiv.org/abs/2010.00711) — *AACL-IJCNLP 2020* · 📈461 — A standard survey on explainability (NLP), surveying major methods, techniques, and algorithmic choices.
- [Post-hoc Interpretability for Neural NLP: A Survey](https://arxiv.org/abs/2108.04840) — *ACM Computing Surveys 2021* · 📈312 — A survey on explainability (NLP), organizing major methods, taxonomies, and design choices.
- [Local Interpretations for Explainable Natural Language Processing: A Survey](https://arxiv.org/abs/2103.11072) — *ACM Computing Surveys 2021* · 📈70 — A survey on explainability (NLP), surveying major methods, techniques, and algorithmic choices.

### Fact-Checking

- [A Survey on Automated Fact-Checking](https://arxiv.org/abs/2108.11896) — *TACL 2021* · 📈724 — A standard survey on fact-checking, summarizing key methods, datasets, applications, and research directions.
- [Explainable Automated Fact-Checking: A Survey](https://arxiv.org/abs/2011.03870) — *COLING 2020* · 📈148 — A survey on fact-checking, surveying major methods, techniques, and algorithmic choices.
- [Generative Large Language Models in Automated Fact-Checking: A Survey](https://arxiv.org/abs/2407.02351) — *arXiv 2024* · 📈20 — A survey on fact-checking, organizing major methods, taxonomies, and design choices.

### Financial NLP

- [A Survey of Large Language Models in Finance (FinLLMs)](https://arxiv.org/abs/2402.02315) — *arXiv 2024* · 📈152 — A survey on financial NLP, covering methods, challenges, and future research directions.
- [Language Modeling for the Future of Finance: A Survey into Metrics, Tasks, and Data Opportunities](https://arxiv.org/abs/2504.07274) — *arXiv 2025* · 📈5 — A survey on financial NLP, summarizing key methods, datasets, applications, and research directions.

### Grammatical Error Correction

- [Grammatical Error Correction: A Survey of the State of the Art](https://arxiv.org/abs/2211.05166) — *Computational Linguistics 2023* · 📈130 — A standard comprehensive survey on grammatical error correction, with emphasis on benchmarks, evaluation, and representative methods.
- [A Comprehensive Survey of Grammar Error Correction](https://arxiv.org/abs/2005.06600) — *arXiv 2020* · 📈42 — A comprehensive comprehensive survey on grammatical error correction, organizing major methods, taxonomies, and design choices.

### Keyphrase Extraction

- [Keyphrase Generation: A Multi-Aspect Survey](https://arxiv.org/abs/1910.05059) — *FRUCT 2019* · 📈24 — A survey on keyphrase extraction, organizing major methods, taxonomies, and design choices.

### Legal NLP

- [Natural Language Processing for the Legal Domain: A Survey of Tasks, Datasets, Models, and Challenges](https://arxiv.org/abs/2410.21306) — *ACM Computing Surveys 2025* · 📈87 — A comprehensive survey on legal NLP, covering methods, challenges, and future research directions.

### Long Document Summarization

- [An Empirical Survey on Long Document Summarization: Datasets, Models and Metrics](https://arxiv.org/abs/2207.00939) — *ACM Computing Surveys 2022* · 📈176 — A survey on long document summarization, with emphasis on benchmarks, evaluation, and representative methods.

### Low-Resource & Multilingual

- [Neural Machine Translation for Low-Resource Languages: A Survey](https://arxiv.org/abs/2106.15115) — *ACM Computing Surveys 2021* · 📈360 — A survey on low-resource & multilingual, summarizing key methods, datasets, applications, and research directions.
- [A Survey on Low-Resource Neural Machine Translation](https://arxiv.org/abs/2107.04239) — *IJCAI 2021* · 📈75 — A survey on low-resource & multilingual, organizing major methods, taxonomies, and design choices.

### Machine Translation

- [Neural Machine Translation: A Review and Survey](https://arxiv.org/abs/1912.02047) — *JAIR 2020* · 📈424 — A standard comprehensive survey on machine translation, organizing major methods, taxonomies, and design choices.
- [A Survey of Deep Learning Techniques for Neural Machine Translation](https://arxiv.org/abs/2002.07526) — *arXiv 2020* · 📈153 — A comprehensive survey on machine translation, organizing major methods, taxonomies, and design choices.
- [A Survey on Non-Autoregressive Generation for Neural Machine Translation and Beyond](https://arxiv.org/abs/2204.09269) — *IEEE TPAMI 2022* · 📈126 — A survey on machine translation, organizing major methods, taxonomies, and design choices.

### Multi-document Summarization

- [Multi-document Summarization via Deep Learning Techniques: A Survey](https://arxiv.org/abs/2011.04843) — *ACM Computing Surveys 2020* · 📈160 — A comprehensive survey on multi-document summarization, organizing major methods, taxonomies, and design choices.
- [Survey on Multi-Document Summarization: Systematic Literature Review](https://arxiv.org/abs/2312.12915) — *arXiv 2023* · 📈1 — A systematic literature review on multi-document summarization, organizing major methods, taxonomies, and design choices.

### NLG Evaluation

- [Leveraging Large Language Models for NLG Evaluation: Advances and Challenges](https://arxiv.org/abs/2401.07103) — *EMNLP 2024* · 📈46 — A key reference on NLG evaluation, with emphasis on benchmarks, evaluation, and representative methods.

### Named Entity Recognition

- [A Survey on Deep Learning for Named Entity Recognition](https://arxiv.org/abs/1812.09449) — *IEEE TKDE 2020* · 📈1458 — A standard survey on named entity recognition, summarizing key methods, datasets, applications, and research directions.
- [Recent Advances in Named Entity Recognition: A Comprehensive Survey and Comparative Study](https://arxiv.org/abs/2401.10825) — *arXiv 2024* · 📈47 — A recent comprehensive survey on named entity recognition, with comparative analysis of representative methods and systems.

### Neural Topic Models

- [A Survey on Neural Topic Models: Methods, Applications, and Challenges](https://arxiv.org/abs/2401.15351) — *Artificial Intelligence Review 2024* · 📈103 — A comprehensive survey on neural topic models, covering methods, challenges, and future research directions.

### Persona Dialogue

- [Recent Trends in Personalized Dialogue Generation: A Review of Datasets, Methodologies, and Evaluations](https://arxiv.org/abs/2405.17974) — *LREC-COLING 2024* · 📈34 — A comprehensive review on persona dialogue, with emphasis on benchmarks, evaluation, and representative methods.

### Pretrained Language Models (BERT)

- [A Primer in BERTology: What We Know About How BERT Works](https://arxiv.org/abs/2002.12327) — *TACL 2020* · 📈1871 — A standard introductory survey on pretrained language models (BERT), summarizing key methods, datasets, applications, and research directions.
- [Pre-trained Models for Natural Language Processing: A Survey](https://arxiv.org/abs/2003.08271) — *Science China Technological Sciences 2020* · 📈1688 — A highly cited survey on pretrained language models (BERT), organizing major methods, taxonomies, and design choices.
- [Recent Advances in Natural Language Processing via Large Pre-Trained Language Models: A Survey](https://arxiv.org/abs/2111.01243) — *ACM Computing Surveys 2021* · 📈1525 — A comprehensive survey on pretrained language models (BERT), organizing major methods, taxonomies, and design choices.
- [Pre-Trained Models: Past, Present and Future](https://arxiv.org/abs/2106.07139) — *AI Open 2021* · 📈1064 — A comprehensive key reference on pretrained language models (BERT), summarizing key methods, datasets, applications, and research directions.

### Prompting

- [Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing](https://arxiv.org/abs/2107.13586) — *ACM Computing Surveys 2021* · 📈5409 — A key survey that systematizes prompting methods and the prompt-based NLP paradigm. — [`thunlp/PromptPapers`](https://github.com/thunlp/PromptPapers) ⭐4315🔴

### Question Answering

- [A Survey on Complex Knowledge Base Question Answering: Methods, Challenges and Solutions](https://arxiv.org/abs/2105.11644) — *IJCAI 2021* · 📈206 — A survey on question answering, covering methods, challenges, and future research directions.
- [QA Dataset Explosion: A Taxonomy of NLP Resources for Question Answering and Reading Comprehension](https://arxiv.org/abs/2107.12708) — *ACM Computing Surveys 2021* · 📈196 — A comprehensive taxonomy on question answering, organizing major methods, taxonomies, and design choices.
- [A Survey on Neural Machine Reading Comprehension](https://arxiv.org/abs/1906.03824) — *arXiv 2019* · 📈32 — A survey on question answering, organizing major methods, taxonomies, and design choices.

### Question Generation

- [A Survey on Neural Question Generation: Methods, Applications, and Prospects](https://arxiv.org/abs/2402.18267) — *IJCAI 2024* · 📈15 — A survey on question generation, organizing major methods, taxonomies, and design choices.

### Readability Assessment

- [Trends, Limitations and Open Challenges in Automatic Readability Assessment Research](https://arxiv.org/abs/2105.00973) — *LREC 2022* · 📈61 — A key reference on readability assessment, with emphasis on benchmarks, evaluation, and representative methods.

### Relation Extraction

- [A Comprehensive Survey on Relation Extraction: Recent Advances and New Frontiers](https://arxiv.org/abs/2306.02051) — *ACM Computing Surveys 2023* · 📈128 — A comprehensive survey on relation extraction, organizing major methods, taxonomies, and design choices.
- [A Survey of Deep Learning Methods for Relation Extraction](https://arxiv.org/abs/1705.03645) — *arXiv 2017* · 📈123 — A survey on relation extraction, summarizing key methods, datasets, applications, and research directions.

### Sarcasm Detection

- [A Survey of Multimodal Sarcasm Detection](https://arxiv.org/abs/2410.18882) — *IJCAI 2024* · 📈33 — A comprehensive survey on sarcasm detection, organizing major methods, taxonomies, and design choices.

### Sentiment Analysis

- [Deep Learning for Sentiment Analysis: A Survey](https://arxiv.org/abs/1801.07883) — *WIREs Data Mining and Knowledge Discovery 2018* · 📈1887 — A highly cited survey on sentiment analysis, summarizing key methods, datasets, applications, and research directions.
- [A Survey on Aspect-Based Sentiment Analysis: Tasks, Methods, and Challenges](https://arxiv.org/abs/2203.01054) — *IEEE TKDE 2022* · 📈407 — A comprehensive survey on sentiment analysis, covering methods, challenges, and future research directions.

### Stance Detection

- [A Survey on Stance Detection for Mis- and Disinformation Identification](https://arxiv.org/abs/2103.00242) — *NAACL Findings 2021* · 📈170 — A survey on stance detection, summarizing key methods, datasets, applications, and research directions.
- [A Survey of Stance Detection on Social Media: New Directions and Perspectives](https://arxiv.org/abs/2409.15690) — *arXiv 2024* · 📈16 — A survey on stance detection, covering methods, challenges, and future research directions.

### Summarization

- [A Survey on Neural Network-Based Summarization Methods](https://arxiv.org/abs/1804.04589) — *arXiv 2018* · 📈37 — A survey on summarization, organizing major methods, taxonomies, and design choices.
- [A Survey on Neural Abstractive Summarization Methods and Factual Consistency of Summarization](https://arxiv.org/abs/2204.09519) — *arXiv 2022* · 📈9 — A survey on summarization, summarizing key methods, datasets, applications, and research directions.

### Syntactic & Semantic Parsing

- [A Survey on Semantic Parsing](https://arxiv.org/abs/1812.00978) — *AKBC 2018* · 📈138 — A survey on syntactic & semantic parsing, summarizing key methods, datasets, applications, and research directions.

### Text Classification

- [Recent Trends in Deep Learning Based Natural Language Processing](https://arxiv.org/abs/1708.02709) — *IEEE Computational Intelligence Magazine 2018* · 📈3068 — A highly cited key reference on text classification, covering core methods, applications, and research trends.
- [Deep Learning Based Text Classification: A Comprehensive Review](https://arxiv.org/abs/2004.03705) — *ACM Computing Surveys 2020* · 📈1315 — A review on text classification, organizing major methods, taxonomies, and design choices.
- [A Survey on Text Classification: From Shallow to Deep Learning](https://arxiv.org/abs/2008.00364) — *ACM TIST 2020* · 📈524 — A survey on text classification, organizing major methods, taxonomies, and design choices.
- [Topic Modelling Meets Deep Neural Networks: A Survey](https://arxiv.org/abs/2103.00498) — *IJCAI 2021* · 📈167 — A comprehensive survey on text classification, organizing major methods, taxonomies, and design choices.

### Text Generation

- [Survey of the State of the Art in Natural Language Generation: Core Tasks, Applications and Evaluation](https://arxiv.org/abs/1703.09902) — *JAIR 2018* · 📈903 — A standard comprehensive survey on text generation, with emphasis on benchmarks, evaluation, and representative methods.

### Text Simplification

- [A Survey on Text Simplification](https://arxiv.org/abs/2008.08612) — *arXiv 2020* · 📈32 — A survey on text simplification, summarizing key methods, datasets, applications, and research directions.
- [Deep Learning Approaches to Lexical Simplification: A Survey](https://arxiv.org/abs/2305.12000) — *arXiv 2023* · 📈24 — A survey on text simplification, organizing major methods, taxonomies, and design choices.

### Text Style Transfer

- [A Survey of Text Style Transfer: Applications and Ethical Implications](https://arxiv.org/abs/2407.16737) — *arXiv 2024* · 📈2 — A survey on text style transfer, covering core methods, applications, and research trends.

### Word & Sentence Embeddings

- [A Survey on Contextual Embeddings](https://arxiv.org/abs/2003.07278) — *arXiv 2020* · 📈177 — A survey on word & sentence embeddings, covering core methods, applications, and research trends.
- [A Comprehensive Survey of Sentence Representations: From the BERT Epoch to the ChatGPT Era and Beyond](https://arxiv.org/abs/2305.12641) — *EACL 2024* · 📈21 — A comprehensive comprehensive survey on word & sentence embeddings, organizing major methods, taxonomies, and design choices.

### Word Embeddings

- [Word Embeddings: A Survey](https://arxiv.org/abs/1901.09069) — *arXiv 2019* · 📈243 — A standard survey on word embeddings, covering theoretical foundations, methods, and implications.

### Word Sense Disambiguation

- [A Survey on Lexical Ambiguity Detection and Word Sense Disambiguation](https://arxiv.org/abs/2403.16129) — *arXiv 2024* · 📈14 — A survey on word sense disambiguation, organizing major methods, taxonomies, and design choices.

## 🔊 Speech and Signal Processing

### Audio Foundation Models

- [Audio-Language Models for Audio-Centric Tasks: A Systematic Survey](https://arxiv.org/abs/2501.15177) — *arXiv 2025* · 📈1 — A comprehensive recent survey on audio foundation models, organizing major methods, taxonomies, and design choices.

### Automatic Speech Recognition (ASR)

- [A Review of Deep Learning Techniques for Speech Processing](https://arxiv.org/abs/2305.00359) — *Information Fusion 2023* · 📈339 — A comprehensive review on automatic speech recognition (ASR), organizing major methods, taxonomies, and design choices.
- [End-to-End Speech Recognition: A Survey](https://arxiv.org/abs/2303.03329) — *IEEE/ACM TASLP 2023* · 📈287 — A standard survey on automatic speech recognition (ASR), organizing major methods, taxonomies, and design choices.
- [Speech Recognition Using Deep Neural Networks: A Systematic Review](https://doi.org/10.1109/ACCESS.2019.2896880) — *IEEE Access 2019* — A highly cited standard review on automatic speech recognition (ASR), organizing major methods, taxonomies, and design choices.

### Controllable TTS

- [Towards Controllable Speech Synthesis in the Era of Large Language Models: A Systematic Survey](https://arxiv.org/abs/2412.06602) — *EMNLP 2025* · 📈26 — A comprehensive survey on controllable TTS, organizing major methods, taxonomies, and design choices. — [`imxtx/awesome-controllable-speech-synthesis`](https://github.com/imxtx/awesome-controllable-speech-synthesis) ⭐249🟢

### Keyword Spotting

- [Advances in Small-Footprint Keyword Spotting: A Comprehensive Review of Efficient Models and Algorithms](https://arxiv.org/abs/2506.11169) — *arXiv 2025* · 📈5 — A comprehensive review on keyword spotting, organizing major methods, taxonomies, and design choices.

### Multilingual ASR

- [A Survey of Multilingual Models for Automatic Speech Recognition](https://arxiv.org/abs/2202.12576) — *LREC 2022* · 📈52 — A survey on multilingual ASR, surveying major methods, techniques, and algorithmic choices.

### Music Information Retrieval

- [A Tutorial on Deep Learning for Music Information Retrieval](https://arxiv.org/abs/1709.04396) — *arXiv 2017* · 📈102 — A tutorial survey on music information retrieval, summarizing key methods, datasets, applications, and research directions.

### Self-Supervised Speech (wav2vec)

- [wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations](https://arxiv.org/abs/2006.11477) — *NeurIPS 2020* · 📈8412 — A foundational reference for self-supervised speech representation learning.
- [Self-Supervised Speech Representation Learning: A Review](https://arxiv.org/abs/2205.10643) — *IEEE JSTSP 2022* · 📈493 — A standard comprehensive review on self-supervised speech (wav2vec), organizing major methods, taxonomies, and design choices.

### Sound Event Detection

- [Sound Event Detection: A Tutorial](https://arxiv.org/abs/2107.05463) — *IEEE Signal Processing Magazine 2021* · 📈265 — A tutorial survey on sound event detection, with emphasis on benchmarks, evaluation, and representative methods.

### Speaker Recognition & Diarization

- [A Review of Speaker Diarization: Recent Advances with Deep Learning](https://arxiv.org/abs/2101.09624) — *Computer Speech & Language 2021* · 📈427 — A standard review on speaker recognition & diarization, organizing major methods, taxonomies, and design choices.

### Speech Emotion Recognition

- [A Comprehensive Survey on Multi-modal Conversational Emotion Recognition with Deep Learning](https://arxiv.org/abs/2312.05735) — *arXiv 2023* · 📈51 — A comprehensive comprehensive survey on speech emotion recognition, organizing major methods, taxonomies, and design choices.
- [Emotion Recognition and Generation: A Comprehensive Review of Face, Speech, and Text Modalities](https://arxiv.org/abs/2502.06803) — *arXiv 2025* · 📈9 — A comprehensive recent review on speech emotion recognition, surveying major methods, techniques, and algorithmic choices.

### Speech Enhancement & Separation

- [Supervised Speech Separation Based on Deep Learning: An Overview](https://arxiv.org/abs/1708.07524) — *IEEE/ACM TASLP 2018* · 📈1584 — A standard comprehensive overview on speech enhancement & separation, organizing major methods, taxonomies, and design choices.

### Speech LLM / Audio Foundation Models

- [A Survey on Speech Large Language Models for Understanding](https://arxiv.org/abs/2410.18908) — *arXiv 2024* · 📈87 — A comprehensive survey on speech LLM and audio foundation models, organizing major methods, taxonomies, and design choices.

### Speech Language Models

- [Recent Advances in Speech Language Models: A Survey](https://arxiv.org/abs/2410.03751) — *ACL 2025* · 📈109 — A comprehensive survey on speech language models, summarizing key methods, datasets, applications, and research directions. — [`dreamtheater123/Awesome-SpeechLM-Survey`](https://github.com/dreamtheater123/Awesome-SpeechLM-Survey) ⭐209🟡

### Speech Translation

- [Direct Speech-to-Speech Neural Machine Translation: A Survey](https://arxiv.org/abs/2411.14453) — *arXiv 2024* · 📈8 — A survey on speech translation, with emphasis on benchmarks, evaluation, and representative methods.

### Spoken Dialogue Systems

- [WavChat: A Survey of Spoken Dialogue Models](https://arxiv.org/abs/2411.13577) — *arXiv 2024* · 📈98 — A comprehensive survey on spoken dialogue systems, with emphasis on benchmarks, evaluation, and representative methods. — [`jishengpeng/WavChat`](https://github.com/jishengpeng/WavChat) ⭐317🔴

### Spoken Language Understanding (SLU)

- [A Survey on Spoken Language Understanding: Recent Advances and New Frontiers](https://arxiv.org/abs/2103.03095) — *IJCAI 2021* · 📈120 — A standard survey on spoken language understanding (SLU), organizing major methods, taxonomies, and design choices.

### Text-to-Speech (TTS)

- [A Survey on Neural Speech Synthesis](https://arxiv.org/abs/2106.15561) — *arXiv 2021* · 📈466 — A standard survey on text-to-speech (TTS), summarizing key methods, datasets, applications, and research directions.

### Voice Conversion

- [An Overview of Voice Conversion and its Challenges: From Statistical Modeling to Deep Learning](https://arxiv.org/abs/2008.03648) — *IEEE/ACM TASLP 2020* · 📈418 — A standard comprehensive overview on voice conversion, summarizing key methods, datasets, applications, and research directions.
- [Reimagining Speech: A Scoping Review of Deep Learning-Powered Voice Conversion](https://arxiv.org/abs/2311.08104) — *arXiv 2023* · 📈9 — A review on voice conversion, summarizing key methods, datasets, applications, and research directions.
- [Generative Adversarial Network based Voice Conversion: Techniques, Challenges, and Recent Advancements](https://arxiv.org/abs/2504.19197) — *arXiv 2025* · 📈7 — A comprehensive recent key reference on voice conversion, covering methods, challenges, and future research directions.

## 👁️ Computer Vision (CV)

### 3D Gaussian Splatting

- [A Survey on 3D Gaussian Splatting](https://arxiv.org/abs/2401.03890) — *TPAMI 2024* · 📈334 — A comprehensive survey on 3D gaussian splatting, covering core methods, applications, and research trends. — [`guikunchen/Awesome3DGS`](https://github.com/guikunchen/Awesome3DGS) ⭐92🟢

### 3D Object Detection

- [3D Object Detection for Autonomous Driving: A Comprehensive Survey](https://arxiv.org/abs/2206.09474) — *IJCV 2023* · 📈440 — A comprehensive comprehensive survey on 3D object detection, summarizing key methods, datasets, applications, and research directions. — [`PointsCoder/Awesome-3D-Object-Detection-for-Autonomous-Driving`](https://github.com/PointsCoder/Awesome-3D-Object-Detection-for-Autonomous-Driving) ⭐609🔴

### 3D Vision / Point Cloud

- [Deep Learning for 3D Point Clouds: A Survey](https://arxiv.org/abs/1912.12033) — *TPAMI 2021* · 📈2215 — A standard comprehensive survey on 3D vision and point cloud, organizing major methods, taxonomies, and design choices.
- [Transformers in 3D Point Clouds: A Survey](https://arxiv.org/abs/2205.07417) — *arXiv 2022* · 📈73 — A comprehensive survey on 3D vision and point cloud, organizing major methods, taxonomies, and design choices.

### 6D Pose Estimation

- [Deep Learning-Based Object Pose Estimation: A Comprehensive Survey](https://arxiv.org/abs/2405.07801) — *IJCV 2024* · 📈67 — A comprehensive comprehensive survey on 6D pose estimation, summarizing key methods, datasets, applications, and research directions.

### Action Recognition

- [Human Action Recognition from Various Data Modalities: A Review](https://arxiv.org/abs/2012.11866) — *TPAMI 2023* · 📈776 — A review on action recognition, organizing major methods, taxonomies, and design choices.
- [Going Deeper into Action Recognition: A Survey](https://arxiv.org/abs/1605.04988) — *Image and Vision Computing 2017* · 📈640 — A standard survey on action recognition, surveying major methods, techniques, and algorithmic choices.

### Adversarial Robustness

- [Threat of Adversarial Attacks on Deep Learning in Computer Vision: A Survey](https://arxiv.org/abs/1801.00553) — *IEEE Access 2018* · 📈2052 — A standard comprehensive survey on adversarial robustness, organizing major methods, taxonomies, and design choices.

### Anomaly Detection

- [Deep Learning for Anomaly Detection: A Review](https://arxiv.org/abs/2007.02500) — *CSUR 2021* · 📈1327 — A comprehensive review on anomaly detection, organizing major methods, taxonomies, and design choices.

### Camouflaged Object Detection

- [A Survey of Camouflaged Object Detection and Beyond](https://arxiv.org/abs/2408.14562) — *arXiv 2024* · 📈64 — A comprehensive recent survey on camouflaged object detection, summarizing key methods, datasets, applications, and research directions.

### Continual Learning

- [Class-Incremental Learning: A Survey](https://arxiv.org/abs/2302.03648) — *TPAMI 2023* · 📈349 — A comprehensive survey on continual learning, with comparative analysis of representative methods and systems.

### Crowd Counting

- [A Survey on Deep Learning-based Single Image Crowd Counting: Network Design, Loss Function and Supervisory Signal](https://arxiv.org/abs/2012.15685) — *Neurocomputing 2020* · 📈31 — A survey on crowd counting, organizing major methods, taxonomies, and design choices.

### Deepfake Detection

- [Deepfake Generation and Detection: A Benchmark and Survey](https://arxiv.org/abs/2403.17881) — *arXiv 2024* · 📈121 — A comprehensive survey on deepfake detection, with emphasis on benchmarks, evaluation, and representative methods.
- [Deepfake Detection: A Comprehensive Survey from the Reliability Perspective](https://arxiv.org/abs/2211.10881) — *ACM Computing Surveys 2022* · 📈120 — A comprehensive survey on deepfake detection, organizing major methods, taxonomies, and design choices.

### Depth Estimation

- [Monocular Depth Estimation Based On Deep Learning: An Overview](https://arxiv.org/abs/2003.06620) — *Science China Technological Sciences 2020* · 📈294 — An overview on depth estimation, surveying major methods, techniques, and algorithmic choices.

### Domain Adaptation

- [Deep Visual Domain Adaptation: A Survey](https://arxiv.org/abs/1802.03601) — *Neurocomputing 2018* · 📈2294 — A standard survey on domain adaptation, organizing major methods, taxonomies, and design choices.
- [Domain Adaptation for Visual Applications: A Comprehensive Survey](https://arxiv.org/abs/1702.05374) — *Springer (book chapter) 2017* · 📈548 — A standard comprehensive comprehensive survey on domain adaptation, summarizing key methods, datasets, applications, and research directions.

### Domain Generalization / Adaptation (CLIP)

- [CLIP-Powered Domain Generalization and Domain Adaptation: A Comprehensive Survey](https://arxiv.org/abs/2504.14280) — *arXiv preprint 2025* · 📈11 — A comprehensive comprehensive survey on domain generalization and adaptation (CLIP), organizing major methods, taxonomies, and design choices. — [`jindongli-Ai/Survey_on_CLIP-Powered_Domain_Generalization_and_Adaptation`](https://github.com/jindongli-Ai/Survey_on_CLIP-Powered_Domain_Generalization_and_Adaptation) ⭐76🟢

### Event Camera

- [Deep Learning for Event-based Vision: A Comprehensive Survey and Benchmarks](https://arxiv.org/abs/2302.08890) — *arXiv 2023* · 📈133 — A comprehensive comprehensive survey on event camera, with emphasis on benchmarks, evaluation, and representative methods.

### Face Generation/Editing

- [Face Generation and Editing with StyleGAN: A Survey](https://arxiv.org/abs/2212.09102) — *TPAMI 2022* · 📈93 — A survey on face generation/editing, organizing major methods, taxonomies, and design choices.

### Face Recognition

- [Deep Face Recognition: A Survey](https://arxiv.org/abs/1804.06655) — *Neurocomputing 2021* · 📈1421 — A standard comprehensive survey on face recognition, organizing major methods, taxonomies, and design choices.

### Facial Expression Recognition

- [Deep Facial Expression Recognition: A Survey](https://arxiv.org/abs/1804.08348) — *IEEE Trans. Affective Computing 2018* · 📈1647 — A survey on facial expression recognition, covering methods, challenges, and future research directions.
- [Deep Learning for Micro-expression Recognition: A Survey](https://arxiv.org/abs/2107.02823) — *IEEE Trans. Affective Computing 2021* · 📈135 — A survey on facial expression recognition, with emphasis on benchmarks, evaluation, and representative methods.

### Few-Shot Learning

- [Generalizing from a Few Examples: A Survey on Few-Shot Learning](https://arxiv.org/abs/1904.05046) — *CSUR 2020* · 📈2118 — A standard survey on few-shot learning, organizing major methods, taxonomies, and design choices.
- [Few-Shot Object Detection: A Comprehensive Survey](https://arxiv.org/abs/2112.11699) — *TNNLS 2023* · 📈117 — A comprehensive comprehensive survey on few-shot learning, organizing major methods, taxonomies, and design choices.

### Fine-Grained Recognition

- [Fine-Grained Image Analysis with Deep Learning: A Survey](https://arxiv.org/abs/2111.06119) — *TPAMI 2021* · 📈444 — A survey on fine-grained recognition, organizing major methods, taxonomies, and design choices.

### Foundation Models / Segmentation

- [A Comprehensive Survey on Segment Anything Model for Vision and Beyond](https://arxiv.org/abs/2305.08196) — *arXiv 2023* · 📈143 — A comprehensive comprehensive survey on foundation models and segmentation, covering core methods, applications, and research trends.

### Gait Recognition

- [Deep Gait Recognition: A Survey](https://arxiv.org/abs/2102.09546) — *TPAMI 2021* · 📈261 — A comprehensive survey on gait recognition, covering methods, challenges, and future research directions.

### Gaussian Splatting

- [3D Gaussian Splatting: Survey, Technologies, Challenges, and Opportunities](https://arxiv.org/abs/2407.17418) — *arXiv 2024* · 📈122 — A comprehensive survey on gaussian splatting, covering methods, challenges, and future research directions. — [`qqqqqqy0227/awesome-3DGS`](https://github.com/qqqqqqy0227/awesome-3DGS) ⭐308🟡
- [A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing, and Generation](https://arxiv.org/abs/2508.09977) — *arXiv 2025* · 📈19 — A survey on gaussian splatting, covering core methods, applications, and research trends. — [`heshuting555/Awesome-3DGS-Applications`](https://github.com/heshuting555/Awesome-3DGS-Applications) ⭐365🟢

### Gaze Estimation

- [Appearance-based Gaze Estimation With Deep Learning: A Review and Benchmark](https://arxiv.org/abs/2104.12668) — *TPAMI 2021* · 📈249 — A review on gaze estimation, with emphasis on benchmarks, evaluation, and representative methods.

### Hand Pose Estimation

- [Efficient Annotation and Learning for 3D Hand Pose Estimation: A Survey](https://arxiv.org/abs/2206.02257) — *IJCV 2022* · 📈26 — A survey on hand pose estimation, organizing major methods, taxonomies, and design choices.

### Human Pose Estimation

- [Deep learning for 3D human pose estimation and mesh recovery: A survey](https://arxiv.org/abs/2402.18844) — *Neurocomputing 2024* · 📈34 — A survey on human pose estimation, organizing major methods, taxonomies, and design choices.

### Human-Object Interaction

- [A Review of Human-Object Interaction Detection](https://arxiv.org/abs/2408.10641) — *arXiv 2024* · 📈11 — A comprehensive review on human-object interaction, surveying major methods, techniques, and algorithmic choices.

### Image Captioning

- [A Comprehensive Survey of Deep Learning for Image Captioning](https://arxiv.org/abs/1810.04020) — *CSUR 2019* · 📈884 — A comprehensive survey on image captioning, with emphasis on benchmarks, evaluation, and representative methods.

### Image Classification / Backbone

- [A Survey of Convolutional Neural Networks: Analysis, Applications, and Prospects](https://arxiv.org/abs/2004.02806) — *TNNLS 2022* · 📈4176 — A backbone survey of CNN history, representative architectures, applications, and prospects.

### Image Colorization

- [Image Colorization: A Survey and Dataset](https://arxiv.org/abs/2008.10774) — *Information Fusion 2020* · 📈106 — A survey on image colorization, organizing major methods, taxonomies, and design choices.

### Image Deblurring

- [Deep Image Deblurring: A Survey](https://arxiv.org/abs/2201.10700) — *IJCV 2022* · 📈377 — A survey on image deblurring, covering core methods, applications, and research trends.

### Image Dehazing

- [A Comprehensive Survey and Taxonomy on Single Image Dehazing Based on Deep Learning](https://arxiv.org/abs/2106.03323) — *ACM Computing Surveys 2021* · 📈98 — A comprehensive comprehensive survey on image dehazing, organizing major methods, taxonomies, and design choices.

### Image Deraining

- [Towards Unified Deep Image Deraining: A Survey and A New Benchmark](https://arxiv.org/abs/2310.03535) — *arXiv 2023* · 📈60 — A survey on image deraining, with emphasis on benchmarks, evaluation, and representative methods.

### Image Fusion

- [Multimodal Alignment and Fusion: A Survey](https://arxiv.org/abs/2411.17040) — *arXiv 2024* · 📈140 — A survey on image fusion, organizing major methods, taxonomies, and design choices.

### Image Generation (Diffusion)

- [Diffusion Models in Vision: A Survey](https://arxiv.org/abs/2209.04747) — *TPAMI 2023* · 📈2118 — A survey on image generation (diffusion), covering core methods, applications, and research trends. — [`CroitoruAlin/Diffusion-Models-in-Vision-A-Survey`](https://github.com/CroitoruAlin/Diffusion-Models-in-Vision-A-Survey) ⭐407🔴
- [Text-to-image Diffusion Models in Generative AI: A Survey](https://arxiv.org/abs/2303.07909) — *arXiv 2023* · 📈424 — A survey on image generation (diffusion), covering core methods, applications, and research trends.

### Image Generation (GAN)

- [Generative Adversarial Networks: An Overview](https://arxiv.org/abs/1710.07035) — *IEEE Signal Processing Magazine 2018* · 📈3730 — A standard overview of GAN training, architectures, and applications including image synthesis.
- [GAN Inversion: A Survey](https://arxiv.org/abs/2101.05278) — *TPAMI 2022* · 📈633 — A survey on image generation (GAN), surveying major methods, techniques, and algorithmic choices. — [`weihaox/GAN-Inversion`](https://github.com/weihaox/GAN-Inversion) ⭐1126🟡

### Image Inpainting

- [Deep Learning-based Image and Video Inpainting: A Survey](https://arxiv.org/abs/2401.03395) — *IJCV 2024* · 📈91 — A comprehensive survey on image inpainting, organizing major methods, taxonomies, and design choices.

### Image Matching / Local Features

- [Local Feature Matching Using Deep Learning: A Survey](https://arxiv.org/abs/2401.17592) — *Information Fusion 2024* · 📈101 — A survey on image matching and local features, organizing major methods, taxonomies, and design choices. — [`vignywang/Awesome-Local-Feature-Matching`](https://github.com/vignywang/Awesome-Local-Feature-Matching) ⭐157🔴

### Image Matting

- [Deep Image Matting: A Comprehensive Survey](https://arxiv.org/abs/2304.04672) — *arXiv 2023* · 📈22 — A comprehensive survey on image matting, organizing major methods, taxonomies, and design choices. — [`JizhiziLi/matting-survey`](https://github.com/JizhiziLi/matting-survey) ⭐201🔴

### Image Quality Assessment

- [A Survey on Image Quality Assessment: Insights, Analysis, and Future Outlook](https://arxiv.org/abs/2502.08540) — *arXiv 2025* · 📈15 — A recent survey on image quality assessment, with emphasis on benchmarks, evaluation, and representative methods.

### Image Restoration

- [Priors in Deep Image Restoration and Enhancement: A Survey](https://arxiv.org/abs/2206.02070) — *arXiv 2022* · 📈8 — A survey on image restoration, organizing major methods, taxonomies, and design choices. — [`yunfanLu/Awesome-Image-Prior`](https://github.com/yunfanLu/Awesome-Image-Prior) ⭐87🟡

### Long-Tailed Recognition

- [A Survey on Long-Tailed Visual Recognition](https://arxiv.org/abs/2205.13775) — *IJCV 2022* · 📈189 — A survey on long-tailed recognition, organizing major methods, taxonomies, and design choices.

### Low-Light Image Enhancement

- [Low-Light Image and Video Enhancement Using Deep Learning: A Survey](https://arxiv.org/abs/2104.10729) — *TPAMI 2021* · 📈550 — A comprehensive survey on low-light image enhancement, organizing major methods, taxonomies, and design choices. — [`ShenZheng2000/LLIE_Survey`](https://github.com/ShenZheng2000/LLIE_Survey) ⭐154🔴

### Medical Image Analysis

- [A Survey on Deep Learning in Medical Image Analysis](https://arxiv.org/abs/1702.05747) — *Medical Image Analysis 2017* · 📈13415 — A classic survey of deep learning for medical image analysis, organizing more than 300 papers.
- [Transformers in Medical Imaging: A Survey](https://arxiv.org/abs/2201.09873) — *Medical Image Analysis 2023* · 📈1145 — A survey on medical image analysis, covering core methods, applications, and research trends.

### Multi-Object Tracking

- [Deep Learning-Based Multi-Object Tracking: A Comprehensive Survey from Foundations to State-of-the-Art](https://arxiv.org/abs/2506.13457) — *arXiv 2025* · 📈7 — A comprehensive recent comprehensive survey on multi-object tracking, covering theoretical foundations, methods, and implications.

### Multi-View Stereo

- [Learning-based Multi-View Stereo: A Survey](https://arxiv.org/abs/2408.15235) — *arXiv 2024* · 📈31 — A survey on multi-view stereo, organizing major methods, taxonomies, and design choices.

### Neural Rendering

- [Advances in Neural Rendering](https://arxiv.org/abs/2111.05849) — *Computer Graphics Forum 2021* · 📈543 — A comprehensive key reference on neural rendering, summarizing key methods, datasets, applications, and research directions.

### Neural Rendering / NeRF

- [NeRF: Neural Radiance Field in 3D Vision: A Comprehensive Review](https://arxiv.org/abs/2210.00379) — *arXiv 2022* · 📈305 — A comprehensive review on neural rendering and nerf, covering core methods, applications, and research trends.
- [Neural Volume Rendering: NeRF And Beyond](https://arxiv.org/abs/2101.05204) — *arXiv 2021* · 📈71 — A key reference on neural rendering and nerf, summarizing key methods, datasets, applications, and research directions.

### Neural Style Transfer

- [Neural Style Transfer: A Review](https://arxiv.org/abs/1705.04058) — *TVCG 2017* · 📈857 — A standard review on neural style transfer, with emphasis on benchmarks, evaluation, and representative methods.

### OCR / Document Analysis

- [A Survey of Deep Learning Approaches for OCR and Document Understanding](https://arxiv.org/abs/2011.13534) — *arXiv 2020* · 📈88 — A survey on OCR and document analysis, organizing major methods, taxonomies, and design choices.

### OCR / Scene Text

- [Scene Text Detection and Recognition: The Deep Learning Era](https://arxiv.org/abs/1811.04256) — *IJCV 2021* · 📈490 — A standard key reference on OCR and scene text, organizing major methods, taxonomies, and design choices.

### Object Detection

- [Object Detection in 20 Years: A Survey](https://arxiv.org/abs/1905.05055) — *Proceedings of the IEEE 2023* · 📈3350 — A standard survey on object detection, surveying major methods, techniques, and algorithmic choices.
- [Deep Learning for Generic Object Detection: A Survey](https://arxiv.org/abs/1809.02165) — *IJCV 2020* · 📈2783 — A comprehensive survey on object detection, organizing major methods, taxonomies, and design choices.
- [A Survey of Deep Learning-based Object Detection](https://arxiv.org/abs/1907.09408) — *IEEE Access 2019* · 📈1129 — A comprehensive survey on object detection, organizing major methods, taxonomies, and design choices.
- [A Survey of Modern Deep Learning based Object Detection Models](https://arxiv.org/abs/2104.11892) — *Digital Signal Processing 2022* · 📈902 — A survey on object detection, organizing major methods, taxonomies, and design choices.

### Object Tracking

- [Deep Learning for Visual Tracking: A Comprehensive Survey](https://arxiv.org/abs/1912.00535) — *IEEE T-ITS 2022* · 📈355 — A comprehensive comprehensive survey on object tracking, with emphasis on benchmarks, evaluation, and representative methods.

### Open-Vocabulary Detection/Segmentation

- [Towards Open Vocabulary Learning: A Survey](https://arxiv.org/abs/2306.15880) — *TPAMI 2023* · 📈255 — A comprehensive survey on open-vocabulary detection/segmentation, summarizing key methods, datasets, applications, and research directions. — [`jianzongwu/Awesome-Open-Vocabulary`](https://github.com/jianzongwu/Awesome-Open-Vocabulary) ⭐998🟢
- [A Survey on Open-Vocabulary Detection and Segmentation: Past, Present, and Future](https://arxiv.org/abs/2307.09220) — *TPAMI 2023* · 📈101 — A survey on open-vocabulary detection/segmentation, organizing major methods, taxonomies, and design choices.

### Optical Flow

- [Optical Flow Estimation in the Deep Learning Age](https://arxiv.org/abs/2004.02853) — *arXiv 2020* · 📈41 — A standard key reference on optical flow, organizing major methods, taxonomies, and design choices.

### Panoptic Segmentation

- [Panoptic Segmentation: A Review](https://arxiv.org/abs/2111.10250) — *arXiv 2021* · 📈49 — A comprehensive review on panoptic segmentation, summarizing key methods, datasets, applications, and research directions.

### Person Re-identification

- [Deep Learning for Person Re-identification: A Survey and Outlook](https://arxiv.org/abs/2001.04193) — *TPAMI 2022* · 📈2134 — A standard survey on person re-identification, organizing major methods, taxonomies, and design choices.
- [Deep Learning for Video-based Person Re-Identification: A Survey](https://arxiv.org/abs/2303.11332) — *arXiv 2023* · 📈10 — A survey on person re-identification, organizing major methods, taxonomies, and design choices.

### Point Cloud

- [A Survey of Label-Efficient Deep Learning for 3D Point Clouds](https://arxiv.org/abs/2305.19812) — *TPAMI 2023* · 📈48 — A survey on point cloud, organizing major methods, taxonomies, and design choices.

### Point Cloud Completion

- [Comprehensive Review of Deep Learning-Based 3D Point Cloud Completion Processing and Analysis](https://arxiv.org/abs/2203.03311) — *IEEE T-ITS 2022* · 📈188 — A comprehensive review on point cloud completion, surveying major methods, techniques, and algorithmic choices.

### Point Cloud Registration

- [Deep Learning-Based Point Cloud Registration: A Comprehensive Survey and Taxonomy](https://arxiv.org/abs/2404.13830) — *IJCV 2024* · 📈12 — A comprehensive comprehensive survey on point cloud registration, organizing major methods, taxonomies, and design choices.

### Pose Estimation

- [Deep Learning-Based Human Pose Estimation: A Survey](https://arxiv.org/abs/2012.13392) — *CSUR 2023* · 📈932 — A survey on pose estimation, organizing major methods, taxonomies, and design choices.
- [2D Human Pose Estimation: A Survey](https://arxiv.org/abs/2204.07370) — *arXiv 2022* · 📈99 — A survey on pose estimation, organizing major methods, taxonomies, and design choices.

### Referring Segmentation

- [Multimodal Referring Segmentation: A Survey](https://arxiv.org/abs/2508.00265) — *arXiv 2025* · 📈22 — A survey on referring segmentation, summarizing key methods, datasets, applications, and research directions.

### Remote Sensing

- [Deep Learning in Remote Sensing: A Review](https://arxiv.org/abs/1710.03959) — *IEEE GRSM 2017* · 📈1848 — A standard review on remote sensing, covering core methods, applications, and research trends.

### Salient Object Detection

- [Salient Object Detection in the Deep Learning Era: An In-Depth Survey](https://arxiv.org/abs/1904.09146) — *TPAMI 2022* · 📈729 — A comprehensive survey on salient object detection, with emphasis on benchmarks, evaluation, and representative methods.
- [RGB-D Salient Object Detection: A Survey](https://arxiv.org/abs/2008.00230) — *Computational Visual Media 2020* · 📈298 — A comprehensive survey on salient object detection, summarizing key methods, datasets, applications, and research directions. — [`taozh2017/RGBD-SODsurvey`](https://github.com/taozh2017/RGBD-SODsurvey) ⭐372🔴

### Scene Graph Generation

- [Scene Graph Generation: A Comprehensive Survey](https://arxiv.org/abs/2201.00443) — *Neurocomputing 2022* · 📈160 — A comprehensive comprehensive survey on scene graph generation, organizing major methods, taxonomies, and design choices.

### Self-Supervised Learning

- [Self-supervised Visual Feature Learning with Deep Neural Networks: A Survey](https://arxiv.org/abs/1902.06162) — *IEEE TPAMI 2021* · 📈2002 — A highly cited comprehensive survey on self-supervised learning, organizing major methods, taxonomies, and design choices.
- [A Survey on Contrastive Self-supervised Learning](https://arxiv.org/abs/2011.00362) — *Technologies 2021* · 📈1733 — A survey on self-supervised learning, summarizing key methods, datasets, applications, and research directions.
- [A Survey on Self-supervised Learning: Algorithms, Applications, and Future Trends](https://arxiv.org/abs/2301.05712) — *TPAMI 2024* · 📈520 — A survey on self-supervised learning, covering core methods, applications, and research trends.
- [Masked Image Modeling: A Survey](https://arxiv.org/abs/2408.06687) — *IJCV 2025* · 📈43 — A survey on self-supervised learning, summarizing key methods, datasets, applications, and research directions.
- [Masked Modeling for Self-supervised Representation Learning on Vision and Beyond](https://arxiv.org/abs/2401.00897) — *arXiv 2024* · 📈34 — A key reference on self-supervised learning, organizing major methods, taxonomies, and design choices. — [`Lupin1998/Awesome-MIM`](https://github.com/Lupin1998/Awesome-MIM) ⭐354🟡

### Semantic Segmentation

- [Image Segmentation Using Deep Learning: A Survey](https://arxiv.org/abs/2001.05566) — *TPAMI 2022* · 📈3717 — A standard survey of deep semantic and instance segmentation methods.
- [A Review on Deep Learning Techniques Applied to Semantic Segmentation](https://arxiv.org/abs/1704.06857) — *arXiv 2017* · 📈1380 — A standard review on semantic segmentation, with emphasis on benchmarks, evaluation, and representative methods.
- [Transformer-Based Visual Segmentation: A Survey](https://arxiv.org/abs/2304.09854) — *TPAMI 2024* · 📈297 — A survey on semantic segmentation, summarizing key methods, datasets, applications, and research directions. — [`lxtGH/Awesome-Segmentation-With-Transformer`](https://github.com/lxtGH/Awesome-Segmentation-With-Transformer) ⭐760🔴

### Stereo Matching

- [A Survey on Deep Stereo Matching in the Twenties](https://arxiv.org/abs/2407.07816) — *IJCV 2024* · 📈56 — A recent survey on stereo matching, organizing major methods, taxonomies, and design choices.

### Super-Resolution

- [Deep Learning for Image Super-resolution: A Survey](https://arxiv.org/abs/1902.06068) — *TPAMI 2021* · 📈1789 — A standard survey on super-resolution, organizing major methods, taxonomies, and design choices.
- [Video Super Resolution Based on Deep Learning: A Comprehensive Survey](https://arxiv.org/abs/2007.12928) — *Artificial Intelligence Review 2020* · 📈221 — A comprehensive comprehensive survey on super-resolution, organizing major methods, taxonomies, and design choices.
- [Diffusion Models, Image Super-Resolution And Everything: A Survey](https://arxiv.org/abs/2401.00736) — *TNNLS 2024* · 📈141 — A survey on super-resolution, summarizing key methods, datasets, applications, and research directions.

### Talking Head Generation

- [From Pixels to Portraits: A Comprehensive Survey of Talking Head Generation Techniques and Applications](https://arxiv.org/abs/2308.16041) — *arXiv 2023* · 📈10 — A comprehensive comprehensive survey on talking head generation, organizing major methods, taxonomies, and design choices.

### Temporal Action Detection

- [A Survey on Deep Learning-based Spatio-temporal Action Detection](https://arxiv.org/abs/2308.01618) — *Int. J. Wavelets Multiresolut. Inf. Process. 2023* · 📈13 — A comprehensive survey on temporal action detection, organizing major methods, taxonomies, and design choices.

### Video Anomaly Detection

- [Video Anomaly Detection in 10 Years: A Survey and Outlook](https://arxiv.org/abs/2405.19387) — *arXiv 2024* · 📈48 — A survey on video anomaly detection, summarizing key methods, datasets, applications, and research directions.

### Video Segmentation

- [A Survey on Deep Learning Technique for Video Segmentation](https://arxiv.org/abs/2107.01153) — *TPAMI 2023* · 📈295 — A survey on video segmentation, organizing major methods, taxonomies, and design choices. — [`tfzhou/VS-Survey`](https://github.com/tfzhou/VS-Survey) ⭐204🔴
- [Deep Learning Techniques for Video Instance Segmentation: A Survey](https://arxiv.org/abs/2310.12393) — *arXiv 2023* · 📈4 — A survey on video segmentation, organizing major methods, taxonomies, and design choices.

### Video Understanding

- [Video Transformers: A Survey](https://arxiv.org/abs/2201.05991) — *TPAMI 2023* · 📈166 — A survey on video understanding, organizing major methods, taxonomies, and design choices.

### Vision Transformer

- [A Survey on Vision Transformer](https://arxiv.org/abs/2012.12556) — *TPAMI 2023* · 📈3581 — A highly cited survey that organizes Vision Transformer methods by task and design choice.
- [Transformers in Vision: A Survey](https://arxiv.org/abs/2101.01169) — *CSUR 2022* · 📈3548 — An ACM CSUR survey covering Transformer applications across vision tasks.
- [A Survey of Visual Transformers](https://arxiv.org/abs/2111.06091) — *TNNLS 2023* · 📈533 — A survey on vision Transformer, organizing major methods, taxonomies, and design choices.

### Vision-Language Models

- [Vision-Language Models for Vision Tasks: A Survey](https://arxiv.org/abs/2304.00685) — *TPAMI 2024* · 📈1376 — A comprehensive survey on vision-language models, organizing major methods, taxonomies, and design choices. — [`jingyi0000/VLM_survey`](https://github.com/jingyi0000/VLM_survey) ⭐3123🟡

### Visual SLAM

- [Deep Learning for Visual Localization and Mapping: A Survey](https://arxiv.org/abs/2308.14039) — *arXiv 2023* · 📈81 — A survey on visual SLAM, organizing major methods, taxonomies, and design choices.

### World Models

- [3D and 4D World Modeling: A Survey](https://arxiv.org/abs/2509.07996) — *arXiv 2025* · 📈54 — A survey on world models, organizing major methods, taxonomies, and design choices. — [`worldbench/awesome-3d-4d-world-models`](https://github.com/worldbench/awesome-3d-4d-world-models) ⭐929🟢 · [project](https://worldbench.github.io/survey)

### Zero-Shot Learning

- [Zero-Shot Learning -- A Comprehensive Evaluation of the Good, the Bad and the Ugly](https://arxiv.org/abs/1707.00600) — *TPAMI 2019* · 📈1833 — A standard key reference on zero-shot learning, with emphasis on benchmarks, evaluation, and representative methods.

## 📈 Machine Learning (General)

### Anomaly Detection

- [A Unified Survey on Anomaly, Novelty, Open-Set, and Out-of-Distribution Detection: Solutions and Future Challenges](https://arxiv.org/abs/2110.14051) — *TMLR 2022* · 📈238 — A survey on anomaly detection, organizing major methods, taxonomies, and design choices.

### AutoML

- [AutoML: A Survey of the State-of-the-Art](https://arxiv.org/abs/1908.00709) — *Knowledge-Based Systems 2021* · 📈1794 — A survey on automl, summarizing key methods, datasets, applications, and research directions.

### Bayesian Deep Learning

- [Hands-on Bayesian Neural Networks -- a Tutorial for Deep Learning Users](https://arxiv.org/abs/2007.06823) — *IEEE Computational Intelligence Magazine 2022* · 📈878 — A tutorial survey on bayesian deep learning, summarizing key methods, datasets, applications, and research directions.

### Calibration

- [Calibration in Deep Learning: A Survey of the State-of-the-Art](https://arxiv.org/abs/2308.01222) — *arXiv 2023* · 📈99 — A survey on calibration, organizing major methods, taxonomies, and design choices.

### Causal Machine Learning

- [Towards Causal Representation Learning](https://arxiv.org/abs/2102.11107) — *Proceedings of the IEEE 2021* · 📈358 — A key reference on causal machine learning, summarizing key methods, datasets, applications, and research directions.

### Clustering

- [Deep Clustering: A Comprehensive Survey](https://arxiv.org/abs/2210.04142) — *IEEE TNNLS 2022* · 📈250 — A comprehensive survey on clustering, organizing major methods, taxonomies, and design choices.

### Conformal Prediction

- [A tutorial on conformal prediction](https://arxiv.org/abs/0706.3188) — *JMLR 2008* · 📈1629 — A standard tutorial survey on conformal prediction, summarizing key methods, datasets, applications, and research directions.
- [A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification](https://arxiv.org/abs/2107.07511) — *arXiv 2021* · 📈1062 — A key reference on conformal prediction, summarizing key methods, datasets, applications, and research directions.
- [Conformal Prediction for Natural Language Processing: A Survey](https://arxiv.org/abs/2405.01976) — *TACL 2024* · 📈52 — A survey on conformal prediction, organizing major methods, taxonomies, and design choices.

### Continual Learning

- [Continual Lifelong Learning with Neural Networks: A Review](https://arxiv.org/abs/1802.07569) — *Neural Networks 2019* · 📈3501 — A standard review on continual learning, organizing major methods, taxonomies, and design choices.
- [A Comprehensive Survey of Continual Learning: Theory, Method and Application](https://arxiv.org/abs/2302.00487) — *TPAMI 2023* · 📈1395 — A comprehensive recent comprehensive survey on continual learning, covering core methods, applications, and research trends.

### Continual Learning / Forgetting

- [A Comprehensive Survey of Forgetting in Deep Learning Beyond Continual Learning](https://arxiv.org/abs/2307.09218) — *IEEE TPAMI 2024* · 📈111 — A comprehensive survey on continual learning and forgetting, summarizing key methods, datasets, applications, and research directions. — [`EnnengYang/Awesome-Forgetting-in-Deep-Learning`](https://github.com/EnnengYang/Awesome-Forgetting-in-Deep-Learning) ⭐363🟢

### Curriculum Learning

- [Curriculum Learning: A Survey](https://arxiv.org/abs/2101.10382) — *IJCV 2022* · 📈552 — A standard comprehensive survey on curriculum learning, organizing major methods, taxonomies, and design choices.

### Data Augmentation

- [Time Series Data Augmentation for Deep Learning: A Survey](https://arxiv.org/abs/2002.12478) — *IJCAI 2021* · 📈821 — A survey on data augmentation, organizing major methods, taxonomies, and design choices.
- [Image Data Augmentation for Deep Learning: A Survey](https://arxiv.org/abs/2204.08610) — *arXiv 2022* · 📈390 — A comprehensive survey on data augmentation, organizing major methods, taxonomies, and design choices.

### Dataset Distillation

- [The Evolution of Dataset Distillation: Toward Scalable and Generalizable Solutions](https://arxiv.org/abs/2502.05673) — *arXiv preprint 2025* · 📈23 — A recent key reference on dataset distillation, organizing major methods, taxonomies, and design choices.

### Dictionary Learning

- [Supervised Dictionary Learning and Sparse Representation-A Review](https://arxiv.org/abs/1502.05928) — *arXiv 2015* · 📈59 — A review on dictionary learning, organizing major methods, taxonomies, and design choices.

### Diffusion (Time Series)

- [A Survey on Diffusion Models for Time Series and Spatio-Temporal Data](https://arxiv.org/abs/2404.18886) — *arXiv 2024* · 📈112 — A survey on diffusion (time series), covering core methods, applications, and research trends. — [`yyysjz1997/Awesome-TimeSeries-SpatioTemporal-Diffusion-Model`](https://github.com/yyysjz1997/Awesome-TimeSeries-SpatioTemporal-Diffusion-Model) ⭐989🟢

### Distributed Deep Learning Systems

- [Systems for Parallel and Distributed Large-Model Deep Learning Training](https://arxiv.org/abs/2301.02691) — *arXiv preprint 2023* · 📈9 — A comprehensive key reference on distributed deep learning systems, covering methods, challenges, and future research directions.

### Distributed LLM Training / ML Systems

- [Efficient Training of Large Language Models on Distributed Infrastructures: A Survey](https://arxiv.org/abs/2407.20018) — *arXiv preprint 2024* · 📈51 — A recent survey on distributed LLM training and ML systems, organizing major methods, taxonomies, and design choices.

### Domain Adaptation

- [A Survey of Unsupervised Deep Domain Adaptation](https://arxiv.org/abs/1812.02849) — *ACM TIST 2020* · 📈996 — A highly cited standard survey on domain adaptation, organizing major methods, taxonomies, and design choices.
- [A Brief Review of Domain Adaptation](https://arxiv.org/abs/2010.03978) — *arXiv 2020* · 📈787 — A review on domain adaptation, organizing major methods, taxonomies, and design choices.

### Domain Generalization

- [Domain Generalization: A Survey](https://arxiv.org/abs/2103.02503) — *TPAMI 2022* · 📈1542 — A survey on domain generalization, with emphasis on benchmarks, evaluation, and representative methods.

### Dynamic Networks

- [Dynamic Neural Networks: A Survey](https://arxiv.org/abs/2102.04906) — *TPAMI 2022* · 📈901 — A survey on dynamic networks, organizing major methods, taxonomies, and design choices.

### Edge AI / Model Optimization

- [Cognitive Edge Computing: A Comprehensive Survey on Optimizing Large Models and AI Agents for Pervasive Deployment](https://arxiv.org/abs/2501.03265) — *arXiv preprint 2025* · 📈28 — A comprehensive comprehensive survey on edge AI and model optimization, organizing major methods, taxonomies, and design choices.

### Efficient Inference / Hardware

- [Efficient Processing of Deep Neural Networks: A Tutorial and Survey](https://arxiv.org/abs/1703.09039) — *Proceedings of the IEEE 2017* · 📈3598 — Sze's highly cited tutorial survey on efficient DNN processing, including hardware-aware methods.

### Energy-Based Models

- [Hitchhiker's guide on the relation of Energy-Based Models with other generative models, sampling and statistical physics: a comprehensive review](https://arxiv.org/abs/2406.13661) — *TMLR 2025* · 📈5 — A comprehensive review on energy-based models, organizing major methods, taxonomies, and design choices.

### Ensemble Learning

- [Ensemble deep learning: A review](https://arxiv.org/abs/2104.02395) — *Engineering Applications of AI 2022* · 📈1953 — A review on ensemble learning, summarizing key methods, datasets, applications, and research directions.

### Explainable AI

- [Interpretable Deep Learning: Interpretation, Interpretability, Trustworthiness, and Beyond](https://arxiv.org/abs/2103.10689) — *Knowledge and Information Systems 2021* · 📈489 — A key reference on explainable AI, organizing major methods, taxonomies, and design choices.
- [Explainable Artificial Intelligence: a Systematic Review](https://arxiv.org/abs/2006.00093) — *arXiv 2020* · 📈316 — A comprehensive review on explainable AI, organizing major methods, taxonomies, and design choices.

### Fairness

- [A Survey on Bias and Fairness in Machine Learning](https://arxiv.org/abs/1908.09635) — *ACM Computing Surveys 2021* · 📈5860 — A highly cited survey of definitions, measurements, and mitigation methods for bias and fairness in machine learning.
- [What-is and How-to for Fairness in Machine Learning: A Survey, Reflection, and Perspective](https://arxiv.org/abs/2206.04101) — *ACM Computing Surveys 2023* · 📈40 — A survey on fairness, organizing major methods, taxonomies, and design choices.

### Gaussian Processes

- [When Gaussian Process Meets Big Data: A Review of Scalable GPs](https://arxiv.org/abs/1807.01065) — *IEEE TNNLS 2018* · 📈860 — A comprehensive review on gaussian processes, organizing major methods, taxonomies, and design choices.
- [Deep Gaussian Processes: A Survey](https://arxiv.org/abs/2106.12135) — *arXiv 2021* · 📈27 — A survey on gaussian processes, organizing major methods, taxonomies, and design choices.

### Generalization

- [Model Complexity of Deep Learning: A Survey](https://arxiv.org/abs/2103.05127) — *Knowledge and Information Systems 2021* · 📈392 — A survey on generalization, organizing major methods, taxonomies, and design choices.

### Generative Recommendation

- [Large Language Models for Generative Recommendation: A Survey and Visionary Discussions](https://arxiv.org/abs/2309.01157) — *arXiv 2023* · 📈148 — A survey on generative recommendation, covering methods, challenges, and future research directions.
- [A Survey of Generative Search and Recommendation in the Era of Large Language Models](https://arxiv.org/abs/2404.16924) — *arXiv 2024* · 📈27 — A survey on generative recommendation, organizing major methods, taxonomies, and design choices.
- [GR-LLMs: Recent Advances in Generative Recommendation Based on Large Language Models](https://arxiv.org/abs/2507.06507) — *arXiv 2025* · 📈4 — A recent key reference on generative recommendation, covering core methods, applications, and research trends.

### Graph Foundation Models

- [Graph Foundation Models: A Comprehensive Survey](https://arxiv.org/abs/2505.15116) — *arXiv 2025* · 📈42 — A comprehensive survey on graph foundation models, organizing major methods, taxonomies, and design choices.

### Green AI / Sustainable ML

- [Green AI: A systematic review and meta-analysis of its definitions, lifecycle models, hardware and measurement attempts](https://arxiv.org/abs/2511.07090) — *arXiv preprint 2025* · 📈4 — A comprehensive systematic review and meta-analysis on green AI and sustainable ML, organizing major methods, taxonomies, and design choices.

### Hardware Acceleration / ML Systems

- [Hardware Acceleration for Neural Networks: A Comprehensive Survey](https://arxiv.org/abs/2512.23914) — *arXiv preprint 2025* · 📈3 — A comprehensive comprehensive survey on hardware acceleration and ML systems, summarizing key methods, datasets, applications, and research directions.

### Hyperparameter Optimization

- [Hyper-Parameter Optimization: A Review of Algorithms and Applications](https://arxiv.org/abs/2003.05689) — *arXiv 2020* · 📈676 — A review on hyperparameter optimization, organizing major methods, taxonomies, and design choices.
- [Hyperparameter Optimization in Machine Learning](https://arxiv.org/abs/2410.22854) — *arXiv preprint 2024* · 📈9 — A key reference on hyperparameter optimization, summarizing key methods, datasets, applications, and research directions.

### Imbalanced Learning

- [A Survey of Methods for Addressing Class Imbalance in Deep-Learning Based Natural Language Processing](https://arxiv.org/abs/2210.04675) — *EACL 2023* · 📈53 — A comprehensive survey on imbalanced learning, organizing major methods, taxonomies, and design choices.

### Kernel Methods

- [Kernel Mean Embedding of Distributions: A Review and Beyond](https://arxiv.org/abs/1605.09522) — *Foundations and Trends in ML 2017* · 📈876 — A comprehensive review on kernel methods, covering core methods, applications, and research trends.
- [Reproducing Kernel Hilbert Space, Mercer's Theorem, Eigenfunctions, Nystrom Method, and Use of Kernels in Machine Learning: Tutorial and Survey](https://arxiv.org/abs/2106.08443) — *arXiv 2021* · 📈60 — A tutorial survey on kernel methods, covering theoretical foundations, methods, and implications.
- [Neural Tangent Kernel: A Survey](https://arxiv.org/abs/2208.13614) — *arXiv 2022* · 📈22 — A survey on kernel methods, covering theoretical foundations, methods, and implications.

### Knowledge Distillation

- [Knowledge Distillation: A Survey](https://arxiv.org/abs/2006.05525) — *IJCV 2021* · 📈4222 — A standard survey of knowledge types, training schemes, and algorithms in knowledge distillation.

### Knowledge Distillation / Amalgamation

- [A Comprehensive Survey on Knowledge Distillation](https://arxiv.org/abs/2503.12067) — *arXiv preprint 2025* · 📈62 — A comprehensive comprehensive survey on knowledge distillation and amalgamation, organizing major methods, taxonomies, and design choices. — [`IPL-sharif/KD_Survey`](https://github.com/IPL-sharif/KD_Survey) ⭐77🟢

### Kolmogorov-Arnold Networks

- [A Survey on Kolmogorov-Arnold Network](https://arxiv.org/abs/2411.06078) — *arXiv 2024* · 📈207 — A recent survey on kolmogorov-arnold networks, covering core methods, applications, and research trends.
- [Kolmogorov-Arnold Networks: A Critical Assessment of Claims, Performance, and Practical Viability](https://arxiv.org/abs/2407.11075) — *arXiv 2024* · 📈54 — A key reference on kolmogorov-arnold networks, with emphasis on benchmarks, evaluation, and representative methods.

### LLM Hardware Acceleration

- [Hardware Acceleration of LLMs: A comprehensive survey and comparison](https://arxiv.org/abs/2409.03384) — *arXiv preprint 2024* · 📈14 — A comprehensive survey on LLM hardware acceleration, with comparative analysis of representative methods and systems.

### LLM Inference Acceleration (Hardware)

- [Large Language Model Inference Acceleration: A Comprehensive Hardware Perspective](https://arxiv.org/abs/2410.04466) — *arXiv preprint 2024* · 📈71 — A key reference on LLM inference acceleration (hardware), organizing major methods, taxonomies, and design choices. — [`Kimho666/LLM_Hardware_Survey`](https://github.com/Kimho666/LLM_Hardware_Survey) ⭐17🟡

### Label-Noise Learning

- [Learning from Noisy Labels with Deep Neural Networks: A Survey](https://arxiv.org/abs/2007.08199) — *IEEE TNNLS 2022* · 📈1360 — A standard comprehensive survey on label-noise learning, organizing major methods, taxonomies, and design choices.

### Machine Unlearning

- [A Survey of Machine Unlearning](https://arxiv.org/abs/2209.02299) — *arXiv 2022* · 📈406 — A standard comprehensive survey on machine unlearning, covering core methods, applications, and research trends. — [`tamlhp/awesome-machine-unlearning`](https://github.com/tamlhp/awesome-machine-unlearning) ⭐953🟢

### Manifold Learning

- [Manifold learning: what, how, and why](https://arxiv.org/abs/2311.03757) — *Annual Review of Statistics 2023* · 📈142 — A standard key reference on manifold learning, organizing major methods, taxonomies, and design choices.

### Meta-Learning

- [Meta-Learning in Neural Networks: A Survey](https://arxiv.org/abs/2004.05439) — *TPAMI 2022* · 📈2647 — A standard survey on meta-learning, organizing major methods, taxonomies, and design choices.

### Metric Learning

- [A Survey on Metric Learning for Feature Vectors and Structured Data](https://arxiv.org/abs/1306.6709) — *arXiv 2013* · 📈709 — A standard comprehensive survey on metric learning, organizing major methods, taxonomies, and design choices.
- [Spectral, Probabilistic, and Deep Metric Learning: Tutorial and Survey](https://arxiv.org/abs/2201.09267) — *arXiv 2022* · 📈30 — A tutorial survey on metric learning, summarizing key methods, datasets, applications, and research directions.

### Model Compression

- [A Survey of Model Compression and Acceleration for Deep Neural Networks](https://arxiv.org/abs/1710.09282) — *IEEE Signal Processing Magazine 2020* · 📈1235 — A highly cited survey on model compression, surveying major methods, techniques, and algorithmic choices.
- [Efficient Deep Learning: A Survey on Making Deep Learning Models Smaller, Faster, and Better](https://arxiv.org/abs/2106.08962) — *ACM Computing Surveys 2021* · 📈616 — A survey on model compression, organizing major methods, taxonomies, and design choices.

### Model Merging

- [Model Merging in LLMs, MLLMs, and Beyond: Methods, Theories, Applications and Opportunities](https://arxiv.org/abs/2408.07666) — *ACM Computing Surveys 2024* · 📈250 — A comprehensive key reference on model merging, covering core methods, applications, and research trends. — [`EnnengYang/Awesome-Model-Merging-Methods-Theories-Applications`](https://github.com/EnnengYang/Awesome-Model-Merging-Methods-Theories-Applications) ⭐750🟢

### Multi-Task Learning

- [A Survey on Multi-Task Learning](https://arxiv.org/abs/1707.08114) — *IEEE TKDE 2021* · 📈2910 — A standard comprehensive survey on multi-task learning, organizing major methods, taxonomies, and design choices.
- [Multi-Task Learning with Deep Neural Networks: A Survey](https://arxiv.org/abs/2009.09796) — *arXiv 2020* · 📈785 — A survey on multi-task learning, organizing major methods, taxonomies, and design choices.

### Multi-label Learning

- [Deep Learning for Multi-Label Learning: A Comprehensive Survey](https://arxiv.org/abs/2401.16549) — *arXiv 2024* · 📈42 — A comprehensive comprehensive survey on multi-label learning, organizing major methods, taxonomies, and design choices.
- [A Survey on Extreme Multi-label Learning](https://arxiv.org/abs/2210.03968) — *arXiv 2022* · 📈13 — A comprehensive survey on multi-label learning, organizing major methods, taxonomies, and design choices.

### Multiple Instance Learning

- [Multiple Instance Learning: A Survey of Problem Characteristics and Applications](https://arxiv.org/abs/1612.03365) — *Pattern Recognition 2016* · 📈740 — A standard comprehensive survey on multiple instance learning, covering core methods, applications, and research trends.

### Neural Architecture Search

- [Neural Architecture Search: Insights from 1000 Papers](https://arxiv.org/abs/2301.08727) — *arXiv 2023* · 📈221 — A comprehensive recent key reference on neural architecture search, summarizing key methods, datasets, applications, and research directions.
- [Neural Architecture Search: A Survey](https://arxiv.org/abs/1808.05377) — *JMLR 2019* — A standard survey on neural architecture search, organizing major methods, taxonomies, and design choices.

### Neural Compression

- [Information Compression in the AI Era: Recent Advances and Future Challenges](https://arxiv.org/abs/2406.10036) — *arXiv 2024* · 📈22 — A key reference on neural compression, covering theoretical foundations, methods, and implications.

### On-Device AI / Edge Intelligence

- [Empowering Edge Intelligence: A Comprehensive Survey on On-Device AI Models](https://arxiv.org/abs/2503.06027) — *arXiv preprint 2025* · 📈162 — A comprehensive comprehensive survey on on-device AI and edge intelligence, organizing major methods, taxonomies, and design choices.

### On-Device Optimization / Edge ML

- [Onboard Optimization and Learning: A Survey](https://arxiv.org/abs/2505.08793) — *arXiv preprint 2025* · 📈2 — A survey on on-device optimization and edge ML, organizing major methods, taxonomies, and design choices.

### Open-set Recognition

- [A Survey on Open Set Recognition](https://arxiv.org/abs/2109.00893) — *arXiv 2021* · 📈49 — A comprehensive survey on open-set recognition, organizing major methods, taxonomies, and design choices.

### Optimization

- [An overview of gradient descent optimization algorithms](https://arxiv.org/abs/1609.04747) — *arXiv 2016* · 📈6929 — A highly cited overview of SGD, momentum, Adam, and related gradient-based optimization algorithms.
- [A Survey of Optimization Methods from a Machine Learning Perspective](https://arxiv.org/abs/1906.06821) — *IEEE Transactions on Cybernetics 2020* · 📈661 — A highly cited comprehensive survey on optimization, organizing major methods, taxonomies, and design choices.
- [A survey and taxonomy of loss functions in machine learning](https://arxiv.org/abs/2301.05579) — *arXiv 2023* · 📈52 — A comprehensive recent survey on optimization, organizing major methods, taxonomies, and design choices.

### Ordinal Regression

- [A Survey on Ordinal Regression: Applications, Advances and Prospects](https://arxiv.org/abs/2503.00952) — *arXiv 2025* · 📈3 — A comprehensive survey on ordinal regression, covering core methods, applications, and research trends.

### Out-of-Distribution Detection

- [Generalized Out-of-Distribution Detection: A Survey](https://arxiv.org/abs/2110.11334) — *IJCV 2024* · 📈1393 — A survey on out-of-distribution detection, organizing major methods, taxonomies, and design choices. — [`huytransformer/Awesome-Out-Of-Distribution-Detection`](https://github.com/huytransformer/Awesome-Out-Of-Distribution-Detection) ⭐1008🟢

### PU Learning

- [Learning from positive and unlabeled data: a survey](https://arxiv.org/abs/1811.04820) — *Machine Learning 2020* · 📈695 — A standard survey on PU learning, summarizing key methods, datasets, applications, and research directions.

### Pruning

- [What is the State of Neural Network Pruning?](https://arxiv.org/abs/2003.03033) — *MLSys 2020* · 📈1254 — A key reference on pruning, with emphasis on benchmarks, evaluation, and representative methods.

### Quantization

- [A Survey of Quantization Methods for Efficient Neural Network Inference](https://arxiv.org/abs/2103.13630) — *arXiv 2021* · 📈1564 — A standard comprehensive survey on quantization, organizing major methods, taxonomies, and design choices.

### Representation Learning

- [Representation Learning: A Review and New Perspectives](https://arxiv.org/abs/1206.5538) — *IEEE TPAMI 2013* · 📈13863 — A classic, highly cited review of representation learning and deep learning perspectives.
- [Recent Advances in Autoencoder-Based Representation Learning](https://arxiv.org/abs/1812.05069) — *NeurIPS Workshop 2018* · 📈504 — A recent key reference on representation learning, organizing major methods, taxonomies, and design choices.

### Self-Supervised Learning

- [Bootstrap your own latent: A new approach to self-supervised Learning](https://arxiv.org/abs/2006.07733) — *NeurIPS 2020* · 📈8589 — The BYOL paper, a landmark self-supervised learning method that avoids negative pairs.
- [Self-supervised Learning: Generative or Contrastive](https://arxiv.org/abs/2006.08218) — *IEEE TKDE 2021* · 📈2155 — A highly cited standard key reference on self-supervised learning, summarizing key methods, datasets, applications, and research directions.
- [Self-Supervised Representation Learning: Introduction, Advances and Challenges](https://arxiv.org/abs/2110.09327) — *IEEE Signal Processing Magazine 2021* · 📈394 — A recent key reference on self-supervised learning, organizing major methods, taxonomies, and design choices.

### Semi-Supervised Learning

- [A survey on Semi-, Self- and Unsupervised Learning for Image Classification](https://arxiv.org/abs/2002.08721) — *IEEE Access 2021* · 📈187 — A survey on semi-supervised learning, with comparative analysis of representative methods and systems.

### Sparse Representation

- [A survey of sparse representation: algorithms and applications](https://arxiv.org/abs/1602.07017) — *IEEE Access 2015* · 📈1057 — A comprehensive survey on sparse representation, covering core methods, applications, and research trends.

### State Space Models

- [Advancing Intelligent Sequence Modeling: Evolution, Trade-offs, and Applications of State-Space Architectures from S4 to Mamba](https://arxiv.org/abs/2503.18970) — *arXiv 2025* · 📈17 — A key reference on state space models, covering core methods, applications, and research trends.

### Tabular Deep Learning

- [Deep Neural Networks and Tabular Data: A Survey](https://arxiv.org/abs/2110.01889) — *IEEE TNNLS 2022* · 📈1124 — A comprehensive survey on tabular deep learning, organizing major methods, taxonomies, and design choices.
- [A Survey on Deep Tabular Learning](https://arxiv.org/abs/2410.12034) — *arXiv 2024* · 📈46 — A survey on tabular deep learning, summarizing key methods, datasets, applications, and research directions.

### Tabular Foundation Models

- [Representation Learning for Tabular Data: A Comprehensive Survey](https://arxiv.org/abs/2504.16109) — *arXiv 2025* · 📈39 — A comprehensive comprehensive survey on tabular foundation models, organizing major methods, taxonomies, and design choices. — [`LAMDA-Tabular/Tabular-Survey`](https://github.com/LAMDA-Tabular/Tabular-Survey) ⭐126🟢

### Time Series Foundation Models

- [Foundation Models for Time Series: A Survey](https://arxiv.org/abs/2504.04011) — *arXiv 2025* · 📈27 — A survey on time series foundation models, organizing major methods, taxonomies, and design choices.

### Transfer Learning

- [A Comprehensive Survey on Transfer Learning](https://arxiv.org/abs/1911.02685) — *Proceedings of the IEEE 2020* · 📈5782 — A highly cited survey that classifies transfer learning methods by their underlying mechanisms.
- [A Survey on Deep Transfer Learning](https://arxiv.org/abs/1808.01974) — *ICANN 2018* · 📈2898 — A survey on transfer learning, organizing major methods, taxonomies, and design choices.
- [A Survey on Negative Transfer](https://arxiv.org/abs/2009.00909) — *IEEE/CAA JAS 2022* · 📈359 — A comprehensive survey on transfer learning, organizing major methods, taxonomies, and design choices.
- [A Survey on Transfer Learning](https://doi.org/10.1109/TKDE.2009.191) — *IEEE TKDE 2010* — A standard survey on transfer learning, summarizing key methods, datasets, applications, and research directions.

### Uncertainty Estimation

- [A Review of Uncertainty Quantification in Deep Learning: Techniques, Applications and Challenges](https://arxiv.org/abs/2011.06225) — *Information Fusion 2021* · 📈2577 — A highly cited comprehensive review on uncertainty estimation, organizing major methods, taxonomies, and design choices.
- [A Survey of Uncertainty in Deep Neural Networks](https://arxiv.org/abs/2107.03342) — *Artificial Intelligence Review 2021* · 📈1768 — A comprehensive survey on uncertainty estimation, organizing major methods, taxonomies, and design choices.

### Variational Inference

- [Variational Inference: A Review for Statisticians](https://arxiv.org/abs/1601.00670) — *JASA 2017* · 📈5701 — A standard, highly cited review of variational inference and its statistical foundations.

### Weak Supervision

- [A Survey on Programmatic Weak Supervision](https://arxiv.org/abs/2202.05433) — *arXiv 2022* · 📈109 — A survey on weak supervision, organizing major methods, taxonomies, and design choices.

## 📐 Learning Theory

### Approximation Theory / Expressive Power

- [Approximation Power of Deep Neural Networks: an explanatory mathematical survey](https://arxiv.org/abs/2207.09511) — *arXiv 2022* · 📈5 — A survey on approximation theory and expressive power, summarizing key methods, datasets, applications, and research directions.

### Bandits

- [Introduction to Multi-Armed Bandits](https://arxiv.org/abs/1904.07272) — *Foundations and Trends in ML 2019* · 📈1250 — A standard comprehensive key reference on bandits, covering theoretical foundations, methods, and implications.

### Deep Learning Theory

- [The Principles of Deep Learning Theory](https://arxiv.org/abs/2106.10165) — *Cambridge University Press 2022* · 📈287 — A comprehensive key reference on deep learning theory, covering theoretical foundations, methods, and implications.
- [The Modern Mathematics of Deep Learning](https://arxiv.org/abs/2105.04026) — *Cambridge University Press 2022* · 📈134 — A comprehensive key reference on deep learning theory, covering theoretical foundations, methods, and implications.
- [A Survey on Statistical Theory of Deep Learning: Approximation, Training Dynamics, and Generative Models](https://arxiv.org/abs/2401.07187) — *Annual Review of Statistics and Its Application 2024* · 📈25 — A survey on deep learning theory, covering theoretical foundations, methods, and implications.

### Differential Privacy Theory

- [A Comprehensive Guide to Differential Privacy: From Theory to User Expectations](https://arxiv.org/abs/2509.03294) — *arXiv 2025* · 📈2 — A comprehensive key reference on differential privacy theory, covering core methods, applications, and research trends.

### Fairness Theory

- [Fairness in Machine Learning: A Survey](https://arxiv.org/abs/2010.04053) — *ACM Computing Surveys 2020* · 📈879 — A survey on fairness theory, organizing major methods, taxonomies, and design choices.

### Generalization Bounds

- [Generalization in Deep Learning](https://arxiv.org/abs/1710.05468) — *Cambridge University Press 2022* · 📈499 — A key reference on generalization bounds, covering theoretical foundations, methods, and implications.

### Implicit Regularization

- [On the Implicit Bias in Deep-Learning Algorithms](https://arxiv.org/abs/2208.12591) — *Communications of the ACM 2022* · 📈116 — A key reference on implicit regularization, summarizing key methods, datasets, applications, and research directions.

### Multi-Armed Bandits

- [A Survey on Practical Applications of Multi-Armed and Contextual Bandits](https://arxiv.org/abs/1904.10040) — *arXiv 2019* · 📈141 — A survey on multi-armed bandits, covering core methods, applications, and research trends.
- [A Survey on Contextual Multi-armed Bandits](https://arxiv.org/abs/1508.03326) — *arXiv 2016* · 📈141 — A survey on multi-armed bandits, organizing major methods, taxonomies, and design choices.
- [A Survey of Risk-Aware Multi-Armed Bandits](https://arxiv.org/abs/2205.05843) — *IJCAI 2022* · 📈10 — A survey on multi-armed bandits, organizing major methods, taxonomies, and design choices.

### Online Convex Optimization

- [Introduction to Online Convex Optimization](https://arxiv.org/abs/1909.05207) — *Foundations and Trends in Optimization 2019* · 📈2256 — A standard comprehensive key reference on online convex optimization, covering theoretical foundations, methods, and implications.
- [Online convex optimization and no-regret learning: Algorithms, guarantees and applications](https://arxiv.org/abs/1804.04529) — *arXiv 2018* · 📈45 — A key reference on online convex optimization, covering core methods, applications, and research trends.

### Online Learning

- [Online Learning: A Comprehensive Survey](https://arxiv.org/abs/1802.02871) — *Neurocomputing 2021* · 📈811 — A comprehensive comprehensive survey on online learning, covering theoretical foundations, methods, and implications.
- [A Modern Introduction to Online Learning](https://arxiv.org/abs/1912.13213) — *arXiv 2019* · 📈537 — A key reference on online learning, summarizing key methods, datasets, applications, and research directions.

### Overparameterization / Generalization

- [Generalization in Neural Networks: A Broad Survey](https://arxiv.org/abs/2209.01610) — *Neurocomputing 2022* · 📈32 — A survey on overparameterization and generalization, organizing major methods, taxonomies, and design choices.

### PAC-Bayes

- [A Primer on PAC-Bayesian Learning](https://arxiv.org/abs/1901.05353) — *arXiv 2019* · 📈238 — An introductory survey on PAC-bayes, covering theoretical foundations, methods, and implications.

## 🎮 Reinforcement Learning (RL)

### Applications (Healthcare)

- [Reinforcement Learning in Healthcare: A Survey](https://arxiv.org/abs/1908.08796) — *ACM Computing Surveys 2021* · 📈759 — A survey on applications (healthcare), covering methods, challenges, and future research directions.

### Bayesian RL

- [Bayesian Reinforcement Learning: A Survey](https://arxiv.org/abs/1609.04436) — *Foundations and Trends in Machine Learning 2015* · 📈719 — A standard comprehensive survey on bayesian RL, organizing major methods, taxonomies, and design choices.

### Credit Assignment

- [A Survey of Temporal Credit Assignment in Deep Reinforcement Learning](https://arxiv.org/abs/2312.01072) — *arXiv 2023* · 📈54 — A survey on credit assignment, with comparative analysis of representative methods and systems.

### Curriculum Learning

- [Curriculum Learning for Reinforcement Learning Domains: A Framework and Survey](https://arxiv.org/abs/2003.04960) — *JMLR 2020* · 📈701 — A survey on curriculum learning, organizing major methods, taxonomies, and design choices.

### Deep RL (general)

- [Deep Reinforcement Learning: A Brief Survey](https://arxiv.org/abs/1708.05866) — *IEEE Signal Processing Magazine 2017* · 📈3549 — A concise standard introduction to value-based and policy-based deep reinforcement learning methods.
- [Deep Reinforcement Learning: An Overview](https://arxiv.org/abs/1701.07274) — *arXiv 2017* · 📈1826 — A comprehensive overview on deep RL (general), covering core methods, applications, and research trends.

### Distributed RL

- [Distributed Deep Reinforcement Learning: A Survey and A Multi-Player Multi-Agent Learning Toolbox](https://arxiv.org/abs/2212.00253) — *Machine Intelligence Research 2024* · 📈35 — A survey on distributed RL, organizing major methods, taxonomies, and design choices.

### Exploration

- [Exploration in Deep Reinforcement Learning: A Survey](https://arxiv.org/abs/2205.00824) — *Information Fusion 2022* · 📈583 — A survey on exploration, organizing major methods, taxonomies, and design choices.
- [A Survey of Exploration Methods in Reinforcement Learning](https://arxiv.org/abs/2109.00157) — *arXiv 2021* · 📈108 — A survey on exploration, organizing major methods, taxonomies, and design choices.

### Generalization

- [A Survey of Zero-shot Generalisation in Deep Reinforcement Learning](https://arxiv.org/abs/2111.09794) — *JAIR 2023* · 📈268 — A survey on generalization, with emphasis on benchmarks, evaluation, and representative methods.

### Goal-Conditioned RL

- [Goal-Conditioned Reinforcement Learning: Problems and Solutions](https://arxiv.org/abs/2201.08299) — *IJCAI 2022* · 📈218 — A comprehensive key reference on goal-conditioned RL, organizing major methods, taxonomies, and design choices.

### Hierarchical RL

- [Hierarchical Reinforcement Learning: A Comprehensive Survey](https://doi.org/10.1145/3453160) — *ACM Computing Surveys 2021* — A comprehensive survey on hierarchical RL, organizing major methods, taxonomies, and design choices.

### Imitation Learning

- [An Algorithmic Perspective on Imitation Learning](https://arxiv.org/abs/1811.06711) — *Foundations and Trends in Robotics 2018* · 📈1006 — A standard comprehensive key reference on imitation learning, organizing major methods, taxonomies, and design choices.

### In-Context Reinforcement Learning

- [A Survey of In-Context Reinforcement Learning](https://arxiv.org/abs/2502.07978) — *arXiv preprint 2025* · 📈34 — A survey on in-context reinforcement learning, organizing major methods, taxonomies, and design choices.

### Inverse RL

- [A Survey of Inverse Reinforcement Learning: Challenges, Methods and Progress](https://arxiv.org/abs/1806.06877) — *Artificial Intelligence 2021* · 📈777 — A survey on inverse RL, covering methods, challenges, and future research directions.

### Meta RL

- [A Tutorial on Meta-Reinforcement Learning](https://arxiv.org/abs/2301.08028) — *Foundations and Trends in Machine Learning 2025* · 📈157 — A comprehensive tutorial survey on meta RL, organizing major methods, taxonomies, and design choices.

### Model-based RL

- [A Survey on Model-based Reinforcement Learning](https://arxiv.org/abs/2206.09328) — *Science China Information Sciences 2024* · 📈172 — A survey on model-based RL, summarizing key methods, datasets, applications, and research directions.
- [Model-based Reinforcement Learning: A Survey](https://arxiv.org/abs/2006.16712) — *Foundations and Trends in Machine Learning 2023* · 📈57 — A standard comprehensive survey on model-based RL, organizing major methods, taxonomies, and design choices.

### Multi-objective RL

- [A Practical Guide to Multi-Objective Reinforcement Learning and Planning](https://arxiv.org/abs/2103.09568) — *AAMAS (JAAMAS) 2022* · 📈537 — A comprehensive key reference on multi-objective RL, summarizing key methods, datasets, applications, and research directions.

### Offline RL

- [Offline Reinforcement Learning: Tutorial, Review, and Perspectives on Open Problems](https://arxiv.org/abs/2005.01643) — *arXiv 2020* · 📈2632 — A tutorial survey on offline RL, covering methods, challenges, and future research directions.
- [A Survey on Offline Reinforcement Learning: Taxonomy, Review, and Open Problems](https://arxiv.org/abs/2203.01387) — *IEEE TNNLS 2023* · 📈397 — A survey on offline RL, organizing major methods, taxonomies, and design choices. — [`larocs/offline-rl-suvey`](https://github.com/larocs/offline-rl-suvey) ⭐8🔴

### RL for Generative AI

- [Reinforcement Learning for Generative AI: State of the Art, Opportunities and Open Research Challenges](https://arxiv.org/abs/2308.00031) — *JAIR 2024* · 📈36 — A key reference on RL for generative AI, covering methods, challenges, and future research directions.
- [Reinforcement Learning for Generative AI: A Survey](https://arxiv.org/abs/2308.14328) — *arXiv 2023* · 📈27 — A survey on RL for generative AI, organizing major methods, taxonomies, and design choices.

### RLHF

- [Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2307.15217) — *TMLR 2023* · 📈875 — A key reference on RLHF, covering methods, challenges, and future research directions.
- [A Survey of Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2312.14925) — *arXiv 2023* · 📈321 — A survey on RLHF, summarizing key methods, datasets, applications, and research directions.

### RLHF / Preference-based RL

- [A Survey of Preference-Based Reinforcement Learning Methods](https://jmlr.org/papers/v18/16-634.html) — *JMLR 2017* — A standard survey on RLHF and preference-based RL, organizing major methods, taxonomies, and design choices.

### Reward Design

- [Reward Models in Deep Reinforcement Learning: A Survey](https://arxiv.org/abs/2506.15421) — *IJCAI 2025* · 📈25 — A recent survey on reward design, organizing major methods, taxonomies, and design choices.

### Safe / Constrained RL

- [A Survey of Safe Reinforcement Learning and Constrained MDPs: A Technical Survey on Single-Agent and Multi-Agent Safety](https://arxiv.org/abs/2505.17342) — *arXiv preprint 2025* · 📈13 — A survey on safe and constrained RL, organizing major methods, taxonomies, and design choices.

### Safe RL

- [A Review of Safe Reinforcement Learning: Methods, Theory and Applications](https://arxiv.org/abs/2205.10330) — *IEEE TPAMI 2024* · 📈322 — A recent review on safe RL, with emphasis on benchmarks, evaluation, and representative methods. — [`chauncygu/Safe-Reinforcement-Learning-Baselines`](https://github.com/chauncygu/Safe-Reinforcement-Learning-Baselines) ⭐794🟢
- [A Survey of Constraint Formulations in Safe Reinforcement Learning](https://arxiv.org/abs/2402.02025) — *IJCAI 2024* · 📈65 — A standard survey on safe RL, covering theoretical foundations, methods, and implications.
- [A Comprehensive Survey on Safe Reinforcement Learning](https://jmlr.org/papers/v16/garcia15a.html) — *JMLR 2015* — A standard comprehensive survey on safe RL, organizing major methods, taxonomies, and design choices.

### Sim-to-Real

- [Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey](https://arxiv.org/abs/2009.13303) — *IEEE SSCI 2020* · 📈1010 — A survey on sim-to-real, surveying major methods, techniques, and algorithmic choices.

### Transfer Learning

- [Transfer Learning in Deep Reinforcement Learning: A Survey](https://arxiv.org/abs/2009.07888) — *IEEE TPAMI 2023* · 📈877 — A survey on transfer learning, organizing major methods, taxonomies, and design choices.

### Visual / Multimodal RL

- [Reinforcement Learning for Large Model: A Survey](https://arxiv.org/abs/2508.08189) — *arXiv preprint 2025* · 📈1 — A comprehensive survey on visual and multimodal RL, organizing major methods, taxonomies, and design choices. — [`weijiawu/Awesome-RL-for-Multimodal-Foundation-Models`](https://github.com/weijiawu/Awesome-RL-for-Multimodal-Foundation-Models) ⭐448🟢

## 🤖 Robotics and Embodied AI

### Autonomous Driving

- [Deep Reinforcement Learning for Autonomous Driving: A Survey](https://arxiv.org/abs/2002.00444) — *IEEE Transactions on Intelligent Transportation Systems 2022* · 📈2332 — A standard survey on autonomous driving, covering methods, challenges, and future research directions.
- [A Survey of Deep Learning Techniques for Autonomous Driving](https://arxiv.org/abs/1910.07738) — *Journal of Field Robotics 2020* · 📈1698 — A standard survey on autonomous driving, surveying major methods, techniques, and algorithmic choices.
- [Survey of Deep Reinforcement Learning for Motion Planning of Autonomous Vehicles](https://arxiv.org/abs/2001.11231) — *IEEE Transactions on Intelligent Transportation Systems 2022* · 📈581 — A survey on autonomous driving, organizing major methods, taxonomies, and design choices.
- [A Survey of Deep RL and IL for Autonomous Driving Policy Learning](https://arxiv.org/abs/2101.01993) — *IEEE Transactions on Intelligent Transportation Systems 2022* · 📈216 — A survey on autonomous driving, organizing major methods, taxonomies, and design choices.
- [A Survey of Deep Reinforcement Learning Algorithms for Motion Planning and Control of Autonomous Vehicles](https://arxiv.org/abs/2105.14218) — *IEEE IV 2021* · 📈70 — A survey on autonomous driving, organizing major methods, taxonomies, and design choices.

### Embodied AI

- [A Survey of Embodied AI: From Simulators to Research Tasks](https://arxiv.org/abs/2103.04918) — *IEEE Transactions on Emerging Topics in Computational Intelligence 2022* · 📈512 — A survey on embodied AI, summarizing key methods, datasets, applications, and research directions.
- [Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI](https://arxiv.org/abs/2407.06886) — *arXiv 2024* · 📈284 — A comprehensive comprehensive survey on embodied AI, organizing major methods, taxonomies, and design choices. — [`HCPLab-SYSU/Embodied_AI_Paper_List`](https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List) ⭐2076🟢

### Grasping

- [Deep Learning Approaches to Grasp Synthesis: A Review](https://arxiv.org/abs/2207.02556) — *IEEE Transactions on Robotics 2023* · 📈261 — A comprehensive review on grasping, organizing major methods, taxonomies, and design choices.

### Legged Locomotion

- [Reinforcement Learning For Quadrupedal Locomotion: Current Advancements And Future Perspectives](https://arxiv.org/abs/2410.10438) — *arXiv 2024* · 📈3 — A key reference on legged locomotion, summarizing key methods, datasets, applications, and research directions.

### Manipulation

- [A Review of Robot Learning for Manipulation: Challenges, Representations, and Algorithms](https://arxiv.org/abs/1907.03146) — *JMLR 2021* · 📈494 — A review on manipulation, summarizing key methods, datasets, applications, and research directions.
- [A Survey on Deep Reinforcement Learning Algorithms for Robotic Manipulation](https://doi.org/10.3390/s23073762) — *Sensors 2023* — A survey on manipulation, organizing major methods, taxonomies, and design choices.

### Manipulation / Embodied AI

- [A Survey of Embodied Learning for Object-Centric Robotic Manipulation](https://arxiv.org/abs/2408.11537) — *arXiv 2024* · 📈40 — A survey on manipulation and embodied AI, organizing major methods, taxonomies, and design choices. — [`RayYoh/OCRM_survey`](https://github.com/RayYoh/OCRM_survey) ⭐255🔴

### Motion Planning (learning)

- [A Survey of Optimization-based Task and Motion Planning: From Classical To Learning Approaches](https://arxiv.org/abs/2404.02817) — *IEEE/ASME Transactions on Mechatronics 2024* · 📈77 — A standard survey on motion planning (learning), surveying major methods, techniques, and algorithmic choices.
- [A Survey on the Integration of Machine Learning with Sampling-based Motion Planning](https://arxiv.org/abs/2211.08368) — *Foundations and Trends in Robotics 2022* · 📈25 — A survey on motion planning (learning), organizing major methods, taxonomies, and design choices.

### Navigation

- [Deep Learning for Embodied Vision Navigation: A Survey](https://arxiv.org/abs/2108.04097) — *arXiv 2021* · 📈1 — A survey on navigation, surveying major methods, techniques, and algorithmic choices.

### Robot Foundation Models

- [Foundation Models in Robotics: Applications, Challenges, and the Future](https://arxiv.org/abs/2312.07843) — *International Journal of Robotics Research 2024* · 📈372 — A key reference on robot foundation models, covering methods, challenges, and future research directions.

### Robot Learning

- [Deep Reinforcement Learning for Robotics: A Survey of Real-World Successes](https://arxiv.org/abs/2408.03539) — *Annual Review of Control, Robotics, and Autonomous Systems 2025* · 📈348 — A survey on robot learning, with emphasis on benchmarks, evaluation, and representative methods.
- [Reinforcement Learning in Robotics: A Survey](https://doi.org/10.1177/0278364913495721) — *International Journal of Robotics Research 2013* — A standard survey on robot learning, covering methods, challenges, and future research directions.

### Safe RL / Control

- [Safe Learning in Robotics: From Learning-Based Control to Safe Reinforcement Learning](https://arxiv.org/abs/2108.06266) — *Annual Review of Control, Robotics, and Autonomous Systems 2022* · 📈932 — A key reference on safe RL and control, covering theoretical foundations, methods, and implications.

### Soft Robotics (learning)

- [Data-driven Methods Applied to Soft Robot Modeling and Control: A Review](https://arxiv.org/abs/2305.12137) — *IEEE Transactions on Automation Science and Engineering 2024* · 📈104 — A review on soft robotics (learning), organizing major methods, taxonomies, and design choices.

### World Models

- [A Comprehensive Survey on World Models for Embodied AI](https://arxiv.org/abs/2510.16732) — *arXiv 2025* · 📈34 — A comprehensive survey on world models, organizing major methods, taxonomies, and design choices. — [`Li-Zn-H/AwesomeWorldModels`](https://github.com/Li-Zn-H/AwesomeWorldModels) ⭐314🟢

### World Models for Robot Learning

- [World Model for Robot Learning: A Comprehensive Survey](https://arxiv.org/abs/2605.00080) — *arXiv preprint 2026* · 📈5 — A comprehensive comprehensive survey on world models for robot learning, organizing major methods, taxonomies, and design choices.

## 👥 Multi-Agent Systems

### Agent Evaluation

- [Survey on Evaluation of LLM-based Agents](https://arxiv.org/abs/2503.16416) — *arXiv 2025* · 📈170 — A comprehensive survey on agent evaluation, with emphasis on benchmarks, evaluation, and representative methods.

### Agent Optimization

- [A Survey on the Optimization of Large Language Model-based Agents](https://arxiv.org/abs/2503.12434) — *arXiv 2025* · 📈38 — A survey on agent optimization, organizing major methods, taxonomies, and design choices.

### Agentic RAG

- [Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG](https://arxiv.org/abs/2501.09136) — *arXiv 2025* · 📈311 — A survey on agentic RAG, summarizing key methods, datasets, applications, and research directions. — [`asinghcsu/AgenticRAG-Survey`](https://github.com/asinghcsu/AgenticRAG-Survey) ⭐1654🟡

### Agentic RL

- [The Landscape of Agentic Reinforcement Learning for LLMs: A Survey](https://arxiv.org/abs/2509.02547) — *arXiv 2025* · 📈139 — A comprehensive survey on agentic RL, organizing major methods, taxonomies, and design choices.

### Autonomous Agents

- [Large Language Model Agent: A Survey on Methodology, Applications and Challenges](https://arxiv.org/abs/2503.21460) — *arXiv 2025* · 📈161 — A survey on autonomous agents, organizing major methods, taxonomies, and design choices. — [`luo-junyu/Awesome-Agent-Papers`](https://github.com/luo-junyu/Awesome-Agent-Papers) ⭐2735🟡

### Cooperative MARL

- [A Review of Cooperative Multi-Agent Deep Reinforcement Learning](https://arxiv.org/abs/1908.03963) — *Applied Intelligence 2023* · 📈613 — A review on cooperative MARL, organizing major methods, taxonomies, and design choices.
- [A Survey of Progress on Cooperative Multi-agent Reinforcement Learning in Open Environment](https://arxiv.org/abs/2312.01058) — *arXiv 2023* · 📈76 — A recent survey on cooperative MARL, organizing major methods, taxonomies, and design choices.

### Emergent Communication

- [A Survey of Multi-Agent Deep Reinforcement Learning with Communication](https://arxiv.org/abs/2203.08975) — *AAMAS (JAAMAS) 2024* · 📈280 — A survey on emergent communication, organizing major methods, taxonomies, and design choices.

### GUI Agents

- [GUI Agents: A Survey](https://arxiv.org/abs/2412.13501) — *ACL Findings 2024* · 📈102 — A survey on GUI agents, with emphasis on benchmarks, evaluation, and representative methods.
- [GUI Agents with Foundation Models: A Comprehensive Survey](https://arxiv.org/abs/2411.04890) — *arXiv 2024* · 📈99 — A comprehensive comprehensive survey on GUI agents, organizing major methods, taxonomies, and design choices.

### Game Theory & Learning

- [An Overview of Multi-Agent Reinforcement Learning from Game Theoretical Perspective](https://arxiv.org/abs/2011.00583) — *arXiv 2020* · 📈216 — An overview on game theory & learning, covering theoretical foundations, methods, and implications.

### LLM Agent Memory

- [A Survey on the Memory Mechanism of Large Language Model based Agents](https://arxiv.org/abs/2404.13501) — *arXiv 2024* · 📈568 — A comprehensive survey on LLM agent memory, with emphasis on benchmarks, evaluation, and representative methods.

### MARL (deep)

- [Deep Reinforcement Learning for Multi-Agent Systems: A Review of Challenges, Solutions and Applications](https://arxiv.org/abs/1812.11794) — *IEEE Transactions on Cybernetics 2020* · 📈1008 — A review on MARL (deep), covering methods, challenges, and future research directions.
- [A Survey and Critique of Multiagent Deep Reinforcement Learning](https://arxiv.org/abs/1810.05587) — *AAMAS (JAAMAS) 2019* · 📈707 — A standard survey on MARL (deep), summarizing key methods, datasets, applications, and research directions.

### MARL (general)

- [Multi-Agent Reinforcement Learning: A Comprehensive Survey](https://arxiv.org/abs/2312.10256) — *arXiv 2024* · 📈65 — A comprehensive comprehensive survey on MARL (general), covering methods, challenges, and future research directions.

### MARL (theory)

- [Multi-Agent Reinforcement Learning: A Selective Overview of Theories and Algorithms](https://arxiv.org/abs/1911.10635) — *Handbook of RL and Control 2021* · 📈1631 — An overview on MARL (theory), covering theoretical foundations, methods, and implications.

### Multi-Agent Collaboration

- [Multi-Agent Collaboration Mechanisms: A Survey of LLMs](https://arxiv.org/abs/2501.06322) — *arXiv 2025* · 📈457 — A survey on multi-agent collaboration, summarizing key methods, datasets, applications, and research directions.

### Multi-Agent Reinforcement Learning

- [A Survey of Multi Agent Reinforcement Learning: Federated Learning and Cooperative and Noncooperative Decentralized Regimes](https://arxiv.org/abs/2507.06278) — *arXiv preprint 2025* · 📈9 — A survey on multi-agent reinforcement learning, organizing major methods, taxonomies, and design choices.

### Role-Playing Agents

- [From Persona to Personalization: A Survey on Role-Playing Language Agents](https://arxiv.org/abs/2404.18231) — *arXiv 2024* · 📈238 — A survey on role-playing agents, with emphasis on benchmarks, evaluation, and representative methods.

### Tool Learning

- [Tool Learning with Large Language Models: A Survey](https://arxiv.org/abs/2405.17935) — *arXiv 2024* · 📈277 — A comprehensive survey on tool learning, with emphasis on benchmarks, evaluation, and representative methods. — [`quchangle1/LLM-Tool-Survey`](https://github.com/quchangle1/LLM-Tool-Survey) ⭐484🟡

### Web Agents

- [A Survey of WebAgents: Towards Next-Generation AI Agents for Web Automation with Large Foundation Models](https://arxiv.org/abs/2503.23350) — *arXiv 2025* · 📈106 — A comprehensive survey on web agents, organizing major methods, taxonomies, and design choices.

## 🕸️ Graph Neural Networks (GNN)

### Dynamic Graph Neural Networks

- [A survey of dynamic graph neural networks](https://arxiv.org/abs/2404.18211) — *Frontiers of Computer Science 2024* · 📈99 — A recent survey on dynamic graph neural networks, organizing major methods, taxonomies, and design choices.

### Dynamic Graphs

- [Representation Learning for Dynamic Graphs: A Survey](https://arxiv.org/abs/1905.11485) — *JMLR 2020* · 📈614 — A standard survey on dynamic graphs, organizing major methods, taxonomies, and design choices.
- [Graph Neural Networks for Temporal Graphs: State of the Art, Open Challenges, and Opportunities](https://arxiv.org/abs/2302.01018) — *TMLR 2023* · 📈107 — A recent key reference on dynamic graphs, covering methods, challenges, and future research directions.

### GNN Benchmark

- [Benchmarking Graph Neural Networks](https://arxiv.org/abs/2003.00982) — *JMLR 2023* · 📈1193 — A standard benchmarking reference on GNN benchmark, with emphasis on benchmarks, evaluation, and representative methods.

### GNN Explainability

- [Explainability in Graph Neural Networks: A Taxonomic Survey](https://arxiv.org/abs/2012.15445) — *IEEE TPAMI 2022* · 📈822 — A standard survey on GNN explainability, with emphasis on benchmarks, evaluation, and representative methods.

### GNN General

- [Graph Neural Networks: A Review of Methods and Applications](https://arxiv.org/abs/1812.08434) — *AI Open 2020* · 📈6987 — A highly cited review that systematizes GNN architectures, design pipelines, and applications.

### GNN for NLP

- [Graph Neural Networks for Natural Language Processing: A Survey](https://arxiv.org/abs/2106.06090) — *Foundations and Trends in Machine Learning 2021* · 📈0 — A survey on GNN for NLP, organizing major methods, taxonomies, and design choices.

### Graph Adversarial Robustness

- [Adversarial Attacks and Defenses on Graphs: A Review, A Tool and Empirical Studies](https://arxiv.org/abs/2003.00653) — *SIGKDD Explorations 2020* · 📈107 — A review on graph adversarial robustness, organizing major methods, taxonomies, and design choices.

### Graph Anomaly Detection

- [Deep Graph Anomaly Detection: A Survey and New Perspectives](https://arxiv.org/abs/2409.09957) — *IEEE TKDE 2024* · 📈83 — A recent survey on graph anomaly detection, organizing major methods, taxonomies, and design choices.

### Graph Condensation

- [Graph Condensation: A Survey](https://arxiv.org/abs/2401.11720) — *arXiv preprint 2024* · 📈36 — A comprehensive survey on graph condensation, covering core methods, applications, and research trends.
- [A Survey on Graph Condensation](https://arxiv.org/abs/2402.02000) — *arXiv preprint 2024* · 📈13 — A comprehensive survey on graph condensation, organizing major methods, taxonomies, and design choices.

### Graph Contrastive Learning

- [Towards Graph Contrastive Learning: A Survey and Beyond](https://arxiv.org/abs/2405.11868) — *arXiv 2024* · 📈62 — A comprehensive survey on graph contrastive learning, organizing major methods, taxonomies, and design choices.

### Graph Distribution Shift

- [Graph Learning under Distribution Shifts: A Comprehensive Survey on Domain Adaptation, Out-of-distribution, and Continual Learning](https://arxiv.org/abs/2402.16374) — *arXiv preprint 2024* · 📈31 — A comprehensive comprehensive survey on graph distribution shift, summarizing key methods, datasets, applications, and research directions.

### Graph Embedding

- [A Comprehensive Survey of Graph Embedding: Problems, Techniques and Applications](https://arxiv.org/abs/1709.07604) — *IEEE TKDE 2018* · 📈1950 — A highly cited standard comprehensive survey on graph embedding, covering core methods, applications, and research trends.
- [Graph Embedding Techniques, Applications, and Performance: A Survey](https://arxiv.org/abs/1705.02801) — *Knowledge-Based Systems 2018* · 📈1818 — A standard survey on graph embedding, with comparative analysis of representative methods and systems.

### Graph Generation

- [A Systematic Survey on Deep Generative Models for Graph Generation](https://arxiv.org/abs/2007.06686) — *IEEE TPAMI 2020* · 📈197 — A comprehensive survey on graph generation, organizing major methods, taxonomies, and design choices.

### Graph OOD Adaptation

- [Beyond Generalization: A Survey of Out-Of-Distribution Adaptation on Graphs](https://arxiv.org/abs/2402.11153) — *arXiv preprint 2024* · 📈10 — A survey on graph OOD adaptation, organizing major methods, taxonomies, and design choices. — [`kaize0409/Awesome-Graph-OOD`](https://github.com/kaize0409/Awesome-Graph-OOD) ⭐85🔴

### Graph OOD Generalization / Adaptation

- [A Survey of Deep Graph Learning under Distribution Shifts: from Graph Out-of-Distribution Generalization to Adaptation](https://arxiv.org/abs/2410.19265) — *arXiv preprint 2024* · 📈19 — A survey on graph OOD generalization and adaptation, organizing major methods, taxonomies, and design choices. — [`kaize0409/Awesome-Graph-OOD`](https://github.com/kaize0409/Awesome-Graph-OOD) ⭐85🔴

### Graph Pooling

- [Graph Pooling for Graph Neural Networks: Progress, Challenges, and Opportunities](https://arxiv.org/abs/2204.07321) — *IJCAI Survey Track 2023* · 📈124 — A key reference on graph pooling, covering methods, challenges, and future research directions.

### Graph Reduction

- [A Comprehensive Survey on Graph Reduction: Sparsification, Coarsening, and Condensation](https://arxiv.org/abs/2402.03358) — *IJCAI 2024 2024* · 📈100 — A comprehensive survey on graph reduction, summarizing key methods, datasets, applications, and research directions.

### Graph Representation Learning

- [Machine Learning on Graphs: A Model and Comprehensive Taxonomy](https://arxiv.org/abs/2005.03675) — *JMLR 2022* · 📈344 — A taxonomy on graph representation learning, organizing major methods, taxonomies, and design choices.

### Graph Self-Supervised Learning

- [Graph Self-Supervised Learning: A Survey](https://arxiv.org/abs/2103.00111) — *IEEE TKDE 2022* · 📈741 — A survey on graph self-supervised learning, organizing major methods, taxonomies, and design choices.
- [Self-Supervised Learning of Graph Neural Networks: A Unified Review](https://arxiv.org/abs/2102.10757) — *IEEE TPAMI 2022* · 📈405 — A review on graph self-supervised learning, organizing major methods, taxonomies, and design choices.
- [Self-supervised Learning on Graphs: Contrastive, Generative, or Predictive](https://arxiv.org/abs/2105.07342) — *IEEE TKDE 2023* · 📈325 — A key reference on graph self-supervised learning, organizing major methods, taxonomies, and design choices. — [`LirongWu/awesome-graph-self-supervised-learning`](https://github.com/LirongWu/awesome-graph-self-supervised-learning) ⭐1435🔴

### Graph Transformers

- [Transformer for Graphs: An Overview from Architecture Perspective](https://arxiv.org/abs/2202.08455) — *arXiv 2022* · 📈208 — An overview on graph transformers, with comparative analysis of representative methods and systems.

### Heterogeneous Graphs

- [Heterogeneous Network Representation Learning: A Unified Framework With Survey and Benchmark](https://arxiv.org/abs/2004.00216) — *IEEE TKDE 2022* · 📈60 — A survey on heterogeneous graphs, with emphasis on benchmarks, evaluation, and representative methods.

### Heterophilic GNN

- [Graph Neural Networks for Graphs with Heterophily: A Survey](https://arxiv.org/abs/2202.07082) — *IEEE TKDE 2022* · 📈314 — A comprehensive survey on heterophilic GNN, organizing major methods, taxonomies, and design choices.

### Hypergraph Neural Networks

- [Recent Advances in Hypergraph Neural Networks](https://arxiv.org/abs/2503.07959) — *arXiv preprint 2025* · 📈12 — A key reference on hypergraph neural networks, organizing major methods, taxonomies, and design choices.

### LLM for Graph Data Challenges

- [A Survey of Large Language Models for Data Challenges in Graphs](https://arxiv.org/abs/2505.18475) — *arXiv preprint 2025* · 📈5 — A survey on LLM for graph data challenges, organizing major methods, taxonomies, and design choices. — [`limengran98/Awesome-Literature-Graph-Learning-Challenges`](https://github.com/limengran98/Awesome-Literature-Graph-Learning-Challenges) ⭐110🟡

### Molecular / Drug Discovery

- [Graph Neural Networks for the Prediction of Molecular Structure-Property Relationships](https://arxiv.org/abs/2208.04852) — *RSC (Machine Learning and Hybrid Modelling for Reaction Engineering) 2022* · 📈19 — A key reference on molecular and drug discovery, summarizing key methods, datasets, applications, and research directions.
- [A Survey of Graph Neural Networks for Drug Discovery: Recent Developments and Challenges](https://arxiv.org/abs/2509.07887) — *arXiv 2025* · 📈0 — A recent survey on molecular and drug discovery, organizing major methods, taxonomies, and design choices.

### Scalable GNN

- [A Comprehensive Survey on Distributed Training of Graph Neural Networks](https://arxiv.org/abs/2211.05368) — *Proceedings of the IEEE 2022* · 📈44 — A comprehensive comprehensive survey on scalable GNN, organizing major methods, taxonomies, and design choices.

### Spatio-Temporal GNN

- [A Systematic Literature Review of Spatio-Temporal Graph Neural Network Models for Time Series Forecasting and Classification](https://arxiv.org/abs/2410.22377) — *arXiv preprint 2024* · 📈23 — A comprehensive systematic literature review on spatio-temporal GNN, organizing major methods, taxonomies, and design choices.

## 🔗 Knowledge Representation and Knowledge Graphs

### Abstract Reasoning (ARC)

- [The ARC of Progress towards AGI: A Living Survey of Abstraction and Reasoning](https://arxiv.org/abs/2603.13372) — *arXiv 2026* · 📈0 — A survey on abstract reasoning (ARC), surveying major methods, techniques, and algorithmic choices.

### Autoformalization / Theorem Proving

- [Autoformalization in the Era of Large Language Models: A Survey](https://arxiv.org/abs/2505.23486) — *arXiv 2025* · 📈13 — A survey on autoformalization and theorem proving, summarizing key methods, datasets, applications, and research directions.

### Entity Alignment

- [A Benchmark and Comprehensive Survey on Knowledge Graph Entity Alignment via Representation Learning](https://arxiv.org/abs/2103.15059) — *The VLDB Journal 2021* · 📈94 — A comprehensive survey on entity alignment, with emphasis on benchmarks, evaluation, and representative methods.

### Graph + LLM

- [A Survey of Large Language Models for Graphs](https://arxiv.org/abs/2405.08011) — *KDD 2024* · 📈139 — A survey on graphs and large language models, organizing major methods, taxonomies, and design choices. — [`HKUDS/Awesome-LLM4Graph-Papers`](https://github.com/HKUDS/Awesome-LLM4Graph-Papers) ⭐370🟡
- [A Survey of Graph Meets Large Language Model: Progress and Future Directions](https://arxiv.org/abs/2311.12399) — *IJCAI 2024* · 📈109 — A survey on graphs and large language models, organizing major methods, taxonomies, and design choices. — [`yhLeeee/Awesome-LLMs-in-Graph-tasks`](https://github.com/yhLeeee/Awesome-LLMs-in-Graph-tasks) ⭐656🟡

### Graph Retrieval-Augmented Generation

- [Graph Retrieval-Augmented Generation: A Survey](https://arxiv.org/abs/2408.08921) — *arXiv 2024* · 📈421 — A comprehensive survey on graph retrieval-augmented generation, organizing major methods, taxonomies, and design choices.

### Knowledge Base Question Answering

- [Complex Knowledge Base Question Answering: A Survey](https://arxiv.org/abs/2108.06688) — *IEEE TKDE 2021* · 📈135 — A survey on knowledge base question answering, organizing major methods, taxonomies, and design choices.

### Knowledge Graph + LLM

- [Unifying Large Language Models and Knowledge Graphs: A Roadmap](https://arxiv.org/abs/2306.08302) — *IEEE TKDE 2023* · 📈1465 — A standard key reference on knowledge graphs and large language models, organizing major methods, taxonomies, and design choices. — [`RManLuo/Awesome-LLM-KG`](https://github.com/RManLuo/Awesome-LLM-KG) ⭐2599🟡
- [LLMs for Knowledge Graph Construction and Reasoning: Recent Capabilities and Future Opportunities](https://arxiv.org/abs/2305.13168) — *World Wide Web Journal 2023* · 📈274 — A key reference on knowledge graphs and large language models, with emphasis on benchmarks, evaluation, and representative methods.

### Knowledge Graph Completion

- [A Review of Knowledge Graph Completion](https://arxiv.org/abs/2208.11652) — *Information (MDPI) 2022* · 📈92 — A recent review on knowledge graph completion, with comparative analysis of representative methods and systems.

### Knowledge Graph Construction

- [A Comprehensive Survey on Automatic Knowledge Graph Construction](https://arxiv.org/abs/2302.05019) — *ACM Computing Surveys 2023* · 📈313 — A comprehensive comprehensive survey on knowledge graph construction, organizing major methods, taxonomies, and design choices.
- [Construction of Knowledge Graphs: State and Challenges](https://arxiv.org/abs/2302.11509) — *arXiv 2023* · 📈73 — A recent key reference on knowledge graph construction, summarizing key methods, datasets, applications, and research directions.

### Knowledge Graph Embedding

- [A Review of Relational Machine Learning for Knowledge Graphs](https://arxiv.org/abs/1503.00759) — *Proceedings of the IEEE 2016* · 📈1724 — A standard review on knowledge graph embedding, summarizing key methods, datasets, applications, and research directions.
- [A Survey of Knowledge Graph Embedding and Their Applications](https://arxiv.org/abs/2107.07842) — *arXiv 2021* · 📈69 — A survey on knowledge graph embedding, covering core methods, applications, and research trends.
- [Negative Sampling in Knowledge Graph Representation Learning: A Review](https://arxiv.org/abs/2402.19195) — *arXiv 2024* · 📈14 — A comprehensive review on knowledge graph embedding, organizing major methods, taxonomies, and design choices.
- [A Survey on Knowledge Graph Structure and Knowledge Graph Embeddings](https://arxiv.org/abs/2412.10092) — *arXiv 2024* · 📈3 — A comprehensive survey on knowledge graph embedding, organizing major methods, taxonomies, and design choices.

### Knowledge Graph General

- [Knowledge Graphs](https://arxiv.org/abs/2003.02320) — *ACM Computing Surveys 2021* · 📈2462 — A comprehensive key reference on knowledge graph general, organizing major methods, taxonomies, and design choices.

### Knowledge Graph Question Answering

- [Large Language Models Meet Knowledge Graphs for Question Answering: Synthesis and Opportunities](https://arxiv.org/abs/2505.20099) — *arXiv 2025* · 📈29 — A key reference on knowledge graph question answering, organizing major methods, taxonomies, and design choices.

### Knowledge Graph Reasoning

- [A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic, and Multimodal](https://arxiv.org/abs/2212.05767) — *IEEE TPAMI 2022* · 📈289 — A survey on knowledge graph reasoning, organizing major methods, taxonomies, and design choices.

### LLM-based Knowledge Graph Construction

- [LLM-empowered knowledge graph construction: A survey](https://arxiv.org/abs/2510.20345) — *arXiv 2025* · 📈12 — A survey on LLM-based knowledge graph construction, organizing major methods, taxonomies, and design choices.

### Neural-Symbolic Reasoning

- [Neural-Symbolic Reasoning over Knowledge Graphs: A Survey from a Query Perspective](https://arxiv.org/abs/2412.10390) — *arXiv 2024* · 📈29 — A survey on neural-symbolic reasoning, summarizing key methods, datasets, applications, and research directions.

### Neurosymbolic AI

- [From Statistical Relational to Neurosymbolic Artificial Intelligence: a Survey](https://arxiv.org/abs/2108.11451) — *Artificial Intelligence 2021* · 📈118 — A survey on neurosymbolic AI, organizing major methods, taxonomies, and design choices.

### Neurosymbolic Reasoning

- [Neurosymbolic AI for Reasoning over Knowledge Graphs: A Survey](https://arxiv.org/abs/2302.07200) — *arXiv 2023* · 📈42 — A survey on neurosymbolic reasoning, organizing major methods, taxonomies, and design choices.

### Ontology Embedding

- [Ontology Embedding: A Survey of Methods, Applications and Resources](https://arxiv.org/abs/2406.10964) — *arXiv 2024* · 📈28 — A comprehensive survey on ontology embedding, covering core methods, applications, and research trends.

### Planning / RL for Optimization

- [A Survey of Reinforcement Learning for Optimization in Automation](https://arxiv.org/abs/2502.09417) — *arXiv 2025* · 📈23 — A survey on planning and RL for optimization, summarizing key methods, datasets, applications, and research directions.

### Program Synthesis

- [From Provable Correctness to Probabilistic Generation: A Comparative Review of Program Synthesis Paradigms](https://arxiv.org/abs/2508.00013) — *arXiv 2025* · 📈0 — A review on program synthesis, with comparative analysis of representative methods and systems.

### RDF Stores and SPARQL Engines

- [A Survey of RDF Stores & SPARQL Engines for Querying Knowledge Graphs](https://arxiv.org/abs/2102.13027) — *The VLDB Journal 2021* · 📈118 — A survey on RDF stores and SPARQL engines, with emphasis on benchmarks, evaluation, and representative methods.

### Temporal Knowledge Graph

- [A Survey on Temporal Knowledge Graph: Representation Learning and Applications](https://arxiv.org/abs/2403.04782) — *arXiv 2024* · 📈45 — A comprehensive survey on temporal knowledge graph, covering core methods, applications, and research trends.

### Temporal Knowledge Graph Completion

- [A Survey on Temporal Knowledge Graph Completion: Taxonomy, Progress, and Prospects](https://arxiv.org/abs/2308.02457) — *arXiv 2023* · 📈42 — A survey on temporal knowledge graph completion, covering methods, challenges, and future research directions.

### Temporal Knowledge Graph Question Answering

- [Temporal Knowledge Graph Question Answering: A Survey](https://arxiv.org/abs/2406.14191) — *arXiv 2024* · 📈14 — A survey on temporal knowledge graph question answering, organizing major methods, taxonomies, and design choices.

## 🎯 Causal Inference

### Causal Discovery

- [D'ya like DAGs? A Survey on Structure Learning and Causal Discovery](https://arxiv.org/abs/2103.02582) — *ACM Computing Surveys 2021* · 📈388 — A standard comprehensive survey on causal discovery, organizing major methods, taxonomies, and design choices.
- [A Survey on Causal Discovery Methods for I.I.D. and Time Series Data](https://arxiv.org/abs/2303.15027) — *TMLR 2023* · 📈61 — A recent survey on causal discovery, organizing major methods, taxonomies, and design choices.

### Causal Generative Modeling

- [From Identifiable Causal Representations to Controllable Counterfactual Generation: A Survey on Causal Generative Modeling](https://arxiv.org/abs/2310.11011) — *TMLR 2024* · 📈28 — A survey on causal generative modeling, covering theoretical foundations, methods, and implications.

### Causal Inference

- [A Survey on Causal Inference](https://arxiv.org/abs/2002.02770) — *ACM TKDD 2021* · 📈673 — A standard survey on causal inference, organizing major methods, taxonomies, and design choices.

### Causal Machine Learning

- [Causal Machine Learning: A Survey and Open Problems](https://arxiv.org/abs/2206.15475) — *arXiv 2022* · 📈162 — A survey on causal machine learning, covering methods, challenges, and future research directions.

### Causal Reinforcement Learning

- [Causal Reinforcement Learning: A Survey](https://arxiv.org/abs/2307.01452) — *TMLR 2023* · 📈39 — A comprehensive survey on causal reinforcement learning, organizing major methods, taxonomies, and design choices.

### Causal Representation Learning

- [A Survey on Causal Representation Learning and Future Work for Medical Image Analysis](https://arxiv.org/abs/2210.16034) — *arXiv 2022* · 📈0 — A survey on causal representation learning, covering methods, challenges, and future research directions.

### Causality + LLM

- [Causal Inference with Large Language Model: A Survey](https://arxiv.org/abs/2409.09822) — *arXiv 2024* · 📈41 — A recent survey on causality + LLM, organizing major methods, taxonomies, and design choices.

### Causality and Fairness

- [Survey on Causal-based Machine Learning Fairness Notions](https://arxiv.org/abs/2010.09553) — *arXiv 2020* · 📈99 — A comprehensive survey on causality and fairness, organizing major methods, taxonomies, and design choices.

### Causality and LLM

- [Large Language Models and Causal Inference in Collaboration: A Survey](https://arxiv.org/abs/2403.09606) — *arXiv 2024* · 📈31 — A survey on causality and LLM, with emphasis on benchmarks, evaluation, and representative methods.

### Causality and NLP

- [Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond](https://arxiv.org/abs/2109.00725) — *TACL 2022* · 📈321 — A standard key reference on causality and NLP, summarizing key methods, datasets, applications, and research directions.

### Causality and Recommendation

- [Causal Inference in Recommender Systems: A Survey and Future Directions](https://arxiv.org/abs/2208.12397) — *ACM TOIS 2022* · 📈155 — A survey on causality and recommendation, covering methods, challenges, and future research directions.

### Counterfactual Explanations

- [Robust Counterfactual Explanations in Machine Learning: A Survey](https://arxiv.org/abs/2402.01928) — *IJCAI 2024* · 📈38 — A survey on counterfactual explanations, summarizing key methods, datasets, applications, and research directions.

### Treatment Effect Estimation

- [A Survey of Deep Causal Models and Their Industrial Applications](https://arxiv.org/abs/2209.08860) — *arXiv 2022* · 📈20 — A survey on treatment effect estimation, covering core methods, applications, and research trends.
- [Causal Inference with Complex Treatments: A Survey](https://arxiv.org/abs/2407.14022) — *arXiv 2024* · 📈6 — A survey on treatment effect estimation, organizing major methods, taxonomies, and design choices.

## ⏱️ Time Series and Spatio-Temporal AI

### EEG / Biosignal Deep Learning

- [Deep learning-based electroencephalography analysis: a systematic review](https://arxiv.org/abs/1901.05498) — *Journal of Neural Engineering 2019* · 📈1306 — A standard review on EEG and biosignal deep learning, covering core methods, applications, and research trends.
- [Deep Learning-Powered Electrical Brain Signals Analysis: Advancing Neurological Diagnostics](https://arxiv.org/abs/2502.17213) — *arXiv 2025* · 📈6 — A comprehensive recent key reference on EEG and biosignal deep learning, organizing major methods, taxonomies, and design choices.

### Financial Time Series

- [Deep learning models for price forecasting of financial time series: A review of recent advancements: 2020-2022](https://arxiv.org/abs/2305.04811) — *arXiv 2023* · 📈144 — A review on financial time series, organizing major methods, taxonomies, and design choices.

### Graph Time Series

- [A Survey on Graph Neural Networks for Time Series: Forecasting, Classification, Imputation, and Anomaly Detection](https://arxiv.org/abs/2307.03759) — *IEEE TPAMI 2024* · 📈458 — A survey on graph time series, organizing major methods, taxonomies, and design choices.

### Human Activity Recognition (HAR)

- [Deep Learning for Sensor-based Human Activity Recognition: Overview, Challenges and Opportunities](https://arxiv.org/abs/2001.07416) — *ACM Computing Surveys 2020* · 📈841 — A standard overview on human activity recognition (HAR), covering methods, challenges, and future research directions.

### Irregular Time Series

- [A Survey on Principles, Models and Methods for Learning from Irregularly Sampled Time Series](https://arxiv.org/abs/2012.00168) — *arXiv 2020* · 📈67 — A survey on irregular time series, organizing major methods, taxonomies, and design choices.

### Spatio-Temporal Forecasting

- [Spatio-Temporal Graph Neural Networks: A Survey](https://arxiv.org/abs/2301.10569) — *arXiv 2023* · 📈55 — A survey on spatio-temporal forecasting, covering methods, challenges, and future research directions.

### Time Series Anomaly Detection

- [Dive into Time-Series Anomaly Detection: A Decade Review](https://arxiv.org/abs/2412.20512) — *arXiv 2024* · 📈33 — A review on time series anomaly detection, organizing major methods, taxonomies, and design choices.

### Time Series Clustering

- [Bridging the Gap: A Decade Review of Time-Series Clustering Methods](https://arxiv.org/abs/2412.20582) — *arXiv 2024* — A standard review on time series clustering, organizing major methods, taxonomies, and design choices.

### Time Series Forecasting

- [Time Series Forecasting With Deep Learning: A Survey](https://arxiv.org/abs/2004.13408) — *Phil. Trans. R. Soc. A 2020* · 📈1891 — A standard survey on time series forecasting, organizing major methods, taxonomies, and design choices.
- [Transformers in Time Series: A Survey](https://arxiv.org/abs/2202.07125) — *IJCAI 2023* · 📈1459 — A standard survey on time series forecasting, organizing major methods, taxonomies, and design choices. — [`qingsongedu/time-series-transformers-review`](https://github.com/qingsongedu/time-series-transformers-review) ⭐2986🔴
- [A Comprehensive Survey of Deep Learning for Time Series Forecasting: Architectural Diversity and Open Challenges](https://arxiv.org/abs/2411.05793) — *Artificial Intelligence Review 2024* · 📈89 — A comprehensive comprehensive survey on time series forecasting, with comparative analysis of representative methods and systems.

### Time Series Foundation Models

- [Foundation Models for Time Series Analysis: A Tutorial and Survey](https://arxiv.org/abs/2403.14735) — *KDD 2024* · 📈397 — A tutorial survey on time series foundation models, covering core methods, applications, and research trends.
- [A Survey of Deep Learning and Foundation Models for Time Series Forecasting](https://arxiv.org/abs/2401.13912) — *arXiv 2024* · 📈71 — A survey on time series foundation models, organizing major methods, taxonomies, and design choices.
- [Empowering Time Series Analysis with Foundation Models: A Comprehensive Survey](https://arxiv.org/abs/2405.02358) — *arXiv 2024* · 📈26 — A comprehensive comprehensive survey on time series foundation models, organizing major methods, taxonomies, and design choices.

### Time Series Imputation

- [Deep Learning for Multivariate Time Series Imputation: A Survey](https://arxiv.org/abs/2402.04059) — *IJCAI 2024* · 📈129 — A survey on time series imputation, organizing major methods, taxonomies, and design choices.

### Time Series Representation Learning

- [Self-Supervised Learning for Time Series Analysis: Taxonomy, Progress, and Prospects](https://arxiv.org/abs/2306.10125) — *IEEE TPAMI 2023* · 📈245 — A taxonomy on time series representation learning, organizing major methods, taxonomies, and design choices. — [`qingsongedu/Awesome-SSL4TS`](https://github.com/qingsongedu/Awesome-SSL4TS) ⭐378🔴
- [Universal Time-Series Representation Learning: A Survey](https://arxiv.org/abs/2401.03717) — *ACM Computing Surveys 2024* · 📈45 — A survey on time series representation learning, organizing major methods, taxonomies, and design choices.

### Time Series x LLM

- [Large Language Models for Time Series: A Survey](https://arxiv.org/abs/2402.01801) — *IJCAI 2024* · 📈164 — A survey on time series for LLM, organizing major methods, taxonomies, and design choices. — [`xiyuanzh/awesome-llm-time-series`](https://github.com/xiyuanzh/awesome-llm-time-series) ⭐517🔴

### Traffic Forecasting

- [STG4Traffic: A Survey and Benchmark of Spatial-Temporal Graph Neural Networks for Traffic Prediction](https://arxiv.org/abs/2307.00495) — *arXiv 2023* · 📈15 — A survey on traffic forecasting, with emphasis on benchmarks, evaluation, and representative methods. — [`jwwthu/GNN4Traffic`](https://github.com/jwwthu/GNN4Traffic) ⭐1206🔴

## ⛏️ Data Mining

### Anomaly Detection

- [Deep Learning for Anomaly Detection: A Survey](https://arxiv.org/abs/1901.03407) — *arXiv 2019* · 📈1805 — A highly cited standard survey on anomaly detection, summarizing key methods, datasets, applications, and research directions.
- [A Unifying Review of Deep and Shallow Anomaly Detection](https://arxiv.org/abs/2009.11732) — *Proceedings of the IEEE 2021* · 📈1028 — A standard review on anomaly detection, organizing major methods, taxonomies, and design choices.
- [Anomaly Detection: A Survey](https://doi.org/10.1145/1541880.1541882) — *ACM Computing Surveys 2009* — A highly cited standard survey on anomaly detection, organizing major methods, taxonomies, and design choices.

### Clustering

- [A Comprehensive Survey on Deep Clustering: Taxonomy, Challenges, and Future Directions](https://arxiv.org/abs/2206.07579) — *ACM Computing Surveys 2024* · 📈203 — A comprehensive survey on clustering, covering methods, challenges, and future research directions.

### Concept Drift

- [Concept Drift Adaptation in Text Stream Mining Settings: A Systematic Review](https://arxiv.org/abs/2312.02901) — *ACM TIST 2024* · 📈12 — A comprehensive review on concept drift, organizing major methods, taxonomies, and design choices.

### Educational Data Mining

- [Educational data mining and learning analytics: An updated survey](https://arxiv.org/abs/2402.07956) — *WIREs Data Mining and Knowledge Discovery 2024* · 📈894 — A recent survey on educational data mining, summarizing key methods, datasets, applications, and research directions.
- [A Comprehensive Survey on Deep Learning Techniques in Educational Data Mining](https://arxiv.org/abs/2309.04761) — *arXiv 2023* · 📈48 — A comprehensive survey on educational data mining, organizing major methods, taxonomies, and design choices.

### Explainable Anomaly Detection

- [A Survey on Explainable Anomaly Detection](https://arxiv.org/abs/2210.06959) — *ACM TKDD 2022* · 📈177 — A comprehensive survey on explainable anomaly detection, organizing major methods, taxonomies, and design choices.

### Frequent Pattern Mining

- [A Survey of Parallel Sequential Pattern Mining](https://arxiv.org/abs/1805.10515) — *ACM TKDD 2019* · 📈256 — A survey on frequent pattern mining, surveying major methods, techniques, and algorithmic choices.

### Graph Anomaly Detection

- [A Comprehensive Survey on Graph Anomaly Detection with Deep Learning](https://arxiv.org/abs/2106.07178) — *IEEE TKDE 2023* · 📈802 — A comprehensive comprehensive survey on graph anomaly detection, organizing major methods, taxonomies, and design choices.
- [Graph Anomaly Detection in Time Series: A Survey](https://arxiv.org/abs/2302.00058) — *IEEE TPAMI 2023* · 📈30 — A comprehensive survey on graph anomaly detection, organizing major methods, taxonomies, and design choices.

### Graph Mining

- [A Comprehensive Survey on Graph Neural Networks](https://arxiv.org/abs/1901.00596) — *IEEE TNNLS 2021* · 📈11192 — A highly cited survey that organizes graph neural networks into a clear taxonomy of major families.

### Graph Representation Learning

- [A Comprehensive Survey on Deep Graph Representation Learning](https://arxiv.org/abs/2304.05055) — *Neural Networks 2024* · 📈312 — A comprehensive recent comprehensive survey on graph representation learning, organizing major methods, taxonomies, and design choices.
- [A Survey on Graph Representation Learning Methods](https://arxiv.org/abs/2204.01855) — *ACM TIST 2024* · 📈227 — A comprehensive survey on graph representation learning, organizing major methods, taxonomies, and design choices.

### Heterogeneous Information Networks

- [A Survey of Heterogeneous Information Network Analysis](https://arxiv.org/abs/1511.04854) — *IEEE TKDE 2017* — A comprehensive survey on heterogeneous information networks, organizing major methods, taxonomies, and design choices.

### Imbalanced Data

- [Learning from Class-Imbalanced Data: Review of Methods and Applications](https://doi.org/10.1016/j.eswa.2016.12.035) — *Expert Systems with Applications 2017* — A review on imbalanced data, covering core methods, applications, and research trends.
- [Learning from Imbalanced Data](https://doi.org/10.1109/TKDE.2008.239) — *IEEE TKDE 2009* — A standard key reference on imbalanced data, covering theoretical foundations, methods, and implications.

### LLM and Graphs

- [Large Language Models on Graphs: A Comprehensive Survey](https://arxiv.org/abs/2312.02783) — *IEEE TKDE 2024* · 📈298 — A comprehensive comprehensive survey on LLM and graphs, organizing major methods, taxonomies, and design choices. — [`PeterGriffinJin/Awesome-Language-Model-on-Graphs`](https://github.com/PeterGriffinJin/Awesome-Language-Model-on-Graphs) ⭐991🟡

### Outlier Detection

- [A Survey on Unsupervised Outlier Detection in High-Dimensional Numerical Data](https://doi.org/10.1002/sam.11161) — *Statistical Analysis and Data Mining 2012* — A standard survey on outlier detection, organizing major methods, taxonomies, and design choices.

### Process Mining

- [Deep Learning for Predictive Business Process Monitoring: Review and Benchmark](https://arxiv.org/abs/2009.13251) — *IEEE TSC 2020* · 📈126 — A review on process mining, with emphasis on benchmarks, evaluation, and representative methods.
- [Advances in Process Optimization: A Comprehensive Survey of Process Mining, Predictive Process Monitoring, and Process-Aware Recommender Systems](https://arxiv.org/abs/2301.10398) — *arXiv 2023* · 📈2 — A comprehensive comprehensive survey on process mining, organizing major methods, taxonomies, and design choices.

### Social Mining

- [Automatic Rumor Detection on Microblogs: A Survey](https://arxiv.org/abs/1807.03505) — *arXiv 2018* · 📈91 — A survey on social mining, organizing major methods, taxonomies, and design choices.
- [Influence Maximization in Social Networks: A Survey](https://arxiv.org/abs/2309.04668) — *arXiv 2023* · 📈10 — A survey on social mining, organizing major methods, taxonomies, and design choices.

### Spatiotemporal Data Mining

- [Spatiotemporal Data Mining: A Survey](https://arxiv.org/abs/2206.12753) — *arXiv 2022* · 📈9 — A survey on spatiotemporal data mining, organizing major methods, taxonomies, and design choices.

### Stream Mining

- [A Survey on Concept Drift Adaptation](https://doi.org/10.1145/2523813) — *ACM Computing Surveys 2014* — A standard survey on stream mining, summarizing key methods, datasets, applications, and research directions.

### Text Mining

- [A Brief Survey of Text Mining: Classification, Clustering and Extraction Techniques](https://arxiv.org/abs/1707.02919) — *arXiv 2017* · 📈565 — A survey on text mining, organizing major methods, taxonomies, and design choices.

### Time Series Anomaly Detection

- [Deep Learning for Time Series Anomaly Detection: A Survey](https://arxiv.org/abs/2211.05244) — *ACM Computing Surveys 2024* · 📈565 — A comprehensive recent survey on time series anomaly detection, organizing major methods, taxonomies, and design choices.

### Time Series Mining

- [Deep Learning for Time Series Classification: A Review](https://arxiv.org/abs/1809.04356) — *Data Mining and Knowledge Discovery 2019* · 📈3246 — A standard comprehensive review on time series mining, with emphasis on benchmarks, evaluation, and representative methods.
- [Deep Learning for Time Series Classification and Extrinsic Regression: A Current Survey](https://arxiv.org/abs/2302.02515) — *ACM Computing Surveys 2024* · 📈270 — A recent survey on time series mining, organizing major methods, taxonomies, and design choices.

## 🗄️ Databases and Data Management

### Approximate Nearest Neighbor Search

- [A Comprehensive Survey and Experimental Comparison of Graph-Based Approximate Nearest Neighbor Search](https://arxiv.org/abs/2101.12631) — *PVLDB 2021* · 📈360 — A standard comprehensive survey on approximate nearest neighbor search, with comparative analysis of representative methods and systems. — [`Lsyhprum/WEAVESS`](https://github.com/Lsyhprum/WEAVESS) ⭐80🔴

### Cardinality Estimation

- [Are We Ready For Learned Cardinality Estimation?](https://arxiv.org/abs/2012.06743) — *VLDB 2021* · 📈156 — A key reference on cardinality estimation, with comparative analysis of representative methods and systems.

### Cloud and Serverless

- [The Serverless Computing Survey: A Technical Primer for Design Architecture](https://arxiv.org/abs/2112.12921) — *ACM Computing Surveys 2022* · 📈197 — An introductory survey on cloud and serverless, surveying major methods, techniques, and algorithmic choices.

### Data Cleaning

- [Data Cleaning: Overview and Emerging Challenges](https://doi.org/10.1145/2882903.2912574) — *SIGMOD 2016* — A standard overview on data cleaning, organizing major methods, taxonomies, and design choices.

### Data Lake

- [Data Lakes: A Survey of Functions and Systems](https://arxiv.org/abs/2106.09592) — *IEEE TKDE 2021* · 📈105 — A survey on data lake, organizing major methods, taxonomies, and design choices.

### Data Pricing

- [A Survey on Data Pricing: from Economics to Data Science](https://arxiv.org/abs/2009.04462) — *IEEE TKDE 2022* · 📈172 — A survey on data pricing, organizing major methods, taxonomies, and design choices.

### Entity Matching

- [Neural Networks for Entity Matching: A Survey](https://arxiv.org/abs/2010.11075) — *ACM TKDD 2021* · 📈137 — A survey on entity matching, organizing major methods, taxonomies, and design choices.

### Entity Resolution

- [End-to-End Entity Resolution for Big Data: A Survey](https://arxiv.org/abs/1905.06397) — *ACM Computing Surveys 2021* · 📈67 — A standard comprehensive survey on entity resolution, organizing major methods, taxonomies, and design choices.

### Learned Index

- [A Survey of Learned Indexes for the Multi-dimensional Space](https://arxiv.org/abs/2403.06456) — *arXiv 2024* · 📈25 — A survey on learned index, organizing major methods, taxonomies, and design choices.
- [How Good Are Multi-dimensional Learned Indices? An Experimental Survey](https://arxiv.org/abs/2405.05536) — *arXiv 2024* · 📈7 — A survey on learned index, with emphasis on benchmarks, evaluation, and representative methods.

### ML for Query Optimization

- [A Survey on Advancing the DBMS Query Optimizer: Cardinality, Cost Model, and Plan Enumeration](https://arxiv.org/abs/2101.01507) — *Data Science and Engineering 2021* · 📈115 — A survey on ML for query optimization, summarizing key methods, datasets, applications, and research directions.

### Text-to-SQL

- [Next-Generation Database Interfaces: A Survey of LLM-based Text-to-SQL](https://arxiv.org/abs/2406.08426) — *arXiv 2024* · 📈222 — A comprehensive survey on text-to-SQL, summarizing key methods, datasets, applications, and research directions.
- [A Survey on Text-to-SQL Parsing: Concepts, Methods, and Future Directions](https://arxiv.org/abs/2208.13629) — *arXiv 2022* · 📈97 — A survey on text-to-SQL, covering methods, challenges, and future research directions.
- [Deep Learning Driven Natural Languages Text to SQL Query Conversion: A Survey](https://arxiv.org/abs/2208.04415) — *arXiv 2022* · 📈26 — A survey on text-to-SQL, organizing major methods, taxonomies, and design choices.

### Time Series Database

- [Time Series Management Systems: A Survey](https://arxiv.org/abs/1710.01077) — *IEEE TKDE 2017* · 📈198 — A survey on time series database, organizing major methods, taxonomies, and design choices.

### Vector Database

- [Survey of Vector Database Management Systems](https://arxiv.org/abs/2310.14021) — *The VLDB Journal 2024* · 📈173 — A comprehensive survey on vector database, organizing major methods, taxonomies, and design choices.
- [A Comprehensive Survey on Vector Database: Storage and Retrieval Technique, Challenge](https://arxiv.org/abs/2310.11703) — *arXiv 2023* · 📈123 — A comprehensive comprehensive survey on vector database, covering methods, challenges, and future research directions.

## 🔍 Information Retrieval (IR)

### Conversational Search

- [Conversational Information Seeking](https://arxiv.org/abs/2201.08808) — *Foundations and Trends in Information Retrieval 2023* · 📈128 — A comprehensive key reference on conversational search, with emphasis on benchmarks, evaluation, and representative methods.
- [A Survey of Conversational Search](https://arxiv.org/abs/2410.15576) — *ACM TOIS 2025* · 📈44 — A comprehensive survey on conversational search, organizing major methods, taxonomies, and design choices.

### Cross-Lingual IR

- [Bridging Language Gaps: Advances in Cross-Lingual Information Retrieval with Multilingual LLMs](https://arxiv.org/abs/2510.00908) — *arXiv 2025* · 📈4 — A key reference on cross-lingual IR, summarizing key methods, datasets, applications, and research directions.

### Cross-modal Retrieval

- [A Comprehensive Survey on Cross-modal Retrieval](https://arxiv.org/abs/1607.06215) — *arXiv 2016* · 📈329 — A comprehensive survey on cross-modal retrieval, organizing major methods, taxonomies, and design choices.

### Dense Retrieval

- [Dense Text Retrieval based on Pretrained Language Models: A Survey](https://arxiv.org/abs/2211.14876) — *ACM TOIS 2024* · 📈306 — A survey on dense retrieval, organizing major methods, taxonomies, and design choices. — [`RUCAIBox/DenseRetrieval`](https://github.com/RUCAIBox/DenseRetrieval) ⭐221🔴

### Explainable IR

- [Explainable Information Retrieval: A Survey](https://arxiv.org/abs/2211.02405) — *arXiv 2022* · 📈39 — A survey on explainable IR, organizing major methods, taxonomies, and design choices.

### Generative Retrieval

- [A Survey of Generative Information Retrieval](https://arxiv.org/abs/2406.01197) — *ACM TOIS 2025* · 📈5 — A comprehensive survey on generative retrieval, organizing major methods, taxonomies, and design choices. — [`RUC-NLPIR/GenIR-Survey`](https://github.com/RUC-NLPIR/GenIR-Survey) ⭐207🟡

### Learning to Rank

- [Learning to Rank for Information Retrieval](https://doi.org/10.1561/1500000016) — *Foundations and Trends in Information Retrieval 2009* — A standard key reference on learning to rank, organizing major methods, taxonomies, and design choices.

### Neural IR

- [Pre-training Methods in Information Retrieval](https://arxiv.org/abs/2111.13853) — *Foundations and Trends in Information Retrieval 2022* · 📈11 — A comprehensive key reference on neural IR, organizing major methods, taxonomies, and design choices.
- [An Introduction to Neural Information Retrieval](https://doi.org/10.1561/1500000061) — *Foundations and Trends in Information Retrieval 2018* — A standard key reference on neural IR, covering theoretical foundations, methods, and implications.

### Neural IR Architectures

- [A Survey of Model Architectures in Information Retrieval](https://arxiv.org/abs/2502.14822) — *arXiv 2025* · 📈25 — A survey on neural IR architectures, organizing major methods, taxonomies, and design choices.

### Neural Ranking

- [Pretrained Transformers for Text Ranking: BERT and Beyond](https://arxiv.org/abs/2010.06467) — *Synthesis Lectures (Morgan & Claypool) 2021* · 📈750 — A standard comprehensive key reference on neural ranking, organizing major methods, taxonomies, and design choices.
- [A Deep Look into Neural Ranking Models for Information Retrieval](https://arxiv.org/abs/1903.06902) — *Information Processing & Management 2019* · 📈378 — A key reference on neural ranking, summarizing key methods, datasets, applications, and research directions.

### Neural Retrieval

- [Information Retrieval: Recent Advances and Beyond](https://arxiv.org/abs/2301.08801) — *IEEE Access 2023* · 📈158 — A key reference on neural retrieval, surveying major methods, techniques, and algorithmic choices.

### RAG and Retrieval

- [Retrieval-Augmented Generation for Large Language Models: A Survey](https://arxiv.org/abs/2312.10997) — *arXiv 2024* · 📈3426 — A standard comprehensive survey on retrieval-augmented generation and retrieval, organizing major methods, taxonomies, and design choices. — [`Tongji-KGLLM/RAG-Survey`](https://github.com/Tongji-KGLLM/RAG-Survey) ⭐2134🔴
- [A Survey on Retrieval-Augmented Text Generation](https://arxiv.org/abs/2202.01110) — *arXiv 2022* · 📈283 — A survey on retrieval-augmented generation and retrieval, organizing major methods, taxonomies, and design choices.

### Table Retrieval and QA

- [Large Language Model for Table Processing: A Survey](https://arxiv.org/abs/2402.05121) — *Frontiers of Computer Science 2024* · 📈102 — A comprehensive survey on table retrieval and QA, summarizing key methods, datasets, applications, and research directions.

## 🛒 Recommender Systems

### AutoML Recommendation

- [AutoML for Deep Recommender Systems: A Survey](https://arxiv.org/abs/2203.13922) — *ACM TOIS 2023* · 📈98 — A survey on automl recommendation, organizing major methods, taxonomies, and design choices.

### Bias and Fairness

- [Bias and Debias in Recommender System: A Survey and Future Directions](https://arxiv.org/abs/2010.03240) — *ACM TOIS 2023* · 📈902 — A standard comprehensive survey on bias and fairness, organizing major methods, taxonomies, and design choices. — [`jiawei-chen/RecDebiasing`](https://github.com/jiawei-chen/RecDebiasing) ⭐462🔴
- [A Survey on the Fairness of Recommender Systems](https://arxiv.org/abs/2206.03761) — *ACM TOIS 2023* · 📈435 — A survey on bias and fairness, organizing major methods, taxonomies, and design choices.

### CTR Prediction

- [Deep Learning for Click-Through Rate Estimation](https://arxiv.org/abs/2104.10584) — *IJCAI 2021* · 📈133 — A key reference on CTR prediction, organizing major methods, taxonomies, and design choices.

### Cold-Start

- [Cold-Start Recommendation towards the Era of Large Language Models (LLMs): A Comprehensive Survey and Roadmap](https://arxiv.org/abs/2501.01945) — *arXiv 2025* · 📈58 — A comprehensive recent comprehensive survey on cold-start, organizing major methods, taxonomies, and design choices. — [`YuanchenBei/Awesome-Cold-Start-Recommendation`](https://github.com/YuanchenBei/Awesome-Cold-Start-Recommendation) ⭐283🟢

### Conversational Recommendation

- [Advances and Challenges in Conversational Recommender Systems: A Survey](https://arxiv.org/abs/2101.09459) — *AI Open 2021* · 📈357 — A standard comprehensive survey on conversational recommendation, covering methods, challenges, and future research directions.

### Cross-Domain Recommendation

- [Cross-Domain Recommendation: Challenges, Progress, and Prospects](https://arxiv.org/abs/2103.01696) — *IJCAI 2021* · 📈294 — A key reference on cross-domain recommendation, covering methods, challenges, and future research directions.

### Deep Learning Recommendation

- [Deep Learning based Recommender System: A Survey and New Perspectives](https://arxiv.org/abs/1707.07435) — *ACM Computing Surveys 2019* · 📈1294 — A standard survey on deep learning recommendation, organizing major methods, taxonomies, and design choices.

### Explainable Recommendation

- [Explainable Recommendation: A Survey and New Perspectives](https://arxiv.org/abs/1804.11192) — *Foundations and Trends in Information Retrieval 2020* · 📈1122 — A standard survey on explainable recommendation, organizing major methods, taxonomies, and design choices.

### Foundation Models Recommendation

- [Foundation Models for Recommender Systems: A Survey and New Perspectives](https://arxiv.org/abs/2402.11143) — *arXiv 2024* · 📈17 — A comprehensive survey on foundation models recommendation, organizing major methods, taxonomies, and design choices.

### Generative Recommendation

- [A Survey on Generative Recommendation: Data, Model, and Tasks](https://arxiv.org/abs/2510.27157) — *arXiv preprint 2025* · 📈12 — A comprehensive survey on generative recommendation, organizing major methods, taxonomies, and design choices.

### Graph-based Recommendation

- [Graph Neural Networks in Recommender Systems: A Survey](https://arxiv.org/abs/2011.02260) — *ACM Computing Surveys 2022* · 📈1772 — A standard survey on graph-based recommendation, organizing major methods, taxonomies, and design choices. — [`wusw14/GNN-in-RS`](https://github.com/wusw14/GNN-in-RS) ⭐307🔴
- [Graph Learning based Recommender Systems: A Review](https://arxiv.org/abs/2105.06339) — *IJCAI 2021* · 📈241 — A comprehensive review on graph-based recommendation, organizing major methods, taxonomies, and design choices.

### LLM Agents for Recommendation

- [A Survey on LLM-powered Agents for Recommender Systems](https://arxiv.org/abs/2502.10050) — *arXiv preprint 2025* · 📈46 — A survey on LLM agents for recommendation, organizing major methods, taxonomies, and design choices.

### LLM and Recommendation

- [A Survey on Large Language Models for Recommendation](https://arxiv.org/abs/2305.19860) — *World Wide Web Journal 2024* · 📈835 — A standard survey on LLM and recommendation, organizing major methods, taxonomies, and design choices.

### Multimodal Recommendation

- [Multimodal Recommender Systems: A Survey](https://arxiv.org/abs/2302.03883) — *ACM Computing Surveys 2024* · 📈162 — A survey on multimodal recommendation, organizing major methods, taxonomies, and design choices.
- [A Comprehensive Survey on Multimodal Recommender Systems: Taxonomy, Evaluation, and Future Directions](https://arxiv.org/abs/2302.04473) — *arXiv 2023* · 📈63 — A comprehensive comprehensive survey on multimodal recommendation, with emphasis on benchmarks, evaluation, and representative methods.

### Reinforcement Learning Recommendation

- [A Survey of Deep Reinforcement Learning in Recommender Systems](https://arxiv.org/abs/2109.03540) — *arXiv 2021* · 📈74 — A comprehensive survey on reinforcement learning recommendation, organizing major methods, taxonomies, and design choices.

### Self-Supervised Recommendation

- [Self-Supervised Learning for Recommender Systems: A Survey](https://arxiv.org/abs/2203.15876) — *IEEE TKDE 2024* · 📈422 — A standard survey on self-supervised recommendation, organizing major methods, taxonomies, and design choices. — [`Coder-Yu/SELFRec`](https://github.com/Coder-Yu/SELFRec) ⭐642🟡

### Sequential Recommendation

- [Sequential Recommender Systems: Challenges, Progress and Prospects](https://arxiv.org/abs/2001.04830) — *IJCAI 2019* · 📈500 — A comprehensive key reference on sequential recommendation, covering methods, challenges, and future research directions.
- [Deep Learning for Sequential Recommendation: Algorithms, Influential Factors, and Evaluations](https://arxiv.org/abs/1905.01997) — *ACM TOIS 2020* · 📈47 — A key reference on sequential recommendation, with emphasis on benchmarks, evaluation, and representative methods.

## 🌐 Web and Social Computing

### Bot Detection

- [Social Media Bot Detection Research: Review of Literature](https://arxiv.org/abs/2503.22838) — *arXiv 2025* · 📈2 — A review on bot detection, covering methods, challenges, and future research directions.

### Community QA

- [A Survey on Expert Recommendation in Community Question Answering](https://arxiv.org/abs/1807.05540) — *Journal of Computer Science and Technology 2018* · 📈75 — A recent survey on community QA, surveying major methods, techniques, and algorithmic choices.

### Computational Social Science

- [Data-driven Computational Social Science: A Survey](https://arxiv.org/abs/2008.12372) — *Big Data Research 2021* · 📈66 — A survey on computational social science, organizing major methods, taxonomies, and design choices.

### Crowdsourcing Quality

- [A Technical Survey on Statistical Modelling and Design Methods for Crowdsourcing Quality Control](https://arxiv.org/abs/1812.02736) — *Artificial Intelligence 2018* · 📈42 — A survey on crowdsourcing quality, surveying major methods, techniques, and algorithmic choices.
- [Quality Control in Open-Ended Crowdsourcing: A Survey](https://arxiv.org/abs/2412.03991) — *arXiv 2024* · 📈2 — A survey on crowdsourcing quality, organizing major methods, taxonomies, and design choices.

### Entity Resolution

- [Heterogeneity in Entity Matching: A Survey and Experimental Analysis](https://arxiv.org/abs/2508.08076) — *arXiv 2025* · 📈2 — A survey on entity resolution, with emphasis on benchmarks, evaluation, and representative methods.

### Fake News Detection

- [Fake News Detection on Social Media: A Data Mining Perspective](https://arxiv.org/abs/1708.01967) — *ACM SIGKDD Explorations 2017* · 📈3244 — A highly cited key reference on fake news detection, organizing major methods, taxonomies, and design choices.

### GNN for Social Networks

- [A Survey of Graph Neural Networks for Social Recommender Systems](https://arxiv.org/abs/2212.04481) — *ACM Computing Surveys 2022* · 📈273 — A survey on GNN for social networks, organizing major methods, taxonomies, and design choices.

### Graph-based Fake News Detection

- [Fake News Detection Through Graph-based Neural Networks: A Survey](https://arxiv.org/abs/2307.12639) — *arXiv 2023* · 📈26 — A survey on graph-based fake news detection, organizing major methods, taxonomies, and design choices.

### Hate Speech Detection

- [Towards generalisable hate speech detection: a review on obstacles and solutions](https://arxiv.org/abs/2102.08886) — *PeerJ Computer Science 2021* · 📈204 — A review on hate speech detection, organizing major methods, taxonomies, and design choices.
- [A Survey on Automatic Online Hate Speech Detection in Low-Resource Languages](https://arxiv.org/abs/2411.19017) — *arXiv 2024* · 📈8 — A survey on hate speech detection, surveying major methods, techniques, and algorithmic choices.

### Link Prediction

- [A Survey of Link Prediction Algorithms](https://arxiv.org/abs/2306.12970) — *arXiv 2023* — A survey on link prediction, with comparative analysis of representative methods and systems.

### Meme Analysis

- [Toxic Memes: A Survey of Computational Perspectives on the Detection and Explanation of Meme Toxicities](https://arxiv.org/abs/2406.07353) — *arXiv 2024* · 📈18 — A comprehensive survey on meme analysis, organizing major methods, taxonomies, and design choices.

### Misinformation Detection

- [Combating Misinformation in the Age of LLMs: Opportunities and Challenges](https://arxiv.org/abs/2311.05656) — *AI Magazine 2024* · 📈201 — A key reference on misinformation detection, covering methods, challenges, and future research directions. — [`llm-misinformation/llm-misinformation-survey`](https://github.com/llm-misinformation/llm-misinformation-survey) ⭐106🔴

### Online Toxicity Detection

- [Toxicity in Online Platforms and AI Systems: A Survey of Needs, Challenges, Mitigations, and Future Directions](https://arxiv.org/abs/2509.25539) — *arXiv 2025* · 📈8 — A survey on online toxicity detection, organizing major methods, taxonomies, and design choices.

### Recommendation Fairness

- [Fairness and Diversity in Recommender Systems: A Survey](https://arxiv.org/abs/2307.04644) — *ACM TIST 2023* · 📈113 — A survey on recommendation fairness, organizing major methods, taxonomies, and design choices.
- [A Survey on Fairness-aware Recommender Systems](https://arxiv.org/abs/2306.00403) — *Information Fusion 2023* · 📈78 — A survey on recommendation fairness, organizing major methods, taxonomies, and design choices.

### Rumor Detection

- [Detection of Rumors and Their Sources in Social Networks: A Comprehensive Survey](https://arxiv.org/abs/2501.05292) — *arXiv 2025* · 📈10 — A comprehensive comprehensive survey on rumor detection, summarizing key methods, datasets, applications, and research directions.

### Social Bot Detection

- [Social Bots: Detection and Challenges](https://arxiv.org/abs/2312.17423) — *Handbook of Computational Social Science 2023* · 📈6 — A key reference on social bot detection, covering methods, challenges, and future research directions.

### Social Network Analysis

- [A Comprehensive Survey on Community Detection with Deep Learning](https://arxiv.org/abs/2105.12584) — *IEEE TNNLS 2024* · 📈440 — A comprehensive comprehensive survey on social network analysis, organizing major methods, taxonomies, and design choices.

### Web Table Extraction

- [Web Table Extraction, Retrieval and Augmentation: A Survey](https://arxiv.org/abs/2002.00207) — *ACM TIST 2020* · 📈65 — A survey on web table extraction, organizing major methods, taxonomies, and design choices.

## 🛡️ Trustworthy AI (Fairness, XAI, and Safety)

### AI Content Watermarking / Detection

- [Watermarking for AI Content Detection: A Review on Text, Visual, and Audio Modalities](https://arxiv.org/abs/2504.03765) — *ICLR 2025 Workshop (GenAI Watermarking) 2025* · 📈6 — A comprehensive review on AI content watermarking and detection, organizing major methods, taxonomies, and design choices.

### AI Fairness / Bias

- [The Frontiers of Fairness in Machine Learning](https://arxiv.org/abs/1810.08810) — *arXiv 2018* · 📈436 — A key reference on AI fairness and bias, covering methods, challenges, and future research directions.
- [Bias Mitigation for Machine Learning Classifiers: A Comprehensive Survey](https://arxiv.org/abs/2207.07068) — *ACM JRC 2022* · 📈276 — A comprehensive comprehensive survey on AI fairness and bias, organizing major methods, taxonomies, and design choices.

### AI Governance / Ethics

- [Worldwide AI Ethics: a review of 200 guidelines and recommendations for AI governance](https://arxiv.org/abs/2206.11922) — *Patterns 2022* · 📈245 — A comprehensive review on AI governance and ethics, summarizing key methods, datasets, applications, and research directions.

### AI Safety

- [Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565) — *arXiv 2016* · 📈3146 — A key reference on AI safety, covering methods, challenges, and future research directions.

### AI-Generated Text Detection

- [Towards Possibilities & Impossibilities of AI-generated Text Detection: A Survey](https://arxiv.org/abs/2310.15264) — *arXiv preprint 2023* · 📈56 — A survey on AI-generated text detection, covering theoretical foundations, methods, and implications.

### AI-Generated Text Forensics

- [A Survey of AI-generated Text Forensic Systems: Detection, Attribution, and Characterization](https://arxiv.org/abs/2403.01152) — *arXiv preprint 2024* · 📈30 — A comprehensive survey on AI-generated text forensics, organizing major methods, taxonomies, and design choices.

### Adversarial Robustness

- [Adversarial Examples: Attacks and Defenses for Deep Learning](https://arxiv.org/abs/1712.07107) — *IEEE TNNLS 2017* · 📈1807 — A standard key reference on adversarial robustness, summarizing key methods, datasets, applications, and research directions.
- [Adversarial Attacks and Defenses in Images, Graphs and Text: A Review](https://arxiv.org/abs/1909.08072) — *IJAC 2019* · 📈751 — A review on adversarial robustness, summarizing key methods, datasets, applications, and research directions.

### Backdoor Attacks

- [Backdoor Learning: A Survey](https://arxiv.org/abs/2007.08745) — *IEEE TNNLS 2020* · 📈823 — A survey on backdoor attacks, organizing major methods, taxonomies, and design choices.
- [Backdoor Attacks and Countermeasures on Deep Learning: A Comprehensive Review](https://arxiv.org/abs/2007.10760) — *arXiv 2020* · 📈283 — A comprehensive review on backdoor attacks, summarizing key methods, datasets, applications, and research directions.

### Data Poisoning Security

- [Wild Patterns Reloaded: A Survey of Machine Learning Security against Training Data Poisoning](https://arxiv.org/abs/2205.01992) — *ACM Computing Surveys 2022* · 📈198 — A comprehensive survey on data poisoning security, organizing major methods, taxonomies, and design choices.

### Deepfake Detection

- [DeepFakes and Beyond: A Survey of Face Manipulation and Fake Detection](https://arxiv.org/abs/2001.00179) — *Information Fusion 2020* · 📈1076 — A standard comprehensive survey on deepfake detection, organizing major methods, taxonomies, and design choices.
- [The Creation and Detection of Deepfakes: A Survey](https://arxiv.org/abs/2004.11138) — *ACM Computing Surveys 2020* · 📈849 — A survey on deepfake detection, organizing major methods, taxonomies, and design choices.

### Differential Privacy

- [Differential Privacy and Machine Learning: a Survey and Review](https://arxiv.org/abs/1412.7584) — *arXiv 2014* · 📈291 — A survey on differential privacy, summarizing key methods, datasets, applications, and research directions.

### Explainable AI (XAI)

- [A Survey of Methods for Explaining Black Box Models](https://arxiv.org/abs/1802.01933) — *ACM Computing Surveys 2018* · 📈4931 — A definitive, highly cited survey that established a taxonomy of explainable-AI methods for black-box models.
- [A Survey on the Explainability of Supervised Machine Learning](https://arxiv.org/abs/2011.07876) — *JAIR 2021* · 📈955 — A survey on explainable AI (XAI), surveying major methods, techniques, and algorithmic choices.
- [Opportunities and Challenges in Explainable Artificial Intelligence (XAI): A Survey](https://arxiv.org/abs/2006.11371) — *arXiv 2020* · 📈750 — A comprehensive survey on explainable AI (XAI), covering methods, challenges, and future research directions.
- [One Explanation Does Not Fit All: A Toolkit and Taxonomy of AI Explainability Techniques](https://arxiv.org/abs/1909.03012) — *arXiv 2019* · 📈467 — A taxonomy on explainable AI (XAI), surveying major methods, techniques, and algorithmic choices.
- [Counterfactual Explanations and Algorithmic Recourses for Machine Learning: A Review](https://arxiv.org/abs/2010.10596) — *ACM Computing Surveys 2020* · 📈299 — A review on explainable AI (XAI), surveying major methods, techniques, and algorithmic choices.

### LLM Red Teaming

- [Building Safe GenAI Applications: An End-to-End Overview of Red Teaming for Large Language Models](https://arxiv.org/abs/2503.01742) — *arXiv preprint 2025* · 📈13 — An overview on LLM red teaming, organizing major methods, taxonomies, and design choices.

### Machine Unlearning

- [Machine Unlearning: A Comprehensive Survey](https://arxiv.org/abs/2405.07406) — *arXiv preprint 2024* · 📈51 — A comprehensive comprehensive survey on machine unlearning, organizing major methods, taxonomies, and design choices.

### Machine Unlearning (GenAI)

- [Machine Unlearning in Generative AI: A Survey](https://arxiv.org/abs/2407.20516) — *arXiv preprint 2024* · 📈53 — A survey on machine unlearning (genai), surveying major methods, techniques, and algorithmic choices. — [`franciscoliu/Awesome-GenAI-Unlearning`](https://github.com/franciscoliu/Awesome-GenAI-Unlearning) ⭐188🟢

### Machine-Generated Text Detection

- [Are AI Detectors Good Enough? A Survey on Quality of Datasets With Machine-Generated Texts](https://arxiv.org/abs/2410.14677) — *arXiv preprint 2024* · 📈20 — A survey on machine-generated text detection, with emphasis on benchmarks, evaluation, and representative methods.

### Membership Inference

- [Membership Inference Attacks on Machine Learning: A Survey](https://arxiv.org/abs/2103.07853) — *ACM Computing Surveys 2021* · 📈682 — A comprehensive survey on membership inference, organizing major methods, taxonomies, and design choices.

### Model Interpretability

- [Towards A Rigorous Science of Interpretable Machine Learning](https://arxiv.org/abs/1702.08608) — *arXiv 2017* · 📈5107 — An influential paper defining a more rigorous science of interpretable machine learning.
- [Interpretable Machine Learning: Fundamental Principles and 10 Grand Challenges](https://arxiv.org/abs/2103.11251) — *Statistics Surveys 2021* · 📈948 — A key reference on model interpretability, covering methods, challenges, and future research directions.

### Privacy-Preserving ML

- [A Survey of Privacy Attacks in Machine Learning](https://arxiv.org/abs/2007.07646) — *ACM Computing Surveys 2020* · 📈329 — A comprehensive survey on privacy-preserving ML, organizing major methods, taxonomies, and design choices.
- [Privacy-Preserving Machine Learning: Methods, Challenges and Directions](https://arxiv.org/abs/2108.04417) — *arXiv 2021* · 📈163 — A key reference on privacy-preserving ML, covering methods, challenges, and future research directions.

### Red Teaming for Generative Models

- [Against The Achilles' Heel: A Survey on Red Teaming for Generative Models](https://arxiv.org/abs/2404.00629) — *arXiv preprint 2024* · 📈59 — A comprehensive survey on red teaming for generative models, surveying major methods, techniques, and algorithmic choices.

### XAI Evaluation

- [From Anecdotal Evidence to Quantitative Evaluation Methods: A Systematic Review on Evaluating Explainable AI](https://arxiv.org/abs/2201.08164) — *ACM Computing Surveys 2022* · 📈675 — A review on XAI evaluation, with emphasis on benchmarks, evaluation, and representative methods.

## 📡 Federated Learning

### Asynchronous FL

- [Asynchronous Federated Learning on Heterogeneous Devices: A Survey](https://arxiv.org/abs/2109.04269) — *arXiv 2021* · 📈376 — A survey on asynchronous FL, organizing major methods, taxonomies, and design choices.

### Communication Efficiency

- [Federated Learning: Strategies for Improving Communication Efficiency](https://arxiv.org/abs/1610.05492) — *NeurIPS Workshop 2016* · 📈5413 — A foundational paper on communication-efficient strategies for federated learning.

### Decentralized FL

- [A Survey on Decentralized Federated Learning](https://arxiv.org/abs/2308.04604) — *arXiv 2023* · 📈46 — A survey on decentralized FL, organizing major methods, taxonomies, and design choices.

### Decentralized Learning

- [Decentralized Deep Learning for Multi-Access Edge Computing: A Survey on Communication Efficiency and Trustworthiness](https://arxiv.org/abs/2108.03980) — *IEEE TAI 2021* · 📈55 — A survey on decentralized learning, summarizing key methods, datasets, applications, and research directions.

### FL Fairness

- [A Survey on Group Fairness in Federated Learning: Challenges, Taxonomy of Solutions and Directions for Future Research](https://arxiv.org/abs/2410.03855) — *arXiv 2024* · 📈7 — A survey on FL fairness, covering methods, challenges, and future research directions.

### FL Generalization/Robustness/Fairness

- [Federated Learning for Generalization, Robustness, Fairness: A Survey and Benchmark](https://arxiv.org/abs/2311.06750) — *IEEE TPAMI 2023* · 📈227 — A survey on FL generalization/robustness/fairness, with emphasis on benchmarks, evaluation, and representative methods.

### FL Incentive Mechanisms

- [A Comprehensive Survey of Incentive Mechanism for Federated Learning](https://arxiv.org/abs/2106.15406) — *arXiv 2021* · 📈128 — A comprehensive survey on FL incentive mechanisms, covering theoretical foundations, methods, and implications.

### FL x Graph

- [Federated Graph Machine Learning: A Survey of Concepts, Techniques, and Applications](https://arxiv.org/abs/2207.11812) — *SIGKDD Explorations 2022* · 📈68 — A survey on FL for graph, organizing major methods, taxonomies, and design choices.

### FL x LLM

- [Federated Large Language Models: Current Progress and Future Directions](https://arxiv.org/abs/2409.15723) — *arXiv 2024* · 📈31 — A key reference on federated learning for large language models, covering methods, challenges, and future research directions.
- [A Survey on Federated Fine-tuning of Large Language Models](https://arxiv.org/abs/2503.12016) — *arXiv 2025* · 📈29 — A comprehensive survey on federated learning for large language models, organizing major methods, taxonomies, and design choices.

### FL x Medical

- [Federated Learning for Medical Image Analysis: A Survey](https://arxiv.org/abs/2306.05980) — *Pattern Recognition 2024* · 📈400 — A survey on FL for medical, organizing major methods, taxonomies, and design choices.

### Federated Learning (General)

- [Advances and Open Problems in Federated Learning](https://arxiv.org/abs/1912.04977) — *FnT in ML 2019* · 📈8640 — A standard, highly cited survey of progress and open problems in federated learning.
- [Federated Learning: Challenges, Methods, and Future Directions](https://arxiv.org/abs/1908.07873) — *IEEE Signal Processing Magazine 2019* · 📈5961 — A highly cited survey of federated learning challenges, methods, and future directions.

### Heterogeneous FL

- [Federated Learning on Non-IID Data: A Survey](https://arxiv.org/abs/2106.06843) — *Neurocomputing 2021* · 📈1275 — A survey on heterogeneous FL, covering methods, challenges, and future research directions.
- [A Survey on Heterogeneous Federated Learning](https://arxiv.org/abs/2210.04505) — *arXiv 2022* · 📈88 — A survey on heterogeneous FL, summarizing key methods, datasets, applications, and research directions.
- [Non-IID data in Federated Learning: A Survey with Taxonomy, Metrics, Methods, Frameworks and Future Directions](https://arxiv.org/abs/2411.12377) — *arXiv 2024* · 📈23 — A comprehensive recent survey on heterogeneous FL, organizing major methods, taxonomies, and design choices.

### Personalization (FL)

- [Towards Personalized Federated Learning](https://arxiv.org/abs/2103.00710) — *IEEE TNNLS 2021* · 📈1245 — A key reference on personalization (FL), organizing major methods, taxonomies, and design choices.

### Privacy / Security (FL)

- [Threats to Federated Learning: A Survey](https://arxiv.org/abs/2003.02133) — *arXiv 2020* · 📈539 — A comprehensive survey on privacy and security (FL), organizing major methods, taxonomies, and design choices.

### Vertical Federated Learning

- [A Survey on Vertical Federated Learning: From a Layered Perspective](https://arxiv.org/abs/2304.01829) — *arXiv 2023* · 📈44 — A comprehensive survey on vertical federated learning, organizing major methods, taxonomies, and design choices.

## 🖐️ HCI and Human-AI Interaction

### AI Trust and Reliance

- [A Survey of AI Reliance](https://arxiv.org/abs/2408.03948) — *arXiv 2024* · 📈14 — A survey on AI trust and reliance, organizing major methods, taxonomies, and design choices.
- [Trust, distrust, and appropriate reliance in (X)AI: a survey of empirical evaluation of user trust](https://arxiv.org/abs/2312.02034) — *arXiv 2023* · 📈13 — A survey on AI trust and reliance, with emphasis on benchmarks, evaluation, and representative methods.

### AI Writing Assistance

- [The Value, Benefits, and Concerns of Generative AI-Powered Assistance in Writing](https://arxiv.org/abs/2403.12004) — *CHI 2024* · 📈102 — A key reference on AI writing assistance, with comparative analysis of representative methods and systems.
- [Co-Writing with AI, on Human Terms: Aligning Research with User Demands Across the Writing Process](https://arxiv.org/abs/2504.12488) — *arXiv 2025* · 📈40 — A key reference on AI writing assistance, organizing major methods, taxonomies, and design choices.

### AI-Assisted Decision Making

- [Towards a Science of Human-AI Decision Making: A Survey of Empirical Studies](https://arxiv.org/abs/2112.11471) — *arXiv 2021* · 📈235 — A survey on AI-assisted decision making, organizing major methods, taxonomies, and design choices.

### Conversational Agent UX

- [UX Research on Conversational Human-AI Interaction: A Literature Review of the ACM Digital Library](https://arxiv.org/abs/2202.09895) — *CHI 2022* · 📈113 — A comprehensive review on conversational agent UX, with emphasis on benchmarks, evaluation, and representative methods.

### Conversational UI

- [How should my chatbot interact? A survey on human-chatbot interaction design](https://arxiv.org/abs/1904.02743) — *International Journal of Human-Computer Interaction 2019* · 📈542 — A survey on conversational UI, covering methods, challenges, and future research directions.

### Crowdsourcing (HCOMP)

- [Quality Control in Crowdsourcing: A Survey of Quality Attributes, Assessment Techniques and Assurance Actions](https://arxiv.org/abs/1801.02546) — *ACM Computing Surveys 2018* · 📈194 — A comprehensive survey on crowdsourcing (HCOMP), with emphasis on benchmarks, evaluation, and representative methods.

### Explainability & HCI

- [Human-Centered Explainable AI (XAI): From Algorithms to User Experiences](https://arxiv.org/abs/2110.10790) — *arXiv 2021* · 📈325 — A key reference on explainability & HCI, surveying major methods, techniques, and algorithmic choices.
- [Towards Human-centered Explainable AI: A Survey of User Studies for Model Explanations](https://arxiv.org/abs/2210.11584) — *IEEE TPAMI 2022* · 📈219 — A survey on explainability & HCI, summarizing key methods, datasets, applications, and research directions.

### Explainable AI Interface

- [How Human-Centered Explainable AI Interface Are Designed and Evaluated: A Systematic Survey](https://arxiv.org/abs/2403.14496) — *arXiv 2024* · 📈18 — A comprehensive survey on explainable AI interface, with emphasis on benchmarks, evaluation, and representative methods.

### Explainable AI and Users

- [Towards Human-centered Design of Explainable Artificial Intelligence (XAI): A Survey of Empirical Studies](https://arxiv.org/abs/2410.21183) — *arXiv 2024* · 📈7 — A survey on explainable AI and users, organizing major methods, taxonomies, and design choices.

### Generative AI and Creativity

- [Generative AI and Creativity: A Systematic Literature Review and Meta-Analysis](https://arxiv.org/abs/2505.17241) — *arXiv 2025* · 📈20 — A comprehensive systematic literature review on generative AI and creativity, with emphasis on benchmarks, evaluation, and representative methods.

### Human-AI Interaction

- [A Survey on Human-AI Collaboration with Large Foundation Models](https://arxiv.org/abs/2403.04931) — *arXiv 2024* · 📈14 — A survey on human-AI interaction, covering core methods, applications, and research trends.

### Human-AI Teaming

- [Advancing Human-Machine Teaming: Concepts, Challenges, and Applications](https://arxiv.org/abs/2503.16518) — *arXiv 2025* · 📈4 — A comprehensive key reference on human-AI teaming, organizing major methods, taxonomies, and design choices.

### Human-in-the-loop

- [A Survey of Human-in-the-loop for Machine Learning](https://arxiv.org/abs/2108.00941) — *Future Generation Computer Systems 2021* · 📈751 — A survey on human-in-the-loop, organizing major methods, taxonomies, and design choices.

### Social Robot HRI

- [Concerns and Values in Human-Robot Interactions: A Focus on Social Robotics](https://arxiv.org/abs/2501.05628) — *arXiv 2025* · 📈13 — A key reference on social robot HRI, surveying major methods, techniques, and algorithmic choices.

### Visualization for ML

- [A Survey of Visual Analytics Techniques for Machine Learning](https://arxiv.org/abs/2008.09632) — *Computational Visual Media 2020* · 📈272 — A survey on visualization for ML, organizing major methods, taxonomies, and design choices.

## 🧬 Evolutionary Computation

### Black-box Optimization

- [A Tutorial on Bayesian Optimization](https://arxiv.org/abs/1807.02811) — *arXiv 2018* · 📈2336 — A standard tutorial survey on black-box optimization, summarizing key methods, datasets, applications, and research directions.

### Evolutionary Deep Learning

- [Survey on Evolutionary Deep Learning: Principles, Algorithms, Applications and Open Issues](https://arxiv.org/abs/2208.10658) — *ACM Computing Surveys 2022* · 📈115 — A survey on evolutionary deep learning, surveying major methods, techniques, and algorithmic choices.

### Evolutionary Feature Selection

- [Quantum-Inspired Evolutionary Algorithms for Feature Subset Selection: A Comprehensive Survey](https://arxiv.org/abs/2407.17946) — *arXiv 2024* · 📈14 — A comprehensive comprehensive survey on evolutionary feature selection, organizing major methods, taxonomies, and design choices.

### Evolutionary Multi-Objective Optimization

- [A Survey of Decomposition-Based Evolutionary Multi-Objective Optimization: Part I-Past and Future](https://arxiv.org/abs/2404.14571) — *IEEE TEVC 2024* · 📈0 — A standard survey on evolutionary multi-objective optimization, summarizing key methods, datasets, applications, and research directions.

### Evolutionary NAS

- [A Survey on Evolutionary Neural Architecture Search](https://arxiv.org/abs/2008.10937) — *IEEE TNNLS 2020* · 📈570 — A survey on evolutionary NAS, organizing major methods, taxonomies, and design choices.

### Evolutionary RL

- [Combining Evolution and Deep Reinforcement Learning for Policy Search: a Survey](https://arxiv.org/abs/2203.14009) — *ACM TELO 2022* · 📈66 — A survey on evolutionary RL, surveying major methods, techniques, and algorithmic choices.

### Evolutionary Reinforcement Learning

- [Bridging Evolutionary Algorithms and Reinforcement Learning: A Comprehensive Survey on Hybrid Algorithms](https://arxiv.org/abs/2401.11963) — *IEEE TEVC 2024* · 📈71 — A comprehensive survey on evolutionary reinforcement learning, organizing major methods, taxonomies, and design choices.

### Evolutionary Transfer Optimization

- [Evolutionary Multitask Optimization: a Methodological Overview, Challenges and Future Research Directions](https://arxiv.org/abs/2102.02558) — *Cognitive Computation 2021* · 📈81 — An overview on evolutionary transfer optimization, organizing major methods, taxonomies, and design choices.

### Genetic Programming

- [A Recent Survey on the Applications of Genetic Programming in Image Processing](https://arxiv.org/abs/1901.07387) — *arXiv 2019* · 📈38 — A survey on genetic programming, covering core methods, applications, and research trends.

### Large-Scale Evolutionary Optimization

- [A Survey on Learnable Evolutionary Algorithms for Scalable Multiobjective Optimization](https://arxiv.org/abs/2206.11526) — *IEEE TEVC 2022* · 📈102 — A survey on large-scale evolutionary optimization, surveying major methods, techniques, and algorithmic choices.

### Multi-objective Optimization

- [A Review of Evolutionary Multi-modal Multi-objective Optimization](https://arxiv.org/abs/2009.13347) — *IEEE TEVC 2020* · 📈193 — A review on multi-objective optimization, summarizing key methods, datasets, applications, and research directions.

### Neuroevolution

- [Neuroevolution in Deep Neural Networks: Current Trends and Future Challenges](https://arxiv.org/abs/2006.05415) — *IEEE TETCI 2020* · 📈174 — A key reference on neuroevolution, surveying major methods, techniques, and algorithmic choices.

### Swarm Intelligence (PSO)

- [Particle Swarm Optimization: A survey of historical and recent developments with hybridization perspectives](https://arxiv.org/abs/1804.05319) — *Machine Learning and Knowledge Extraction 2018* · 📈475 — A comprehensive recent survey on swarm intelligence (PSO), organizing major methods, taxonomies, and design choices.

## 🔢 Theoretical Computer Science

### Algorithmic Fairness Testing

- [Fairness Testing: A Comprehensive Survey and Analysis of Trends](https://arxiv.org/abs/2207.10223) — *ACM TOSEM 2022* · 📈140 — A comprehensive comprehensive survey on algorithmic fairness testing, organizing major methods, taxonomies, and design choices.

### Algorithmic Game Theory

- [Empirical Game-Theoretic Analysis: A Survey](https://arxiv.org/abs/2403.04018) — *JAIR 2025* · 📈37 — A survey on algorithmic game theory, covering theoretical foundations, methods, and implications.

### Algorithms with Predictions

- [Algorithms with Predictions](https://arxiv.org/abs/2006.09123) — *Beyond the Worst-Case Analysis of Algorithms (book chapter) 2020* · 📈307 — A standard key reference on algorithms with predictions, covering theoretical foundations, methods, and implications.

### Computational Social Choice

- [Preference Restrictions in Computational Social Choice: A Survey](https://arxiv.org/abs/2205.09092) — *arXiv 2022* · 📈48 — A survey on computational social choice, organizing major methods, taxonomies, and design choices.

### Constrained Optimization Learning

- [End-to-End Constrained Optimization Learning: A Survey](https://arxiv.org/abs/2103.16378) — *IJCAI 2021* · 📈256 — A survey on constrained optimization learning, organizing major methods, taxonomies, and design choices.

### Convex Optimization Theory

- [Convex Optimization: Algorithms and Complexity](https://arxiv.org/abs/1405.4980) — *Foundations and Trends in Machine Learning 2015* · 📈2152 — A comprehensive key reference on convex optimization theory, organizing major methods, taxonomies, and design choices.

### Differentiable Optimization

- [Differentiable Convex Optimization Layers in Neural Architectures: Foundations and Perspectives](https://arxiv.org/abs/2412.20679) — *arXiv 2024* · 📈2 — A key reference on differentiable optimization, covering theoretical foundations, methods, and implications.

### Differential Privacy Theory

- [Differential Privacy in Machine Learning: A Survey from Symbolic AI to LLMs](https://arxiv.org/abs/2506.11687) — *arXiv 2025* · 📈2 — A survey on differential privacy theory, covering theoretical foundations, methods, and implications.

### Distributed Optimization

- [A Survey of Distributed Optimization Methods for Multi-Robot Systems](https://arxiv.org/abs/2103.12840) — *arXiv 2021* · 📈59 — A survey on distributed optimization, with emphasis on benchmarks, evaluation, and representative methods.
- [Survey of Distributed Algorithms for Resource Allocation over Multi-Agent Systems](https://arxiv.org/abs/2401.15607) — *arXiv 2024* · 📈28 — A comprehensive survey on distributed optimization, surveying major methods, techniques, and algorithmic choices.

### Fair Division

- [Fair Division of Indivisible Goods: A Survey](https://arxiv.org/abs/2202.07551) — *IJCAI 2022* · 📈94 — A survey on fair division, organizing major methods, taxonomies, and design choices.
- [Fair Division: The Computer Scientist's Perspective](https://arxiv.org/abs/2005.04855) — *IJCAI 2020* · 📈40 — A key reference on fair division, organizing major methods, taxonomies, and design choices.

### Federated Optimization Theory

- [Review of Mathematical Optimization in Federated Learning](https://arxiv.org/abs/2412.01630) — *arXiv 2024* · 📈6 — A comprehensive review on federated optimization theory, covering theoretical foundations, methods, and implications.

### ML for Combinatorial Optimization

- [Machine Learning for Combinatorial Optimization: a Methodological Tour d'Horizon](https://arxiv.org/abs/1811.06128) — *European Journal of Operational Research 2018* · 📈1784 — A standard key reference on ML for combinatorial optimization, summarizing key methods, datasets, applications, and research directions.

### Spectral Methods

- [A Comprehensive Survey on Spectral Clustering with Graph Structure Learning](https://arxiv.org/abs/2501.13597) — *arXiv 2025* · 📈59 — A comprehensive comprehensive survey on spectral methods, summarizing key methods, datasets, applications, and research directions.

### Streaming / Sketching Algorithms

- [Streaming and Sketching Complexity of CSPs: A survey](https://arxiv.org/abs/2205.02744) — *ICALP 2022* · 📈11 — A survey on streaming and sketching algorithms, summarizing key methods, datasets, applications, and research directions.

### Submodular Optimization

- [Learning with Submodular Functions: A Convex Optimization Perspective](https://arxiv.org/abs/1111.6453) — *Foundations and Trends in Machine Learning 2013* · 📈518 — A standard key reference on submodular optimization, summarizing key methods, datasets, applications, and research directions.
- [Convex Analysis and Optimization with Submodular Functions: a Tutorial](https://arxiv.org/abs/1010.4207) — *arXiv 2010* · 📈40 — A tutorial survey on submodular optimization, summarizing key methods, datasets, applications, and research directions.

## 🔬 AI for Science

### AI Drug Discovery

- [Deep Learning Methods for Small Molecule Drug Discovery: A Survey](https://arxiv.org/abs/2303.00313) — *IEEE TKDE 2023* · 📈23 — A survey on AI drug discovery, summarizing key methods, datasets, applications, and research directions.

### AI Physics Simulation

- [Scientific Machine Learning through Physics-Informed Neural Networks: Where we are and What's next](https://arxiv.org/abs/2201.05624) — *Journal of Scientific Computing 2022* · 📈2304 — A key reference on AI physics simulation, covering methods, challenges, and future research directions.

### AI for Science (Overview)

- [A Survey of Deep Learning for Scientific Discovery](https://arxiv.org/abs/2003.11755) — *arXiv 2020* · 📈153 — A comprehensive survey on AI for science (overview), organizing major methods, taxonomies, and design choices.

### AI4Science - Astronomy / Astrophysics

- [Deep Learning in Astrophysics](https://arxiv.org/abs/2510.10713) — *Annual Review of Astronomy and Astrophysics 2026* · 📈1 — A key reference on ai4science: astronomy and astrophysics, organizing major methods, taxonomies, and design choices.

### AI4Science - Computational Fluid Dynamics

- [Recent Advances on Machine Learning for Computational Fluid Dynamics: A Survey](https://arxiv.org/abs/2408.12171) — *arXiv 2024* · 📈63 — A survey on ai4science: computational fluid dynamics, covering core methods, applications, and research trends.

### AI4Science - Materials Discovery

- [Machine Learning-Driven Materials Discovery: Unlocking Next-Generation Functional Materials - A review](https://arxiv.org/abs/2503.18975) — *arXiv 2025* · 📈24 — A review on ai4science: materials discovery, organizing major methods, taxonomies, and design choices.

### AI4Science - Molecular Generation / Drug Design

- [A Survey of Generative AI for de novo Drug Design: New Frontiers in Molecule and Protein Generation](https://arxiv.org/abs/2402.08703) — *arXiv 2024* · 📈108 — A comprehensive survey on ai4science: molecular generation and drug design, organizing major methods, taxonomies, and design choices.

### AI4Science - Neuroscience & Deep Learning

- [A Review of Neuroscience-Inspired Machine Learning](https://arxiv.org/abs/2403.18929) — *arXiv 2024* · 📈16 — A review on ai4science: neuroscience & deep learning, summarizing key methods, datasets, applications, and research directions.

### AI4Science - PDE Solvers

- [Partial Differential Equations Meet Deep Neural Networks: A Survey](https://arxiv.org/abs/2211.05567) — *arXiv 2022* · 📈48 — A survey on ai4science: PDE solvers, organizing major methods, taxonomies, and design choices.

### AI4Science - Protein Design

- [A Model-Centric Review of Deep Learning for Protein Design](https://arxiv.org/abs/2502.19173) — *arXiv 2025* · 📈11 — A review on ai4science: protein design, organizing major methods, taxonomies, and design choices.

### AI4Science - Protein Structure Prediction

- [Deep Learning-Driven Protein Structure Prediction and Design: Key Model Developments by Nobel Laureates and Multi-Domain Applications](https://arxiv.org/abs/2504.01490) — *arXiv 2025* · 📈3 — A comprehensive key reference on ai4science: protein structure prediction, organizing major methods, taxonomies, and design choices.

### AI4Science - Quantum Chemistry

- [Ab-initio Quantum Chemistry with Neural-Network Wavefunctions](https://doi.org/10.1038/s41570-023-00516-8) — *Nature Reviews Chemistry 2023* · 📈132 — A key reference on ai4science: quantum chemistry, summarizing key methods, datasets, applications, and research directions.

### AI4Science - Single-Cell Bioinformatics

- [LLM4Cell: A Survey of Large Language and Agentic Models for Single-Cell Biology](https://arxiv.org/abs/2510.07793) — *arXiv 2025* · 📈2 — A survey on ai4science: single-cell bioinformatics, organizing major methods, taxonomies, and design choices.

### Bioinformatics Deep Learning

- [A Systematic Review of Deep Graph Neural Networks: Challenges, Classification, Architectures, Applications & Potential Utility in Bioinformatics](https://arxiv.org/abs/2311.02127) — *arXiv 2023* · 📈6 — A review on bioinformatics deep learning, covering core methods, applications, and research trends.

### Climate / Weather ML

- [Deep Learning and Foundation Models for Weather Prediction: A Survey](https://arxiv.org/abs/2501.06907) — *arXiv 2025* · 📈22 — A survey on climate and weather ML, organizing major methods, taxonomies, and design choices.
- [Interpretable Machine Learning for Weather and Climate Prediction: A Survey](https://arxiv.org/abs/2403.18864) — *arXiv 2024* · 📈11 — A survey on climate and weather ML, summarizing key methods, datasets, applications, and research directions.

### Clinical NLP

- [Neural Natural Language Processing for Unstructured Data in Electronic Health Records: a Review](https://arxiv.org/abs/2107.02975) — *Computer Science Review 2021* · 📈226 — A review on clinical NLP, summarizing key methods, datasets, applications, and research directions.

### Materials Science ML

- [Advances of Machine Learning in Materials Science: Ideas and Techniques](https://arxiv.org/abs/2307.14032) — *Frontiers of Physics 2023* · 📈74 — A key reference on materials science ML, covering core methods, applications, and research trends.

### Physics-Guided / Scientific ML

- [Integrating Scientific Knowledge with Machine Learning for Engineering and Environmental Systems](https://arxiv.org/abs/2003.04919) — *ACM Computing Surveys 2022* · 📈662 — A standard comprehensive key reference on physics-guided and scientific ML, organizing major methods, taxonomies, and design choices.

### Protein Structure Prediction

- [A Survey of Deep Learning Methods in Protein Bioinformatics and its Impact on Protein Design](https://arxiv.org/abs/2501.01477) — *arXiv 2025* · 📈2 — A survey on protein structure prediction, surveying major methods, techniques, and algorithmic choices.

## 🌟 Artificial Intelligence (General)

### Artificial General Intelligence

- [Approaches to Artificial General Intelligence: An Analysis](https://arxiv.org/abs/2202.03153) — *arXiv 2022* · 📈4 — A key reference on artificial general intelligence, with comparative analysis of representative methods and systems.

### Automated Planning

- [LLMs as Planning Formalizers: A Survey for Leveraging Large Language Models to Construct Automated Planning Models](https://arxiv.org/abs/2503.18971) — *arXiv 2025* · 📈38 — A survey on automated planning, organizing major methods, taxonomies, and design choices.
- [AI Planning: A Primer and Survey (Preliminary Report)](https://arxiv.org/abs/2412.05528) — *arXiv 2024* · 📈5 — An introductory survey on automated planning, covering theoretical foundations, methods, and implications.

### Commonsense Reasoning

- [Commonsense Reasoning for Natural Language Understanding: A Survey of Benchmarks, Resources, and Approaches](https://arxiv.org/abs/1904.01172) — *arXiv 2019* · 📈144 — A standard survey on commonsense reasoning, with emphasis on benchmarks, evaluation, and representative methods.
- [Commonsense Knowledge Reasoning and Generation with Pre-trained Language Models: A Survey](https://arxiv.org/abs/2201.12438) — *AAAI 2022* · 📈78 — A survey on commonsense reasoning, organizing major methods, taxonomies, and design choices.

### Computational Argumentation

- [Computational Argumentation-based Chatbots: a Survey](https://arxiv.org/abs/2401.03454) — *JAIR 2024* · 📈19 — A survey on computational argumentation, summarizing key methods, datasets, applications, and research directions.

### Foundation Models

- [On the Opportunities and Risks of Foundation Models](https://arxiv.org/abs/2108.07258) — *arXiv 2021* · 📈6555 — A broad Stanford report on the capabilities, technology, applications, and social impacts of foundation models.

### Knowledge Graphs & Reasoning

- [A Survey on Knowledge Graphs: Representation, Acquisition and Applications](https://arxiv.org/abs/2002.00388) — *IEEE TNNLS 2021* · 📈2705 — A highly cited comprehensive survey on knowledge graphs & reasoning, covering core methods, applications, and research trends.

### Mathematical Reasoning

- [A Survey of Deep Learning for Mathematical Reasoning](https://arxiv.org/abs/2212.10535) — *ACL 2023* · 📈195 — A survey on mathematical reasoning, covering methods, challenges, and future research directions. — [`lupantech/dl4math`](https://github.com/lupantech/dl4math) ⭐372🔴

### Neuro-Symbolic AI

- [Towards Data-and Knowledge-Driven Artificial Intelligence: A Survey on Neuro-Symbolic Computing](https://arxiv.org/abs/2210.15889) — *IEEE TPAMI 2024* · 📈62 — A comprehensive survey on neuro-symbolic AI, organizing major methods, taxonomies, and design choices.

### Neurosymbolic AI

- [Neuro-Symbolic AI in 2024: A Systematic Review](https://arxiv.org/abs/2501.05435) — *arXiv 2025* · 📈67 — A comprehensive review on neurosymbolic AI, organizing major methods, taxonomies, and design choices.

### SAT Solving and ML

- [Machine Learning Methods in Solving the Boolean Satisfiability Problem](https://arxiv.org/abs/2203.04755) — *Machine Intelligence Research 2022* · 📈52 — A key reference on SAT solving and ML, organizing major methods, taxonomies, and design choices.

### Self-Improving AI

- [A Survey on Self-Evolution of Large Language Models](https://arxiv.org/abs/2404.14387) — *arXiv 2024* · 📈70 — A survey on self-improving AI, organizing major methods, taxonomies, and design choices.

### Theorem Proving & ML

- [A Survey on Deep Learning for Theorem Proving](https://arxiv.org/abs/2404.09939) — *COLM 2024* · 📈63 — A comprehensive survey on theorem proving & ML, covering core methods, applications, and research trends. — [`zhaoyu-li/DL4TP`](https://github.com/zhaoyu-li/DL4TP) ⭐225🟡

### World Models

- [Understanding World or Predicting Future? A Comprehensive Survey of World Models](https://arxiv.org/abs/2411.14499) — *ACM Computing Surveys 2025* · 📈159 — A comprehensive comprehensive survey on world models, organizing major methods, taxonomies, and design choices. — [`tsinghua-fib-lab/World-Model`](https://github.com/tsinghua-fib-lab/World-Model) ⭐738🟡

## 🧩 Neural Network Foundations

### Activation Functions

- [Activation Functions in Deep Learning: A Comprehensive Survey and Benchmark](https://arxiv.org/abs/2109.14545) — *Neurocomputing 2022* · 📈1087 — A comprehensive survey on activation functions, with emphasis on benchmarks, evaluation, and representative methods.
- [Three Decades of Activations: A Comprehensive Survey of 400 Activation Functions for Neural Networks](https://arxiv.org/abs/2402.09092) — *arXiv 2024* · 📈53 — A comprehensive comprehensive survey on activation functions, organizing major methods, taxonomies, and design choices.

### Attention Mechanisms

- [Attention, please! A survey of Neural Attention Models in Deep Learning](https://arxiv.org/abs/2103.16775) — *Artificial Intelligence Review 2022* · 📈279 — A survey on attention mechanisms, organizing major methods, taxonomies, and design choices.

### CNN Fundamentals

- [Recent Advances in Convolutional Neural Networks](https://arxiv.org/abs/1512.07108) — *Pattern Recognition 2018* · 📈5945 — A standard survey of CNN advances, including layer design, activations, losses, regularization, and optimization.
- [A Survey of the Recent Architectures of Deep Convolutional Neural Networks](https://arxiv.org/abs/1901.06032) — *Artificial Intelligence Review 2020* · 📈2686 — A highly cited survey on CNN fundamentals, organizing major methods, taxonomies, and design choices.

### Capsule Networks

- [Learning with Capsules: A Survey](https://arxiv.org/abs/2206.02664) — *ACM Computing Surveys 2024* · 📈22 — A survey on capsule networks, covering core methods, applications, and research trends.

### Deep Learning Overview

- [Deep Learning in Neural Networks: An Overview](https://arxiv.org/abs/1404.7828) — *Neural Networks 2015* · 📈17506 — Schmidhuber's broad, highly cited review of the history and landscape of deep learning.

### Diffusion Models Theory

- [Diffusion Models: A Comprehensive Survey of Methods and Applications](https://arxiv.org/abs/2209.00796) — *ACM Computing Surveys 2023* · 📈2245 — A comprehensive survey on diffusion models theory, organizing major methods, taxonomies, and design choices. — [`YangLing0818/Diffusion-Models-Papers-Survey-Taxonomy`](https://github.com/YangLing0818/Diffusion-Models-Papers-Survey-Taxonomy) ⭐3345🟡

### Efficient Transformers

- [Efficient Transformers: A Survey](https://arxiv.org/abs/2009.06732) — *ACM Computing Surveys 2022* · 📈1522 — A standard survey on efficient transformers, organizing major methods, taxonomies, and design choices.

### Equivariant Neural Networks

- [Geometric Deep Learning and Equivariant Neural Networks](https://arxiv.org/abs/2105.13926) — *Artificial Intelligence Review 2023* · 📈112 — A key reference on equivariant neural networks, covering theoretical foundations, methods, and implications.

### Geometric Deep Learning

- [Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges](https://arxiv.org/abs/2104.13478) — *arXiv 2021* · 📈1598 — A comprehensive key reference on geometric deep learning, organizing major methods, taxonomies, and design choices. — [project](https://geometricdeeplearning.com/book/)

### Implicit Neural Representations

- [Where Do We Stand with Implicit Neural Representations? A Technical and Performance Survey](https://arxiv.org/abs/2411.03688) — *arXiv 2024* · 📈54 — A survey on implicit neural representations, with comparative analysis of representative methods and systems.

### Mixture of Experts

- [A Review of Sparse Expert Models in Deep Learning](https://arxiv.org/abs/2209.01667) — *arXiv 2022* · 📈204 — A review on mixture of experts, organizing major methods, taxonomies, and design choices.
- [A Comprehensive Survey of Mixture-of-Experts: Algorithms, Theory, and Applications](https://arxiv.org/abs/2503.07137) — *arXiv 2025* · 📈97 — A comprehensive recent comprehensive survey on mixture of experts, covering core methods, applications, and research trends.

### Neural ODE / Differential Equations

- [Comprehensive Review of Neural Differential Equations for Time Series Analysis](https://arxiv.org/abs/2502.09885) — *IJCAI (Survey Track) 2025* · 📈22 — A review on neural ODE and differential equations, covering core methods, applications, and research trends.

### Normalization Layers

- [Normalization Techniques in Training DNNs: Methodology, Analysis and Application](https://arxiv.org/abs/2009.12836) — *IEEE TPAMI 2023* · 📈438 — A key reference on normalization layers, organizing major methods, taxonomies, and design choices. — [`huangleiBuaa/NormalizationSurvey`](https://github.com/huangleiBuaa/NormalizationSurvey) ⭐85🔴

### Physics-Informed NN

- [Physics-Informed Machine Learning: A Survey on Problems, Methods and Applications](https://arxiv.org/abs/2211.08064) — *arXiv 2023* · 📈178 — A comprehensive survey on physics-informed NN, organizing major methods, taxonomies, and design choices.

### Quantum Machine Learning

- [A comprehensive review of Quantum Machine Learning: from NISQ to Fault Tolerance](https://arxiv.org/abs/2401.11351) — *Reports on Progress in Physics 2024* · 📈108 — A review on quantum machine learning, covering theoretical foundations, methods, and implications.
- [A Survey on Quantum Machine Learning: Current Trends, Challenges, Opportunities, and the Road Ahead](https://arxiv.org/abs/2310.10315) — *arXiv 2023* · 📈74 — A comprehensive survey on quantum machine learning, organizing major methods, taxonomies, and design choices.

### RNN / LSTM

- [Fundamentals of Recurrent Neural Network (RNN) and Long Short-Term Memory (LSTM) Network](https://arxiv.org/abs/1808.03314) — *Physica D 2020* · 📈4982 — A theoretical primer deriving canonical RNN and LSTM forms from differential-equation perspectives.
- [Recent Advances in Recurrent Neural Networks](https://arxiv.org/abs/1801.01078) — *arXiv 2018* · 📈728 — A standard recent key reference on RNN and LSTM, covering theoretical foundations, methods, and implications.

### Regularization / Dropout

- [Survey of Dropout Methods for Deep Neural Networks](https://arxiv.org/abs/1904.13310) — *arXiv 2019* · 📈174 — A comprehensive survey on regularization and dropout, organizing major methods, taxonomies, and design choices.

### Sparse Neural Networks

- [Sparsity in Deep Learning: Pruning and growth for efficient inference and training in neural networks](https://arxiv.org/abs/2102.00554) — *JMLR 2021* · 📈966 — A comprehensive key reference on sparse neural networks, surveying major methods, techniques, and algorithmic choices.
- [A Survey on Deep Neural Network Pruning: Taxonomy, Comparison, Analysis, and Recommendations](https://arxiv.org/abs/2308.06767) — *IEEE TPAMI 2024* · 📈483 — A comprehensive recent survey on sparse neural networks, with comparative analysis of representative methods and systems.

### Spiking Neural Networks

- [Deep Learning in Spiking Neural Networks](https://arxiv.org/abs/1804.08150) — *Neural Networks 2019* · 📈1345 — A key reference on spiking neural networks, with comparative analysis of representative methods and systems.
- [Toward Large-scale Spiking Neural Networks: A Comprehensive Survey and Future Directions](https://arxiv.org/abs/2409.02111) — *arXiv 2024* · 📈12 — A comprehensive comprehensive survey on spiking neural networks, summarizing key methods, datasets, applications, and research directions.

### State Space Models

- [A Survey of Mamba](https://arxiv.org/abs/2408.01129) — *arXiv 2024* · 📈93 — A survey on state space models, covering core methods, applications, and research trends.
- [Mamba-360: Survey of State Space Models as Transformer Alternative for Long Sequence Modelling](https://arxiv.org/abs/2404.16112) — *arXiv 2024* · 📈89 — A survey on state space models, with comparative analysis of representative methods and systems. — [`badripatro/mamba360`](https://github.com/badripatro/mamba360) ⭐71🔴

### Test-Time Adaptation

- [A Comprehensive Survey on Test-Time Adaptation under Distribution Shifts](https://arxiv.org/abs/2303.15361) — *IJCV 2025* · 📈512 — A comprehensive comprehensive survey on test-time adaptation, organizing major methods, taxonomies, and design choices. — [`tim-learn/awesome-test-time-adaptation`](https://github.com/tim-learn/awesome-test-time-adaptation) ⭐1288🟡

### Transformer Architectures

- [A Survey of Transformers](https://arxiv.org/abs/2106.04554) — *AI Open 2022* · 📈1494 — A survey on Transformer architectures, covering core methods, applications, and research trends.

## 🏭 Applications and Cross-Domain AI

### AI x Agriculture

- [AI in Agriculture: A Survey of Deep Learning Techniques for Crops, Fisheries and Livestock](https://arxiv.org/abs/2507.22101) — *arXiv 2026* · 📈8 — A comprehensive survey on AI for agriculture, organizing major methods, taxonomies, and design choices.

### AI x Cybersecurity - Intrusion Detection

- [Deep Learning-based Intrusion Detection Systems: A Survey](https://arxiv.org/abs/2504.07839) — *arXiv 2025* · 📈29 — A comprehensive survey on AI for cybersecurity: intrusion detection, organizing major methods, taxonomies, and design choices.

### AI x Education - Intelligent Tutoring

- [Large Language Models for Education: A Survey](https://arxiv.org/abs/2405.13001) — *arXiv 2024* · 📈79 — A comprehensive survey on AI for education: intelligent tutoring, covering core methods, applications, and research trends.

### AI x Energy - Load Forecasting

- [Short-Term Electricity-Load Forecasting by Deep Learning: A Comprehensive Survey](https://arxiv.org/abs/2408.16202) — *arXiv 2025* · 📈59 — A comprehensive comprehensive survey on AI for energy: load forecasting, organizing major methods, taxonomies, and design choices.

### AI x Finance

- [Deep Learning for Financial Applications : A Survey](https://arxiv.org/abs/2002.05786) — *Applied Soft Computing 2020* · 📈498 — A highly cited survey on AI for finance, covering core methods, applications, and research trends.

### AI x Finance - Algorithmic Trading

- [Deep Reinforcement Learning in Quantitative Algorithmic Trading: A Review](https://arxiv.org/abs/2106.00123) — *arXiv 2021* · 📈56 — A review on AI for finance: algorithmic trading, organizing major methods, taxonomies, and design choices.

### AI x Finance - Financial LLM

- [A Survey of Large Language Models for Financial Applications: Progress, Prospects and Challenges](https://arxiv.org/abs/2406.11903) — *arXiv 2024* · 📈151 — A survey on AI for finance: financial LLM, covering methods, challenges, and future research directions.

### AI x Finance - Fraud Detection

- [Year-over-Year Developments in Financial Fraud Detection via Deep Learning: A Systematic Literature Review](https://arxiv.org/abs/2502.00201) — *arXiv 2025* · 📈40 — A systematic literature review on AI for finance: fraud detection, surveying major methods, techniques, and algorithmic choices.

### AI x Healthcare

- [Deep EHR: A Survey of Recent Advances in Deep Learning Techniques for Electronic Health Record (EHR) Analysis](https://arxiv.org/abs/1706.03446) — *IEEE JBHI 2018* · 📈1438 — A survey on AI for healthcare, covering core methods, applications, and research trends.

### AI x Healthcare - Clinical NLP / EHR

- [A Comprehensive Survey of Electronic Health Record Modeling: From Deep Learning Approaches to Large Language Models](https://arxiv.org/abs/2507.12774) — *arXiv 2025* · 📈10 — A comprehensive comprehensive survey on AI for healthcare: clinical NLP and EHR, organizing major methods, taxonomies, and design choices.

### AI x Healthcare - Computational Pathology

- [Artificial Intelligence for Digital and Computational Pathology](https://doi.org/10.1038/s44222-023-00096-8) — *Nature Reviews Bioengineering 2023* · 📈323 — A key reference on AI for healthcare: computational pathology, covering methods, challenges, and future research directions.

### AI x Healthcare - Digital Pathology Foundation Models

- [A New Era in Computational Pathology: A Survey on Foundation and Vision-Language Models](https://arxiv.org/abs/2408.14496) — *arXiv 2024* · 📈12 — A recent survey on AI for healthcare: digital pathology foundation models, summarizing key methods, datasets, applications, and research directions.

### AI x Healthcare - Medical Image Segmentation

- [From CNN to Transformer: A Review of Medical Image Segmentation Models](https://arxiv.org/abs/2308.05305) — *arXiv 2023* · 📈197 — A review on AI for healthcare: medical image segmentation, organizing major methods, taxonomies, and design choices.

### AI x Healthcare - Medical LLM

- [A Survey on Medical Large Language Models: Technology, Application, Trustworthiness, and Future Directions](https://arxiv.org/abs/2406.03712) — *arXiv 2024* · 📈53 — A comprehensive survey on AI for healthcare: medical LLM, covering methods, challenges, and future research directions.

### AI x Healthcare - Mental Health NLP

- [A Survey on Multilingual Mental Disorders Detection from Social Media Data](https://arxiv.org/abs/2505.15556) — *arXiv 2026* · 📈4 — A survey on AI for healthcare: mental health NLP, summarizing key methods, datasets, applications, and research directions.

### AI x Healthcare - Radiology Report Generation

- [A Survey of Deep Learning-based Radiology Report Generation Using Multimodal Data](https://arxiv.org/abs/2405.12833) — *arXiv 2025* · 📈8 — A survey on AI for healthcare: radiology report generation, summarizing key methods, datasets, applications, and research directions.

### AI x IoT/Edge - TinyML

- [From Tiny Machine Learning to Tiny Deep Learning: A Survey](https://arxiv.org/abs/2506.18927) — *arXiv 2025* · 📈31 — A comprehensive survey on AI for iot/edge: tinyml, organizing major methods, taxonomies, and design choices.

### AI x Law - Legal LLM

- [Large Language Models Meet Legal Artificial Intelligence: A Survey](https://arxiv.org/abs/2509.09969) — *arXiv 2025* · 📈8 — A comprehensive survey on AI for law: legal LLM, with emphasis on benchmarks, evaluation, and representative methods.

### AI x Manufacturing - Anomaly Detection

- [Deep Learning for Unsupervised Anomaly Localization in Industrial Images: A Survey](https://arxiv.org/abs/2207.10298) — *arXiv 2022* · 📈247 — A survey on AI for manufacturing: anomaly detection, organizing major methods, taxonomies, and design choices.

### AI x Manufacturing - Industrial Time Series Anomaly Detection

- [A Comprehensive Survey of Deep Transfer Learning for Anomaly Detection in Industrial Time Series: Methods, Applications, and Directions](https://arxiv.org/abs/2307.05638) — *arXiv 2024* · 📈164 — A comprehensive comprehensive survey on AI for manufacturing: industrial time series anomaly detection, organizing major methods, taxonomies, and design choices.

### AI x Mobility - Autonomous Driving Foundation Models

- [A Survey for Foundation Models in Autonomous Driving](https://arxiv.org/abs/2402.01105) — *arXiv 2024* · 📈65 — A survey on AI for mobility: autonomous driving foundation models, organizing major methods, taxonomies, and design choices.

### AI x Music - Deep Music Generation

- [A Comprehensive Survey on Deep Music Generation: Multi-level Representations, Algorithms, Evaluations, and Future Directions](https://arxiv.org/abs/2011.06801) — *arXiv 2020* · 📈148 — A comprehensive comprehensive survey on AI for music: deep music generation, with emphasis on benchmarks, evaluation, and representative methods.

### AI x Networking

- [Deep Learning in Mobile and Wireless Networking: A Survey](https://arxiv.org/abs/1803.04311) — *IEEE Communications Surveys & Tutorials 2019* · 📈1499 — A standard survey on AI for networking, covering core methods, applications, and research trends.

### AI x Society - Finance/Healthcare/Law

- [A Survey on Large Language Models for Critical Societal Domains: Finance, Healthcare, and Law](https://arxiv.org/abs/2405.01769) — *arXiv 2024* · 📈100 — A survey on AI for society: finance/healthcare/law, covering core methods, applications, and research trends.

### AI x Software Engineering

- [A Survey on Deep Learning for Software Engineering](https://arxiv.org/abs/2011.14597) — *ACM Computing Surveys 2022* · 📈234 — A survey on AI for software engineering, covering core methods, applications, and research trends.

### AI x Software Engineering - LLM Agents

- [Large Language Model-Based Agents for Software Engineering: A Survey](https://arxiv.org/abs/2409.02977) — *arXiv 2025* · 📈193 — A survey on AI for software engineering: LLM agents, organizing major methods, taxonomies, and design choices.

### AI x Transportation - GNN

- [Graph Neural Networks in Intelligent Transportation Systems: Advances, Applications and Trends](https://arxiv.org/abs/2401.00713) — *arXiv 2024* · 📈18 — A key reference on AI for transportation: GNN, covering core methods, applications, and research trends.

### Geospatial - Remote Sensing Foundation Models

- [Foundation Models for Remote Sensing and Earth Observation: A Survey](https://arxiv.org/abs/2410.16602) — *IEEE Geoscience and Remote Sensing Magazine 2025* · 📈86 — A comprehensive survey on geospatial: remote sensing foundation models, organizing major methods, taxonomies, and design choices.

### Geospatial - Self-Supervised GeoAI

- [Self-Supervised Representation Learning for Geospatial Objects: A Survey](https://arxiv.org/abs/2408.12133) — *arXiv 2025* · 📈17 — A survey on geospatial: self-supervised geoai, organizing major methods, taxonomies, and design choices.

## 📊 Data-Centric AI and Evaluation

### Active Learning

- [A Survey of Deep Active Learning](https://arxiv.org/abs/2009.00236) — *ACM Computing Surveys 2022* · 📈1481 — A comprehensive survey on active learning, organizing major methods, taxonomies, and design choices.
- [A Survey on Deep Active Learning: Recent Advances and New Frontiers](https://arxiv.org/abs/2405.00334) — *IEEE TNNLS 2024* · 📈136 — A survey on active learning, organizing major methods, taxonomies, and design choices.

### Benchmark Contamination

- [Benchmark Data Contamination of Large Language Models: A Survey](https://arxiv.org/abs/2406.04244) — *arXiv 2024* · 📈120 — A survey on benchmark contamination, with emphasis on benchmarks, evaluation, and representative methods.
- [A Survey on Data Contamination for Large Language Models](https://arxiv.org/abs/2502.14425) — *arXiv 2025* · 📈28 — A survey on benchmark contamination, with emphasis on benchmarks, evaluation, and representative methods.

### Benchmark Design / Model Evaluation

- [Evaluation and Benchmarking of LLM Agents: A Survey](https://arxiv.org/abs/2507.21504) — *arXiv 2025* · 📈125 — A survey on benchmark design and model evaluation, with emphasis on benchmarks, evaluation, and representative methods.

### Benchmark Methodology

- [Can We Trust AI Benchmarks? An Interdisciplinary Review of Current Issues in AI Evaluation](https://arxiv.org/abs/2502.06559) — *arXiv 2025* · 📈57 — A review on benchmark methodology, with emphasis on benchmarks, evaluation, and representative methods.

### Coreset Selection / Data Pruning

- [A Coreset Selection of Coreset Selection Literature: Introduction and Recent Advances](https://arxiv.org/abs/2505.17799) — *arXiv 2025* · 📈18 — A key reference on coreset selection and data pruning, organizing major methods, taxonomies, and design choices.

### Data Augmentation (Graph)

- [Graph Data Augmentation for Graph Machine Learning: A Survey](https://arxiv.org/abs/2202.08871) — *IEEE Data Engineering Bulletin 2022* · 📈107 — A comprehensive survey on data augmentation (graph), organizing major methods, taxonomies, and design choices.

### Data-Centric AI

- [Data-centric Artificial Intelligence: A Survey](https://arxiv.org/abs/2303.10158) — *ACM Computing Surveys 2025* · 📈429 — A survey on data-centric AI, summarizing key methods, datasets, applications, and research directions. — [`daochenzha/data-centric-AI`](https://github.com/daochenzha/data-centric-AI) ⭐1149🔴

### Dataset Distillation

- [Dataset Distillation: A Comprehensive Review](https://arxiv.org/abs/2301.07014) — *IEEE TPAMI 2024* · 📈197 — A recent review on dataset distillation, organizing major methods, taxonomies, and design choices.
- [A Comprehensive Survey of Dataset Distillation](https://arxiv.org/abs/2301.05603) — *IEEE TPAMI 2024* · 📈175 — A comprehensive survey on dataset distillation, covering core methods, applications, and research trends.

### LLM-as-Judge Evaluation

- [A Survey on LLM-as-a-Judge](https://arxiv.org/abs/2411.15594) — *arXiv 2024* · 📈1410 — A survey on LLM-as-judge evaluation, organizing major methods, taxonomies, and design choices.

### Multimodal Harmful Content

- [Detecting and Understanding Harmful Memes: A Survey](https://arxiv.org/abs/2205.04274) — *IJCAI 2022* · 📈109 — A comprehensive survey on multimodal harmful content, organizing major methods, taxonomies, and design choices.

### Synthetic Data

- [Machine Learning for Synthetic Data Generation: A Review](https://arxiv.org/abs/2302.04062) — *arXiv 2023* · 📈282 — A review on synthetic data, covering core methods, applications, and research trends.
- [Comprehensive Exploration of Synthetic Data Generation: A Survey](https://arxiv.org/abs/2401.02524) — *arXiv 2024* · 📈104 — A survey on synthetic data, organizing major methods, taxonomies, and design choices.

### Synthetic Data (LLM)

- [On LLMs-Driven Synthetic Data Generation, Curation, and Evaluation: A Survey](https://arxiv.org/abs/2406.15126) — *ACL Findings 2024* · 📈325 — A survey on synthetic data (LLM), with emphasis on benchmarks, evaluation, and representative methods.

### Synthetic Data Generation

- [Synthetic Data Generation Using Large Language Models: Advances in Text and Code](https://arxiv.org/abs/2503.14023) — *IEEE Access 2025* · 📈84 — A key reference on synthetic data generation, surveying major methods, techniques, and algorithmic choices.
- [A Survey on Data Synthesis and Augmentation for Large Language Models](https://arxiv.org/abs/2410.12896) — *arXiv 2024* · 📈46 — A survey on synthetic data generation, organizing major methods, taxonomies, and design choices.

## Contributing

See [`contributing.md`](contributing.md) for additions and corrections. Only survey, review, and overview papers are included, and entries should be verified against arXiv/DOI/GitHub before publication.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](LICENSE) This curated list is released under CC0 (public domain). Copyright for each paper belongs to its original authors.
