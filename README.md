# Awesome AI Survey Papers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> AI関連分野のトップ会議・トップジャーナル・arXiv で公開された**サーベイ論文 (survey / review / overview)** の厳選キュレーション。研究サーベイの出発点として、良質で網羅的なレビュー論文へ最短で辿り着くことを目的とします。

**889 本のサーベイ論文** / 30 分野 / companion リポジトリ 122 件付き。最終更新 2026-06-05。

各項目は `[タイトル](論文URL) — *venue 年* · 📈被引用数。説明 — [`companion repo`](github) ⭐star🟢鮮度 · [project](ページ)` の形式。

凡例: 📈 被引用数 (Semantic Scholar) · ⭐ GitHub star · 鮮度 🟢直近6ヶ月 / 🟡18ヶ月内 / 🔴それ以前（サーベイ companion は鮮度が低くても網羅性・権威性で価値があります）。

> 📑 収集の全メタデータ・統計・調査手法は [`docs/research-notes.md`](docs/research-notes.md) を参照。

## 目次

- [🧠 大規模言語モデル (LLM)](#-大規模言語モデル-llm) (82)
- [🎨 生成AI・拡散モデル](#-生成ai拡散モデル) (27)
- [🖼️ マルチモーダル・視覚言語](#-マルチモーダル視覚言語) (22)
- [💬 自然言語処理 (NLP)](#-自然言語処理-nlp) (77)
- [🔊 音声・信号処理](#-音声信号処理) (23)
- [👁️ コンピュータビジョン (CV)](#-コンピュータビジョン-cv) (106)
- [📈 機械学習 (一般)](#-機械学習-一般) (93)
- [📐 学習理論](#-学習理論) (18)
- [🎮 強化学習 (RL)](#-強化学習-rl) (34)
- [🤖 ロボティクス・身体性](#-ロボティクス身体性) (22)
- [👥 マルチエージェント](#-マルチエージェント) (21)
- [🕸️ グラフニューラルネット (GNN)](#-グラフニューラルネット-gnn) (31)
- [🔗 知識表現・知識グラフ](#-知識表現知識グラフ) (30)
- [🎯 因果推論](#-因果推論) (15)
- [⏱️ 時系列・時空間](#-時系列時空間) (20)
- [⛏️ データマイニング](#-データマイニング) (28)
- [🗄️ データベース・データ管理](#-データベースデータ管理) (17)
- [🔍 情報検索 (IR)](#-情報検索-ir) (14)
- [🛒 推薦システム](#-推薦システム) (21)
- [🌐 Web・ソーシャル](#-webソーシャル) (11)
- [🛡️ 信頼できるAI (公平性・XAI・安全性)](#-信頼できるai-公平性xai安全性) (30)
- [📡 連合学習](#-連合学習) (19)
- [🖐️ HCI・ヒューマンAI](#-hciヒューマンai) (14)
- [🧬 進化計算](#-進化計算) (11)
- [🔢 理論計算機科学](#-理論計算機科学) (8)
- [🔬 AI for Science](#-ai-for-science) (19)
- [🌟 人工知能 (全般)](#-人工知能-全般) (9)
- [🧩 ニューラルネット基礎](#-ニューラルネット基礎) (27)
- [🏭 応用・横断領域](#-応用横断領域) (29)
- [📊 データ中心AI・評価](#-データ中心ai評価) (11)

## 🧠 大規模言語モデル (LLM)

### Code LLM

- [Large Language Models for Software Engineering: A Systematic Literature Review](https://arxiv.org/abs/2308.10620) — *ACM TOSEM 2023* · 📈988。395論文を分析したソフトウェア工学向けLLMの系統的文献レビュー
- [A Survey on Large Language Models for Code Generation](https://arxiv.org/abs/2406.00515) — *arXiv 2024* · 📈943。コード生成LLMのデータ・手法・評価・倫理を体系化したサーベイ — [`huybery/Awesome-Code-LLM`](https://github.com/huybery/Awesome-Code-LLM) ⭐1285🔴
- [Unifying the Perspectives of NLP and Software Engineering: A Survey on Language Models for Code](https://arxiv.org/abs/2311.07989) — *TMLR 2023* · 📈113。70+モデル・900+研究を整理したコード言語モデルの包括的サーベイ — [`codefuse-ai/Awesome-Code-LLM`](https://github.com/codefuse-ai/Awesome-Code-LLM) ⭐3373🟢

### Code Reasoning

- [Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence in LLMs](https://arxiv.org/abs/2502.19411) — *arXiv 2025* · 📈50。コードと推論の双方向関係(コード生成と推論駆動)を整理した総説

### Compression / Quantization

- [A Survey on Model Compression for Large Language Models](https://arxiv.org/abs/2308.07633) — *TACL 2023* · 📈445。量子化・枝刈り・蒸留を軸にLLM圧縮を整理したTACLサーベイ
- [Efficient Large Language Models: A Survey](https://arxiv.org/abs/2312.03863) — *TMLR 2023* · 📈232。モデル/データ/フレームワークの3視点でLLM効率化を網羅した総説 — [`AIoT-MLSys-Lab/Efficient-LLMs-Survey`](https://github.com/AIoT-MLSys-Lab/Efficient-LLMs-Survey) ⭐1260🟡
- [The Efficiency Spectrum of Large Language Models: An Algorithmic Survey](https://arxiv.org/abs/2312.00678) — *arXiv 2023* · 📈37。スケーリング則から推論までLLM効率のアルゴリズム的側面を俯瞰

### Context Engineering

- [A Survey of Context Engineering for Large Language Models](https://arxiv.org/abs/2507.13334) — *arXiv 2025* · 📈105。1400本超を分析しプロンプト設計を超える文脈最適化を体系化(3k+ star companion) — [`Meirtz/Awesome-Context-Engineering`](https://github.com/Meirtz/Awesome-Context-Engineering) ⭐3169🟢

### Continual Learning

- [Towards Lifelong Learning of Large Language Models: A Survey](https://arxiv.org/abs/2406.06391) — *ACM Computing Surveys 2024* · 📈94。内部/外部知識の12シナリオでLLMの生涯学習を分類したサーベイ

### Data Agents

- [A Survey of Data Agents: Emerging Paradigm or Overstated Hype?](https://arxiv.org/abs/2510.23587) — *arXiv 2025* · 📈24。自律性の度合いに沿ってデータエージェント研究を構造化したサーベイ — [`HKUSTDial/awesome-data-agents`](https://github.com/HKUSTDial/awesome-data-agents) ⭐568🟢

### Diffusion Language Models

- [A Survey on Diffusion Language Models](https://arxiv.org/abs/2508.10875) — *arXiv 2025* · 📈64。拡散言語モデルの原理・最新モデル・学習・推論・マルチモーダル拡張を俯瞰(1k+ star) — [`VILA-Lab/Awesome-DLMs`](https://github.com/VILA-Lab/Awesome-DLMs) ⭐1075🟢

### Efficient Inference / KV Cache

- [A Survey on Efficient Inference for Large Language Models](https://arxiv.org/abs/2404.14294) — *arXiv 2024* · 📈228。データ/モデル/システムの3層でLLM効率推論を整理し比較実験も実施
- [LLM Inference Unveiled: Survey and Roofline Model Insights](https://arxiv.org/abs/2402.16363) — *arXiv 2024* · 📈185。Rooflineモデルでボトルネックを可視化したLLM推論効率化サーベイ
- [Towards Efficient Generative LLM Serving: A Survey from Algorithms to Systems](https://arxiv.org/abs/2312.15234) — *ACM Computing Surveys 2023* · 📈155。アルゴリズムからシステムまでLLMサービングの効率化技術を俯瞰

### Efficient Reasoning

- [Stop Overthinking: A Survey on Efficient Reasoning for Large Language Models](https://arxiv.org/abs/2503.16419) — *arXiv 2025* · 📈391。推論モデルの過剰思考を抑える効率的推論手法を体系化したサーベイ — [`Eclipsess/Awesome-Efficient-Reasoning-LLMs`](https://github.com/Eclipsess/Awesome-Efficient-Reasoning-LLMs) ⭐769🟢
- [A Survey of Efficient Reasoning for Large Reasoning Models: Language, Multimodality, and Beyond](https://arxiv.org/abs/2503.21614) — *arXiv 2025* · 📈131。冗長な推論トレースの効率化を言語・マルチモーダル・エージェント横断で整理 — [`XiaoYee/Awesome_Efficient_LRM_Reasoning`](https://github.com/XiaoYee/Awesome_Efficient_LRM_Reasoning) ⭐355🟢

### Emergent Abilities / Scaling

- [Emergent Abilities in Large Language Models: A Survey](https://arxiv.org/abs/2503.05788) — *arXiv 2025* · 📈50。創発能力をスケーリング則・タスク複雑度等の観点で整理したサーベイ

### GUI Agents

- [Large Language Model-Brained GUI Agents: A Survey](https://arxiv.org/abs/2411.18279) — *arXiv 2024* · 📈171。GUI操作を行うLLMエージェントの歴史・構成要素・技術を包括的に整理 — [`vyokky/LLM-Brained-GUI-Agents-Survey`](https://github.com/vyokky/LLM-Brained-GUI-Agents-Survey) ⭐230🟡

### GraphRAG

- [A Survey of Graph Retrieval-Augmented Generation for Customized Large Language Models](https://arxiv.org/abs/2501.13958) — *arXiv 2025* · 📈108。グラフベースRAG(GraphRAG)を体系的に分析したサーベイ(2.4k+ star companion) — [`DEEP-PolyU/Awesome-GraphRAG`](https://github.com/DEEP-PolyU/Awesome-GraphRAG) ⭐2430🟢

### Hallucination

- [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://arxiv.org/abs/2311.05232) — *ACM TOIS 2023* · 📈2940。幻覚の原理・分類・課題を網羅した代表的ハルシネーションサーベイ — [`LuckyyySTA/Awesome-LLM-hallucination`](https://github.com/LuckyyySTA/Awesome-LLM-hallucination) ⭐335🔴
- [Siren's Song in the AI Ocean: A Survey on Hallucination in Large Language Models](https://arxiv.org/abs/2309.01219) — *arXiv 2023* · 📈1014。入力矛盾・文脈矛盾・事実矛盾の分類でLLM幻覚を整理したサーベイ — [`HillZhang1999/llm-hallucination-survey`](https://github.com/HillZhang1999/llm-hallucination-survey) ⭐1086🟡
- [A Comprehensive Survey of Hallucination Mitigation Techniques in Large Language Models](https://arxiv.org/abs/2401.01313) — *arXiv 2024* · 📈449。RAG等32種超の幻覚緩和手法を分類・比較したミティゲーション専門サーベイ

### In-Context Learning

- [A Survey on In-context Learning](https://arxiv.org/abs/2301.00234) — *EMNLP 2023* · 📈1044。文脈内学習の定義・手法・分析を体系化した定番サーベイ — [`EgoAlpha/prompt-in-context-learning`](https://github.com/EgoAlpha/prompt-in-context-learning) ⭐2239🟢

### In-Context Learning Theory

- [The Mystery of In-Context Learning: A Comprehensive Survey on Interpretation and Analysis](https://arxiv.org/abs/2311.00237) — *EMNLP 2023* · 📈46。文脈内学習の解釈・理論的分析を包括的に整理したサーベイ

### Instruction Tuning

- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) — *NeurIPS 2022* · 📈21350。InstructGPT論文。人間フィードバックによる指示追従学習の基礎を確立
- [Instruction Tuning for Large Language Models: A Survey](https://arxiv.org/abs/2308.10792) — *arXiv 2023* · 📈878。指示チューニング(SFT)の手法・データ構築・応用を整理した代表的サーベイ — [`xiaoya-li/Instruction-Tuning-Survey`](https://github.com/xiaoya-li/Instruction-Tuning-Survey) ⭐232🟡

### KV Cache Compression

- [KV Cache Compression for Inference Efficiency in LLMs: A Review](https://arxiv.org/abs/2508.06297) — *arXiv preprint 2025* · 📈7。選択的トークン・量子化・注意圧縮などKVキャッシュ圧縮による推論効率化をレビュー。

### Knowledge & Dataset Distillation for LLMs

- [Knowledge Distillation and Dataset Distillation of Large Language Models: Emerging Trends, Challenges, and Future Directions](https://arxiv.org/abs/2504.14772) — *arXiv preprint 2025* · 📈40。LLM圧縮の補完的2手法、知識蒸留とデータセット蒸留を包括的に分析したサーベイ。

### Knowledge Distillation

- [A Survey on Knowledge Distillation of Large Language Models](https://arxiv.org/abs/2402.13116) — *arXiv 2024* · 📈327。LLMの知識蒸留(技能蒸留・データ拡張)を体系化した総説 — [`Tebmer/Awesome-Knowledge-Distillation-of-LLMs`](https://github.com/Tebmer/Awesome-Knowledge-Distillation-of-LLMs) ⭐1283🟡

### Knowledge Editing

- [Editing Large Language Models: Problems, Methods, and Opportunities](https://arxiv.org/abs/2305.13172) — *EMNLP 2023* · 📈454。知識編集タスクの定義・手法・課題を整理しベンチも提供(1.2k+ star companion) — [`zjunlp/KnowledgeEditingPapers`](https://github.com/zjunlp/KnowledgeEditingPapers) ⭐1231🟡
- [Knowledge Editing for Large Language Models: A Survey](https://arxiv.org/abs/2310.16218) — *ACM Computing Surveys 2023* · 📈253。知識編集(KME)技術の分類・評価・課題を整理した代表的サーベイ
- [A Comprehensive Study of Knowledge Editing for Large Language Models](https://arxiv.org/abs/2401.01286) — *arXiv 2024* · 📈160。外部/パラメータ/内部の3分類とKnowEditベンチを提案した知識編集研究 — [`zjunlp/EasyEdit`](https://github.com/zjunlp/EasyEdit) ⭐2836🟢

### Knowledge Mechanisms

- [Knowledge Mechanisms in Large Language Models: A Survey and Perspective](https://arxiv.org/abs/2407.15017) — *EMNLP Findings 2024* · 📈69。LLMが知識を記憶・理解・適用・進化させる機構をレビュー(EMNLP 2024 Findings) — [`zjunlp/KnowledgeEditingPapers`](https://github.com/zjunlp/KnowledgeEditingPapers) ⭐1231🟡

### LLM Agents

- [A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432) — *Frontiers of Computer Science 2023* · 📈3008。LLM自律エージェントの構築統一枠組・応用・評価を整理した代表的サーベイ — [`Paitesanshi/LLM-Agent-Survey`](https://github.com/Paitesanshi/LLM-Agent-Survey) ⭐2901🟡
- [The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/abs/2309.07864) — *arXiv 2023* · 📈1769。脳・知覚・行動の枠組で単体/マルチエージェントと社会を俯瞰した大規模総説 — [`WooooDyy/LLM-Agent-Paper-List`](https://github.com/WooooDyy/LLM-Agent-Paper-List) ⭐8142🟡
- [ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate](https://arxiv.org/abs/2308.07201) — *ICLR 2024* · 📈924。複数LLMの討論で評価精度を高めるマルチエージェント評価枠組 — [`thunlp/ChatEval`](https://github.com/thunlp/ChatEval) ⭐335🔴

### LLM Evaluation

- [A Survey on Evaluation of Large Language Models](https://arxiv.org/abs/2307.03109) — *ACM TIST 2023* · 📈3399。何を/どこで/どう評価するかの3軸でLLM評価を整理した定番サーベイ — [`MLGroupJLU/LLM-eval-survey`](https://github.com/MLGroupJLU/LLM-eval-survey) ⭐1600🟢
- [Evaluating Large Language Models: A Comprehensive Survey](https://arxiv.org/abs/2310.19736) — *arXiv 2023* · 📈311。知識能力・整合性・安全性の3分類でLLM評価を網羅したサーベイ — [`tjunlp-lab/Awesome-LLMs-Evaluation-Papers`](https://github.com/tjunlp-lab/Awesome-LLMs-Evaluation-Papers) ⭐803🔴

### LLM General

- [A Survey of Large Language Models](https://arxiv.org/abs/2303.18223) — *arXiv 2023* · 📈4514。事前学習・適応・利用・評価の4側面でLLMを俯瞰した定番大規模サーベイ(144頁) — [`RUCAIBox/LLMSurvey`](https://github.com/RUCAIBox/LLMSurvey) ⭐12168🟡
- [A Comprehensive Overview of Large Language Models](https://arxiv.org/abs/2307.06435) — *arXiv 2023* · 📈1657。アーキテクチャ・学習・微調整・マルチモーダル等を広く整理したLLM総説
- [Large Language Models: A Survey](https://arxiv.org/abs/2402.06196) — *arXiv 2024* · 📈970。主要LLMファミリと構築・評価・データセットを概観した総説
- [Datasets for Large Language Models: A Comprehensive Survey](https://arxiv.org/abs/2402.18041) — *arXiv 2024* · 📈133。事前学習・指示・選好・評価データ444件を体系化したデータセットサーベイ

### LLM Unlearning

- [A Comprehensive Survey of Machine Unlearning Techniques for Large Language Models](https://arxiv.org/abs/2503.01854) — *arXiv 2025* · 📈29。LLMの機械的アンラーニング手法を4分類で網羅した総説

### Long Context

- [Advancing Transformer Architecture in Long-Context LLMs: A Comprehensive Survey](https://arxiv.org/abs/2311.12351) — *arXiv 2023* · 📈121。長文コンテキスト処理のTransformer改良を網羅した長文LLMサーベイ — [`Strivin0311/long-llms-learning`](https://github.com/Strivin0311/long-llms-learning) ⭐274🔴
- [Beyond the Limits: A Survey of Techniques to Extend the Context Length in Large Language Models](https://arxiv.org/abs/2402.02244) — *IJCAI 2024* · 📈103。LLMの文脈長拡張技術(位置符号化・注意機構の改変)を整理した総説
- [The What, Why, and How of Context Length Extension Techniques in Large Language Models](https://arxiv.org/abs/2401.07872) — *arXiv 2024* · 📈47。コンテキスト長拡張技術を体系的にレビューし評価課題を整理

### Long Context Modeling

- [A Comprehensive Survey on Long Context Language Modeling](https://arxiv.org/abs/2503.17407) — *arXiv 2025* · 📈111。長文脈LLMの獲得・学習/展開・評価を網羅した包括サーベイ(2k+ star companion) — [`Xnhyacinth/Awesome-LLM-Long-Context-Modeling`](https://github.com/Xnhyacinth/Awesome-LLM-Long-Context-Modeling) ⭐2111🟢

### Mathematical Reasoning

- [A Survey on Large Language Models for Mathematical Reasoning](https://arxiv.org/abs/2506.08446) — *arXiv 2025* · 📈47。LLMの数学推論を理解と解生成の2認知段階で整理したサーベイ

### Mechanistic Interpretability

- [A Survey on Sparse Autoencoders: Interpreting the Internal Mechanisms of Large Language Models](https://arxiv.org/abs/2503.05613) — *arXiv 2025* · 📈53。スパースオートエンコーダによるLLM内部機構の解釈手法を整理

### Mixture-of-Experts

- [A Survey on Mixture of Experts in Large Language Models](https://arxiv.org/abs/2407.06204) — *IEEE TKDE 2024* · 📈313。LLMにおけるMoEのアルゴリズム・システム・応用を整理した専門サーベイ — [`withinmiaov/A-Survey-on-Mixture-of-Experts-in-LLMs`](https://github.com/withinmiaov/A-Survey-on-Mixture-of-Experts-in-LLMs) ⭐504🟡

### Multilingual LLM

- [A Survey on Multilingual Large Language Models: Corpora, Alignment, and Bias](https://arxiv.org/abs/2404.00929) — *arXiv 2024* · 📈127。多言語LLMのコーパス・アラインメント・バイアスを整理したサーベイ

### Parameter-Efficient Fine-Tuning

- [Parameter-Efficient Fine-Tuning for Large Models: A Comprehensive Survey](https://arxiv.org/abs/2403.14608) — *TMLR 2024* · 📈934。LoRA系を含むPEFTの分類・アルゴリズム・システム実装を網羅した総説
- [Parameter-Efficient Fine-Tuning Methods for Pretrained Language Models: A Critical Review and Assessment](https://arxiv.org/abs/2312.12148) — *arXiv 2023* · 📈344。PEFT手法を批判的にレビューしパラメータ/メモリ効率を実験評価
- [Scaling Down to Scale Up: A Guide to Parameter-Efficient Fine-Tuning](https://arxiv.org/abs/2303.15647) — *arXiv 2023* · 📈276。50件超のPEFTを分類し15手法を実験比較した実践ガイド型サーベイ
- [A Survey on LoRA of Large Language Models](https://arxiv.org/abs/2407.11046) — *Frontiers of Computer Science 2024* · 📈146。LLMのLoRAをパラメータ効率/分散学習/応用の観点で整理したサーベイ — [`ZJU-LLMs/Awesome-LoRAs`](https://github.com/ZJU-LLMs/Awesome-LoRAs) ⭐271🔴

### Persona / Role-Play

- [Two Tales of Persona in LLMs: A Survey of Role-Playing and Personalization](https://arxiv.org/abs/2406.01171) — *arXiv 2024* · 📈256。LLMのロールプレイとパーソナライゼーションを二系統で整理したサーベイ

### Personal LLM Agents

- [Personal LLM Agents: Insights and Survey about the Capability, Efficiency and Security](https://arxiv.org/abs/2401.05459) — *arXiv 2024* · 📈340。能力・効率・セキュリティの観点で個人向けLLMエージェントを整理 — [`MobileLLM/Personal_LLM_Agents_Survey`](https://github.com/MobileLLM/Personal_LLM_Agents_Survey) ⭐430🔴

### RL for Deep Research Agents

- [Reinforcement Learning Foundations for Deep Research Systems: A Survey](https://arxiv.org/abs/2509.06733) — *arXiv preprint 2025* · 📈8。深層リサーチ系エージェントのRL基盤をデータ合成・RL手法・訓練システムの3軸で整理したサーベイ。

### RL for LLMs

- [Reinforcement Learning Meets Large Language Models: A Survey of Advancements and Applications Across the LLM Lifecycle](https://arxiv.org/abs/2509.16679) — *arXiv preprint 2025* · 📈23。事前学習・アライメント・推論強化までLLMの全段階でのRL活用を俯瞰したサーベイ。

### RL for Reasoning

- [A Survey of Reinforcement Learning for Large Reasoning Models](https://arxiv.org/abs/2509.08827) — *arXiv 2025* · 📈140。推論自体を促す大規模推論モデル向けRLを整理したサーベイ

### RLHF / Alignment

- [Safe RLHF: Safe Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2310.12773) — *ICLR 2024* · 📈705。有用性と無害性を分離し制約付き最適化で安全に整合する手法を提示
- [AI Alignment: A Comprehensive Survey](https://arxiv.org/abs/2310.19852) — *arXiv 2023* · 📈353。RICE原則と前方/後方アラインメントでAI整合性研究を網羅した大規模総説 — [`PKU-Alignment/AlignmentSurvey`](https://github.com/PKU-Alignment/AlignmentSurvey) ⭐137🔴 · [project](https://alignmentsurvey.com)
- [Large Language Model Alignment: A Survey](https://arxiv.org/abs/2309.15025) — *arXiv 2023* · 📈316。外部/内部アラインメントの分類と評価手法を整理したアラインメント総説
- [Secrets of RLHF in Large Language Models Part I: PPO](https://arxiv.org/abs/2307.04964) — *arXiv 2023* · 📈275。RLHFのPPO実装の要点と安定化(PPO-max)を詳細に解説した実践サーベイ

### Reasoning / Chain-of-Thought

- [Towards Reasoning in Large Language Models: A Survey](https://arxiv.org/abs/2212.10403) — *ACL Findings 2022* · 📈896。LLMの推論能力を喚起・評価・分析する技術を俯瞰した推論サーベイ
- [Navigate through Enigmatic Labyrinth: A Survey of Chain of Thought Reasoning](https://arxiv.org/abs/2309.15402) — *ACL 2024* · 📈257。Chain-of-Thought推論の進展・フロンティア・将来を整理したCoT専門サーベイ — [`Zoeyyao27/CoT-Igniting-Agent`](https://github.com/Zoeyyao27/CoT-Igniting-Agent) ⭐365🔴
- [LLM Post-Training: A Deep Dive into Reasoning Large Language Models](https://arxiv.org/abs/2502.21321) — *arXiv 2025* · 📈100。微調整・強化学習・推論時スケーリング等のポストトレーニングを概観

### Retrieval-Augmented Generation

- [A Survey on RAG Meeting LLMs: Towards Retrieval-Augmented Large Language Models](https://arxiv.org/abs/2405.06211) — *KDD 2024* · 📈877。LLM時代のRAGアーキテクチャと学習・応用を俯瞰したKDDサーベイ
- [Retrieval-Augmented Generation for AI-Generated Content: A Survey](https://arxiv.org/abs/2402.19473) — *arXiv 2024* · 📈596。RAGの基盤・強化・応用をAIGC全般にわたり分類した大規模サーベイ(1.7k+ star) — [`hymie122/RAG-Survey`](https://github.com/hymie122/RAG-Survey) ⭐1788🔴

### Role-Play

- [The Oscars of AI Theater: A Survey on Role-Playing with Language Models](https://arxiv.org/abs/2407.11484) — *arXiv 2024* · 📈55。言語モデルのキャラクタ・ロールプレイ研究を体系化した総説

### Safety / Jailbreak

- [Trustworthy LLMs: A Survey and Guideline for Evaluating Large Language Models' Alignment](https://arxiv.org/abs/2308.05374) — *arXiv 2023* · 📈542。信頼性7カテゴリ29サブカテゴリでLLMの安全性評価指針を提示
- [Jailbreak Attacks and Defenses Against Large Language Models: A Survey](https://arxiv.org/abs/2407.04295) — *arXiv 2024* · 📈274。ジェイルブレイク攻撃と防御の分類体系を整理した専門サーベイ
- [Attacks, Defenses and Evaluations for LLM Conversation Safety: A Survey](https://arxiv.org/abs/2402.09283) — *NAACL 2024* · 📈160。会話安全の攻撃・防御・評価を3分類で整理したNAACLサーベイ — [`niconi19/LLM-Conversation-Safety`](https://github.com/niconi19/LLM-Conversation-Safety) ⭐111🔴

### Self-Correction

- [Automatically Correcting Large Language Models: Surveying the landscape of diverse self-correction strategies](https://arxiv.org/abs/2308.03188) — *TACL 2023* · 📈285。LLMの自己修正/自己改善戦略を多様な観点で整理したサーベイ

### Small Language Models

- [A Comprehensive Survey of Small Language Models in the Era of Large Language Models](https://arxiv.org/abs/2411.03350) — *arXiv 2024* · 📈193。SLMの技術・応用・LLMとの協調・信頼性を包括的に整理したサーベイ
- [A Survey of Small Language Models](https://arxiv.org/abs/2410.20011) — *arXiv 2024* · 📈48。小規模言語モデルのアーキテクチャ・学習・圧縮手法を分類した総説

### Speculative Decoding

- [Closer Look at Efficient Inference Methods: A Survey of Speculative Decoding](https://arxiv.org/abs/2411.13157) — *arXiv preprint 2024* · 📈7。LLM推論加速の中核である投機的デコーディング手法を包括的に整理したサーベイ。

### Test-Time Compute

- [A Survey of Test-Time Compute: From Intuitive Inference to Deliberate Reasoning](https://arxiv.org/abs/2501.02497) — *arXiv 2025* · 📈19。o1系のテスト時計算/推論時スケーリングをSystem-1/2の観点で整理した総説

### Text Watermarking

- [A Survey of Text Watermarking in the Era of Large Language Models](https://arxiv.org/abs/2312.07913) — *arXiv 2023* · 📈167。LLM時代のテキスト透かし技術・評価・応用を概観したサーベイ

### Theory of Mind

- [A Survey of Theory of Mind in Large Language Models: Evaluations, Representations, and Safety Risks](https://arxiv.org/abs/2502.06470) — *arXiv 2025* · 📈7。LLMの心の理論の評価・内部表現・安全リスクを整理した総説

### Tool Use

- [Tool Learning with Foundation Models](https://arxiv.org/abs/2304.08354) — *ACM Computing Surveys 2023* · 📈397。基盤モデルのツール学習を体系化し18種ツールで実証した代表的サーベイ — [`OpenBMB/BMTools`](https://github.com/OpenBMB/BMTools) ⭐2774🔴
- [What Are Tools Anyway? A Survey from the Language Model Perspective](https://arxiv.org/abs/2403.15452) — *COLM 2024* · 📈64。LM視点でツールを定義し利用効果と効率を実証分析したツール利用サーベイ

## 🎨 生成AI・拡散モデル

### 3D Generation

- [Generative AI meets 3D: A Survey on Text-to-3D in AIGC Era](https://arxiv.org/abs/2305.06131) — *arXiv 2023* · 📈102。忠実度・効率・一貫性等の観点でテキスト3D生成を整理したサーベイ
- [Advances in 3D Generation: A Survey](https://arxiv.org/abs/2401.17807) — *arXiv 2024* · 📈91。3D表現・生成手法・データ・応用を俯瞰した3D生成サーベイ

### 4D Generation

- [Advances in 4D Generation: A Survey](https://arxiv.org/abs/2503.14501) — *arXiv 2025* · 📈0。4D(時空間)生成の表現・手法・応用を包括的に整理したサーベイ

### AIGC General

- [A Comprehensive Survey of AI-Generated Content (AIGC): A History of Generative AI from GAN to ChatGPT](https://arxiv.org/abs/2303.04226) — *arXiv 2023* · 📈796。GANからChatGPTまで生成AIの歴史と単一/マルチモーダル生成を俯瞰

### Audio / Music Generation

- [Sparks of Large Audio Models: A Survey and Outlook](https://arxiv.org/abs/2308.12792) — *arXiv 2023* · 📈63。音声認識・TTS・音楽生成等の大規模音声モデルを概観したサーベイ — [`EmulationAI/awesome-large-audio-models`](https://github.com/EmulationAI/awesome-large-audio-models) ⭐731🟢

### Autoregressive Visual Generation

- [Autoregressive Models in Vision: A Survey](https://arxiv.org/abs/2411.05902) — *TMLR 2024* · 📈51。視覚における自己回帰モデル(画像/動画/3D生成)を分類した総説 — [`ChaofanTao/Autoregressive-Models-in-Vision-Survey`](https://github.com/ChaofanTao/Autoregressive-Models-in-Vision-Survey) ⭐796🟢

### Concept Erasure

- [A Comprehensive Survey on Concept Erasure in Text-to-Image Diffusion Models](https://arxiv.org/abs/2502.14896) — *arXiv 2025* · 📈9。安全な画像生成のための概念消去手法を介入レベル別に整理した総説

### Controllable Generation

- [Controllable Generation with Text-to-Image Diffusion Models: A Survey](https://arxiv.org/abs/2403.04279) — *IEEE TPAMI 2024* · 📈94。特定条件・複数条件・汎用制御の3分類で制御可能T2I生成を整理 — [`PRIV-Creation/Awesome-Controllable-T2I-Diffusion-Models`](https://github.com/PRIV-Creation/Awesome-Controllable-T2I-Diffusion-Models) ⭐1113🟡

### Diffusion Acceleration

- [Efficient Diffusion Models: A Comprehensive Survey from Principles to Practices](https://arxiv.org/abs/2410.11795) — *TMLR 2024* · 📈53。アーキ・学習・高速推論・展開の効率視点で拡散モデルを俯瞰したサーベイ — [`AIoT-MLSys-Lab/Efficient-Diffusion-Model-Survey`](https://github.com/AIoT-MLSys-Lab/Efficient-Diffusion-Model-Survey) ⭐184🟢

### Diffusion Distillation

- [A Survey on Pre-Trained Diffusion Model Distillations](https://arxiv.org/abs/2502.08364) — *arXiv 2025* · 📈5。事前学習拡散モデルの蒸留を出力損失/軌道/敵対的の観点で整理

### Diffusion Theory

- [Score-based Diffusion Models via Stochastic Differential Equations -- a Technical Tutorial](https://arxiv.org/abs/2402.07487) — *arXiv 2024* · 📈50。SDEによるスコアベース拡散モデルの理論を解説したチュートリアル

### Efficient Diffusion

- [Efficient Diffusion Models: A Survey](https://arxiv.org/abs/2502.06805) — *TMLR 2025* · 📈41。拡散モデルの効率化をアルゴリズム/システム/フレームワークで整理 — [`AIoT-MLSys-Lab/Efficient-Diffusion-Model-Survey`](https://github.com/AIoT-MLSys-Lab/Efficient-Diffusion-Model-Survey) ⭐184🟢

### GAN

- [A Review on Generative Adversarial Networks: Algorithms, Theory, and Applications](https://arxiv.org/abs/2001.06937) — *IEEE TKDE 2020* · 📈1108。GANのアルゴリズム・理論・応用を体系的に俯瞰した代表的レビュー

### Human Motion Generation

- [Human Motion Generation: A Survey](https://arxiv.org/abs/2307.10894) — *IEEE TPAMI 2023* · 📈136。テキスト/音声/シーン条件付きの人間モーション生成を概観した総説

### Image Editing

- [Diffusion Model-Based Image Editing: A Survey](https://arxiv.org/abs/2402.17525) — *IEEE TPAMI 2024* · 📈263。学習戦略・入力条件・タスク別に拡散ベース画像編集を整理したサーベイ — [`SiatMMLab/Awesome-Diffusion-Model-Based-Image-Editing-Methods`](https://github.com/SiatMMLab/Awesome-Diffusion-Model-Based-Image-Editing-Methods) ⭐713🟡
- [A Survey of Multimodal-Guided Image Editing with Text-to-Image Diffusion Models](https://arxiv.org/abs/2406.14555) — *arXiv 2024* · 📈62。テキスト画像拡散モデルによるマルチモーダル誘導画像編集の総説

### Music Generation

- [Vision-to-Music Generation: A Survey](https://arxiv.org/abs/2503.21254) — *ISMIR 2025* · 📈5。動画・画像から音楽を生成する手法・データ・評価を整理(ISMIR 2025) — [`wzk1015/Awesome-Vision-to-Music-Generation`](https://github.com/wzk1015/Awesome-Vision-to-Music-Generation) ⭐124🟡

### Normalizing Flow

- [Normalizing Flows: An Introduction and Review of Current Methods](https://arxiv.org/abs/1908.09257) — *IEEE TPAMI 2019* · 📈58。正規化フローの構築法と最新手法を整理した代表的レビュー

### Personalization

- [A Survey on Personalized Content Synthesis with Diffusion Models](https://arxiv.org/abs/2405.05538) — *arXiv 2024* · 📈38。拡散モデルによる被写体駆動パーソナライズ生成を整理した総説

### Text-to-Image

- [RenAIssance: A Survey into AI Text-to-Image Generation in the Era of Large Model](https://arxiv.org/abs/2309.00810) — *IEEE TPAMI 2023* · 📈78。大規模モデル時代のテキスト画像生成を5節で俯瞰したTPAMIサーベイ

### Text-to-Video

- [A Survey on Video Diffusion Models](https://arxiv.org/abs/2310.10647) — *ACM Computing Surveys 2023* · 📈277。動画生成・編集・理解の3領域で動画拡散モデルを整理した代表的サーベイ — [`ChenHsing/Awesome-Video-Diffusion-Models`](https://github.com/ChenHsing/Awesome-Video-Diffusion-Models) ⭐2293🟢
- [Sora as a World Model? A Complete Survey on Text-to-Video Generation](https://arxiv.org/abs/2403.05131) — *arXiv 2024* · 📈72。250件超を世界モデルの観点で整理したテキスト動画生成サーベイ
- [Video Diffusion Models: A Survey](https://arxiv.org/abs/2405.03150) — *TMLR 2024* · 📈45。時間的一貫性や入力モダリティ別に動画拡散モデルを分類したサーベイ — [`ndrwmlnk/Awesome-Video-Diffusion-Models`](https://github.com/ndrwmlnk/Awesome-Video-Diffusion-Models) ⭐56🟡

### VAE

- [An Introduction to Variational Autoencoders](https://arxiv.org/abs/1906.02691) — *Foundations and Trends in ML 2019* · 📈3045。VAEの理論と実装を体系的に解説した定番の入門・総説

### Video Editing

- [Diffusion Model-Based Video Editing: A Survey](https://arxiv.org/abs/2407.07111) — *arXiv 2024* · 📈50。拡散モデルによる動画編集の理論基盤と手法を整理した総説

### Video Generation

- [Controllable Video Generation: A Survey](https://arxiv.org/abs/2507.16869) — *arXiv 2025* · 📈64。カメラ・深度・ポーズ等の条件付き制御動画生成を体系的にレビュー — [`mayuelala/Awesome-Controllable-Video-Generation`](https://github.com/mayuelala/Awesome-Controllable-Video-Generation) ⭐741🟢

### World Models

- [Simulating the Real World: A Unified Survey of Multimodal Generative Models](https://arxiv.org/abs/2503.04641) — *IEEE TPAMI 2025* · 📈16。2D/video/3D/4D生成を世界シミュレーションの観点で統一的に俯瞰(TPAMI 2026) — [`ALEEEHU/World-Simulator`](https://github.com/ALEEEHU/World-Simulator) ⭐378🟢

## 🖼️ マルチモーダル・視覚言語

### 3D-LLM

- [When LLMs step into the 3D World: A Survey and Meta-Analysis of 3D Tasks via Multi-modal Large Language Models](https://arxiv.org/abs/2405.10255) — *arXiv 2024* · 📈38。点群/NeRF等の3DタスクをMLLMで扱う研究を網羅したメタ分析付き総説 — [`ActiveVisionLab/Awesome-LLM-3D`](https://github.com/ActiveVisionLab/Awesome-LLM-3D) ⭐2215🟢

### Audio-Visual

- [Deep Audio-Visual Learning: A Survey](https://arxiv.org/abs/2001.04758) — *International Journal of Automation and Computing 2020* · 📈191。分離・対応・生成・表現学習の4分野で音響視覚学習を整理した代表的サーベイ

### Autonomous Driving

- [A Survey on Multimodal Large Language Models for Autonomous Driving](https://arxiv.org/abs/2311.12320) — *WACV 2024* · 📈515。自動運転向けマルチモーダルLLMのツール・データ・課題を整理(WACV 2024) — [`IrohXu/Awesome-Multimodal-LLM-Autonomous-Driving`](https://github.com/IrohXu/Awesome-Multimodal-LLM-Autonomous-Driving) ⭐311🔴

### Document AI

- [Document AI: Benchmarks, Models and Applications](https://arxiv.org/abs/2111.08609) — *arXiv 2021* · 📈97。文書理解のベンチマーク・モデル・応用を俯瞰したDocument AIサーベイ

### Embodied Multimodal

- [A Survey on Vision-Language-Action Models for Embodied AI](https://arxiv.org/abs/2405.14093) — *arXiv 2024* · 📈266。身体化AI向けVision-Language-Action(VLA)モデルを整理したサーベイ
- [Agent AI: Surveying the Horizons of Multimodal Interaction](https://arxiv.org/abs/2401.03568) — *arXiv 2024* · 📈250。環境に接地したマルチモーダルエージェントAIの地平を俯瞰した総説

### Label-Free VLM Adaptation

- [Adapting Vision-Language Models Without Labels: A Comprehensive Survey](https://arxiv.org/abs/2508.05547) — *arXiv preprint 2025* · 📈6。ラベルなしでVLMを適応する手法(プロンプト学習・擬似ラベル等)を4パラダイムで整理したサーベイ。 — [`tim-learn/Awesome-LabelFree-VLMs`](https://github.com/tim-learn/Awesome-LabelFree-VLMs) ⭐91🟢

### Mathematical Reasoning

- [A Survey of Mathematical Reasoning in the Era of Multimodal Large Language Model: Benchmark, Method & Challenges](https://arxiv.org/abs/2412.11936) — *ACL Findings 2024* · 📈58。MLLM時代の数学推論をベンチマーク/手法/課題で整理した総説

### Mechanistic Interpretability

- [A Survey on Mechanistic Interpretability for Multi-Modal Foundation Models](https://arxiv.org/abs/2502.17516) — *arXiv 2025* · 📈34。マルチモーダル基盤モデルの機構的解釈可能性を整理した総説

### Multimodal Agents

- [Large Multimodal Agents: A Survey](https://arxiv.org/abs/2402.15116) — *arXiv 2024* · 📈111。大規模マルチモーダルエージェント(LMA)の構成要素と協調枠組を整理 — [`jun0wanan/awesome-large-multimodal-agents`](https://github.com/jun0wanan/awesome-large-multimodal-agents) ⭐491🔴

### Multimodal Hallucination

- [Hallucination of Multimodal Large Language Models: A Survey](https://arxiv.org/abs/2404.18930) — *arXiv 2024* · 📈392。MLLMの視覚と不整合な出力(幻覚)の原因・評価・緩和を整理したサーベイ

### Multimodal LLM

- [A Survey on Multimodal Large Language Models](https://arxiv.org/abs/2306.13549) — *National Science Review 2023* · 📈1385。MLLMのアーキ・学習・データ・評価を整理した最も参照される代表的サーベイ — [`BradyFU/Awesome-Multimodal-Large-Language-Models`](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models) ⭐17857🟢
- [MM-LLMs: Recent Advances in MultiModal Large Language Models](https://arxiv.org/abs/2401.13601) — *ACL Findings 2024* · 📈423。126種MM-LLMの設計枠組と学習技術を分類したACLサーベイ — [project](https://mm-llms.github.io)

### Multimodal RAG

- [Ask in Any Modality: A Comprehensive Survey on Multimodal Retrieval-Augmented Generation](https://arxiv.org/abs/2502.08826) — *ACL Findings 2025* · 📈50。任意モダリティのマルチモーダルRAGを包括的に整理した総説
- [A Survey of Multimodal Retrieval-Augmented Generation](https://arxiv.org/abs/2504.08748) — *arXiv 2025* · 📈43。マルチモーダルRAGの検索・生成統合手法を概観したサーベイ

### Multimodal Reasoning

- [Multimodal Chain-of-Thought Reasoning: A Comprehensive Survey](https://arxiv.org/abs/2503.12605) — *arXiv 2025* · 📈179。マルチモーダル連鎖思考(MCoT)推論を初めて体系的に整理した総説 — [`yaotingwangofficial/Awesome-MCoT`](https://github.com/yaotingwangofficial/Awesome-MCoT) ⭐1004🟢
- [Perception, Reason, Think, and Plan: A Survey on Large Multimodal Reasoning Models](https://arxiv.org/abs/2505.04921) — *arXiv 2025* · 📈73。大規模マルチモーダル推論モデルをSystem-2志向で整理した総説

### Prompt Engineering

- [A Systematic Survey of Prompt Engineering on Vision-Language Foundation Models](https://arxiv.org/abs/2307.12980) — *arXiv 2023*。CLIP/Flamingo/Stable Diffusion等VLMへのプロンプト工学を体系的にレビュー — [`JindongGu/Awesome-Prompting-on-Vision-Language-Model`](https://github.com/JindongGu/Awesome-Prompting-on-Vision-Language-Model) ⭐510🟡

### Unified Multimodal Models

- [Unified Multimodal Understanding and Generation Models: Advances, Challenges, and Opportunities](https://arxiv.org/abs/2505.02567) — *arXiv 2025* · 📈62。理解と生成を統一するマルチモーダルモデルの進展と課題を概観 — [`AIDC-AI/Awesome-Unified-Multimodal-Models`](https://github.com/AIDC-AI/Awesome-Unified-Multimodal-Models) ⭐1277🟢

### Video LLM

- [Video Understanding with Large Language Models: A Survey](https://arxiv.org/abs/2312.17432) — *arXiv 2023* · 📈255。LLMを活用したビデオ理解(Vid-LLM)の手法を分類した総説

### Video-Language

- [Video-Language Understanding: A Survey from Model Architecture, Model Training, and Data Perspectives](https://arxiv.org/abs/2406.05615) — *ACL Findings 2024* · 📈42。アーキ・学習・データの3視点で動画言語理解を整理したACLサーベイ

### Vision-Language Pretraining

- [Vision-Language Pre-training: Basics, Recent Advances, and Future Trends](https://arxiv.org/abs/2210.09263) — *Foundations and Trends in CV 2022* · 📈214。画像テキスト・コアCV・動画テキストでVLP手法を俯瞰した大規模総説(102頁)

## 💬 自然言語処理 (NLP)

### Adversarial Attacks (NLP)

- [Adversarial Attacks on Deep Learning Models in Natural Language Processing: A Survey](https://arxiv.org/abs/1901.06796) — *ACM TIST 2019* · 📈57。テキストへの敵対的サンプル生成手法を網羅した定番サーベイ
- [A Survey of Adversarial Defences and Robustness in NLP](https://arxiv.org/abs/2203.06414) — *ACM Computing Surveys 2022* · 📈36。NLPの敵対的防御・頑健性手法を新分類学で整理
- [Adversarial Attacks and Defense on Texts: A Survey](https://arxiv.org/abs/2005.14108) — *arXiv 2020* · 📈24。テキスト敵対的攻撃を文字・単語・文・複数レベルで分類

### Argument Mining

- [Large Language Models in Argument Mining: A Survey](https://arxiv.org/abs/2506.16383) — *arXiv 2025* · 📈14。LLM時代の議論マイニング各サブタスクを再整理したサーベイ

### Biomedical NLP

- [SECNLP: A Survey of Embeddings in Clinical Natural Language Processing](https://arxiv.org/abs/1903.01039) — *Journal of Biomedical Informatics 2019* · 📈95。臨床NLPにおける各種埋め込み表現を初めて詳細に整理したサーベイ

### Code-switching

- [A Survey of Code-switched Speech and Language Processing](https://arxiv.org/abs/1904.00784) — *arXiv 2019* · 📈155。コードスイッチングの音声・言語処理とデータ資源を整理したサーベイ
- [The Decades Progress on Code-Switching Research in NLP: A Systematic Survey on Trends and Challenges](https://arxiv.org/abs/2212.09660) — *ACL Findings 2023* · 📈62。数十年のコードスイッチング研究の動向と課題を体系的に整理

### Computational Morphology

- [Recent advancements in computational morphology: A comprehensive survey](https://arxiv.org/abs/2406.05424) — *arXiv 2024* · 📈5。形態素解析・語形変化・分割等の計算形態論を包括的に整理したサーベイ

### Coreference Resolution

- [A Neural Entity Coreference Resolution Review](https://arxiv.org/abs/1910.09329) — *Expert Systems with Applications 2019* · 📈43。ニューラル共参照解析の進展・データ・評価指標を整理
- [Coreference Resolution for the Biomedical Domain: A Survey](https://arxiv.org/abs/2109.12424) — *arXiv 2021* · 📈20。生物医学ドメインの共参照解析データと手法を整理したサーベイ

### Cross-lingual Transfer

- [Transfer Learning for Multi-lingual Tasks -- a Survey](https://arxiv.org/abs/2110.02052) — *arXiv 2021* · 📈6。多言語・言語横断タスクへの転移学習をアーキテクチャ視点で整理

### Data Augmentation (NLP)

- [A Survey of Data Augmentation Approaches for NLP](https://arxiv.org/abs/2105.03075) — *Findings of ACL 2021* · 📈979。NLPのデータ拡張手法を体系的に整理した代表的サーベイ

### Data-to-Text Generation

- [Innovations in Neural Data-to-text Generation: A Survey](https://arxiv.org/abs/2207.12571) — *arXiv 2022* · 📈12。ニューラルなデータ/表→テキスト生成の手法とデータを整理したサーベイ

### Dialogue State Tracking

- ["Do you follow me?": A Survey of Recent Approaches in Dialogue State Tracking](https://arxiv.org/abs/2207.14627) — *SIGDIAL 2022* · 📈36。タスク指向対話の対話状態追跡の近年の手法を整理したサーベイ

### Dialogue Systems

- [A Survey on Dialogue Systems: Recent Advances and New Frontiers](https://arxiv.org/abs/1711.01731) — *ACM SIGKDD Explorations 2017* · 📈766。タスク指向型・非タスク指向型対話システムを概観した定番サーベイ
- [Recent Advances in Deep Learning Based Dialogue Systems: A Systematic Survey](https://arxiv.org/abs/2105.04387) — *Artificial Intelligence Review 2021* · 📈342。深層学習ベース対話システムを体系的に整理した大規模サーベイ
- [A Short Survey of Pre-trained Language Models for Conversational AI - A New Age in NLP](https://arxiv.org/abs/2104.10810) — *ACSW 2020* · 📈82。会話AIにおける事前学習言語モデル活用を簡潔に整理

### Discourse Parsing

- [A Survey of Implicit Discourse Relation Recognition](https://arxiv.org/abs/2203.02982) — *ACM Computing Surveys 2022* · 📈34。暗黙的談話関係認識の手法を体系的に整理した談話解析サーベイ

### Empathetic Dialogue

- [Empathetic Conversational Systems: A Review of Current Advances, Gaps, and Opportunities](https://arxiv.org/abs/2206.05017) — *IEEE Transactions on Affective Computing 2022* · 📈52。共感的対話システムの進展・ギャップ・機会をレビューしたサーベイ

### Evaluation & Benchmarks

- [A Survey of Evaluation Metrics Used for NLG Systems](https://arxiv.org/abs/2008.12009) — *ACM Computing Surveys 2020* · 📈329。NLG評価指標の発展(ヒューリスティック〜学習型)を整理
- [Survey on Factuality in Large Language Models: Knowledge, Retrieval and Domain-Specificity](https://arxiv.org/abs/2310.07521) — *arXiv 2023* · 📈286。LLMの事実性(factuality)を知識・検索・ドメイン観点で整理

### Explainability (NLP)

- [A Survey of the State of Explainable AI for Natural Language Processing](https://arxiv.org/abs/2010.00711) — *AACL-IJCNLP 2020* · 📈461。NLPの説明可能AI技術を概観した代表的サーベイ
- [Post-hoc Interpretability for Neural NLP: A Survey](https://arxiv.org/abs/2108.04840) — *ACM Computing Surveys 2021* · 📈312。ニューラルNLPの事後解釈手法を分類・検証法とともに整理
- [Local Interpretations for Explainable Natural Language Processing: A Survey](https://arxiv.org/abs/2103.11072) — *ACM Computing Surveys 2021* · 📈69。局所的解釈手法に焦点を当てた説明可能NLPのサーベイ

### Fact-Checking

- [A Survey on Automated Fact-Checking](https://arxiv.org/abs/2108.11896) — *TACL 2021* · 📈723。主張検出・証拠検索・検証を貫く自動事実検証の定番サーベイ
- [Explainable Automated Fact-Checking: A Survey](https://arxiv.org/abs/2011.03870) — *COLING 2020* · 📈148。事実検証における説明生成手法に焦点を当てたサーベイ
- [Generative Large Language Models in Automated Fact-Checking: A Survey](https://arxiv.org/abs/2407.02351) — *arXiv 2024* · 📈20。生成LLMを事実検証に用いる手法とプロンプト戦略を整理したサーベイ

### Financial NLP

- [A Survey of Large Language Models in Finance (FinLLMs)](https://arxiv.org/abs/2402.02315) — *arXiv 2024* · 📈150。金融特化LLMの歴史・技術・性能と課題を整理したサーベイ
- [Language Modeling for the Future of Finance: A Survey into Metrics, Tasks, and Data Opportunities](https://arxiv.org/abs/2504.07274) — *arXiv 2025* · 📈5。金融NLP論文374件を指標・タスク・データの観点で定量分析したサーベイ

### Grammatical Error Correction

- [Grammatical Error Correction: A Survey of the State of the Art](https://arxiv.org/abs/2211.05166) — *Computational Linguistics 2023* · 📈130。文法誤り訂正の手法・データ・評価を網羅した決定版サーベイ
- [A Comprehensive Survey of Grammar Error Correction](https://arxiv.org/abs/2005.06600) — *arXiv 2020* · 📈42。SMT/NMT/分類/言語モデルの4系統でGECを整理した包括サーベイ

### Keyphrase Extraction

- [Keyphrase Generation: A Multi-Aspect Survey](https://arxiv.org/abs/1910.05059) — *FRUCT 2019* · 📈24。抽出型・生成型のキーフレーズ抽出/生成を多角的に整理したサーベイ

### Legal NLP

- [Natural Language Processing for the Legal Domain: A Survey of Tasks, Datasets, Models, and Challenges](https://arxiv.org/abs/2410.21306) — *ACM Computing Surveys 2025* · 📈86。法律ドメインNLPのタスク・データ・モデル・課題を体系化したサーベイ

### Long Document Summarization

- [An Empirical Survey on Long Document Summarization: Datasets, Models and Metrics](https://arxiv.org/abs/2207.00939) — *ACM Computing Surveys 2022* · 📈176。長文要約のデータ・モデル・評価指標を実証的に比較したサーベイ

### Low-Resource & Multilingual

- [Neural Machine Translation for Low-Resource Languages: A Survey](https://arxiv.org/abs/2106.15115) — *ACM Computing Surveys 2021* · 📈359。低資源言語NMTの研究進展を定量分析付きで概観
- [A Survey on Low-Resource Neural Machine Translation](https://arxiv.org/abs/2107.04239) — *IJCAI 2021* · 📈75。低資源NMTの補助データ活用手法を3分類で整理

### Machine Translation

- [Neural Machine Translation: A Review and Survey](https://arxiv.org/abs/1912.02047) — *JAIR 2020* · 📈423。NMTのモデル・学習・推論を網羅した定番の包括的レビュー
- [A Survey of Deep Learning Techniques for Neural Machine Translation](https://arxiv.org/abs/2002.07526) — *arXiv 2020* · 📈153。ニューラル機械翻訳の深層学習技術を体系的に整理した入門的サーベイ
- [A Survey on Non-Autoregressive Generation for Neural Machine Translation and Beyond](https://arxiv.org/abs/2204.09269) — *IEEE TPAMI 2022* · 📈126。非自己回帰生成によるNMT高速化手法を整理したサーベイ

### Multi-document Summarization

- [Multi-document Summarization via Deep Learning Techniques: A Survey](https://arxiv.org/abs/2011.04843) — *ACM Computing Surveys 2020* · 📈160。深層学習による多文書要約モデルを初めて体系化したサーベイ
- [Survey on Multi-Document Summarization: Systematic Literature Review](https://arxiv.org/abs/2312.12915) — *arXiv 2023* · 📈1。多文書要約手法を系統的文献レビューで整理したサーベイ

### NLG Evaluation

- [Leveraging Large Language Models for NLG Evaluation: Advances and Challenges](https://arxiv.org/abs/2401.07103) — *EMNLP 2024* · 📈46。LLMを用いたNLG評価手法を分類整理したサーベイ

### Named Entity Recognition

- [A Survey on Deep Learning for Named Entity Recognition](https://arxiv.org/abs/1812.09449) — *IEEE TKDE 2020* · 📈1457。深層学習によるNERの定番サーベイ(分散表現・文脈エンコーダ等)
- [Recent Advances in Named Entity Recognition: A Comprehensive Survey and Comparative Study](https://arxiv.org/abs/2401.10825) — *arXiv 2024* · 📈47。Transformer/LLM時代のNER最新手法と比較実験を含むサーベイ

### Neural Topic Models

- [A Survey on Neural Topic Models: Methods, Applications, and Challenges](https://arxiv.org/abs/2401.15351) — *Artificial Intelligence Review 2024* · 📈103。ニューラルトピックモデルの手法・応用・課題を網羅したサーベイ

### Persona Dialogue

- [Recent Trends in Personalized Dialogue Generation: A Review of Datasets, Methodologies, and Evaluations](https://arxiv.org/abs/2405.17974) — *LREC-COLING 2024* · 📈33。ペルソナ対話生成のデータ・手法・評価を体系的にレビューしたサーベイ

### Pretrained Language Models (BERT)

- [A Primer in BERTology: What We Know About How BERT Works](https://arxiv.org/abs/2002.12327) — *TACL 2020* · 📈1868。BERTの内部挙動に関する知見をまとめた定番BERTologyサーベイ
- [Pre-trained Models for Natural Language Processing: A Survey](https://arxiv.org/abs/2003.08271) — *Science China Technological Sciences 2020* · 📈1688。NLP事前学習モデルを4視点の分類学で整理した高被引用サーベイ
- [Recent Advances in Natural Language Processing via Large Pre-Trained Language Models: A Survey](https://arxiv.org/abs/2111.01243) — *ACM Computing Surveys 2021* · 📈1521。大規模事前学習モデルによるNLPの最近の進展を整理
- [Pre-Trained Models: Past, Present and Future](https://arxiv.org/abs/2106.07139) — *AI Open 2021* · 📈1064。事前学習モデルの過去・現在・未来を俯瞰した大規模レビュー

### Prompting

- [Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing](https://arxiv.org/abs/2107.13586) — *ACM Computing Surveys 2021* · 📈5397。プロンプト手法を体系化した最重要サーベイ(prompt paradigm) — [`thunlp/PromptPapers`](https://github.com/thunlp/PromptPapers) ⭐4314🔴

### Question Answering

- [A Survey on Complex Knowledge Base Question Answering: Methods, Challenges and Solutions](https://arxiv.org/abs/2105.11644) — *IJCAI 2021* · 📈206。複雑な知識ベースQA(KBQA)の手法と課題を整理
- [QA Dataset Explosion: A Taxonomy of NLP Resources for Question Answering and Reading Comprehension](https://arxiv.org/abs/2107.12708) — *ACM Computing Surveys 2021* · 📈196。QA/読解の大量データセットを分類学として体系化
- [A Survey on Neural Machine Reading Comprehension](https://arxiv.org/abs/1906.03824) — *arXiv 2019* · 📈32。ニューラル機械読解(MRC)の手法とデータセットを整理

### Question Generation

- [A Survey on Neural Question Generation: Methods, Applications, and Prospects](https://arxiv.org/abs/2402.18267) — *IJCAI 2024* · 📈15。構造化/非構造化/ハイブリッドの観点でニューラル質問生成を整理

### Readability Assessment

- [Trends, Limitations and Open Challenges in Automatic Readability Assessment Research](https://arxiv.org/abs/2105.00973) — *LREC 2022* · 📈60。自動可読性評価研究の動向・限界・課題を総括したサーベイ

### Relation Extraction

- [A Comprehensive Survey on Relation Extraction: Recent Advances and New Frontiers](https://arxiv.org/abs/2306.02051) — *ACM Computing Surveys 2023* · 📈127。関係抽出を表現・文脈・トリプル予測の3視点で整理した新分類学
- [A Survey of Deep Learning Methods for Relation Extraction](https://arxiv.org/abs/1705.03645) — *arXiv 2017* · 📈123。関係抽出における各種深層学習モデルの初期サーベイ

### Sarcasm Detection

- [A Survey of Multimodal Sarcasm Detection](https://arxiv.org/abs/2410.18882) — *IJCAI 2024* · 📈33。マルチモーダル皮肉検出のモデルとデータを初めて体系化したサーベイ

### Sentiment Analysis

- [Deep Learning for Sentiment Analysis: A Survey](https://arxiv.org/abs/1801.07883) — *WIREs Data Mining and Knowledge Discovery 2018* · 📈1886。感情分析への深層学習適用を概観した高被引用サーベイ
- [A Survey on Aspect-Based Sentiment Analysis: Tasks, Methods, and Challenges](https://arxiv.org/abs/2203.01054) — *IEEE TKDE 2022* · 📈407。アスペクトベース感情分析(ABSA)のタスク・手法・課題を体系化

### Stance Detection

- [A Survey on Stance Detection for Mis- and Disinformation Identification](https://arxiv.org/abs/2103.00242) — *NAACL Findings 2021* · 📈170。偽情報識別のためのスタンス検出に焦点を当てたサーベイ
- [A Survey of Stance Detection on Social Media: New Directions and Perspectives](https://arxiv.org/abs/2409.15690) — *arXiv 2024* · 📈16。ソーシャルメディアにおけるスタンス検出の課題・手法・展望を整理

### Summarization

- [A Survey on Neural Network-Based Summarization Methods](https://arxiv.org/abs/1804.04589) — *arXiv 2018* · 📈37。抽出型・生成型ニューラル要約手法を整理した初期サーベイ
- [A Survey on Neural Abstractive Summarization Methods and Factual Consistency of Summarization](https://arxiv.org/abs/2204.09519) — *arXiv 2022* · 📈9。生成型要約と事実整合性(factual consistency)に焦点を当てたサーベイ

### Syntactic & Semantic Parsing

- [A Survey on Semantic Parsing](https://arxiv.org/abs/1812.00978) — *AKBC 2018* · 📈138。自然言語から論理形式への意味解析をルールベース〜ニューラルまで概観

### Text Classification

- [Recent Trends in Deep Learning Based Natural Language Processing](https://arxiv.org/abs/1708.02709) — *IEEE Computational Intelligence Magazine 2018* · 📈3068。深層学習NLPの主要モデルと応用を俯瞰した高被引用レビュー
- [Deep Learning Based Text Classification: A Comprehensive Review](https://arxiv.org/abs/2004.03705) — *ACM Computing Surveys 2020* · 📈1314。150超の深層学習テキスト分類モデルと40超のデータセットを整理
- [A Survey on Text Classification: From Shallow to Deep Learning](https://arxiv.org/abs/2008.00364) — *ACM TIST 2020* · 📈523。テキスト分類を浅い手法から深層学習まで時系列で整理
- [Topic Modelling Meets Deep Neural Networks: A Survey](https://arxiv.org/abs/2103.00498) — *IJCAI 2021* · 📈167。ニューラルトピックモデルの手法を体系的に整理したサーベイ

### Text Generation

- [Survey of the State of the Art in Natural Language Generation: Core Tasks, Applications and Evaluation](https://arxiv.org/abs/1703.09902) — *JAIR 2018* · 📈903。自然言語生成のコアタスク・応用・評価を網羅した定番サーベイ

### Text Simplification

- [A Survey on Text Simplification](https://arxiv.org/abs/2008.08612) — *arXiv 2020* · 📈32。語彙・統語・意味の各側面からテキスト平易化を概観したサーベイ
- [Deep Learning Approaches to Lexical Simplification: A Survey](https://arxiv.org/abs/2305.12000) — *arXiv 2023* · 📈24。語彙平易化の深層学習手法を2017-2023年で整理したサーベイ

### Text Style Transfer

- [A Survey of Text Style Transfer: Applications and Ethical Implications](https://arxiv.org/abs/2407.16737) — *arXiv 2024* · 📈2。テキストスタイル変換を応用と倫理的含意の観点から整理したサーベイ

### Word & Sentence Embeddings

- [A Survey on Contextual Embeddings](https://arxiv.org/abs/2003.07278) — *arXiv 2020* · 📈177。文脈化単語埋め込み(ELMo/BERT系)の手法と応用を整理
- [A Comprehensive Survey of Sentence Representations: From the BERT Epoch to the ChatGPT Era and Beyond](https://arxiv.org/abs/2305.12641) — *EACL 2024* · 📈21。文表現学習をBERT期からChatGPT期まで包括的に整理

### Word Sense Disambiguation

- [A Survey on Lexical Ambiguity Detection and Word Sense Disambiguation](https://arxiv.org/abs/2403.16129) — *arXiv 2024* · 📈14。語彙的曖昧性検出と語義曖昧性解消の手法を整理したサーベイ

## 🔊 音声・信号処理

### Audio Foundation Models

- [Audio-Language Models for Audio-Centric Tasks: A Systematic Survey](https://arxiv.org/abs/2501.15177) — *arXiv 2025*。音声中心タスク向け音声言語モデル（audio-language models）を体系的に俯瞰した最新サーベイ

### Automatic Speech Recognition (ASR)

- [A Review of Deep Learning Techniques for Speech Processing](https://arxiv.org/abs/2305.00359) — *Information Fusion 2023* · 📈338。音声処理全般の深層学習技術を網羅的に概観したレビュー
- [End-to-End Speech Recognition: A Survey](https://arxiv.org/abs/2303.03329) — *IEEE/ACM TASLP 2023* · 📈287。エンドツーエンドASRのモデル分類と古典HMM系との関係を整理

### Controllable TTS

- [Towards Controllable Speech Synthesis in the Era of Large Language Models: A Systematic Survey](https://arxiv.org/abs/2412.06602) — *EMNLP 2025* · 📈25。感情・音色・スタイル等を制御するTTSをLLM時代の観点で体系化(EMNLP 2025 main) — [`imxtx/awesome-controllable-speech-synthesis`](https://github.com/imxtx/awesome-controllable-speech-synthesis) ⭐247🟢

### Keyword Spotting

- [Advances in Small-Footprint Keyword Spotting: A Comprehensive Review of Efficient Models and Algorithms](https://arxiv.org/abs/2506.11169) — *arXiv 2025*。小型デバイス向けキーワード検出の効率モデル・アルゴリズムを7分類で包括レビュー

### Multilingual ASR

- [A Survey of Multilingual Models for Automatic Speech Recognition](https://arxiv.org/abs/2202.12576) — *LREC 2022*。多言語ASRの転移学習・共同学習・自己教師あり手法とベストプラクティスをまとめたサーベイ

### Music Information Retrieval

- [A Tutorial on Deep Learning for Music Information Retrieval](https://arxiv.org/abs/1709.04396) — *arXiv 2017* · 📈102。音楽情報処理(MIR)への深層学習適用を解説したチュートリアル兼レビュー

### Self-Supervised Speech (wav2vec)

- [wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations](https://arxiv.org/abs/2006.11477) — *NeurIPS 2020* · 📈8392。自己教師あり音声表現学習の代表的基盤モデル(分野の基礎参照)
- [Self-Supervised Speech Representation Learning: A Review](https://arxiv.org/abs/2205.10643) — *IEEE JSTSP 2022* · 📈492。自己教師あり音声表現学習(wav2vec/HuBERT系)を網羅した定番レビュー

### Sound Event Detection

- [Sound Event Detection: A Tutorial](https://arxiv.org/abs/2107.05463) — *IEEE Signal Processing Magazine 2021*。音響イベント検出(SED)の基礎・手法・評価を解説した入門チュートリアル

### Speaker Recognition & Diarization

- [A Review of Speaker Diarization: Recent Advances with Deep Learning](https://arxiv.org/abs/2101.09624) — *Computer Speech & Language 2021* · 📈427。話者ダイアライゼーションの深層学習による進展を整理した定番レビュー

### Speech Emotion Recognition

- [Emotion Recognition and Generation: A Comprehensive Review of Face, Speech, and Text Modalities](https://arxiv.org/abs/2502.06803) — *arXiv 2025*。顔・音声・テキストにまたがる感情認識と生成の最新技術を包括的にレビュー
- [A Comprehensive Survey on Multi-modal Conversational Emotion Recognition with Deep Learning](https://arxiv.org/abs/2312.05735) — *arXiv 2023*。音声を含むマルチモーダル会話感情認識の深層学習手法を4分類で網羅したサーベイ

### Speech Enhancement & Separation

- [Supervised Speech Separation Based on Deep Learning: An Overview](https://arxiv.org/abs/1708.07524) — *IEEE/ACM TASLP 2018* · 📈1583。深層学習による教師あり音声分離・強調を網羅した定番オーバービュー

### Speech LLM / Audio Foundation Models

- [A Survey on Speech Large Language Models for Understanding](https://arxiv.org/abs/2410.18908) — *arXiv 2024*。音声理解向け音声大規模言語モデルのアーキテクチャと学習戦略を整理したサーベイ

### Speech Language Models

- [Recent Advances in Speech Language Models: A Survey](https://arxiv.org/abs/2410.03751) — *ACL 2025* · 📈109。テキストを介さずend-to-endで音声対話する音声LMの初の包括サーベイ(ACL 2025) — [`dreamtheater123/Awesome-SpeechLM-Survey`](https://github.com/dreamtheater123/Awesome-SpeechLM-Survey) ⭐209🟡

### Speech Translation

- [Direct Speech-to-Speech Neural Machine Translation: A Survey](https://arxiv.org/abs/2411.14453) — *arXiv 2024* · 📈7。直接音声対音声翻訳(S2ST)のモデル・データ・評価を整理したサーベイ

### Spoken Dialogue Systems

- [WavChat: A Survey of Spoken Dialogue Models](https://arxiv.org/abs/2411.13577) — *arXiv 2024*。音声対話モデルをcascaded/end-to-endに分類し技術・データ・評価を網羅したサーベイ — [`jishengpeng/WavChat`](https://github.com/jishengpeng/WavChat) ⭐317🔴

### Spoken Language Understanding (SLU)

- [A Survey on Spoken Language Understanding: Recent Advances and New Frontiers](https://arxiv.org/abs/2103.03095) — *IJCAI 2021*。音声言語理解(SLU)の単一/結合モデルや事前学習パラダイムを整理した定番サーベイ

### Text-to-Speech (TTS)

- [A Survey on Neural Speech Synthesis](https://arxiv.org/abs/2106.15561) — *arXiv 2021* · 📈466。ニューラル音声合成(テキスト解析・音響モデル・ボコーダ)の定番サーベイ

### Voice Conversion

- [Generative Adversarial Network based Voice Conversion: Techniques, Challenges, and Recent Advancements](https://arxiv.org/abs/2504.19197) — *arXiv 2025*。GANベース声質変換の手法・課題・最新動向を体系化したレビュー
- [Reimagining Speech: A Scoping Review of Deep Learning-Powered Voice Conversion](https://arxiv.org/abs/2311.08104) — *arXiv 2023*。2017-2023年の123本を精査した深層学習ベース声質変換のスコーピングレビュー
- [An Overview of Voice Conversion and its Challenges: From Statistical Modeling to Deep Learning](https://arxiv.org/abs/2008.03648) — *IEEE/ACM TASLP 2020*。声質変換を統計モデルから深層学習まで通観した定番の包括的オーバービュー

## 👁️ コンピュータビジョン (CV)

### 3D Gaussian Splatting

- [A Survey on 3D Gaussian Splatting](https://arxiv.org/abs/2401.03890) — *TPAMI 2024*。3Dガウシアンスプラッティングの体系的サーベイ。表現・最適化・応用を整理 — [`guikunchen/Awesome3DGS`](https://github.com/guikunchen/Awesome3DGS) ⭐91🟢

### 3D Object Detection

- [3D Object Detection for Autonomous Driving: A Comprehensive Survey](https://arxiv.org/abs/2206.09474) — *IJCV 2023* · 📈438。自動運転向け3D物体検出(LiDAR/カメラ/マルチモーダル)の包括サーベイ — [`PointsCoder/Awesome-3D-Object-Detection-for-Autonomous-Driving`](https://github.com/PointsCoder/Awesome-3D-Object-Detection-for-Autonomous-Driving) ⭐609🔴

### 3D Vision / Point Cloud

- [Deep Learning for 3D Point Clouds: A Survey](https://arxiv.org/abs/1912.12033) — *TPAMI 2021* · 📈2211。点群の分類/検出/セグメンテーションを網羅した定番サーベイ
- [Transformers in 3D Point Clouds: A Survey](https://arxiv.org/abs/2205.07417) — *arXiv 2022* · 📈73。3D点群解析へのTransformer適用を分類・整理した初の包括サーベイ

### 6D Pose Estimation

- [Deep Learning-Based Object Pose Estimation: A Comprehensive Survey](https://arxiv.org/abs/2405.07801) — *IJCV 2024* · 📈67。物体姿勢推定(インスタンス/カテゴリレベル6D)の包括的サーベイ

### Action Recognition

- [Human Action Recognition from Various Data Modalities: A Review](https://arxiv.org/abs/2012.11866) — *TPAMI 2023* · 📈773。RGB/骨格/深度など多様なモダリティでの行動認識を整理
- [Going Deeper into Action Recognition: A Survey](https://arxiv.org/abs/1605.04988) — *Image and Vision Computing 2017* · 📈640。行動認識の手作り表現から深層手法までの進化を俯瞰した定番サーベイ

### Adversarial Robustness

- [Threat of Adversarial Attacks on Deep Learning in Computer Vision: A Survey](https://arxiv.org/abs/1801.00553) — *IEEE Access 2018* · 📈2050。CVにおける敵対的攻撃と防御を初めて包括的に整理した定番サーベイ

### Anomaly Detection

- [Deep Learning for Anomaly Detection: A Review](https://arxiv.org/abs/2007.02500) — *CSUR 2021* · 📈1325。深層異常検知の手法を体系的な分類で整理したCSURレビュー

### Camouflaged Object Detection

- [A Survey of Camouflaged Object Detection and Beyond](https://arxiv.org/abs/2408.14562) — *arXiv 2024* · 📈64。カモフラージュ物体検出(COD)の最新までを包括的にレビュー

### Continual Learning

- [Class-Incremental Learning: A Survey](https://arxiv.org/abs/2302.03648) — *TPAMI 2023* · 📈349。クラス増分学習(継続学習)の深層手法を分類・比較した包括サーベイ

### Crowd Counting

- [A Survey on Deep Learning-based Single Image Crowd Counting: Network Design, Loss Function and Supervisory Signal](https://arxiv.org/abs/2012.15685) — *Neurocomputing 2020*。単一画像群衆カウントをネットワーク設計・損失・監督信号の観点で整理

### Deepfake Detection

- [Deepfake Generation and Detection: A Benchmark and Survey](https://arxiv.org/abs/2403.17881) — *arXiv 2024* · 📈121。ディープフェイク生成と検出をベンチマークとともに包括的に整理
- [Deepfake Detection: A Comprehensive Survey from the Reliability Perspective](https://arxiv.org/abs/2211.10881) — *ACM Computing Surveys 2022* · 📈119。ディープフェイク検出を信頼性(転移性・解釈性・頑健性)の観点で整理

### Depth Estimation

- [Monocular Depth Estimation Based On Deep Learning: An Overview](https://arxiv.org/abs/2003.06620) — *Science China Technological Sciences 2020* · 📈294。単眼深度推定の深層手法・損失・学習戦略を概観したサーベイ

### Domain Adaptation

- [Deep Visual Domain Adaptation: A Survey](https://arxiv.org/abs/1802.03601) — *Neurocomputing 2018* · 📈2291。視覚タスク向け深層ドメイン適応をシナリオ別に分類した定番サーベイ

### Domain Generalization / Adaptation (CLIP)

- [CLIP-Powered Domain Generalization and Domain Adaptation: A Comprehensive Survey](https://arxiv.org/abs/2504.14280) — *arXiv preprint 2025* · 📈11。CLIPのゼロショット能力を活かしたドメイン汎化・適応手法を体系化した包括サーベイ。 — [`jindongli-Ai/Survey_on_CLIP-Powered_Domain_Generalization_and_Adaptation`](https://github.com/jindongli-Ai/Survey_on_CLIP-Powered_Domain_Generalization_and_Adaptation) ⭐76🟢

### Event Camera

- [Deep Learning for Event-based Vision: A Comprehensive Survey and Benchmarks](https://arxiv.org/abs/2302.08890) — *arXiv 2023* · 📈133。イベントカメラ向け深層学習の表現・タスク・ベンチマークを包括整理

### Face Generation/Editing

- [Face Generation and Editing with StyleGAN: A Survey](https://arxiv.org/abs/2212.09102) — *TPAMI 2022* · 📈93。StyleGANによる顔生成・編集をインバージョン・潜在空間の観点で整理

### Face Recognition

- [Deep Face Recognition: A Survey](https://arxiv.org/abs/1804.06655) — *Neurocomputing 2021* · 📈1421。深層顔認識のアルゴリズム/損失関数/データセットを網羅した定番サーベイ

### Facial Expression Recognition

- [Deep Learning for Micro-expression Recognition: A Survey](https://arxiv.org/abs/2107.02823) — *IEEE Trans. Affective Computing 2021*。微表情認識の深層学習手法・データセット・ベンチマークを整理
- [Deep Facial Expression Recognition: A Survey](https://arxiv.org/abs/1804.08348) — *IEEE Trans. Affective Computing 2018*。深層表情認識(FER)の標準パイプライン・データセット・課題を整理

### Few-Shot Learning

- [Generalizing from a Few Examples: A Survey on Few-Shot Learning](https://arxiv.org/abs/1904.05046) — *CSUR 2020* · 📈2117。少数ショット学習をデータ/モデル/アルゴリズム観点で整理した定番サーベイ
- [Few-Shot Object Detection: A Comprehensive Survey](https://arxiv.org/abs/2112.11699) — *TNNLS 2023* · 📈117。少数ショット物体検出手法の包括的な分類とサーベイ

### Fine-Grained Recognition

- [Fine-Grained Image Analysis with Deep Learning: A Survey](https://arxiv.org/abs/2111.06119) — *TPAMI 2021* · 📈441。細粒度画像解析(認識・検索)の深層学習手法を統合的に整理

### Foundation Models / Segmentation

- [A Comprehensive Survey on Segment Anything Model for Vision and Beyond](https://arxiv.org/abs/2305.08196) — *arXiv 2023* · 📈142。基盤モデルSAMの応用・限界を視覚分野横断で整理した初の包括サーベイ

### Gait Recognition

- [Deep Gait Recognition: A Survey](https://arxiv.org/abs/2102.09546) — *TPAMI 2021*。歩容認識の深層学習手法・データセット・課題を体系的に整理

### Gaussian Splatting

- [3D Gaussian Splatting: Survey, Technologies, Challenges, and Opportunities](https://arxiv.org/abs/2407.17418) — *arXiv 2024* · 📈120。タスク・技術・課題の多視点から3DGSを分析した包括的サーベイ — [`qqqqqqy0227/awesome-3DGS`](https://github.com/qqqqqqy0227/awesome-3DGS) ⭐307🟡
- [A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing, and Generation](https://arxiv.org/abs/2508.09977) — *arXiv 2025* · 📈19。セグメンテーション・編集・生成という3DGS下流応用に特化した初のサーベイ — [`heshuting555/Awesome-3DGS-Applications`](https://github.com/heshuting555/Awesome-3DGS-Applications) ⭐365🟢

### Gaze Estimation

- [Appearance-based Gaze Estimation With Deep Learning: A Review and Benchmark](https://arxiv.org/abs/2104.12668) — *TPAMI 2021*。外観ベース視線推定の深層学習手法のレビューとベンチマーク

### Hand Pose Estimation

- [Efficient Annotation and Learning for 3D Hand Pose Estimation: A Survey](https://arxiv.org/abs/2206.02257) — *IJCV 2022* · 📈26。3D手姿勢推定をアノテーション・学習効率の観点で整理したサーベイ

### Human Pose Estimation

- [Deep learning for 3D human pose estimation and mesh recovery: A survey](https://arxiv.org/abs/2402.18844) — *Neurocomputing 2024* · 📈34。3D人体姿勢推定・メッシュ復元の深層学習手法を200本超で整理

### Human-Object Interaction

- [A Review of Human-Object Interaction Detection](https://arxiv.org/abs/2408.10641) — *arXiv 2024*。HOI検出の2段階・1段階・Transformer手法を包括的にレビュー

### Image Captioning

- [A Comprehensive Survey of Deep Learning for Image Captioning](https://arxiv.org/abs/1810.04020) — *CSUR 2019* · 📈884。画像キャプション生成の深層手法・データセット・評価を整理したCSURサーベイ

### Image Classification / Backbone

- [A Survey of Convolutional Neural Networks: Analysis, Applications, and Prospects](https://arxiv.org/abs/2004.02806) — *TNNLS 2022* · 📈4169。CNNの歴史・代表モデル・応用を俯瞰したバックボーンサーベイ

### Image Colorization

- [Image Colorization: A Survey and Dataset](https://arxiv.org/abs/2008.10774) — *Information Fusion 2020* · 📈106。画像カラー化の深層学習手法を7分類し新データセットも提供

### Image Deblurring

- [Deep Image Deblurring: A Survey](https://arxiv.org/abs/2201.10700) — *IJCV 2022* · 📈374。画像ボケ除去の深層学習手法をアーキテクチャ・損失・応用で分類

### Image Dehazing

- [A Comprehensive Survey and Taxonomy on Single Image Dehazing Based on Deep Learning](https://arxiv.org/abs/2106.03323) — *ACM Computing Surveys 2021*。単一画像デヘイズの深層学習手法を分類学とともに包括的に整理

### Image Deraining

- [Towards Unified Deep Image Deraining: A Survey and A New Benchmark](https://arxiv.org/abs/2310.03535) — *arXiv 2023* · 📈59。画像デレイン(雨除去)の統一的サーベイと新ベンチマーク

### Image Fusion

- [Multimodal Alignment and Fusion: A Survey](https://arxiv.org/abs/2411.17040) — *arXiv 2024* · 📈140。マルチモーダルアラインメント・融合を構造・手法論の観点で整理

### Image Generation (Diffusion)

- [Diffusion Models in Vision: A Survey](https://arxiv.org/abs/2209.04747) — *TPAMI 2023* · 📈2108。視覚タスクへの拡散モデル応用を理論・実装両面で整理 — [`CroitoruAlin/Diffusion-Models-in-Vision-A-Survey`](https://github.com/CroitoruAlin/Diffusion-Models-in-Vision-A-Survey) ⭐407🔴
- [Text-to-image Diffusion Models in Generative AI: A Survey](https://arxiv.org/abs/2303.07909) — *arXiv 2023* · 📈423。テキストから画像への拡散モデル生成と応用を整理したサーベイ

### Image Generation (GAN)

- [Generative Adversarial Networks: An Overview](https://arxiv.org/abs/1710.07035) — *IEEE Signal Processing Magazine 2018* · 📈3730。画像合成等を含むGANの学習・構築手法を概観した定番オーバービュー
- [GAN Inversion: A Survey](https://arxiv.org/abs/2101.05278) — *TPAMI 2022* · 📈632。実画像編集を支えるGANインバージョン手法のサーベイ — [`weihaox/GAN-Inversion`](https://github.com/weihaox/GAN-Inversion) ⭐1126🟡

### Image Inpainting

- [Deep Learning-based Image and Video Inpainting: A Survey](https://arxiv.org/abs/2401.03395) — *IJCV 2024* · 📈90。画像・動画インペインティングをCNN/VAE/GAN/拡散で分類した包括サーベイ

### Image Matching / Local Features

- [Local Feature Matching Using Deep Learning: A Survey](https://arxiv.org/abs/2401.17592) — *Information Fusion 2024* · 📈101。局所特徴マッチングの深層学習手法をdetector有無で分類整理 — [`vignywang/Awesome-Local-Feature-Matching`](https://github.com/vignywang/Awesome-Local-Feature-Matching) ⭐157🔴

### Image Matting

- [Deep Image Matting: A Comprehensive Survey](https://arxiv.org/abs/2304.04672) — *arXiv 2023* · 📈22。画像マッティングの深層学習手法を補助入力型・自動型で整理 — [`JizhiziLi/matting-survey`](https://github.com/JizhiziLi/matting-survey) ⭐201🔴

### Image Quality Assessment

- [A Survey on Image Quality Assessment: Insights, Analysis, and Future Outlook](https://arxiv.org/abs/2502.08540) — *arXiv 2025*。画質評価(IQA)の統計手法からCNN/Transformerまでを整理した最新サーベイ

### Image Restoration

- [Priors in Deep Image Restoration and Enhancement: A Survey](https://arxiv.org/abs/2206.02070) — *arXiv 2022* · 📈8。画像復元・強調における事前分布(prior)の観点で手法を整理 — [`yunfanLu/Awesome-Image-Prior`](https://github.com/yunfanLu/Awesome-Image-Prior) ⭐87🟡

### Long-Tailed Recognition

- [A Survey on Long-Tailed Visual Recognition](https://arxiv.org/abs/2205.13775) — *IJCV 2022* · 📈185。ロングテール視覚認識のデータセット・主要手法を整理したサーベイ

### Low-Light Image Enhancement

- [Low-Light Image and Video Enhancement Using Deep Learning: A Survey](https://arxiv.org/abs/2104.10729) — *TPAMI 2021*。低照度画像・動画強調の深層学習手法を網羅的に整理したサーベイ — [`ShenZheng2000/LLIE_Survey`](https://github.com/ShenZheng2000/LLIE_Survey) ⭐154🔴

### Medical Image Analysis

- [A Survey on Deep Learning in Medical Image Analysis](https://arxiv.org/abs/1702.05747) — *Medical Image Analysis 2017* · 📈13399。医用画像解析への深層学習応用を300本超で整理した古典的定番サーベイ
- [Transformers in Medical Imaging: A Survey](https://arxiv.org/abs/2201.09873) — *Medical Image Analysis 2023* · 📈1141。医用画像のセグメンテーション/分類/再構成等へのTransformer応用を整理

### Multi-Object Tracking

- [Deep Learning-Based Multi-Object Tracking: A Comprehensive Survey from Foundations to State-of-the-Art](https://arxiv.org/abs/2506.13457) — *arXiv 2025*。深層学習による多物体追跡を基礎から最新手法まで包括的に整理

### Multi-View Stereo

- [Learning-based Multi-View Stereo: A Survey](https://arxiv.org/abs/2408.15235) — *arXiv 2024* · 📈31。学習ベースMVSをdepth/voxel/NeRF/3DGS/feed-forwardで分類整理

### Neural Rendering

- [Advances in Neural Rendering](https://arxiv.org/abs/2111.05849) — *Computer Graphics Forum 2021*。ニューラルレンダリングの進展を包括的にまとめたstate-of-the-artレポート

### Neural Rendering / NeRF

- [NeRF: Neural Radiance Field in 3D Vision: A Comprehensive Review](https://arxiv.org/abs/2210.00379) — *arXiv 2022* · 📈304。NeRFのアーキテクチャ/応用/性能を体系化した包括的レビュー
- [Neural Volume Rendering: NeRF And Beyond](https://arxiv.org/abs/2101.05204) — *arXiv 2021* · 📈71。ニューラルボリュームレンダリング(NeRF)の俯瞰レビュー

### Neural Style Transfer

- [Neural Style Transfer: A Review](https://arxiv.org/abs/1705.04058) — *TVCG 2017* · 📈856。ニューラルスタイル変換の手法・評価を整理した代表的レビュー

### OCR / Document Analysis

- [A Survey of Deep Learning Approaches for OCR and Document Understanding](https://arxiv.org/abs/2011.13534) — *arXiv 2020* · 📈88。OCRと文書理解の深層手法を整理した実務向けサーベイ

### OCR / Scene Text

- [Scene Text Detection and Recognition: The Deep Learning Era](https://arxiv.org/abs/1811.04256) — *IJCV 2021* · 📈490。シーンテキスト検出・認識の深層学習時代の進展を整理した定番サーベイ

### Object Detection

- [Object Detection in 20 Years: A Survey](https://arxiv.org/abs/1905.05055) — *Proceedings of the IEEE 2023* · 📈3344。物体検出20年の技術進化を400本超で俯瞰した定番サーベイ
- [Deep Learning for Generic Object Detection: A Survey](https://arxiv.org/abs/1809.02165) — *IJCV 2020* · 📈2781。深層学習による汎用物体検出の包括的サーベイ(300本超を整理)
- [A Survey of Deep Learning-based Object Detection](https://arxiv.org/abs/1907.09408) — *IEEE Access 2019* · 📈1128。一段/二段検出器を体系的に整理した深層物体検出サーベイ
- [A Survey of Modern Deep Learning based Object Detection Models](https://arxiv.org/abs/2104.11892) — *Digital Signal Processing 2022* · 📈901。近代的な深層物体検出モデルとバックボーン・軽量化を整理

### Object Tracking

- [Deep Learning for Visual Tracking: A Comprehensive Survey](https://arxiv.org/abs/1912.00535) — *IEEE T-ITS 2022* · 📈354。深層学習ベースの視覚追跡手法・ベンチマークを包括的に整理

### Open-Vocabulary Detection/Segmentation

- [Towards Open Vocabulary Learning: A Survey](https://arxiv.org/abs/2306.15880) — *TPAMI 2023* · 📈254。オープン語彙学習(検出・セグメンテーション等)の包括的サーベイ — [`jianzongwu/Awesome-Open-Vocabulary`](https://github.com/jianzongwu/Awesome-Open-Vocabulary) ⭐998🟢
- [A Survey on Open-Vocabulary Detection and Segmentation: Past, Present, and Future](https://arxiv.org/abs/2307.09220) — *TPAMI 2023* · 📈100。オープン語彙検出・セグメンテーションを分類学とともに整理

### Optical Flow

- [Optical Flow Estimation in the Deep Learning Age](https://arxiv.org/abs/2004.02853) — *arXiv 2020* · 📈41。古典的エネルギー最小化からCNNまでのオプティカルフロー推定を整理

### Panoptic Segmentation

- [Panoptic Segmentation: A Review](https://arxiv.org/abs/2111.10250) — *arXiv 2021* · 📈48。セマンティック+インスタンスを統合するパノプティックセグの初の包括レビュー

### Person Re-identification

- [Deep Learning for Person Re-identification: A Survey and Outlook](https://arxiv.org/abs/2001.04193) — *TPAMI 2022* · 📈2133。人物再同定をclosed/open-world双方の観点で整理した定番サーベイ
- [Deep Learning for Video-based Person Re-Identification: A Survey](https://arxiv.org/abs/2303.11332) — *arXiv 2023*。動画ベース人物再同定の深層学習手法を整理したサーベイ

### Point Cloud

- [A Survey of Label-Efficient Deep Learning for 3D Point Clouds](https://arxiv.org/abs/2305.19812) — *TPAMI 2023* · 📈48。ラベル効率(弱/半/自己教師)の3D点群深層学習を整理したサーベイ

### Point Cloud Completion

- [Comprehensive Review of Deep Learning-Based 3D Point Cloud Completion Processing and Analysis](https://arxiv.org/abs/2203.03311) — *IEEE T-ITS 2022* · 📈188。3D点群補完の深層学習手法(point/conv/graph/生成系)を包括レビュー

### Point Cloud Registration

- [Deep Learning-Based Point Cloud Registration: A Comprehensive Survey and Taxonomy](https://arxiv.org/abs/2404.13830) — *IJCV 2024* · 📈11。点群レジストレーションの深層学習手法を分類学とともに包括整理

### Pose Estimation

- [Deep Learning-Based Human Pose Estimation: A Survey](https://arxiv.org/abs/2012.13392) — *CSUR 2023* · 📈930。2D/3D人体姿勢推定の深層手法を250本超で整理したCSURサーベイ
- [2D Human Pose Estimation: A Survey](https://arxiv.org/abs/2204.07370) — *arXiv 2022* · 📈99。2D人体姿勢推定をネットワーク設計/学習/後処理の観点で整理

### Referring Segmentation

- [Multimodal Referring Segmentation: A Survey](https://arxiv.org/abs/2508.00265) — *arXiv 2025* · 📈21。画像・動画・3Dにわたる参照セグメンテーションの統一的サーベイ

### Remote Sensing

- [Deep Learning in Remote Sensing: A Review](https://arxiv.org/abs/1710.03959) — *IEEE GRSM 2017* · 📈1845。リモートセンシングデータ解析への深層学習応用を整理した定番レビュー

### Salient Object Detection

- [Salient Object Detection in the Deep Learning Era: An In-Depth Survey](https://arxiv.org/abs/1904.09146) — *TPAMI 2022* · 📈728。深層学習時代の顕著性物体検出を体系的にベンチマーク・整理
- [RGB-D Salient Object Detection: A Survey](https://arxiv.org/abs/2008.00230) — *Computational Visual Media 2020* · 📈298。深度情報を用いたRGB-D顕著性物体検出の包括的サーベイ — [`taozh2017/RGBD-SODsurvey`](https://github.com/taozh2017/RGBD-SODsurvey) ⭐372🔴

### Scene Graph Generation

- [Scene Graph Generation: A Comprehensive Survey](https://arxiv.org/abs/2201.00443) — *Neurocomputing 2022*。シーングラフ生成の138本を特徴表現・精緻化の観点で整理した包括サーベイ

### Self-Supervised Learning

- [A Survey on Contrastive Self-supervised Learning](https://arxiv.org/abs/2011.00362) — *Technologies 2021* · 📈1732。対照学習を中心とした自己教師あり学習のサーベイ
- [A Survey on Self-supervised Learning: Algorithms, Applications, and Future Trends](https://arxiv.org/abs/2301.05712) — *TPAMI 2024* · 📈519。自己教師あり学習のアルゴリズム/応用/動向を多角的に整理
- [Masked Image Modeling: A Survey](https://arxiv.org/abs/2408.06687) — *IJCV 2025* · 📈43。マスク画像モデリング(MIM)による自己教師あり事前学習のサーベイ
- [Masked Modeling for Self-supervised Representation Learning on Vision and Beyond](https://arxiv.org/abs/2401.00897) — *arXiv 2024* · 📈34。マスク戦略・復元対象・アーキを軸にマスクモデリング自己教師あり学習を整理 — [`Lupin1998/Awesome-MIM`](https://github.com/Lupin1998/Awesome-MIM) ⭐354🟡

### Semantic Segmentation

- [Image Segmentation Using Deep Learning: A Survey](https://arxiv.org/abs/2001.05566) — *TPAMI 2022* · 📈3715。意味的/インスタンスセグメンテーションの深層手法を網羅した定番サーベイ
- [A Review on Deep Learning Techniques Applied to Semantic Segmentation](https://arxiv.org/abs/1704.06857) — *arXiv 2017* · 📈1380。意味的セグメンテーションの深層手法・データセット・評価を整理した初期定番
- [Transformer-Based Visual Segmentation: A Survey](https://arxiv.org/abs/2304.09854) — *TPAMI 2024* · 📈297。DETR系メタアーキを軸にしたTransformerベースのセグメンテーションサーベイ — [`lxtGH/Awesome-Segmentation-With-Transformer`](https://github.com/lxtGH/Awesome-Segmentation-With-Transformer) ⭐760🔴

### Stereo Matching

- [A Survey on Deep Stereo Matching in the Twenties](https://arxiv.org/abs/2407.07816) — *IJCV 2024* · 📈56。2020年代の深層ステレオマッチング手法の最新動向を整理したサーベイ

### Super-Resolution

- [Deep Learning for Image Super-resolution: A Survey](https://arxiv.org/abs/1902.06068) — *TPAMI 2021* · 📈1788。画像超解像の深層手法を教師あり/なし/ドメイン特化で整理した定番サーベイ
- [Diffusion Models, Image Super-Resolution And Everything: A Survey](https://arxiv.org/abs/2401.00736) — *TNNLS 2024*。拡散モデルによる画像超解像の進化と動向を詳述したサーベイ
- [Video Super Resolution Based on Deep Learning: A Comprehensive Survey](https://arxiv.org/abs/2007.12928) — *Artificial Intelligence Review 2020*。動画超解像の深層学習33手法をフレーム間情報利用法で分類した包括サーベイ

### Talking Head Generation

- [From Pixels to Portraits: A Comprehensive Survey of Talking Head Generation Techniques and Applications](https://arxiv.org/abs/2308.16041) — *arXiv 2023* · 📈10。トーキングヘッド生成を画像・音声・動画駆動・NeRF系で分類した包括サーベイ

### Temporal Action Detection

- [A Survey on Deep Learning-based Spatio-temporal Action Detection](https://arxiv.org/abs/2308.01618) — *Int. J. Wavelets Multiresolut. Inf. Process. 2023* · 📈13。時空間アクション検出の深層学習手法を体系的に整理したサーベイ

### Video Anomaly Detection

- [Video Anomaly Detection in 10 Years: A Survey and Outlook](https://arxiv.org/abs/2405.19387) — *arXiv 2024* · 📈48。動画異常検知10年を弱教師・自己教師・教師なしまで俯瞰したサーベイ

### Video Segmentation

- [A Survey on Deep Learning Technique for Video Segmentation](https://arxiv.org/abs/2107.01153) — *TPAMI 2023* · 📈294。動画オブジェクト/意味セグメンテーションの深層手法を整理 — [`tfzhou/VS-Survey`](https://github.com/tfzhou/VS-Survey) ⭐204🔴
- [Deep Learning Techniques for Video Instance Segmentation: A Survey](https://arxiv.org/abs/2310.12393) — *arXiv 2023* · 📈4。動画インスタンスセグメンテーションの深層学習手法を整理したサーベイ

### Video Understanding

- [Video Transformers: A Survey](https://arxiv.org/abs/2201.05991) — *TPAMI 2023* · 📈165。動画モデリング向けTransformerの効率化と自己教師あり戦略を整理

### Vision Transformer

- [A Survey on Vision Transformer](https://arxiv.org/abs/2012.12556) — *TPAMI 2023* · 📈3572。Vision Transformerをタスク別に整理した高被引用サーベイ
- [Transformers in Vision: A Survey](https://arxiv.org/abs/2101.01169) — *CSUR 2022* · 📈3543。視覚タスク全般へのTransformer応用を網羅したACM CSURサーベイ
- [A Survey of Visual Transformers](https://arxiv.org/abs/2111.06091) — *TNNLS 2023* · 📈531。分類/検出/セグメンテーション軸で100超のViTを整理

### Vision-Language Models

- [Vision-Language Models for Vision Tasks: A Survey](https://arxiv.org/abs/2304.00685) — *TPAMI 2024* · 📈1369。視覚認識タスク向けVLMの事前学習/転移/蒸留を体系的に整理 — [`jingyi0000/VLM_survey`](https://github.com/jingyi0000/VLM_survey) ⭐3124🟡

### Visual SLAM

- [Deep Learning for Visual Localization and Mapping: A Survey](https://arxiv.org/abs/2308.14039) — *arXiv 2023* · 📈81。学習ベースの視覚オドメトリ・再局在化・マッピング・SLAMを整理

### World Models

- [3D and 4D World Modeling: A Survey](https://arxiv.org/abs/2509.07996) — *arXiv 2025* · 📈53。video/occupancy/LiDARベースの3D・4Dワールドモデリングを初めて統合的に整理 — [`worldbench/awesome-3d-4d-world-models`](https://github.com/worldbench/awesome-3d-4d-world-models) ⭐929🟢 · [project](https://worldbench.github.io/survey)

### Zero-Shot Learning

- [Zero-Shot Learning -- A Comprehensive Evaluation of the Good, the Bad and the Ugly](https://arxiv.org/abs/1707.00600) — *TPAMI 2019* · 📈1831。ゼロショット学習の統一ベンチマーク・評価を提示した定番サーベイ

## 📈 機械学習 (一般)

### Anomaly Detection

- [A Unified Survey on Anomaly, Novelty, Open-Set, and Out-of-Distribution Detection: Solutions and Future Challenges](https://arxiv.org/abs/2110.14051) — *TMLR 2022* · 📈238。異常検知・新規性検出・開集合認識・OOD検出を統一的に整理したサーベイ

### AutoML

- [AutoML: A Survey of the State-of-the-Art](https://arxiv.org/abs/1908.00709) — *Knowledge-Based Systems 2021* · 📈1793。データ準備からNASまでAutoMLパイプライン全体を概観したサーベイ

### Bayesian Deep Learning

- [Hands-on Bayesian Neural Networks -- a Tutorial for Deep Learning Users](https://arxiv.org/abs/2007.06823) — *IEEE Computational Intelligence Magazine 2022* · 📈877。ベイズ深層学習の実践的チュートリアル兼概説

### Calibration

- [Calibration in Deep Learning: A Survey of the State-of-the-Art](https://arxiv.org/abs/2308.01222) — *arXiv 2023* · 📈99。深層学習モデルの確信度キャリブレーション手法を整理したサーベイ

### Causal Machine Learning

- [Towards Causal Representation Learning](https://arxiv.org/abs/2102.11107) — *Proceedings of the IEEE 2021* · 📈358。因果性と表現学習の融合を論じた影響力の大きい概説

### Clustering

- [Deep Clustering: A Comprehensive Survey](https://arxiv.org/abs/2210.04142) — *IEEE TNNLS 2022* · 📈248。深層クラスタリングを単視点/半教師/多視点/転移で分類したサーベイ

### Conformal Prediction

- [A tutorial on conformal prediction](https://arxiv.org/abs/0706.3188) — *JMLR 2008* · 📈1626。コンフォーマル予測の原理を解説した古典的チュートリアル
- [A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification](https://arxiv.org/abs/2107.07511) — *arXiv 2021* · 📈1060。分布フリー不確実性定量化とコンフォーマル予測の実践的入門兼レビュー
- [Conformal Prediction for Natural Language Processing: A Survey](https://arxiv.org/abs/2405.01976) — *TACL 2024* · 📈52。NLPタスクへのコンフォーマル予測適用を整理したサーベイ

### Continual Learning

- [Continual Lifelong Learning with Neural Networks: A Review](https://arxiv.org/abs/1802.07569) — *Neural Networks 2019* · 📈3499。破滅的忘却と継続学習手法を整理した定番レビュー
- [A Comprehensive Survey of Continual Learning: Theory, Method and Application](https://arxiv.org/abs/2302.00487) — *TPAMI 2023* · 📈1391。継続学習を理論/手法/応用の3層で網羅した近年の包括サーベイ

### Continual Learning / Forgetting

- [A Comprehensive Survey of Forgetting in Deep Learning Beyond Continual Learning](https://arxiv.org/abs/2307.09218) — *IEEE TPAMI 2024* · 📈110。継続学習を越えて生成・連合学習等での忘却を両義的に論じたTPAMIサーベイ — [`EnnengYang/Awesome-Forgetting-in-Deep-Learning`](https://github.com/EnnengYang/Awesome-Forgetting-in-Deep-Learning) ⭐363🟢

### Data Augmentation

- [Time Series Data Augmentation for Deep Learning: A Survey](https://arxiv.org/abs/2002.12478) — *IJCAI 2021* · 📈821。時系列データ拡張手法を整理したサーベイ
- [Image Data Augmentation for Deep Learning: A Survey](https://arxiv.org/abs/2204.08610) — *arXiv 2022* · 📈388。画像データ拡張手法を体系的に分類したサーベイ

### Dataset Distillation

- [The Evolution of Dataset Distillation: Toward Scalable and Generalizable Solutions](https://arxiv.org/abs/2502.05673) — *arXiv preprint 2025* · 📈22。ImageNet級へのスケーラビリティを重視したデータセット蒸留の最新進展(2023-2025)を整理。

### Dictionary Learning

- [Supervised Dictionary Learning and Sparse Representation-A Review](https://arxiv.org/abs/1502.05928) — *arXiv 2015* · 📈59。教師あり辞書学習とスパース表現を6分類で整理したレビュー

### Diffusion (Time Series)

- [A Survey on Diffusion Models for Time Series and Spatio-Temporal Data](https://arxiv.org/abs/2404.18886) — *arXiv 2024* · 📈111。時系列・時空間データへの拡散モデルをモデル/タスク/応用で整理 — [`yyysjz1997/Awesome-TimeSeries-SpatioTemporal-Diffusion-Model`](https://github.com/yyysjz1997/Awesome-TimeSeries-SpatioTemporal-Diffusion-Model) ⭐989🟢

### Distributed Deep Learning Systems

- [Systems for Parallel and Distributed Large-Model Deep Learning Training](https://arxiv.org/abs/2301.02691) — *arXiv preprint 2023* · 📈9。大規模モデルの並列・分散学習システムの課題と技術を俯瞰したサーベイ。

### Distributed LLM Training / ML Systems

- [Efficient Training of Large Language Models on Distributed Infrastructures: A Survey](https://arxiv.org/abs/2407.20018) — *arXiv preprint 2024* · 📈51。アクセラレータ・通信・並列戦略を含む分散LLM訓練システムの最新進展を整理したサーベイ。

### Domain Adaptation

- [A Brief Review of Domain Adaptation](https://arxiv.org/abs/2010.03978) — *arXiv 2020* · 📈785。ドメイン適応の主要手法を簡潔に整理したレビュー

### Domain Generalization

- [Domain Generalization: A Survey](https://arxiv.org/abs/2103.02503) — *TPAMI 2022* · 📈1537。ドメイン汎化の手法分類とベンチマークを整理したサーベイ

### Dynamic Networks

- [Dynamic Neural Networks: A Survey](https://arxiv.org/abs/2102.04906) — *TPAMI 2022* · 📈897。入力依存で計算を変える動的ニューラルネットを整理したサーベイ

### Edge AI / Model Optimization

- [Cognitive Edge Computing: A Comprehensive Survey on Optimizing Large Models and AI Agents for Pervasive Deployment](https://arxiv.org/abs/2501.03265) — *arXiv preprint 2025* · 📈28。大規模モデルとAIエージェントのエッジ展開に向けたモデル最適化・システム設計を整理したサーベイ。

### Energy-Based Models

- [Hitchhiker's guide on the relation of Energy-Based Models with other generative models, sampling and statistical physics: a comprehensive review](https://arxiv.org/abs/2406.13661) — *TMLR 2025* · 📈4。エネルギーベースモデルと他の生成モデル/統計物理の関係を整理した包括レビュー

### Ensemble Learning

- [Ensemble deep learning: A review](https://arxiv.org/abs/2104.02395) — *Engineering Applications of AI 2022* · 📈1951。アンサンブル深層学習(bagging/boosting/stacking等)を概観したレビュー

### Explainable AI

- [Interpretable Deep Learning: Interpretation, Interpretability, Trustworthiness, and Beyond](https://arxiv.org/abs/2103.10689) — *Knowledge and Information Systems 2021* · 📈489。解釈/解釈可能性/信頼性の概念整理と手法分類を行ったサーベイ
- [Explainable Artificial Intelligence: a Systematic Review](https://arxiv.org/abs/2006.00093) — *arXiv 2020* · 📈316。XAI手法を体系的レビューで分類した網羅的サーベイ

### Fairness

- [A Survey on Bias and Fairness in Machine Learning](https://arxiv.org/abs/1908.09635) — *ACM Computing Surveys 2021* · 📈5855。機械学習のバイアスと公平性の定義/対策を網羅した高被引用サーベイ
- [What-is and How-to for Fairness in Machine Learning: A Survey, Reflection, and Perspective](https://arxiv.org/abs/2206.04101) — *ACM Computing Surveys 2023* · 📈40。公平性の定義と実現手法を反省的視点で整理したサーベイ

### Gaussian Processes

- [When Gaussian Process Meets Big Data: A Review of Scalable GPs](https://arxiv.org/abs/1807.01065) — *IEEE TNNLS 2018* · 📈859。大規模データ向けスケーラブルなガウス過程手法を整理したレビュー
- [Deep Gaussian Processes: A Survey](https://arxiv.org/abs/2106.12135) — *arXiv 2021* · 📈27。深層ガウス過程の定式化・限界・研究動向を整理したサーベイ

### Generalization

- [Model Complexity of Deep Learning: A Survey](https://arxiv.org/abs/2103.05127) — *Knowledge and Information Systems 2021* · 📈392。深層学習のモデル複雑度と汎化の関係を整理したサーベイ

### Generative Recommendation

- [Large Language Models for Generative Recommendation: A Survey and Visionary Discussions](https://arxiv.org/abs/2309.01157) — *arXiv 2023* · 📈148。LLMによる生成的推薦の手法と将来展望を整理したサーベイ
- [A Survey of Generative Search and Recommendation in the Era of Large Language Models](https://arxiv.org/abs/2404.16924) — *arXiv 2024* · 📈27。LLM時代の生成的検索・推薦を統一的観点で整理した総説
- [GR-LLMs: Recent Advances in Generative Recommendation Based on Large Language Models](https://arxiv.org/abs/2507.06507) — *arXiv 2025* · 📈4。LLMベース生成的推薦(GR-LLM)の最新動向と産業応用を整理

### Graph Foundation Models

- [Graph Foundation Models: A Comprehensive Survey](https://arxiv.org/abs/2505.15116) — *arXiv 2025* · 📈41。グラフ基盤モデルの事前学習と転移をGNNからの転換として整理

### Green AI / Sustainable ML

- [Green AI: A systematic review and meta-analysis of its definitions, lifecycle models, hardware and measurement attempts](https://arxiv.org/abs/2511.07090) — *arXiv preprint 2025* · 📈4。グリーンAIの定義・ライフサイクル・ハードウェア・計測手法を体系的レビュー+メタ分析。

### Hardware Acceleration / ML Systems

- [Hardware Acceleration for Neural Networks: A Comprehensive Survey](https://arxiv.org/abs/2512.23914) — *arXiv preprint 2025* · 📈3。GPU・TPU/NPU・FPGA・ASIC・LPU等を横断したニューラルネット向けハードウェア加速の包括サーベイ。

### Hyperparameter Optimization

- [Hyper-Parameter Optimization: A Review of Algorithms and Applications](https://arxiv.org/abs/2003.05689) — *arXiv 2020* · 📈676。ハイパーパラメータ最適化アルゴリズムを整理したレビュー
- [Hyperparameter Optimization in Machine Learning](https://arxiv.org/abs/2410.22854) — *arXiv preprint 2024* · 📈9。ベイズ最適化・進化計算・メタ学習等を含むハイパーパラメータ最適化の統一的サーベイ。

### Imbalanced Learning

- [A Survey of Methods for Addressing Class Imbalance in Deep-Learning Based Natural Language Processing](https://arxiv.org/abs/2210.04675) — *EACL 2023* · 📈53。深層学習NLPにおけるクラス不均衡対処法を体系的に整理したサーベイ

### Kernel Methods

- [Kernel Mean Embedding of Distributions: A Review and Beyond](https://arxiv.org/abs/1605.09522) — *Foundations and Trends in ML 2017* · 📈876。分布のカーネル平均埋め込みの理論と応用を整理した包括レビュー
- [Reproducing Kernel Hilbert Space, Mercer's Theorem, Eigenfunctions, Nystrom Method, and Use of Kernels in Machine Learning: Tutorial and Survey](https://arxiv.org/abs/2106.08443) — *arXiv 2021* · 📈60。RKHS・Mercer定理・カーネル法の基礎を解説したチュートリアル兼サーベイ
- [Neural Tangent Kernel: A Survey](https://arxiv.org/abs/2208.13614) — *arXiv 2022* · 📈22。ニューラルタンジェントカーネル理論を整理したサーベイ

### Knowledge Distillation

- [Knowledge Distillation: A Survey](https://arxiv.org/abs/2006.05525) — *IJCV 2021* · 📈4212。知識蒸留の知識種別/スキーム/アルゴリズムを網羅した定番サーベイ

### Knowledge Distillation / Amalgamation

- [A Comprehensive Survey on Knowledge Distillation](https://arxiv.org/abs/2503.12067) — *arXiv preprint 2025* · 📈62。知識融合(multi-teacher amalgamation)を含む知識蒸留全般を網羅した包括サーベイ。 — [`IPL-sharif/KD_Survey`](https://github.com/IPL-sharif/KD_Survey) ⭐76🟢

### Kolmogorov-Arnold Networks

- [A Survey on Kolmogorov-Arnold Network](https://arxiv.org/abs/2411.06078) — *arXiv 2024* · 📈207。KANの理論/変種/応用を整理した近年のサーベイ
- [Kolmogorov-Arnold Networks: A Critical Assessment of Claims, Performance, and Practical Viability](https://arxiv.org/abs/2407.11075) — *arXiv 2024* · 📈53。KANの理論・性能・実用性を批判的に評価したサーベイ

### LLM Hardware Acceleration

- [Hardware Acceleration of LLMs: A comprehensive survey and comparison](https://arxiv.org/abs/2409.03384) — *arXiv preprint 2024* · 📈14。Transformer向けハードウェア加速の研究を横断比較したサーベイ。

### LLM Inference Acceleration (Hardware)

- [Large Language Model Inference Acceleration: A Comprehensive Hardware Perspective](https://arxiv.org/abs/2410.04466) — *arXiv preprint 2024* · 📈71。CPU/GPU/FPGA/ASIC/PIM等プラットフォーム別にLLM推論加速をハードウェア視点で整理したサーベイ。 — [`Kimho666/LLM_Hardware_Survey`](https://github.com/Kimho666/LLM_Hardware_Survey) ⭐17🟡

### Label-Noise Learning

- [Learning from Noisy Labels with Deep Neural Networks: A Survey](https://arxiv.org/abs/2007.08199) — *IEEE TNNLS 2022* · 📈1359。ノイズラベル下の頑健学習手法を体系化した定番サーベイ

### Machine Unlearning

- [A Survey of Machine Unlearning](https://arxiv.org/abs/2209.02299) — *arXiv 2022* · 📈405。機械的忘却の概念・シナリオ・手法・応用を包括した定番サーベイ(950+ star companion) — [`tamlhp/awesome-machine-unlearning`](https://github.com/tamlhp/awesome-machine-unlearning) ⭐953🟢

### Manifold Learning

- [Manifold learning: what, how, and why](https://arxiv.org/abs/2311.03757) — *Annual Review of Statistics 2023* · 📈141。多様体学習の原理・代表手法・統計的基盤を整理したレビュー

### Meta-Learning

- [Meta-Learning in Neural Networks: A Survey](https://arxiv.org/abs/2004.05439) — *TPAMI 2022* · 📈2642。メタ学習の統一的分類法を提示した定番サーベイ

### Metric Learning

- [A Survey on Metric Learning for Feature Vectors and Structured Data](https://arxiv.org/abs/1306.6709) — *arXiv 2013* · 📈709。特徴ベクトルと構造化データの距離学習を体系化した定番サーベイ
- [Spectral, Probabilistic, and Deep Metric Learning: Tutorial and Survey](https://arxiv.org/abs/2201.09267) — *arXiv 2022* · 📈30。スペクトル/確率/深層の各距離学習を統一的に解説したチュートリアル兼サーベイ

### Model Compression

- [A Survey of Model Compression and Acceleration for Deep Neural Networks](https://arxiv.org/abs/1710.09282) — *IEEE Signal Processing Magazine 2020* · 📈1234。枝刈り/量子化/蒸留など圧縮高速化手法を概観した高被引用サーベイ
- [Efficient Deep Learning: A Survey on Making Deep Learning Models Smaller, Faster, and Better](https://arxiv.org/abs/2106.08962) — *ACM Computing Surveys 2021* · 📈616。効率的深層学習の手法/インフラ/ハードを横断的に整理したサーベイ

### Model Merging

- [Model Merging in LLMs, MLLMs, and Beyond: Methods, Theories, Applications and Opportunities](https://arxiv.org/abs/2408.07666) — *ACM Computing Surveys 2024* · 📈250。モデルマージの手法・理論・応用を網羅したCSUR採録サーベイ — [`EnnengYang/Awesome-Model-Merging-Methods-Theories-Applications`](https://github.com/EnnengYang/Awesome-Model-Merging-Methods-Theories-Applications) ⭐747🟢

### Multi-Task Learning

- [A Survey on Multi-Task Learning](https://arxiv.org/abs/1707.08114) — *IEEE TKDE 2021* · 📈2907。マルチタスク学習の手法を体系的に分類した定番サーベイ
- [Multi-Task Learning with Deep Neural Networks: A Survey](https://arxiv.org/abs/2009.09796) — *arXiv 2020* · 📈785。深層マルチタスク学習のアーキテクチャと最適化を整理したサーベイ

### Multi-label Learning

- [Deep Learning for Multi-Label Learning: A Comprehensive Survey](https://arxiv.org/abs/2401.16549) — *arXiv 2024* · 📈42。深層学習によるマルチラベル学習を2006-2023年で網羅したサーベイ
- [A Survey on Extreme Multi-label Learning](https://arxiv.org/abs/2210.03968) — *arXiv 2022* · 📈13。超大規模ラベル空間の極端マルチラベル学習を整理したサーベイ

### Multiple Instance Learning

- [Multiple Instance Learning: A Survey of Problem Characteristics and Applications](https://arxiv.org/abs/1612.03365) — *Pattern Recognition 2016* · 📈737。マルチインスタンス学習の問題特性と応用を体系化した代表的サーベイ

### Neural Architecture Search

- [Neural Architecture Search: Insights from 1000 Papers](https://arxiv.org/abs/2301.08727) — *arXiv 2023* · 📈219。1000本超の論文からNAS研究全体を俯瞰した近年の包括的サーベイ
- [Neural Architecture Search: A Survey](https://arxiv.org/abs/1808.05377) — *JMLR 2019*。探索空間/探索戦略/性能推定の3軸でNASを整理した代表的サーベイ

### Neural Compression

- [Information Compression in the AI Era: Recent Advances and Future Challenges](https://arxiv.org/abs/2406.10036) — *arXiv 2024* · 📈22。機械学習とデータ圧縮の接点(目的指向圧縮・RDP理論)を整理した総説

### On-Device AI / Edge Intelligence

- [Empowering Edge Intelligence: A Comprehensive Survey on On-Device AI Models](https://arxiv.org/abs/2503.06027) — *arXiv preprint 2025* · 📈158。エッジ端末上で動くAIモデルの設計・最適化・ハードウェア加速を体系化した包括サーベイ。

### On-Device Optimization / Edge ML

- [Onboard Optimization and Learning: A Survey](https://arxiv.org/abs/2505.08793) — *arXiv preprint 2025* · 📈2。端末上での推論加速・協調学習・モデル軽量化など組込み最適化を整理したサーベイ。

### Open-set Recognition

- [A Survey on Open Set Recognition](https://arxiv.org/abs/2109.00893) — *arXiv 2021* · 📈49。未知クラスを扱う開集合認識の手法を体系的に整理したサーベイ

### Optimization

- [An overview of gradient descent optimization algorithms](https://arxiv.org/abs/1609.04747) — *arXiv 2016* · 📈6929。SGD/Momentum/Adam等の勾配降下最適化手法を概説した高被引用記事
- [A survey and taxonomy of loss functions in machine learning](https://arxiv.org/abs/2301.05579) — *arXiv 2023* · 📈51。機械学習における損失関数を網羅的に分類した近年のサーベイ

### Ordinal Regression

- [A Survey on Ordinal Regression: Applications, Advances and Prospects](https://arxiv.org/abs/2503.00952) — *arXiv 2025* · 📈3。順序回帰の手法と応用を3カテゴリで初めて体系化したサーベイ

### Out-of-Distribution Detection

- [Generalized Out-of-Distribution Detection: A Survey](https://arxiv.org/abs/2110.11334) — *IJCV 2024* · 📈1391。OOD検出/異常検知/新規性検出を統一的枠組みで整理したサーベイ — [`huytransformer/Awesome-Out-Of-Distribution-Detection`](https://github.com/huytransformer/Awesome-Out-Of-Distribution-Detection) ⭐1008🟢

### PU Learning

- [Learning from positive and unlabeled data: a survey](https://arxiv.org/abs/1811.04820) — *Machine Learning 2020* · 📈695。正例とラベルなしデータからの学習(PU learning)の決定版サーベイ

### Pruning

- [What is the State of Neural Network Pruning?](https://arxiv.org/abs/2003.03033) — *MLSys 2020* · 📈1254。枝刈り研究の評価不統一を指摘しメタ分析した重要サーベイ

### Quantization

- [A Survey of Quantization Methods for Efficient Neural Network Inference](https://arxiv.org/abs/2103.13630) — *arXiv 2021* · 📈1558。ニューラルネット量子化手法を体系的に整理した定番サーベイ

### Representation Learning

- [Recent Advances in Autoencoder-Based Representation Learning](https://arxiv.org/abs/1812.05069) — *NeurIPS Workshop 2018* · 📈504。オートエンコーダによる表現学習の最新進展を整理した概説

### Self-Supervised Learning

- [Bootstrap your own latent: A new approach to self-supervised Learning](https://arxiv.org/abs/2006.07733) — *NeurIPS 2020* · 📈8575。負例なしで自己教師あり学習を達成したBYOLの代表論文
- [Self-Supervised Representation Learning: Introduction, Advances and Challenges](https://arxiv.org/abs/2110.09327) — *IEEE Signal Processing Magazine 2021* · 📈392。自己教師あり表現学習の入門と最新動向を整理した概説

### Semi-Supervised Learning

- [A survey on Semi-, Self- and Unsupervised Learning for Image Classification](https://arxiv.org/abs/2002.08721) — *IEEE Access 2021* · 📈187。半教師/自己教師/教師なし学習を横断的に比較したサーベイ

### Sparse Representation

- [A survey of sparse representation: algorithms and applications](https://arxiv.org/abs/1602.07017) — *IEEE Access 2015* · 📈1056。スパース表現のアルゴリズムと応用を網羅的に整理したサーベイ

### State Space Models

- [Advancing Intelligent Sequence Modeling: Evolution, Trade-offs, and Applications of State-Space Architectures from S4 to Mamba](https://arxiv.org/abs/2503.18970) — *arXiv 2025* · 📈18。S4からMambaまで状態空間アーキテクチャの進化と応用を整理した総説

### Tabular Deep Learning

- [Deep Neural Networks and Tabular Data: A Survey](https://arxiv.org/abs/2110.01889) — *IEEE TNNLS 2022* · 📈1121。表形式データ向け深層学習手法を体系的に整理したサーベイ
- [A Survey on Deep Tabular Learning](https://arxiv.org/abs/2410.12034) — *arXiv 2024* · 📈46。表形式データの深層学習をFCNからTabNet/Mamba系まで概観した総説

### Tabular Foundation Models

- [Representation Learning for Tabular Data: A Comprehensive Survey](https://arxiv.org/abs/2504.16109) — *arXiv 2025* · 📈38。表形式データの表現学習と表基盤モデルを包括的に整理したサーベイ — [`LAMDA-Tabular/Tabular-Survey`](https://github.com/LAMDA-Tabular/Tabular-Survey) ⭐126🟢

### Time Series Foundation Models

- [Foundation Models for Time Series: A Survey](https://arxiv.org/abs/2504.04011) — *arXiv 2025* · 📈26。時系列基盤モデルを予測形式やスケールで分類した総説

### Transfer Learning

- [A Comprehensive Survey on Transfer Learning](https://arxiv.org/abs/1911.02685) — *Proceedings of the IEEE 2020* · 📈5774。転移学習の手法を機構別に分類した高被引用サーベイ
- [A Survey on Deep Transfer Learning](https://arxiv.org/abs/1808.01974) — *ICANN 2018* · 📈2897。深層転移学習を4カテゴリに分類した簡潔なサーベイ
- [A Survey on Negative Transfer](https://arxiv.org/abs/2009.00909) — *IEEE/CAA JAS 2022* · 📈357。転移学習で性能低下を招く負の転移を体系化したサーベイ

### Uncertainty Estimation

- [A Review of Uncertainty Quantification in Deep Learning: Techniques, Applications and Challenges](https://arxiv.org/abs/2011.06225) — *Information Fusion 2021* · 📈2574。深層学習の不確実性定量化技術を網羅した高被引用レビュー
- [A Survey of Uncertainty in Deep Neural Networks](https://arxiv.org/abs/2107.03342) — *Artificial Intelligence Review 2021* · 📈1764。DNNの不確実性の源泉と推定/較正手法を体系化したサーベイ

### Weak Supervision

- [A Survey on Programmatic Weak Supervision](https://arxiv.org/abs/2202.05433) — *arXiv 2022* · 📈109。プログラム的弱教師あり学習の手法とパイプラインを整理したサーベイ

## 📐 学習理論

### Approximation Theory / Expressive Power

- [Approximation Power of Deep Neural Networks: an explanatory mathematical survey](https://arxiv.org/abs/2207.09511) — *arXiv 2022*。深層ニューラルネットの近似能力(表現能力)を数学的に解説したサーベイ

### Bandits

- [Introduction to Multi-Armed Bandits](https://arxiv.org/abs/1904.07272) — *Foundations and Trends in ML 2019* · 📈1248。多腕バンディットの理論を体系的にまとめた定番教科書/概説

### Deep Learning Theory

- [The Principles of Deep Learning Theory](https://arxiv.org/abs/2106.10165) — *Cambridge University Press 2022* · 📈285。有効場理論的アプローチで深層学習を解析した体系的教科書/概説
- [The Modern Mathematics of Deep Learning](https://arxiv.org/abs/2105.04026) — *Cambridge University Press 2022* · 📈134。深層学習理論(汎化/最適化/表現力)を数学的に俯瞰した包括的概説
- [A Survey on Statistical Theory of Deep Learning: Approximation, Training Dynamics, and Generative Models](https://arxiv.org/abs/2401.07187) — *Annual Review of Statistics and Its Application 2024*。深層学習の統計理論(近似・学習ダイナミクス・生成モデル)を俯瞰したサーベイ

### Differential Privacy Theory

- [A Comprehensive Guide to Differential Privacy: From Theory to User Expectations](https://arxiv.org/abs/2509.03294) — *arXiv 2025*。微分プライバシーの理論基盤・メカニズム・応用を網羅した包括ガイド

### Fairness Theory

- [Fairness in Machine Learning: A Survey](https://arxiv.org/abs/2010.04053) — *ACM Computing Surveys 2020*。機械学習の公平性を前処理/学習中/後処理の11手法群に整理したサーベイ

### Generalization Bounds

- [Generalization in Deep Learning](https://arxiv.org/abs/1710.05468) — *Cambridge University Press 2022* · 📈499。深層学習の汎化に関する理論的洞察を整理した概説

### Implicit Regularization

- [On the Implicit Bias in Deep-Learning Algorithms](https://arxiv.org/abs/2208.12591) — *Communications of the ACM 2022*。勾配ベース学習の暗黙的バイアス(暗黙的正則化)の主要結果を概説したサーベイ

### Multi-Armed Bandits

- [A Survey of Risk-Aware Multi-Armed Bandits](https://arxiv.org/abs/2205.05843) — *IJCAI 2022*。リスク尺度を考慮した多腕バンディット研究を統合・整理したサーベイ
- [A Survey on Practical Applications of Multi-Armed and Contextual Bandits](https://arxiv.org/abs/1904.10040) — *arXiv 2019*。多腕バンディット・文脈バンディットの実応用を幅広く概観したサーベイ
- [A Survey on Contextual Multi-armed Bandits](https://arxiv.org/abs/1508.03326) — *arXiv 2016*。確率的・敵対的文脈バンディットの各アルゴリズムと後悔限界を整理したサーベイ

### Online Convex Optimization

- [Introduction to Online Convex Optimization](https://arxiv.org/abs/1909.05207) — *Foundations and Trends in Optimization 2019*。オンライン凸最適化の理論とアルゴリズムを体系化した定番の入門書/サーベイ
- [Online convex optimization and no-regret learning: Algorithms, guarantees and applications](https://arxiv.org/abs/1804.04529) — *arXiv 2018*。no-regret学習の保証と応用例(計量学習・無線資源配分等)を解説するチュートリアル

### Online Learning

- [Online Learning: A Comprehensive Survey](https://arxiv.org/abs/1802.02871) — *Neurocomputing 2021* · 📈811。オンライン学習の理論と手法を網羅した包括的サーベイ
- [A Modern Introduction to Online Learning](https://arxiv.org/abs/1912.13213) — *arXiv 2019*。OMD/FTRLを軸にオンライン学習の一次・二次法を統一的に解説した入門サーベイ

### Overparameterization / Generalization

- [Generalization in Neural Networks: A Broad Survey](https://arxiv.org/abs/2209.01610) — *Neurocomputing 2022*。過剰パラメータ化を含むニューラルネットの汎化を広範に整理したサーベイ

### PAC-Bayes

- [A Primer on PAC-Bayesian Learning](https://arxiv.org/abs/1901.05353) — *arXiv 2019*。PAC-Bayes枠組みの理論とアルゴリズム的発展を自己完結的に解説した入門サーベイ

## 🎮 強化学習 (RL)

### Applications (Healthcare)

- [Reinforcement Learning in Healthcare: A Survey](https://arxiv.org/abs/1908.08796) — *ACM Computing Surveys 2021* · 📈756。医療領域へのRL応用の理論基盤・手法・課題を整理したサーベイ

### Bayesian RL

- [Bayesian Reinforcement Learning: A Survey](https://arxiv.org/abs/1609.04436) — *Foundations and Trends in Machine Learning 2015* · 📈719。探索と事前知識をベイズ的に扱うRL手法を網羅した定番サーベイ

### Credit Assignment

- [A Survey of Temporal Credit Assignment in Deep Reinforcement Learning](https://arxiv.org/abs/2312.01072) — *arXiv 2023* · 📈52。時間的クレジット割当を統一形式で比較した深層RLサーベイ

### Curriculum Learning

- [Curriculum Learning for Reinforcement Learning Domains: A Framework and Survey](https://arxiv.org/abs/2003.04960) — *JMLR 2020* · 📈699。RL向けカリキュラム学習の枠組みを提示し既存手法を分類したサーベイ

### Deep RL (general)

- [Deep Reinforcement Learning: A Brief Survey](https://arxiv.org/abs/1708.05866) — *IEEE Signal Processing Magazine 2017* · 📈3545。価値ベース/方策ベース手法と主要アルゴリズムを簡潔に整理した定番入門サーベイ
- [Deep Reinforcement Learning: An Overview](https://arxiv.org/abs/1701.07274) — *arXiv 2017* · 📈1824。深層強化学習の要素・機構・応用を網羅した初期の包括的概観

### Distributed RL

- [Distributed Deep Reinforcement Learning: A Survey and A Multi-Player Multi-Agent Learning Toolbox](https://arxiv.org/abs/2212.00253) — *Machine Intelligence Research 2024* · 📈35。サンプル効率と分散化の観点で分散深層RLを整理したサーベイ

### Exploration

- [Exploration in Deep Reinforcement Learning: A Survey](https://arxiv.org/abs/2205.00824) — *Information Fusion 2022* · 📈583。新規状態報酬・目標ベース等に分類した深層RLの探索サーベイ
- [A Survey of Exploration Methods in Reinforcement Learning](https://arxiv.org/abs/2109.00157) — *arXiv 2021* · 📈108。RLにおける探索手法を分類体系とともに概観したサーベイ

### Generalization

- [A Survey of Zero-shot Generalisation in Deep Reinforcement Learning](https://arxiv.org/abs/2111.09794) — *JAIR 2023* · 📈267。未知環境への汎化問題を統一形式とベンチマークで整理したサーベイ

### Goal-Conditioned RL

- [Goal-Conditioned Reinforcement Learning: Problems and Solutions](https://arxiv.org/abs/2201.08299) — *IJCAI 2022* · 📈218。目標条件付きRLの問題設定・目標表現・解法を体系化したサーベイ

### Hierarchical RL

- [Hierarchical Reinforcement Learning: A Comprehensive Survey](https://doi.org/10.1145/3453160) — *ACM Computing Surveys 2021*。サブタスク発見・転移・多エージェントを含む階層RLの新分類サーベイ

### Imitation Learning

- [An Algorithmic Perspective on Imitation Learning](https://arxiv.org/abs/1811.06711) — *Foundations and Trends in Robotics 2018* · 📈1005。模倣学習をアルゴリズム視点で体系化した定番サーベイ

### In-Context Reinforcement Learning

- [A Survey of In-Context Reinforcement Learning](https://arxiv.org/abs/2502.07978) — *arXiv preprint 2025* · 📈34。推論時にコンテキストから適応するin-context強化学習の研究を整理したサーベイ。

### Inverse RL

- [A Survey of Inverse Reinforcement Learning: Challenges, Methods and Progress](https://arxiv.org/abs/1806.06877) — *Artificial Intelligence 2021* · 📈776。逆強化学習の課題・手法・進展を整理したサーベイ

### Meta RL

- [A Tutorial on Meta-Reinforcement Learning](https://arxiv.org/abs/2301.08028) — *Foundations and Trends in Machine Learning 2025* · 📈157。タスク分布と学習予算の観点でメタRLを分類した包括的チュートリアル

### Model-based RL

- [A Survey on Model-based Reinforcement Learning](https://arxiv.org/abs/2206.09328) — *Science China Information Sciences 2024* · 📈172。深層MBRLの最近の進展に焦点を当てたモデルベースRLサーベイ
- [Model-based Reinforcement Learning: A Survey](https://arxiv.org/abs/2006.16712) — *Foundations and Trends in Machine Learning 2023* · 📈57。学習と計画の統合という観点でMBRLを体系化した定番サーベイ

### Multi-objective RL

- [A Practical Guide to Multi-Objective Reinforcement Learning and Planning](https://arxiv.org/abs/2103.09568) — *AAMAS (JAAMAS) 2022* · 📈534。多目的RL/計画の実務的指針を提供する包括的ガイド

### Offline RL

- [Offline Reinforcement Learning: Tutorial, Review, and Perspectives on Open Problems](https://arxiv.org/abs/2005.01643) — *arXiv 2020* · 📈2625。オフラインRLの基礎と未解決問題を整理した最重要チュートリアル兼レビュー
- [A Survey on Offline Reinforcement Learning: Taxonomy, Review, and Open Problems](https://arxiv.org/abs/2203.01387) — *IEEE TNNLS 2023* · 📈397。新たな分類体系でオフラインRLアルゴリズムを整理したサーベイ — [`larocs/offline-rl-suvey`](https://github.com/larocs/offline-rl-suvey) ⭐8🔴

### RL for Generative AI

- [Reinforcement Learning for Generative AI: State of the Art, Opportunities and Open Research Challenges](https://arxiv.org/abs/2308.00031) — *JAIR 2024* · 📈36。生成AIへのRL適用の現状・機会・未解決課題を整理したサーベイ
- [Reinforcement Learning for Generative AI: A Survey](https://arxiv.org/abs/2308.14328) — *arXiv 2023* · 📈27。生成モデルへのRL適用(新訓練信号・人間バイアス注入)を整理したサーベイ

### RLHF

- [Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2307.15217) — *TMLR 2023* · 📈873。RLHFの未解決問題・根本的限界と監査基準を整理した重要サーベイ
- [A Survey of Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2312.14925) — *arXiv 2023* · 📈320。制御・ロボティクス起源からLLMまでRLHFの原理と研究動向を概観

### RLHF / Preference-based RL

- [A Survey of Preference-Based Reinforcement Learning Methods](https://jmlr.org/papers/v18/16-634.html) — *JMLR 2017*。専門家の選好から学ぶ選好ベースRL手法を整理した定番サーベイ

### Reward Design

- [Reward Models in Deep Reinforcement Learning: A Survey](https://arxiv.org/abs/2506.15421) — *IJCAI 2025* · 📈25。報酬モデルを出所・機構・学習様式の観点で整理した近年のサーベイ

### Safe / Constrained RL

- [A Survey of Safe Reinforcement Learning and Constrained MDPs: A Technical Survey on Single-Agent and Multi-Agent Safety](https://arxiv.org/abs/2505.17342) — *arXiv preprint 2025* · 📈13。制約付きMDPに基づく安全RLを単一/マルチエージェント両面から数学的に整理した技術サーベイ。

### Safe RL

- [A Review of Safe Reinforcement Learning: Methods, Theory and Applications](https://arxiv.org/abs/2205.10330) — *IEEE TPAMI 2024* · 📈322。2H3Wの観点で手法・理論・応用・ベンチマークを整理した近年の安全RLレビュー — [`chauncygu/Safe-Reinforcement-Learning-Baselines`](https://github.com/chauncygu/Safe-Reinforcement-Learning-Baselines) ⭐794🟢
- [A Survey of Constraint Formulations in Safe Reinforcement Learning](https://arxiv.org/abs/2402.02025) — *IJCAI 2024* · 📈65。安全RLの制約定式化を代表的アルゴリズムと数理的関係から整理したサーベイ
- [A Comprehensive Survey on Safe Reinforcement Learning](https://jmlr.org/papers/v16/garcia15a.html) — *JMLR 2015*。安全RLの最適性基準修正と探索修正アプローチを整理した古典的サーベイ

### Sim-to-Real

- [Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey](https://arxiv.org/abs/2009.13303) — *IEEE SSCI 2020* · 📈1008。ドメインランダム化・適応等のsim-to-real手法を概観したサーベイ

### Transfer Learning

- [Transfer Learning in Deep Reinforcement Learning: A Survey](https://arxiv.org/abs/2009.07888) — *IEEE TPAMI 2023* · 📈876。転移知識の形式と転移様式で深層RLの転移学習を分類したサーベイ

### Visual / Multimodal RL

- [Reinforcement Learning for Large Model: A Survey](https://arxiv.org/abs/2508.08189) — *arXiv preprint 2025* · 📈1。マルチモーダル大規模モデルにおける視覚強化学習の進展を整理したサーベイ。 — [`weijiawu/Awesome-RL-for-Multimodal-Foundation-Models`](https://github.com/weijiawu/Awesome-RL-for-Multimodal-Foundation-Models) ⭐447🟢

## 🤖 ロボティクス・身体性

### Autonomous Driving

- [Deep Reinforcement Learning for Autonomous Driving: A Survey](https://arxiv.org/abs/2002.00444) — *IEEE Transactions on Intelligent Transportation Systems 2022* · 📈2324。自動運転タスクへの(深層)RL適用を分類し展開上の課題を整理した定番サーベイ
- [A Survey of Deep Learning Techniques for Autonomous Driving](https://arxiv.org/abs/1910.07738) — *Journal of Field Robotics 2020* · 📈1698。知覚・計画・制御からEnd2Endまで自動運転の深層学習技術を概観した定番サーベイ
- [Survey of Deep Reinforcement Learning for Motion Planning of Autonomous Vehicles](https://arxiv.org/abs/2001.11231) — *IEEE Transactions on Intelligent Transportation Systems 2022* · 📈581。自動運転車の階層的運動計画問題に対する深層RLを整理したサーベイ
- [A Survey of Deep RL and IL for Autonomous Driving Policy Learning](https://arxiv.org/abs/2101.01993) — *IEEE Transactions on Intelligent Transportation Systems 2022* · 📈215。自動運転の方策学習における深層RLと深層模倣学習を整理したサーベイ
- [A Survey of Deep Reinforcement Learning Algorithms for Motion Planning and Control of Autonomous Vehicles](https://arxiv.org/abs/2105.14218) — *IEEE IV 2021* · 📈69。自動運転車の運動計画・制御に向けた深層RL手法を整理したサーベイ

### Embodied AI

- [A Survey of Embodied AI: From Simulators to Research Tasks](https://arxiv.org/abs/2103.04918) — *IEEE Transactions on Emerging Topics in Computational Intelligence 2022* · 📈511。シミュレータと探索・ナビ・EQAタスクを軸にEmbodied AIを概観
- [Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI](https://arxiv.org/abs/2407.06886) — *arXiv 2024* · 📈284。サイバー空間と物理世界の統合を軸にembodied AIを体系化した大型サーベイ(2k+ star companion) — [`HCPLab-SYSU/Embodied_AI_Paper_List`](https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List) ⭐2076🟢

### Grasping

- [Deep Learning Approaches to Grasp Synthesis: A Review](https://arxiv.org/abs/2207.02556) — *IEEE Transactions on Robotics 2023* · 📈260。6自由度把持を中心に深層学習による把持合成手法を体系化したレビュー

### Legged Locomotion

- [Reinforcement Learning For Quadrupedal Locomotion: Current Advancements And Future Perspectives](https://arxiv.org/abs/2410.10438) — *arXiv 2024* · 📈2。学習則・カリキュラム・報酬・sim-to-realを含む四足歩行RL制御の概観

### Manipulation

- [A Review of Robot Learning for Manipulation: Challenges, Representations, and Algorithms](https://arxiv.org/abs/1907.03146) — *JMLR 2021* · 📈491。ロボット操作学習問題を統一枠組みで定式化したレビュー
- [A Survey on Deep Reinforcement Learning Algorithms for Robotic Manipulation](https://doi.org/10.3390/s23073762) — *Sensors 2023*。把持・操作タスク向けの深層RLアルゴリズムを整理したサーベイ

### Manipulation / Embodied AI

- [A Survey of Embodied Learning for Object-Centric Robotic Manipulation](https://arxiv.org/abs/2408.11537) — *arXiv 2024* · 📈40。物体中心ロボット操作の身体性学習を知覚・方策・タスクで整理 — [`RayYoh/OCRM_survey`](https://github.com/RayYoh/OCRM_survey) ⭐255🔴

### Motion Planning (learning)

- [A Survey of Optimization-based Task and Motion Planning: From Classical To Learning Approaches](https://arxiv.org/abs/2404.02817) — *IEEE/ASME Transactions on Mechatronics 2024* · 📈77。古典手法から学習ベースまでタスク&モーションプランニングを概観
- [A Survey on the Integration of Machine Learning with Sampling-based Motion Planning](https://arxiv.org/abs/2211.08368) — *Foundations and Trends in Robotics 2022* · 📈25。サンプリングベース運動計画への機械学習統合を分類したサーベイ

### Navigation

- [Deep Learning for Embodied Vision Navigation: A Survey](https://arxiv.org/abs/2108.04097) — *arXiv 2021* · 📈1。目標指向/指示指向のEmbodied視覚ナビゲーションの深層学習手法を概観

### Robot Foundation Models

- [Foundation Models in Robotics: Applications, Challenges, and the Future](https://arxiv.org/abs/2312.07843) — *International Journal of Robotics Research 2024* · 📈370。知覚から制御まで基盤モデルのロボティクス応用と課題を整理したサーベイ

### Robot Learning

- [Deep Reinforcement Learning for Robotics: A Survey of Real-World Successes](https://arxiv.org/abs/2408.03539) — *Annual Review of Control, Robotics, and Autonomous Systems 2025* · 📈346。実世界で成功した深層RLロボティクス事例を主要能力ごとに評価したレビュー
- [Reinforcement Learning in Robotics: A Survey](https://doi.org/10.1177/0278364913495721) — *International Journal of Robotics Research 2013*。ロボットRLの課題・表現・事前知識を整理した古典的定番サーベイ

### Safe RL / Control

- [Safe Learning in Robotics: From Learning-Based Control to Safe Reinforcement Learning](https://arxiv.org/abs/2108.06266) — *Annual Review of Control, Robotics, and Autonomous Systems 2022* · 📈930。制御理論とRLを統一視点で結ぶロボティクスの安全学習レビュー

### Soft Robotics (learning)

- [Data-driven Methods Applied to Soft Robot Modeling and Control: A Review](https://arxiv.org/abs/2305.12137) — *IEEE Transactions on Automation Science and Engineering 2024* · 📈102。統計手法・NN・RLによるソフトロボットのモデリングと制御を整理したレビュー

### World Models

- [A Comprehensive Survey on World Models for Embodied AI](https://arxiv.org/abs/2510.16732) — *arXiv 2025* · 📈33。機能・時間・空間表現の3軸タクソノミでembodied AI向けワールドモデルを整理 — [`Li-Zn-H/AwesomeWorldModels`](https://github.com/Li-Zn-H/AwesomeWorldModels) ⭐314🟢

### World Models for Robot Learning

- [World Model for Robot Learning: A Comprehensive Survey](https://arxiv.org/abs/2605.00080) — *arXiv preprint 2026* · 📈4。ロボット学習における世界モデル(拡散世界モデル等)を体系化した包括サーベイ。

## 👥 マルチエージェント

### Agent Evaluation

- [Survey on Evaluation of LLM-based Agents](https://arxiv.org/abs/2503.16416) — *arXiv 2025* · 📈169。LLMエージェントの評価手法・ベンチマークを体系化したサーベイ

### Agent Optimization

- [A Survey on the Optimization of Large Language Model-based Agents](https://arxiv.org/abs/2503.12434) — *arXiv 2025* · 📈37。LLMエージェントの最適化(フィードバック・自己改善)を整理した総説

### Agentic RAG

- [Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG](https://arxiv.org/abs/2501.09136) — *arXiv 2025* · 📈309。自律エージェントを組み込んだエージェント的RAGを類型化した総説 — [`asinghcsu/AgenticRAG-Survey`](https://github.com/asinghcsu/AgenticRAG-Survey) ⭐1649🟡

### Agentic RL

- [The Landscape of Agentic Reinforcement Learning for LLMs: A Survey](https://arxiv.org/abs/2509.02547) — *arXiv 2025* · 📈139。計画/ツール/記憶/自己改善を軸にエージェント的RLを体系化した総説

### Autonomous Agents

- [Large Language Model Agent: A Survey on Methodology, Applications and Challenges](https://arxiv.org/abs/2503.21460) — *arXiv 2025* · 📈161。LLMエージェントを構築/協調/進化の3軸で方法論中心に整理した総説 — [`luo-junyu/Awesome-Agent-Papers`](https://github.com/luo-junyu/Awesome-Agent-Papers) ⭐2732🟡

### Cooperative MARL

- [A Review of Cooperative Multi-Agent Deep Reinforcement Learning](https://arxiv.org/abs/1908.03963) — *Applied Intelligence 2023* · 📈613。独立学習・価値分解・通信学習等5アプローチで協調MARLを整理
- [A Survey of Progress on Cooperative Multi-agent Reinforcement Learning in Open Environment](https://arxiv.org/abs/2312.01058) — *arXiv 2023* · 📈76。オープン環境での協調MARLの進展を整理した近年のサーベイ

### Emergent Communication

- [A Survey of Multi-Agent Deep Reinforcement Learning with Communication](https://arxiv.org/abs/2203.08975) — *AAMAS (JAAMAS) 2024* · 📈278。DIAL/CommNet等の通信付きMARL 41モデルを設計次元で分類

### GUI Agents

- [GUI Agents: A Survey](https://arxiv.org/abs/2412.13501) — *ACL Findings 2024* · 📈102。GUIエージェントのアーキテクチャ・ベンチマークを整理した総説
- [GUI Agents with Foundation Models: A Comprehensive Survey](https://arxiv.org/abs/2411.04890) — *arXiv 2024* · 📈99。基盤モデルを用いたGUIエージェント/computer useを網羅したサーベイ

### Game Theory & Learning

- [An Overview of Multi-Agent Reinforcement Learning from Game Theoretical Perspective](https://arxiv.org/abs/2011.00583) — *arXiv 2020* · 📈216。ゲーム理論の視点でMARLの基礎から最前線までを自己完結的に整理

### LLM Agent Memory

- [A Survey on the Memory Mechanism of Large Language Model based Agents](https://arxiv.org/abs/2404.13501) — *arXiv 2024* · 📈563。LLMエージェントのメモリ機構の設計・評価を体系的に整理した総説

### MARL (deep)

- [Deep Reinforcement Learning for Multi-Agent Systems: A Review of Challenges, Solutions and Applications](https://arxiv.org/abs/1812.11794) — *IEEE Transactions on Cybernetics 2020* · 📈1008。非定常性・部分観測等のMADRL課題と解決策・応用を整理したサーベイ
- [A Survey and Critique of Multiagent Deep Reinforcement Learning](https://arxiv.org/abs/1810.05587) — *AAMAS (JAAMAS) 2019* · 📈707。MARLと深層RLの構成要素を結びつけ実践指針を示した定番サーベイ

### MARL (general)

- [Multi-Agent Reinforcement Learning: A Comprehensive Survey](https://arxiv.org/abs/2312.10256) — *arXiv 2024* · 📈64。ゲーム理論と機械学習を結びつけMARLの課題を体系化した包括サーベイ

### MARL (theory)

- [Multi-Agent Reinforcement Learning: A Selective Overview of Theories and Algorithms](https://arxiv.org/abs/1911.10635) — *Handbook of RL and Control 2021* · 📈1629。理論的裏付けのあるMARLアルゴリズムを選択的に概観したサーベイ

### Multi-Agent Collaboration

- [Multi-Agent Collaboration Mechanisms: A Survey of LLMs](https://arxiv.org/abs/2501.06322) — *arXiv 2025* · 📈454。LLMマルチエージェントの協調メカニズムを類型化したサーベイ

### Multi-Agent Reinforcement Learning

- [A Survey of Multi Agent Reinforcement Learning: Federated Learning and Cooperative and Noncooperative Decentralized Regimes](https://arxiv.org/abs/2507.06278) — *arXiv preprint 2025* · 📈9。協調/非協調/連合学習の相互作用トポロジでマルチエージェントRLを整理したサーベイ。

### Role-Playing Agents

- [From Persona to Personalization: A Survey on Role-Playing Language Agents](https://arxiv.org/abs/2404.18231) — *arXiv 2024* · 📈236。ロールプレイ言語エージェントのペルソナ能力と評価を概観したサーベイ

### Tool Learning

- [Tool Learning with Large Language Models: A Survey](https://arxiv.org/abs/2405.17935) — *arXiv 2024* · 📈276。LLMのツール学習の動機・手法・ベンチマークを体系化したサーベイ — [`quchangle1/LLM-Tool-Survey`](https://github.com/quchangle1/LLM-Tool-Survey) ⭐484🟡

### Web Agents

- [A Survey of WebAgents: Towards Next-Generation AI Agents for Web Automation with Large Foundation Models](https://arxiv.org/abs/2503.23350) — *arXiv 2025* · 📈105。大規模基盤モデルによるWeb自動化エージェントを体系化した総説

## 🕸️ グラフニューラルネット (GNN)

### Dynamic Graph Neural Networks

- [A survey of dynamic graph neural networks](https://arxiv.org/abs/2404.18211) — *Frontiers of Computer Science 2024* · 📈98。時間情報の取り込み方で動的GNNを分類し最新モデルを概観したサーベイ。

### Dynamic Graphs

- [Representation Learning for Dynamic Graphs: A Survey](https://arxiv.org/abs/1905.11485) — *JMLR 2020* · 📈614。動的グラフ表現学習をエンコーダ・デコーダの枠組みで整理した定番サーベイ
- [Graph Neural Networks for Temporal Graphs: State of the Art, Open Challenges, and Opportunities](https://arxiv.org/abs/2302.01018) — *TMLR 2023* · 📈107。時間発展グラフ向けGNNの最新動向と課題を整理した近年サーベイ

### GNN Benchmark

- [Benchmarking Graph Neural Networks](https://arxiv.org/abs/2003.00982) — *JMLR 2023* · 📈1186。中規模データセットで主要GNNを公平比較する定番ベンチマーク論文

### GNN Explainability

- [Explainability in Graph Neural Networks: A Taxonomic Survey](https://arxiv.org/abs/2012.15445) — *IEEE TPAMI 2022* · 📈820。GNN説明可能性手法の統一的分類体系と評価指標を提示した定番サーベイ

### GNN General

- [Graph Neural Networks: A Review of Methods and Applications](https://arxiv.org/abs/1812.08434) — *AI Open 2020* · 📈6982。GNNの設計パイプラインと応用を体系化した高被引用レビュー

### GNN for NLP

- [Graph Neural Networks for Natural Language Processing: A Survey](https://arxiv.org/abs/2106.06090) — *Foundations and Trends in Machine Learning 2021* · 📈0。NLP向けGNNをグラフ構築・表現学習・エンコーダデコーダ軸で整理した大著

### Graph Adversarial Robustness

- [Adversarial Attacks and Defenses on Graphs: A Review, A Tool and Empirical Studies](https://arxiv.org/abs/2003.00653) — *SIGKDD Explorations 2020* · 📈107。グラフへの敵対的攻撃と防御の手法・ツール・実証研究を整理

### Graph Anomaly Detection

- [Deep Graph Anomaly Detection: A Survey and New Perspectives](https://arxiv.org/abs/2409.09957) — *IEEE TKDE 2024* · 📈82。深層グラフ異常検知の新たな分類視点を提示した近年サーベイ

### Graph Condensation

- [Graph Condensation: A Survey](https://arxiv.org/abs/2401.11720) — *arXiv preprint 2024* · 📈36。グラフ凝縮の最適化目標・生成戦略・応用を体系化したサーベイ(別系統の凝縮サーベイ)。
- [A Survey on Graph Condensation](https://arxiv.org/abs/2402.02000) — *arXiv preprint 2024* · 📈13。大規模グラフを小さく情報量の高いグラフへ凝縮するグラフ凝縮手法の定義と分類を与えたサーベイ。

### Graph Contrastive Learning

- [Towards Graph Contrastive Learning: A Survey and Beyond](https://arxiv.org/abs/2405.11868) — *arXiv 2024* · 📈62。グラフ対照学習をデータ拡張・対照モード・最適化目的の観点で網羅

### Graph Distribution Shift

- [Graph Learning under Distribution Shifts: A Comprehensive Survey on Domain Adaptation, Out-of-distribution, and Continual Learning](https://arxiv.org/abs/2402.16374) — *arXiv preprint 2024* · 📈31。ドメイン適応・OOD・継続学習を横断してグラフの分布シフト対処を俯瞰した包括サーベイ。

### Graph Generation

- [A Systematic Survey on Deep Generative Models for Graph Generation](https://arxiv.org/abs/2007.06686) — *IEEE TPAMI 2020* · 📈197。グラフ生成の深層生成モデルを体系的に整理したサーベイ

### Graph OOD Adaptation

- [Beyond Generalization: A Survey of Out-Of-Distribution Adaptation on Graphs](https://arxiv.org/abs/2402.11153) — *arXiv preprint 2024* · 📈10。グラフのOOD適応(訓練時/テスト時)に特化して手法を分類したサーベイ。 — [`kaize0409/Awesome-Graph-OOD`](https://github.com/kaize0409/Awesome-Graph-OOD) ⭐85🔴

### Graph OOD Generalization / Adaptation

- [A Survey of Deep Graph Learning under Distribution Shifts: from Graph Out-of-Distribution Generalization to Adaptation](https://arxiv.org/abs/2410.19265) — *arXiv preprint 2024* · 📈19。分布シフト下のグラフ学習をOOD汎化と訓練時/テスト時適応に分けて整理したサーベイ。 — [`kaize0409/Awesome-Graph-OOD`](https://github.com/kaize0409/Awesome-Graph-OOD) ⭐85🔴

### Graph Pooling

- [Graph Pooling for Graph Neural Networks: Progress, Challenges, and Opportunities](https://arxiv.org/abs/2204.07321) — *IJCAI Survey Track 2023* · 📈124。GNNのグラフプーリング手法を分類し進展と課題を整理したサーベイ

### Graph Reduction

- [A Comprehensive Survey on Graph Reduction: Sparsification, Coarsening, and Condensation](https://arxiv.org/abs/2402.03358) — *IJCAI 2024 2024* · 📈100。スパース化・粗視化・凝縮を統一的に俯瞰したグラフ縮約のサーベイ(IJCAI 2024)。

### Graph Representation Learning

- [Machine Learning on Graphs: A Model and Comprehensive Taxonomy](https://arxiv.org/abs/2005.03675) — *JMLR 2022* · 📈344。ノード埋め込み・グラフ正則化・GNNを統一的分類体系で整理

### Graph Self-Supervised Learning

- [Graph Self-Supervised Learning: A Survey](https://arxiv.org/abs/2103.00111) — *IEEE TKDE 2022* · 📈740。グラフ自己教師あり学習の手法を生成・対照・予測で分類したサーベイ
- [Self-Supervised Learning of Graph Neural Networks: A Unified Review](https://arxiv.org/abs/2102.10757) — *IEEE TPAMI 2022* · 📈404。GNNの自己教師あり学習を対照型・予測型に統一的に整理したレビュー
- [Self-supervised Learning on Graphs: Contrastive, Generative, or Predictive](https://arxiv.org/abs/2105.07342) — *IEEE TKDE 2023* · 📈323。グラフSSLを対照・生成・予測の3カテゴリで整理（コンパニオンawesomeリスト付） — [`LirongWu/awesome-graph-self-supervised-learning`](https://github.com/LirongWu/awesome-graph-self-supervised-learning) ⭐1435🔴

### Graph Transformers

- [Transformer for Graphs: An Overview from Architecture Perspective](https://arxiv.org/abs/2202.08455) — *arXiv 2022* · 📈208。グラフTransformerをアーキテクチャ観点で分類・比較したサーベイ

### Heterogeneous Graphs

- [Heterogeneous Network Representation Learning: A Unified Framework With Survey and Benchmark](https://arxiv.org/abs/2004.00216) — *IEEE TKDE 2022* · 📈60。異種ネットワーク表現学習を統一フレームワークとベンチマークで整理(IEEE TKDE 2022掲載)

### Heterophilic GNN

- [Graph Neural Networks for Graphs with Heterophily: A Survey](https://arxiv.org/abs/2202.07082) — *IEEE TKDE 2022* · 📈313。ヘテロフィリ（異種接続）グラフ向けGNN手法を体系的に整理したサーベイ

### Hypergraph Neural Networks

- [Recent Advances in Hypergraph Neural Networks](https://arxiv.org/abs/2503.07959) — *arXiv preprint 2025* · 📈12。ハイパーグラフニューラルネットワークの主要モデルを5つのアーキテクチャ系統で分類したサーベイ。

### LLM for Graph Data Challenges

- [A Survey of Large Language Models for Data Challenges in Graphs](https://arxiv.org/abs/2505.18475) — *arXiv preprint 2025* · 📈5。グラフの欠損・不均衡・異種性・動的不安定性をLLMで克服する研究を整理したサーベイ。 — [`limengran98/Awesome-Literature-Graph-Learning-Challenges`](https://github.com/limengran98/Awesome-Literature-Graph-Learning-Challenges) ⭐110🟡

### Molecular / Drug Discovery

- [Graph Neural Networks for the Prediction of Molecular Structure-Property Relationships](https://arxiv.org/abs/2208.04852) — *RSC (Machine Learning and Hybrid Modelling for Reaction Engineering) 2022* · 📈19。分子構造-物性予測のためのGNNを化学工学視点で解説したレビュー
- [A Survey of Graph Neural Networks for Drug Discovery: Recent Developments and Challenges](https://arxiv.org/abs/2509.07887) — *arXiv 2025* · 📈0。創薬向けGNNの最新動向（分子物性・DTI・DDI・新薬設計）を整理

### Scalable GNN

- [A Comprehensive Survey on Distributed Training of Graph Neural Networks](https://arxiv.org/abs/2211.05368) — *Proceedings of the IEEE 2022* · 📈44。大規模グラフ向けGNN分散学習手法を網羅的に整理したサーベイ

### Spatio-Temporal GNN

- [A Systematic Literature Review of Spatio-Temporal Graph Neural Network Models for Time Series Forecasting and Classification](https://arxiv.org/abs/2410.22377) — *arXiv preprint 2024* · 📈23。時系列予測・分類のための時空間GNNモデルを366論文から体系的にレビュー。

## 🔗 知識表現・知識グラフ

### Abstract Reasoning (ARC)

- [The ARC of Progress towards AGI: A Living Survey of Abstraction and Reasoning](https://arxiv.org/abs/2603.13372) — *arXiv 2026* · 📈0。ARC-AGIの3世代ベンチと82手法を横断分析しプログラム合成/ニューロシンボリック/ニューラルの限界を示した生きたサーベイ

### Autoformalization / Theorem Proving

- [Autoformalization in the Era of Large Language Models: A Survey](https://arxiv.org/abs/2505.23486) — *arXiv 2025* · 📈13。LLM時代の自動形式化(autoformalization)を数学とLLMの両視点で俯瞰したサーベイ

### Entity Alignment

- [A Benchmark and Comprehensive Survey on Knowledge Graph Entity Alignment via Representation Learning](https://arxiv.org/abs/2103.15059) — *The VLDB Journal 2021*。表現学習による知識グラフのエンティティアラインメント手法のベンチマーク付き総覧。

### Graph + LLM

- [A Survey of Large Language Models for Graphs](https://arxiv.org/abs/2405.08011) — *KDD 2024* · 📈136。グラフ向けLLM手法を分類したKDD24サーベイ（コンパニオンawesomeリスト付） — [`HKUDS/Awesome-LLM4Graph-Papers`](https://github.com/HKUDS/Awesome-LLM4Graph-Papers) ⭐370🟡
- [A Survey of Graph Meets Large Language Model: Progress and Future Directions](https://arxiv.org/abs/2311.12399) — *IJCAI 2024* · 📈108。LLMをenhancer/predictor/alignmentの役割で分類したサーベイ（awesomeリスト付） — [`yhLeeee/Awesome-LLMs-in-Graph-tasks`](https://github.com/yhLeeee/Awesome-LLMs-in-Graph-tasks) ⭐657🟡

### Graph Retrieval-Augmented Generation

- [Graph Retrieval-Augmented Generation: A Survey](https://arxiv.org/abs/2408.08921) — *arXiv 2024*。知識グラフを用いたGraphRAGの手法を初めて包括的に整理したサーベイ。

### Knowledge Base Question Answering

- [Complex Knowledge Base Question Answering: A Survey](https://arxiv.org/abs/2108.06688) — *IEEE TKDE 2021*。複雑な質問に対するKBQAを意味解析型と情報検索型に分けて整理したサーベイ。

### Knowledge Graph + LLM

- [Unifying Large Language Models and Knowledge Graphs: A Roadmap](https://arxiv.org/abs/2306.08302) — *IEEE TKDE 2023* · 📈1462。LLMとKGの統合をKG強化LLM/LLM強化KG/協調の3視点で整理した定番ロードマップ — [`RManLuo/Awesome-LLM-KG`](https://github.com/RManLuo/Awesome-LLM-KG) ⭐2598🟡
- [LLMs for Knowledge Graph Construction and Reasoning: Recent Capabilities and Future Opportunities](https://arxiv.org/abs/2305.13168) — *World Wide Web Journal 2023* · 📈271。LLMによるKG構築・推論の能力と課題を実験的に評価した論文

### Knowledge Graph Completion

- [A Review of Knowledge Graph Completion](https://arxiv.org/abs/2208.11652) — *Information (MDPI) 2022* · 📈92。知識グラフ補完（リンク予測）の手法を分類・比較した近年レビュー

### Knowledge Graph Construction

- [A Comprehensive Survey on Automatic Knowledge Graph Construction](https://arxiv.org/abs/2302.05019) — *ACM Computing Surveys 2023* · 📈311。300超の手法を整理した自動知識グラフ構築の包括的サーベイ。
- [Construction of Knowledge Graphs: State and Challenges](https://arxiv.org/abs/2302.11509) — *arXiv 2023* · 📈73。高品質な知識グラフ構築の各工程と最新研究状況を328文献で総覧。

### Knowledge Graph Embedding

- [A Review of Relational Machine Learning for Knowledge Graphs](https://arxiv.org/abs/1503.00759) — *Proceedings of the IEEE 2016* · 📈1724。知識グラフ向け関係機械学習（潜在変数・グラフ特徴）の古典的定番レビュー
- [A Survey of Knowledge Graph Embedding and Their Applications](https://arxiv.org/abs/2107.07842) — *arXiv 2021* · 📈69。翻訳ベースから拡張ベースまでKG埋め込み手法と応用を整理したサーベイ
- [A Survey on Knowledge Graph Structure and Knowledge Graph Embeddings](https://arxiv.org/abs/2412.10092) — *arXiv 2024*。KG埋め込みモデルとグラフ構造の関係を初めて包括的に整理したサーベイ。
- [Negative Sampling in Knowledge Graph Representation Learning: A Review](https://arxiv.org/abs/2402.19195) — *arXiv 2024*。KG表現学習における負例サンプリング手法を体系的に整理したレビュー。

### Knowledge Graph General

- [Knowledge Graphs](https://arxiv.org/abs/2003.02320) — *ACM Computing Surveys 2021* · 📈2456。知識グラフの定義・スキーマ・推論・品質を網羅した教科書的大著

### Knowledge Graph Question Answering

- [Large Language Models Meet Knowledge Graphs for Question Answering: Synthesis and Opportunities](https://arxiv.org/abs/2505.20099) — *arXiv 2025*。LLMと知識グラフを統合したKGQA手法を新たな分類体系で整理したサーベイ。

### Knowledge Graph Reasoning

- [A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic, and Multimodal](https://arxiv.org/abs/2212.05767) — *IEEE TPAMI 2022* · 📈288。静的・動的・マルチモーダルの観点で知識グラフ推論を整理したサーベイ

### LLM-based Knowledge Graph Construction

- [LLM-empowered knowledge graph construction: A survey](https://arxiv.org/abs/2510.20345) — *arXiv 2025* · 📈12。LLMがオントロジー設計・知識抽出・知識融合の3層構築をどう変えるかを整理したサーベイ。

### Neural-Symbolic Reasoning

- [Neural-Symbolic Reasoning over Knowledge Graphs: A Survey from a Query Perspective](https://arxiv.org/abs/2412.10390) — *arXiv 2024* · 📈28。クエリの観点から知識グラフのニューラル/記号推論を概観したサーベイ。

### Neurosymbolic AI

- [From Statistical Relational to Neurosymbolic Artificial Intelligence: a Survey](https://arxiv.org/abs/2108.11451) — *Artificial Intelligence 2021* · 📈118。統計的関係学習からニューロシンボリックAIへの統合を整理したサーベイ

### Neurosymbolic Reasoning

- [Neurosymbolic AI for Reasoning over Knowledge Graphs: A Survey](https://arxiv.org/abs/2302.07200) — *arXiv 2023* · 📈42。知識グラフ上のニューロシンボリック推論手法を新たな分類体系で整理したサーベイ。

### Ontology Embedding

- [Ontology Embedding: A Survey of Methods, Applications and Resources](https://arxiv.org/abs/2406.10964) — *arXiv 2024*。オントロジー埋め込みの手法・応用・リソースを整理した初の包括サーベイ。

### Planning / RL for Optimization

- [A Survey of Reinforcement Learning for Optimization in Automation](https://arxiv.org/abs/2502.09417) — *arXiv 2025* · 📈23。製造・エネルギー・ロボティクスにおける最適化向け強化学習を俯瞰したサーベイ

### Program Synthesis

- [From Provable Correctness to Probabilistic Generation: A Comparative Review of Program Synthesis Paradigms](https://arxiv.org/abs/2508.00013) — *arXiv 2025* · 📈0。プログラム合成の5パラダイム(論理・帰納・スケッチ・LLM・ニューロシンボリック)を比較したレビュー

### RDF Stores and SPARQL Engines

- [A Survey of RDF Stores & SPARQL Engines for Querying Knowledge Graphs](https://arxiv.org/abs/2102.13027) — *The VLDB Journal 2021* · 📈118。100超のSPARQLエンジンとRDFストアの技術・ベンチマークを総覧したサーベイ。

### Temporal Knowledge Graph

- [A Survey on Temporal Knowledge Graph: Representation Learning and Applications](https://arxiv.org/abs/2403.04782) — *arXiv 2024* · 📈45。時間的知識グラフの表現学習と応用を包括的にまとめたサーベイ。

### Temporal Knowledge Graph Completion

- [A Survey on Temporal Knowledge Graph Completion: Taxonomy, Progress, and Prospects](https://arxiv.org/abs/2308.02457) — *arXiv 2023* · 📈42。時間的知識グラフ補完(TKGC)手法の分類・進展・展望を整理したサーベイ。

### Temporal Knowledge Graph Question Answering

- [Temporal Knowledge Graph Question Answering: A Survey](https://arxiv.org/abs/2406.14191) — *arXiv 2024* · 📈14。時間的知識グラフ質問応答(TKGQA)を時間質問の分類と手法体系の2軸で整理したサーベイ。

## 🎯 因果推論

### Causal Discovery

- [D'ya like DAGs? A Survey on Structure Learning and Causal Discovery](https://arxiv.org/abs/2103.02582) — *ACM Computing Surveys 2021* · 📈388。構造学習・因果発見手法を網羅的に整理した定番サーベイ
- [A Survey on Causal Discovery Methods for I.I.D. and Time Series Data](https://arxiv.org/abs/2303.15027) — *TMLR 2023* · 📈61。i.i.d.データと時系列データ双方の因果発見手法・ツールを整理した近年サーベイ

### Causal Generative Modeling

- [From Identifiable Causal Representations to Controllable Counterfactual Generation: A Survey on Causal Generative Modeling](https://arxiv.org/abs/2310.11011) — *TMLR 2024* · 📈27。因果表現学習と制御可能な反実仮想生成を識別可能性理論から技術的に俯瞰したサーベイ

### Causal Inference

- [A Survey on Causal Inference](https://arxiv.org/abs/2002.02770) — *ACM TKDD 2021* · 📈672。潜在的結果枠組みの因果推論手法を伝統的・ML手法で整理した定番サーベイ

### Causal Machine Learning

- [Causal Machine Learning: A Survey and Open Problems](https://arxiv.org/abs/2206.15475) — *arXiv 2022* · 📈162。因果機械学習を教師あり/生成/説明/公平性/強化学習の5系統に整理し未解決課題を提示したサーベイ

### Causal Reinforcement Learning

- [Causal Reinforcement Learning: A Survey](https://arxiv.org/abs/2307.01452) — *TMLR 2023* · 📈39。因果強化学習の手法をサンプル効率・汎化・転移・説明性・公平性の観点で体系化したサーベイ

### Causal Representation Learning

- [A Survey on Causal Representation Learning and Future Work for Medical Image Analysis](https://arxiv.org/abs/2210.16034) — *arXiv 2022* · 📈0。因果表現学習(CRL)の最近の進展を整理し医療画像解析への応用展望を論じたサーベイ

### Causality + LLM

- [Causal Inference with Large Language Model: A Survey](https://arxiv.org/abs/2409.09822) — *arXiv 2024* · 📈40。LLMを用いた因果推論（発見・効果推定）の最新研究を整理したサーベイ

### Causality and Fairness

- [Survey on Causal-based Machine Learning Fairness Notions](https://arxiv.org/abs/2010.09553) — *arXiv 2020* · 📈99。因果に基づく公平性概念を網羅し実世界シナリオでの適用可能性を因果のはしごで順位付けしたサーベイ

### Causality and LLM

- [Large Language Models and Causal Inference in Collaboration: A Survey](https://arxiv.org/abs/2403.09606) — *arXiv 2024* · 📈31。因果推論とLLMの相互作用(因果視点でのLLM評価とLLMによる因果発見支援)を整理したサーベイ

### Causality and NLP

- [Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond](https://arxiv.org/abs/2109.00725) — *TACL 2022* · 📈320。NLPにおける因果推論を推定・予測・解釈の観点で統一的に俯瞰した定番サーベイ

### Causality and Recommendation

- [Causal Inference in Recommender Systems: A Survey and Future Directions](https://arxiv.org/abs/2208.12397) — *ACM TOIS 2022* · 📈154。推薦システムへの因果推論応用を3側面の課題分類で俯瞰し将来方向を示したサーベイ

### Counterfactual Explanations

- [Robust Counterfactual Explanations in Machine Learning: A Survey](https://arxiv.org/abs/2402.01928) — *IJCAI 2024* · 📈38。頑健な反実仮想説明(robust CE)の研究を頑健性の形態別に分析したサーベイ

### Treatment Effect Estimation

- [A Survey of Deep Causal Models and Their Industrial Applications](https://arxiv.org/abs/2209.08860) — *arXiv 2022* · 📈20。反実仮想に基づく深層因果モデルと産業応用を時系列・分類軸で整理
- [Causal Inference with Complex Treatments: A Survey](https://arxiv.org/abs/2407.14022) — *arXiv 2024* · 📈6。多値・連続・バンドル等の複雑な処置に対する因果推論手法を整理

## ⏱️ 時系列・時空間

### EEG / Biosignal Deep Learning

- [Deep learning-based electroencephalography analysis: a systematic review](https://arxiv.org/abs/1901.05498) — *Journal of Neural Engineering 2019* · 📈1306。EEGへの深層学習適用156編をてんかん・睡眠・BCI等の応用別に分析した定番の系統的レビュー
- [Deep Learning-Powered Electrical Brain Signals Analysis: Advancing Neurological Diagnostics](https://arxiv.org/abs/2502.17213) — *arXiv 2025* · 📈6。EEG/iEEGの深層学習を7種の神経疾患診断にわたり46データセットで体系化した最新レビュー

### Financial Time Series

- [Deep learning models for price forecasting of financial time series: A review of recent advancements: 2020-2022](https://arxiv.org/abs/2305.04811) — *arXiv 2023* · 📈143。金融時系列の価格予測向け深層学習モデルの最近の進展(2020-2022)を整理したレビュー

### Graph Time Series

- [A Survey on Graph Neural Networks for Time Series: Forecasting, Classification, Imputation, and Anomaly Detection](https://arxiv.org/abs/2307.03759) — *IEEE TPAMI 2024* · 📈455。予測・分類・補完・異常検知の4次元でグラフニューラルネット×時系列(GNN4TS)を俯瞰したサーベイ

### Human Activity Recognition (HAR)

- [Deep Learning for Sensor-based Human Activity Recognition: Overview, Challenges and Opportunities](https://arxiv.org/abs/2001.07416) — *ACM Computing Surveys 2020* · 📈839。センサーベース人間活動認識(HAR)の深層学習手法を課題別の分類体系で整理した定番サーベイ

### Irregular Time Series

- [A Survey on Principles, Models and Methods for Learning from Irregularly Sampled Time Series](https://arxiv.org/abs/2012.00168) — *arXiv 2020* · 📈67。不規則サンプリング時系列からの学習を3つのデータ表現と5つのモデリング基本要素で整理したサーベイ

### Spatio-Temporal Forecasting

- [Spatio-Temporal Graph Neural Networks: A Survey](https://arxiv.org/abs/2301.10569) — *arXiv 2023* · 📈55。時空間グラフニューラルネットの手法・応用・課題を整理したサーベイ

### Time Series Anomaly Detection

- [Dive into Time-Series Anomaly Detection: A Decade Review](https://arxiv.org/abs/2412.20512) — *arXiv 2024* · 📈33。時系列異常検知の10年間の研究をプロセス中心の分類体系で整理しメタ分析したレビュー

### Time Series Clustering

- [Bridging the Gap: A Decade Review of Time-Series Clustering Methods](https://arxiv.org/abs/2412.20582) — *arXiv 2024*。古典手法から深層学習までの時系列クラスタリングを統一的分類体系で俯瞰した10年レビュー

### Time Series Forecasting

- [Time Series Forecasting With Deep Learning: A Survey](https://arxiv.org/abs/2004.13408) — *Phil. Trans. R. Soc. A 2020* · 📈1885。深層学習による時系列予測（1段/多段・確率的予測）を整理した定番サーベイ
- [Transformers in Time Series: A Survey](https://arxiv.org/abs/2202.07125) — *IJCAI 2023* · 📈1452。時系列Transformerを予測・異常検知・分類で整理した定番サーベイ（リスト付） — [`qingsongedu/time-series-transformers-review`](https://github.com/qingsongedu/time-series-transformers-review) ⭐2985🔴
- [A Comprehensive Survey of Deep Learning for Time Series Forecasting: Architectural Diversity and Open Challenges](https://arxiv.org/abs/2411.05793) — *Artificial Intelligence Review 2024* · 📈88。MLP/CNN/RNN/GNN/Transformer/拡散/基盤モデル/Mambaを比較した網羅的サーベイ

### Time Series Foundation Models

- [Foundation Models for Time Series Analysis: A Tutorial and Survey](https://arxiv.org/abs/2403.14735) — *KDD 2024* · 📈390。時系列解析向け基盤モデルの設計・事前学習・応用を解説したKDD24チュートリアル
- [A Survey of Deep Learning and Foundation Models for Time Series Forecasting](https://arxiv.org/abs/2401.13912) — *arXiv 2024* · 📈69。深層学習と基盤モデルによる時系列予測を知識・言語モデルの観点で整理
- [Empowering Time Series Analysis with Foundation Models: A Comprehensive Survey](https://arxiv.org/abs/2405.02358) — *arXiv 2024* · 📈26。他モダリティ事前学習モデルの時系列適応を網羅的に整理したサーベイ

### Time Series Imputation

- [Deep Learning for Multivariate Time Series Imputation: A Survey](https://arxiv.org/abs/2402.04059) — *IJCAI 2024* · 📈126。多変量時系列補完(MTSI)の深層学習手法を予測型/生成型の分類体系で整理したサーベイ

### Time Series Representation Learning

- [Self-Supervised Learning for Time Series Analysis: Taxonomy, Progress, and Prospects](https://arxiv.org/abs/2306.10125) — *IEEE TPAMI 2023* · 📈245。時系列SSLを生成・対照・敵対的に分類し10サブカテゴリで整理したサーベイ — [`qingsongedu/Awesome-SSL4TS`](https://github.com/qingsongedu/Awesome-SSL4TS) ⭐378🔴
- [Universal Time-Series Representation Learning: A Survey](https://arxiv.org/abs/2401.03717) — *ACM Computing Surveys 2024* · 📈45。汎用時系列表現学習の手法を3要素の新分類体系で整理したサーベイ

### Time Series x LLM

- [Large Language Models for Time Series: A Survey](https://arxiv.org/abs/2402.01801) — *IJCAI 2024* · 📈164。LLMを時系列解析に活用する手法(プロンプト・量子化・整列・視覚橋渡し等)を分類したサーベイ — [`xiyuanzh/awesome-llm-time-series`](https://github.com/xiyuanzh/awesome-llm-time-series) ⭐517🔴

### Traffic Forecasting

- [STG4Traffic: A Survey and Benchmark of Spatial-Temporal Graph Neural Networks for Traffic Prediction](https://arxiv.org/abs/2307.00495) — *arXiv 2023* · 📈15。交通予測向け時空間GNNのサーベイ兼ベンチマーク（コンパニオンリスト付） — [`jwwthu/GNN4Traffic`](https://github.com/jwwthu/GNN4Traffic) ⭐1206🔴

## ⛏️ データマイニング

### Anomaly Detection

- [A Unifying Review of Deep and Shallow Anomaly Detection](https://arxiv.org/abs/2009.11732) — *Proceedings of the IEEE 2021* · 📈1026。深層・浅層の異常検知手法を統一的枠組みで整理した定番レビュー
- [Anomaly Detection: A Survey](https://doi.org/10.1145/1541880.1541882) — *ACM Computing Surveys 2009*。異常検知研究の体系を確立した古典的サーベイ(被引用1万超)

### Clustering

- [A Comprehensive Survey on Deep Clustering: Taxonomy, Challenges, and Future Directions](https://arxiv.org/abs/2206.07579) — *ACM Computing Surveys 2024* · 📈203。深層クラスタリングの分類体系と課題・将来方向を整理

### Concept Drift

- [Concept Drift Adaptation in Text Stream Mining Settings: A Systematic Review](https://arxiv.org/abs/2312.02901) — *ACM TIST 2024*。テキストストリームにおける概念ドリフト適応を48文献で整理した体系的レビュー。

### Educational Data Mining

- [Educational data mining and learning analytics: An updated survey](https://arxiv.org/abs/2402.07956) — *WIREs Data Mining and Knowledge Discovery 2024*。教育データマイニングと学習分析の最新動向を2013年版から更新したサーベイ。
- [A Comprehensive Survey on Deep Learning Techniques in Educational Data Mining](https://arxiv.org/abs/2309.04761) — *arXiv 2023*。知識追跡・行動検出・成績予測・推薦の4場面での教育データマイニング深層学習を整理。

### Explainable Anomaly Detection

- [A Survey on Explainable Anomaly Detection](https://arxiv.org/abs/2210.06959) — *ACM TKDD 2022*。説明可能な異常検知手法を分類体系付きで包括的に整理したサーベイ。

### Frequent Pattern Mining

- [A Survey of Parallel Sequential Pattern Mining](https://arxiv.org/abs/1805.10515) — *ACM TKDD 2019* · 📈256。並列系列パターンマイニングの手法とフレームワークを概観

### Graph Anomaly Detection

- [A Comprehensive Survey on Graph Anomaly Detection with Deep Learning](https://arxiv.org/abs/2106.07178) — *IEEE TKDE 2023* · 📈799。グラフ上の深層異常検知をワンストップで整理した包括サーベイ
- [Graph Anomaly Detection in Time Series: A Survey](https://arxiv.org/abs/2302.00058) — *IEEE TPAMI 2023*。時系列に対するグラフベース異常検知(G-TSAD)を包括的に整理したサーベイ。

### Graph Mining

- [A Comprehensive Survey on Graph Neural Networks](https://arxiv.org/abs/1901.00596) — *IEEE TNNLS 2021* · 📈11176。GNNを4分類で体系化した最も引用される定番サーベイ

### Graph Representation Learning

- [A Comprehensive Survey on Deep Graph Representation Learning](https://arxiv.org/abs/2304.05055) — *Neural Networks 2024* · 📈312。深層グラフ表現学習の最新手法を体系的に総覧
- [A Survey on Graph Representation Learning Methods](https://arxiv.org/abs/2204.01855) — *ACM TIST 2024* · 📈225。グラフ表現学習の非GNN/GNN手法を網羅的に整理

### Heterogeneous Information Networks

- [A Survey of Heterogeneous Information Network Analysis](https://arxiv.org/abs/1511.04854) — *IEEE TKDE 2017*。異種情報ネットワーク解析の概念・タスクを体系化

### Imbalanced Data

- [Learning from Class-Imbalanced Data: Review of Methods and Applications](https://doi.org/10.1016/j.eswa.2016.12.035) — *Expert Systems with Applications 2017*。527文献を技術・応用両面から整理した不均衡学習レビュー
- [Learning from Imbalanced Data](https://doi.org/10.1109/TKDE.2008.239) — *IEEE TKDE 2009*。不均衡データ学習の基礎を確立した古典的サーベイ

### LLM and Graphs

- [Large Language Models on Graphs: A Comprehensive Survey](https://arxiv.org/abs/2312.02783) — *IEEE TKDE 2024* · 📈297。グラフデータへのLLM適用シナリオを網羅的に整理 — [`PeterGriffinJin/Awesome-Language-Model-on-Graphs`](https://github.com/PeterGriffinJin/Awesome-Language-Model-on-Graphs) ⭐991🟡

### Outlier Detection

- [A Survey on Unsupervised Outlier Detection in High-Dimensional Numerical Data](https://doi.org/10.1002/sam.11161) — *Statistical Analysis and Data Mining 2012*。高次元データの教師なし外れ値検出を部分空間視点で整理した定番サーベイ

### Process Mining

- [Advances in Process Optimization: A Comprehensive Survey of Process Mining, Predictive Process Monitoring, and Process-Aware Recommender Systems](https://arxiv.org/abs/2301.10398) — *arXiv 2023*。プロセスマイニング・予測的プロセス監視・プロセス対応推薦を包括的に整理したサーベイ。
- [Deep Learning for Predictive Business Process Monitoring: Review and Benchmark](https://arxiv.org/abs/2009.13251) — *IEEE TSC 2020*。予測的ビジネスプロセス監視の深層学習10手法を12ログで比較したレビュー兼ベンチマーク。

### Social Mining

- [Influence Maximization in Social Networks: A Survey](https://arxiv.org/abs/2309.04668) — *arXiv 2023*。ソーシャルネットワークにおける影響最大化問題の拡散モデルとアルゴリズムを整理したサーベイ。
- [Automatic Rumor Detection on Microblogs: A Survey](https://arxiv.org/abs/1807.03505) — *arXiv 2018*。マイクロブログ上の自動デマ検出を特徴量・伝播・ニューラルの3系統で整理したサーベイ。

### Spatiotemporal Data Mining

- [Spatiotemporal Data Mining: A Survey](https://arxiv.org/abs/2206.12753) — *arXiv 2022*。時空間データマイニング手法を6つの出力パターン族と並列定式化で整理したサーベイ。

### Stream Mining

- [A Survey on Concept Drift Adaptation](https://doi.org/10.1145/2523813) — *ACM Computing Surveys 2014*。ストリーム学習における概念ドリフト適応の定番サーベイ

### Text Mining

- [A Brief Survey of Text Mining: Classification, Clustering and Extraction Techniques](https://arxiv.org/abs/1707.02919) — *arXiv 2017*。テキストマイニングの分類・クラスタリング・抽出技術を概観したサーベイ。

### Time Series Anomaly Detection

- [Deep Learning for Time Series Anomaly Detection: A Survey](https://arxiv.org/abs/2211.05244) — *ACM Computing Surveys 2024* · 📈560。時系列異常検知の深層モデルを体系的に分類した近年の包括サーベイ

### Time Series Mining

- [Deep Learning for Time Series Classification: A Review](https://arxiv.org/abs/1809.04356) — *Data Mining and Knowledge Discovery 2019* · 📈3243。時系列分類の深層アーキテクチャを大規模実証評価した定番レビュー
- [Deep Learning for Time Series Classification and Extrinsic Regression: A Current Survey](https://arxiv.org/abs/2302.02515) — *ACM Computing Surveys 2024* · 📈270。時系列分類・回帰の深層手法を最新状況まで整理

## 🗄️ データベース・データ管理

### Approximate Nearest Neighbor Search

- [A Comprehensive Survey and Experimental Comparison of Graph-Based Approximate Nearest Neighbor Search](https://arxiv.org/abs/2101.12631) — *PVLDB 2021* · 📈360。13のグラフベースANNS手法を統一分類・実験比較した定番サーベイ — [`Lsyhprum/WEAVESS`](https://github.com/Lsyhprum/WEAVESS) ⭐80🔴

### Cardinality Estimation

- [Are We Ready For Learned Cardinality Estimation?](https://arxiv.org/abs/2012.06743) — *VLDB 2021*。学習型カーディナリティ推定5手法と従来8手法を比較した実験的サーベイ。

### Cloud and Serverless

- [The Serverless Computing Survey: A Technical Primer for Design Architecture](https://arxiv.org/abs/2112.12921) — *ACM Computing Surveys 2022* · 📈197。サーバレス計算の設計アーキテクチャを技術的に総覧したサーベイ

### Data Cleaning

- [Data Cleaning: Overview and Emerging Challenges](https://doi.org/10.1145/2882903.2912574) — *SIGMOD 2016*。データクリーニングの分類体系と統計的推定枠組みを提示した定番チュートリアル

### Data Lake

- [Data Lakes: A Survey of Functions and Systems](https://arxiv.org/abs/2106.09592) — *IEEE TKDE 2021*。データレイクの発展・アーキテクチャ・システムを整理したサーベイ。

### Data Pricing

- [A Survey on Data Pricing: from Economics to Data Science](https://arxiv.org/abs/2009.04462) — *IEEE TKDE 2022* · 📈172。経済学からデータサイエンスまでデータ価格付けを横断的に整理

### Entity Matching

- [Neural Networks for Entity Matching: A Survey](https://arxiv.org/abs/2010.11075) — *ACM TKDD 2021*。ニューラルネットワークによるエンティティマッチング手法を工程別に整理したサーベイ。

### Entity Resolution

- [End-to-End Entity Resolution for Big Data: A Survey](https://arxiv.org/abs/1905.06397) — *ACM Computing Surveys 2021* · 📈67。ブロッキングからマッチングまでER全工程を網羅した定番サーベイ

### Learned Index

- [A Survey of Learned Indexes for the Multi-dimensional Space](https://arxiv.org/abs/2403.06456) — *arXiv 2024* · 📈24。多次元空間向け学習型インデックスを分類整理したサーベイ
- [How Good Are Multi-dimensional Learned Indices? An Experimental Survey](https://arxiv.org/abs/2405.05536) — *arXiv 2024*。6種の多次元学習型索引を統一環境で比較評価した実験的サーベイ。

### ML for Query Optimization

- [A Survey on Advancing the DBMS Query Optimizer: Cardinality, Cost Model, and Plan Enumeration](https://arxiv.org/abs/2101.01507) — *Data Science and Engineering 2021* · 📈115。学習型のカーディナリティ推定・コストモデル・プラン列挙を概観

### Text-to-SQL

- [Next-Generation Database Interfaces: A Survey of LLM-based Text-to-SQL](https://arxiv.org/abs/2406.08426) — *arXiv 2024*。LLMベースのText-to-SQL研究を包括的にレビューしたサーベイ。
- [A Survey on Text-to-SQL Parsing: Concepts, Methods, and Future Directions](https://arxiv.org/abs/2208.13629) — *arXiv 2022*。深層学習によるText-to-SQL構文解析の概念・手法・将来方向を整理したサーベイ。
- [Deep Learning Driven Natural Languages Text to SQL Query Conversion: A Survey](https://arxiv.org/abs/2208.04415) — *arXiv 2022*。24のニューラルモデルと11データセットを整理したText-to-SQLサーベイ。

### Time Series Database

- [Time Series Management Systems: A Survey](https://arxiv.org/abs/1710.01077) — *IEEE TKDE 2017*。時系列管理システム(TSMS)の保存・問い合わせ・ストリーム処理機能を分類した総覧。

### Vector Database

- [Survey of Vector Database Management Systems](https://arxiv.org/abs/2310.14021) — *The VLDB Journal 2024* · 📈173。20超の商用ベクトルDBの記憶・索引戦略を整理した包括サーベイ
- [A Comprehensive Survey on Vector Database: Storage and Retrieval Technique, Challenge](https://arxiv.org/abs/2310.11703) — *arXiv 2023*。ベクトルDBの保存・検索技術と課題を体系的にまとめたサーベイ。

## 🔍 情報検索 (IR)

### Conversational Search

- [Conversational Information Seeking](https://arxiv.org/abs/2201.08808) — *Foundations and Trends in Information Retrieval 2023* · 📈128。対話的情報探索の定義・設計・評価を網羅した包括的モノグラフ
- [A Survey of Conversational Search](https://arxiv.org/abs/2410.15576) — *ACM TOIS 2025* · 📈44。クエリ再定式化・明確化・検索・応答生成と LLM 統合を網羅した会話検索サーベイ

### Cross-Lingual IR

- [Bridging Language Gaps: Advances in Cross-Lingual Information Retrieval with Multilingual LLMs](https://arxiv.org/abs/2510.00908) — *arXiv 2025*。翻訳ベースから埋め込み・生成型まで多言語LLMによるクロスリンガルIRを概観したサーベイ。

### Cross-modal Retrieval

- [A Comprehensive Survey on Cross-modal Retrieval](https://arxiv.org/abs/1607.06215) — *arXiv 2016*。クロスモーダル検索を実数値表現学習と二値表現学習に分けて整理したサーベイ。

### Dense Retrieval

- [Dense Text Retrieval based on Pretrained Language Models: A Survey](https://arxiv.org/abs/2211.14876) — *ACM TOIS 2024* · 📈304。アーキテクチャ・学習・索引・統合の4軸でdense retrievalを整理 — [`RUCAIBox/DenseRetrieval`](https://github.com/RUCAIBox/DenseRetrieval) ⭐221🔴

### Explainable IR

- [Explainable Information Retrieval: A Survey](https://arxiv.org/abs/2211.02405) — *arXiv 2022*。説明可能な情報検索手法を統一的枠組みで分類・整理したサーベイ。

### Generative Retrieval

- [A Survey of Generative Information Retrieval](https://arxiv.org/abs/2406.01197) — *ACM TOIS 2025* · 📈5。クエリからDocIDを直接生成する生成型検索を体系的に整理 — [`RUC-NLPIR/GenIR-Survey`](https://github.com/RUC-NLPIR/GenIR-Survey) ⭐207🟡

### Learning to Rank

- [Learning to Rank for Information Retrieval](https://doi.org/10.1561/1500000016) — *Foundations and Trends in Information Retrieval 2009*。pointwise/pairwise/listwiseを整理したランキング学習の定番教科書的サーベイ

### Neural IR

- [Pre-training Methods in Information Retrieval](https://arxiv.org/abs/2111.13853) — *Foundations and Trends in Information Retrieval 2022* · 📈11。IR各コンポーネントへの事前学習手法適用を体系的に整理
- [An Introduction to Neural Information Retrieval](https://doi.org/10.1561/1500000061) — *Foundations and Trends in Information Retrieval 2018*。ニューラルIRの基礎を古典手法と対比して解説した入門サーベイ

### Neural IR Architectures

- [A Survey of Model Architectures in Information Retrieval](https://arxiv.org/abs/2502.14822) — *arXiv 2025*。情報検索におけるモデルアーキテクチャの進化を密/疎/BM25を統一的観点で整理したサーベイ。

### Neural Ranking

- [Pretrained Transformers for Text Ranking: BERT and Beyond](https://arxiv.org/abs/2010.06467) — *Synthesis Lectures (Morgan & Claypool) 2021* · 📈750。BERT系トランスフォーマによるテキストランキングを網羅した定番サーベイ

### RAG and Retrieval

- [Retrieval-Augmented Generation for Large Language Models: A Survey](https://arxiv.org/abs/2312.10997) — *arXiv 2024* · 📈3410。Naive/Advanced/Modular RAGの発展と検索・生成・拡張を網羅した定番サーベイ — [`Tongji-KGLLM/RAG-Survey`](https://github.com/Tongji-KGLLM/RAG-Survey) ⭐2133🔴
- [A Survey on Retrieval-Augmented Text Generation](https://arxiv.org/abs/2202.01110) — *arXiv 2022* · 📈283。対話・翻訳など各タスクの検索拡張生成を整理した先駆的サーベイ

## 🛒 推薦システム

### AutoML Recommendation

- [AutoML for Deep Recommender Systems: A Survey](https://arxiv.org/abs/2203.13922) — *ACM TOIS 2023* · 📈98。深層推薦へのAutoML適用(特徴選択・埋め込み・アーキ探索)を整理

### Bias and Fairness

- [Bias and Debias in Recommender System: A Survey and Future Directions](https://arxiv.org/abs/2010.03240) — *ACM TOIS 2023* · 📈901。推薦の7種バイアスと除去手法を体系化した定番サーベイ — [`jiawei-chen/RecDebiasing`](https://github.com/jiawei-chen/RecDebiasing) ⭐462🔴
- [A Survey on the Fairness of Recommender Systems](https://arxiv.org/abs/2206.03761) — *ACM TOIS 2023* · 📈434。推薦の公平性定義と手法を多視点で分類整理

### CTR Prediction

- [Deep Learning for Click-Through Rate Estimation](https://arxiv.org/abs/2104.10584) — *IJCAI 2021* · 📈133。CTR予測の浅層から深層への発展と特徴交互作用を整理

### Cold-Start

- [Cold-Start Recommendation towards the Era of Large Language Models (LLMs): A Comprehensive Survey and Roadmap](https://arxiv.org/abs/2501.01945) — *arXiv 2025* · 📈58。LLM時代のコールドスタート推薦を包括整理した最新サーベイ — [`YuanchenBei/Awesome-Cold-Start-Recommendation`](https://github.com/YuanchenBei/Awesome-Cold-Start-Recommendation) ⭐283🟢

### Conversational Recommendation

- [Advances and Challenges in Conversational Recommender Systems: A Survey](https://arxiv.org/abs/2101.09459) — *AI Open 2021* · 📈357。会話型推薦システムの進展と課題を体系的に整理した定番サーベイ

### Cross-Domain Recommendation

- [Cross-Domain Recommendation: Challenges, Progress, and Prospects](https://arxiv.org/abs/2103.01696) — *IJCAI 2021* · 📈294。データ疎性を緩和するクロスドメイン推薦の課題と進展を整理

### Deep Learning Recommendation

- [Deep Learning based Recommender System: A Survey and New Perspectives](https://arxiv.org/abs/1707.07435) — *ACM Computing Surveys 2019* · 📈1293。深層推薦100本超を分類した最も引用される定番サーベイ

### Explainable Recommendation

- [Explainable Recommendation: A Survey and New Perspectives](https://arxiv.org/abs/1804.11192) — *Foundations and Trends in Information Retrieval 2020* · 📈1121。説明可能推薦を時系列・2次元分類体系で整理した定番サーベイ

### Foundation Models Recommendation

- [Foundation Models for Recommender Systems: A Survey and New Perspectives](https://arxiv.org/abs/2402.11143) — *arXiv 2024* · 📈17。推薦における基盤モデル(FM4RecSys)の活用を体系的に整理

### Generative Recommendation

- [A Survey on Generative Recommendation: Data, Model, and Tasks](https://arxiv.org/abs/2510.27157) — *arXiv preprint 2025* · 📈12。生成推薦をデータ・モデル・タスクの観点で分類し、LLM/拡散/大規模推薦モデルを俯瞰したサーベイ。

### Graph-based Recommendation

- [Graph Neural Networks in Recommender Systems: A Survey](https://arxiv.org/abs/2011.02260) — *ACM Computing Surveys 2022* · 📈1768。GNNベース推薦を情報種別とタスクで分類した定番サーベイ — [`wusw14/GNN-in-RS`](https://github.com/wusw14/GNN-in-RS) ⭐307🔴
- [Graph Learning based Recommender Systems: A Review](https://arxiv.org/abs/2105.06339) — *IJCAI 2021* · 📈241。グラフ学習ベース推薦を初めて体系的に整理したレビュー

### LLM Agents for Recommendation

- [A Survey on LLM-powered Agents for Recommender Systems](https://arxiv.org/abs/2502.10050) — *arXiv preprint 2025* · 📈46。推薦システム向けLLMエージェントを推薦指向/対話指向/シミュレーション指向に分けて整理したサーベイ。

### LLM and Recommendation

- [A Survey on Large Language Models for Recommendation](https://arxiv.org/abs/2305.19860) — *World Wide Web Journal 2024* · 📈832。LLMベース推薦のパラダイムを分類した代表的サーベイ

### Multimodal Recommendation

- [Multimodal Recommender Systems: A Survey](https://arxiv.org/abs/2302.03883) — *ACM Computing Surveys 2024* · 📈161。マルチモーダル推薦を符号化・交互作用・強化・最適化で整理
- [A Comprehensive Survey on Multimodal Recommender Systems: Taxonomy, Evaluation, and Future Directions](https://arxiv.org/abs/2302.04473) — *arXiv 2023* · 📈63。マルチモーダル推薦の分類体系と評価・将来方向を網羅

### Reinforcement Learning Recommendation

- [A Survey of Deep Reinforcement Learning in Recommender Systems](https://arxiv.org/abs/2109.03540) — *arXiv 2021* · 📈74。推薦における深層強化学習の動向を体系的にレビュー

### Self-Supervised Recommendation

- [Self-Supervised Learning for Recommender Systems: A Survey](https://arxiv.org/abs/2203.15876) — *IEEE TKDE 2024* · 📈421。自己教師あり推薦を対照/生成/予測/混合に分類した定番サーベイ — [`Coder-Yu/SELFRec`](https://github.com/Coder-Yu/SELFRec) ⭐642🟡

### Sequential Recommendation

- [Sequential Recommender Systems: Challenges, Progress and Prospects](https://arxiv.org/abs/2001.04830) — *IJCAI 2019* · 📈499。系列推薦の課題と進展を体系化したIJCAIサーベイトラック論文
- [Deep Learning for Sequential Recommendation: Algorithms, Influential Factors, and Evaluations](https://arxiv.org/abs/1905.01997) — *ACM TOIS 2020* · 📈47。系列推薦の深層手法を行動系列タイプ別に整理し評価

## 🌐 Web・ソーシャル

### Bot Detection

- [Social Media Bot Detection Research: Review of Literature](https://arxiv.org/abs/2503.22838) — *arXiv 2025*。ソーシャルメディアのボット検出研究の手法と課題を文献レビューで整理

### Computational Social Science

- [Data-driven Computational Social Science: A Survey](https://arxiv.org/abs/2008.12372) — *Big Data Research 2021* · 📈66。個人・関係・集団の3視点で計算社会科学の人間ダイナミクス研究を整理

### Fake News Detection

- [Fake News Detection on Social Media: A Data Mining Perspective](https://arxiv.org/abs/1708.01967) — *ACM SIGKDD Explorations 2017* · 📈3243。データマイニング視点でフェイクニュース検出を整理した高被引用サーベイ

### Graph-based Fake News Detection

- [Fake News Detection Through Graph-based Neural Networks: A Survey](https://arxiv.org/abs/2307.12639) — *arXiv 2023*。グラフベースのフェイクニュース検出手法を知識・伝播・社会文脈の3分類で整理

### Hate Speech Detection

- [A Survey on Automatic Online Hate Speech Detection in Low-Resource Languages](https://arxiv.org/abs/2411.19017) — *arXiv 2024*。低資源言語のオンラインヘイトスピーチ検出のデータ・特徴・手法を概観したサーベイ
- [Towards generalisable hate speech detection: a review on obstacles and solutions](https://arxiv.org/abs/2102.08886) — *PeerJ Computer Science 2021*。ヘイトスピーチ検出モデルの汎化性の障壁と解決策を整理したレビュー

### Link Prediction

- [A Survey of Link Prediction Algorithms](https://arxiv.org/abs/2306.12970) — *arXiv 2023*。局所類似度・ランダムウォーク・埋め込みなどリンク予測アルゴリズムを比較したサーベイ

### Misinformation Detection

- [Combating Misinformation in the Age of LLMs: Opportunities and Challenges](https://arxiv.org/abs/2311.05656) — *AI Magazine 2024* · 📈201。LLM時代の誤情報生成・検出の機会と課題を整理したサーベイ — [`llm-misinformation/llm-misinformation-survey`](https://github.com/llm-misinformation/llm-misinformation-survey) ⭐106🔴

### Recommendation Fairness

- [A Survey on Fairness-aware Recommender Systems](https://arxiv.org/abs/2306.00403) — *Information Fusion 2023*。公平性配慮型推薦システムをシナリオ別に分類し信頼性原則と結びつけたサーベイ
- [Fairness and Diversity in Recommender Systems: A Survey](https://arxiv.org/abs/2307.04644) — *ACM TIST 2023*。推薦における公平性と多様性の関係を統合的に整理したサーベイ

### Social Network Analysis

- [A Comprehensive Survey on Community Detection with Deep Learning](https://arxiv.org/abs/2105.12584) — *IEEE TNNLS 2024* · 📈439。コミュニティ検出の深層手法を分類体系で整理した包括サーベイ

## 🛡️ 信頼できるAI (公平性・XAI・安全性)

### AI Content Watermarking / Detection

- [Watermarking for AI Content Detection: A Review on Text, Visual, and Audio Modalities](https://arxiv.org/abs/2504.03765) — *ICLR 2025 Workshop (GenAI Watermarking) 2025* · 📈6。テキスト・画像・音声を横断したAI生成コンテンツの透かし検出技術を初めて体系的に整理したレビュー。

### AI Fairness / Bias

- [The Frontiers of Fairness in Machine Learning](https://arxiv.org/abs/1810.08810) — *arXiv 2018* · 📈436。ML公平性の未解決問題と研究フロンティアを整理した展望論文
- [Bias Mitigation for Machine Learning Classifiers: A Comprehensive Survey](https://arxiv.org/abs/2207.07068) — *ACM JRC 2022* · 📈275。分類器のバイアス緩和手法341本を網羅した包括的サーベイ

### AI Governance / Ethics

- [Worldwide AI Ethics: a review of 200 guidelines and recommendations for AI governance](https://arxiv.org/abs/2206.11922) — *Patterns 2022* · 📈244。世界の200のAI倫理ガイドラインをメタ分析した大規模レビュー

### AI Safety

- [Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565) — *arXiv 2016* · 📈3140。AI安全性の具体的課題を提起した分野定義的論文

### AI-Generated Text Detection

- [Towards Possibilities & Impossibilities of AI-generated Text Detection: A Survey](https://arxiv.org/abs/2310.15264) — *arXiv preprint 2023* · 📈55。AI生成テキスト検出の可能性と限界を理論・実証両面から論じたサーベイ。

### AI-Generated Text Forensics

- [A Survey of AI-generated Text Forensic Systems: Detection, Attribution, and Characterization](https://arxiv.org/abs/2403.01152) — *arXiv preprint 2024* · 📈28。AI生成テキストの検出・帰属・特徴づけを扱うフォレンジック系手法を網羅したサーベイ。

### Adversarial Robustness

- [Adversarial Examples: Attacks and Defenses for Deep Learning](https://arxiv.org/abs/1712.07107) — *IEEE TNNLS 2017* · 📈1806。深層学習に対する敵対的サンプル攻撃と防御の定番サーベイ
- [Adversarial Attacks and Defenses in Images, Graphs and Text: A Review](https://arxiv.org/abs/1909.08072) — *IJAC 2019* · 📈751。画像・グラフ・テキストの敵対的攻撃と防御を横断レビュー

### Backdoor Attacks

- [Backdoor Learning: A Survey](https://arxiv.org/abs/2007.08745) — *IEEE TNNLS 2020* · 📈822。バックドア学習攻撃と防御を統一的に整理したサーベイ
- [Backdoor Attacks and Countermeasures on Deep Learning: A Comprehensive Review](https://arxiv.org/abs/2007.10760) — *arXiv 2020* · 📈282。深層学習へのバックドア攻撃と対策を包括的にレビュー

### Data Poisoning Security

- [Wild Patterns Reloaded: A Survey of Machine Learning Security against Training Data Poisoning](https://arxiv.org/abs/2205.01992) — *ACM Computing Surveys 2022* · 📈198。学習データポイズニング攻撃と防御を15年分100本超で体系化

### Deepfake Detection

- [DeepFakes and Beyond: A Survey of Face Manipulation and Fake Detection](https://arxiv.org/abs/2001.00179) — *Information Fusion 2020* · 📈1075。顔操作とディープフェイク検出を網羅した定番サーベイ
- [The Creation and Detection of Deepfakes: A Survey](https://arxiv.org/abs/2004.11138) — *ACM Computing Surveys 2020* · 📈848。ディープフェイクの生成と検出を技術的に整理したサーベイ

### Differential Privacy

- [Differential Privacy and Machine Learning: a Survey and Review](https://arxiv.org/abs/1412.7584) — *arXiv 2014* · 📈291。差分プライバシーと機械学習の交点を概観した初期サーベイ

### Explainable AI (XAI)

- [A Survey on the Explainability of Supervised Machine Learning](https://arxiv.org/abs/2011.07876) — *JAIR 2021* · 📈955。教師あり学習の説明可能性手法を概観したサーベイ
- [Opportunities and Challenges in Explainable Artificial Intelligence (XAI): A Survey](https://arxiv.org/abs/2006.11371) — *arXiv 2020* · 📈749。XAIの機会と課題を体系的に整理した概観サーベイ
- [One Explanation Does Not Fit All: A Toolkit and Taxonomy of AI Explainability Techniques](https://arxiv.org/abs/1909.03012) — *arXiv 2019* · 📈466。AI説明技術のタクソノミーとツールキット(AIX360)を提示
- [Counterfactual Explanations and Algorithmic Recourses for Machine Learning: A Review](https://arxiv.org/abs/2010.10596) — *ACM Computing Surveys 2020* · 📈297。反実仮想説明とアルゴリズム的救済の手法をレビュー

### LLM Red Teaming

- [Building Safe GenAI Applications: An End-to-End Overview of Red Teaming for Large Language Models](https://arxiv.org/abs/2503.01742) — *arXiv preprint 2025* · 📈13。LLMのレッドチーミングをエンドツーエンドのシステム視点で整理した実務的概観。

### Machine Unlearning

- [Machine Unlearning: A Comprehensive Survey](https://arxiv.org/abs/2405.07406) — *arXiv preprint 2024* · 📈51。中央集権/分散/検証/プライバシの4シナリオで機械アンラーニングを整理した包括サーベイ。

### Machine Unlearning (GenAI)

- [Machine Unlearning in Generative AI: A Survey](https://arxiv.org/abs/2407.20516) — *arXiv preprint 2024* · 📈53。生成AIから著作権・個人情報等の望ましくない知識を消去するアンラーニング手法のサーベイ。 — [`franciscoliu/Awesome-GenAI-Unlearning`](https://github.com/franciscoliu/Awesome-GenAI-Unlearning) ⭐188🟢

### Machine-Generated Text Detection

- [Are AI Detectors Good Enough? A Survey on Quality of Datasets With Machine-Generated Texts](https://arxiv.org/abs/2410.14677) — *arXiv preprint 2024* · 📈20。機械生成テキスト検出用データセットの品質評価に焦点を当てたサーベイ。

### Membership Inference

- [Membership Inference Attacks on Machine Learning: A Survey](https://arxiv.org/abs/2103.07853) — *ACM Computing Surveys 2021* · 📈681。メンバーシップ推論攻撃と防御を初めて包括的に分類したサーベイ

### Model Interpretability

- [Towards A Rigorous Science of Interpretable Machine Learning](https://arxiv.org/abs/1702.08608) — *arXiv 2017* · 📈5099。解釈可能MLの定義と評価枠組みを提起した影響力の高い論文
- [Interpretable Machine Learning: Fundamental Principles and 10 Grand Challenges](https://arxiv.org/abs/2103.11251) — *Statistics Surveys 2021* · 📈947。解釈可能MLの基本原則と10の重要課題を提示した必読サーベイ

### Privacy-Preserving ML

- [A Survey of Privacy Attacks in Machine Learning](https://arxiv.org/abs/2007.07646) — *ACM Computing Surveys 2020* · 📈328。MLに対するプライバシー攻撃を網羅的に分類したサーベイ
- [Privacy-Preserving Machine Learning: Methods, Challenges and Directions](https://arxiv.org/abs/2108.04417) — *arXiv 2021* · 📈163。プライバシー保護MLの手法・課題・研究ロードマップを整理

### Red Teaming for Generative Models

- [Against The Achilles' Heel: A Survey on Red Teaming for Generative Models](https://arxiv.org/abs/2404.00629) — *arXiv preprint 2024* · 📈59。生成モデルへの攻撃手法と防御を含むレッドチーミングの包括サーベイ。

### XAI Evaluation

- [From Anecdotal Evidence to Quantitative Evaluation Methods: A Systematic Review on Evaluating Explainable AI](https://arxiv.org/abs/2201.08164) — *ACM Computing Surveys 2022* · 📈674。XAI評価の12特性を提案し300本超の評価実践を系統レビュー

## 📡 連合学習

### Asynchronous FL

- [Asynchronous Federated Learning on Heterogeneous Devices: A Survey](https://arxiv.org/abs/2109.04269) — *arXiv 2021* · 📈377。異種デバイス上の非同期連合学習(AFL)の変種をデバイス/データ異種性・プライバシ等で分類したサーベイ

### Communication Efficiency

- [Federated Learning: Strategies for Improving Communication Efficiency](https://arxiv.org/abs/1610.05492) — *NeurIPS Workshop 2016* · 📈5409。連合学習の通信効率改善手法を提案した基礎論文

### Decentralized FL

- [A Survey on Decentralized Federated Learning](https://arxiv.org/abs/2308.04604) — *arXiv 2023* · 📈46。分散型連合学習(DFL)を従来型分散FLとブロックチェーン型FLの2系統で系統的に整理したサーベイ

### Decentralized Learning

- [Decentralized Deep Learning for Multi-Access Edge Computing: A Survey on Communication Efficiency and Trustworthiness](https://arxiv.org/abs/2108.03980) — *IEEE TAI 2021* · 📈55。エッジ向け分散深層学習(連合/swarm学習)を通信効率と信頼性の観点で俯瞰したサーベイ

### FL Fairness

- [A Survey on Group Fairness in Federated Learning: Challenges, Taxonomy of Solutions and Directions for Future Research](https://arxiv.org/abs/2410.03855) — *arXiv 2024* · 📈7。連合学習における群公平性の課題と解法を分割方法・戦略の軸で分類したサーベイ

### FL Generalization/Robustness/Fairness

- [Federated Learning for Generalization, Robustness, Fairness: A Survey and Benchmark](https://arxiv.org/abs/2311.06750) — *IEEE TPAMI 2023* · 📈223。連合学習の汎化・頑健性・公平性の3軸を背景・課題・手法とベンチマークで横断的に整理したサーベイ

### FL Incentive Mechanisms

- [A Comprehensive Survey of Incentive Mechanism for Federated Learning](https://arxiv.org/abs/2106.15406) — *arXiv 2021* · 📈128。連合学習のインセンティブ機構をStackelbergゲーム・オークション・契約理論・Shapley値等で分類したサーベイ

### FL x Graph

- [Federated Graph Machine Learning: A Survey of Concepts, Techniques, and Applications](https://arxiv.org/abs/2207.11812) — *SIGKDD Explorations 2022* · 📈68。連合グラフ機械学習(FGML)を構造化データのFLと構造化FLの2設定で分類したサーベイ

### FL x LLM

- [Federated Large Language Models: Current Progress and Future Directions](https://arxiv.org/abs/2409.15723) — *arXiv 2024* · 📈31。連合LLM(FedLLM)のファインチューニングとプロンプト学習の進展と課題を俯瞰したサーベイ
- [A Survey on Federated Fine-tuning of Large Language Models](https://arxiv.org/abs/2503.12016) — *arXiv 2025* · 📈29。連合学習によるLLMファインチューニング(FedLLM)を体系的に俯瞰したサーベイ

### FL x Medical

- [Federated Learning for Medical Image Analysis: A Survey](https://arxiv.org/abs/2306.05980) — *Pattern Recognition 2024* · 📈398。医療画像解析における連合学習手法をクライアント側・サーバ側・通信技術の観点で整理したサーベイ

### Federated Learning (General)

- [Advances and Open Problems in Federated Learning](https://arxiv.org/abs/1912.04977) — *FnT in ML 2019* · 📈8614。連合学習の進展と未解決問題を網羅した最も引用される定番
- [Federated Learning: Challenges, Methods, and Future Directions](https://arxiv.org/abs/1908.07873) — *IEEE Signal Processing Magazine 2019* · 📈5953。連合学習の課題・手法・将来方向を整理した高被引用サーベイ

### Heterogeneous FL

- [Federated Learning on Non-IID Data: A Survey](https://arxiv.org/abs/2106.06843) — *Neurocomputing 2021* · 📈1270。non-IIDデータ下の連合学習の課題と手法を整理したサーベイ
- [A Survey on Heterogeneous Federated Learning](https://arxiv.org/abs/2210.04505) — *arXiv 2022* · 📈88。データ・統計・システムの異種性に着目した連合学習サーベイ
- [Non-IID data in Federated Learning: A Survey with Taxonomy, Metrics, Methods, Frameworks and Future Directions](https://arxiv.org/abs/2411.12377) — *arXiv 2024* · 📈22。non-IIDデータのタクソノミー・指標・手法を網羅した近年のサーベイ

### Personalization (FL)

- [Towards Personalized Federated Learning](https://arxiv.org/abs/2103.00710) — *IEEE TNNLS 2021* · 📈1243。パーソナライズド連合学習の手法を分類したサーベイ

### Privacy / Security (FL)

- [Threats to Federated Learning: A Survey](https://arxiv.org/abs/2003.02133) — *arXiv 2020* · 📈540。連合学習に対する脅威(攻撃・防御)を体系化したサーベイ

### Vertical Federated Learning

- [A Survey on Vertical Federated Learning: From a Layered Perspective](https://arxiv.org/abs/2304.01829) — *arXiv 2023* · 📈44。垂直連合学習(VFL)をハードウェア層からシステム層まで階層的視点で体系化したサーベイ

## 🖐️ HCI・ヒューマンAI

### AI Trust and Reliance

- [A Survey of AI Reliance](https://arxiv.org/abs/2408.03948) — *arXiv 2024*。AIへの依存(reliance)行動に関する研究を整理し概念枠組みを与えたサーベイ
- [Trust, distrust, and appropriate reliance in (X)AI: a survey of empirical evaluation of user trust](https://arxiv.org/abs/2312.02034) — *arXiv 2023*。XAIがユーザ信頼に与える影響の実証評価を整理し分類学を提示したサーベイ

### AI Writing Assistance

- [Co-Writing with AI, on Human Terms: Aligning Research with User Demands Across the Writing Process](https://arxiv.org/abs/2504.12488) — *arXiv 2025*。執筆プロセス全体でのAI共同執筆研究をユーザ要求と対応づけて整理したレビュー
- [The Value, Benefits, and Concerns of Generative AI-Powered Assistance in Writing](https://arxiv.org/abs/2403.12004) — *CHI 2024*。生成AIライティング支援の価値・便益・懸念を実験的に検証した研究

### AI-Assisted Decision Making

- [Towards a Science of Human-AI Decision Making: A Survey of Empirical Studies](https://arxiv.org/abs/2112.11471) — *arXiv 2021* · 📈235。AI支援意思決定の実証研究100本超を設計軸で整理したサーベイ

### Conversational UI

- [How should my chatbot interact? A survey on human-chatbot interaction design](https://arxiv.org/abs/1904.02743) — *International Journal of Human-Computer Interaction 2019*。チャットボットの社会的特性に着目した会話型UI設計の課題と戦略を整理したサーベイ

### Crowdsourcing (HCOMP)

- [Quality Control in Crowdsourcing: A Survey of Quality Attributes, Assessment Techniques and Assurance Actions](https://arxiv.org/abs/1801.02546) — *ACM Computing Surveys 2018* · 📈194。クラウドソーシングの品質管理を属性・評価・保証で体系化

### Explainability & HCI

- [Human-Centered Explainable AI (XAI): From Algorithms to User Experiences](https://arxiv.org/abs/2110.10790) — *arXiv 2021* · 📈325。人間中心XAIをアルゴリズムからUXまで概観した書籍章サーベイ
- [Towards Human-centered Explainable AI: A Survey of User Studies for Model Explanations](https://arxiv.org/abs/2210.11584) — *IEEE TPAMI 2022* · 📈219。XAIのユーザ研究97本を信頼・理解・協調の観点で系統レビュー

### Explainable AI and Users

- [Towards Human-centered Design of Explainable Artificial Intelligence (XAI): A Survey of Empirical Studies](https://arxiv.org/abs/2410.21183) — *arXiv 2024*。人間中心XAI設計に関する実証研究を整理したサーベイ

### Human-AI Interaction

- [A Survey on Human-AI Collaboration with Large Foundation Models](https://arxiv.org/abs/2403.04931) — *arXiv 2024* · 📈14。基盤モデル時代の人間-AI協調を設計・倫理・応用で概観

### Human-AI Teaming

- [Advancing Human-Machine Teaming: Concepts, Challenges, and Applications](https://arxiv.org/abs/2503.16518) — *arXiv 2025*。ヒューマンマシンチーミングの分類学と信頼較正・チーム認知等を体系化したサーベイ

### Human-in-the-loop

- [A Survey of Human-in-the-loop for Machine Learning](https://arxiv.org/abs/2108.00941) — *Future Generation Computer Systems 2021* · 📈749。human-in-the-loop機械学習をデータ視点で整理したサーベイ

### Visualization for ML

- [A Survey of Visual Analytics Techniques for Machine Learning](https://arxiv.org/abs/2008.09632) — *Computational Visual Media 2020* · 📈272。機械学習向けビジュアルアナリティクス259本を分類したサーベイ

## 🧬 進化計算

### Black-box Optimization

- [A Tutorial on Bayesian Optimization](https://arxiv.org/abs/1807.02811) — *arXiv 2018* · 📈2332。ベイズ最適化(ブラックボックス最適化)の定番チュートリアル

### Evolutionary Deep Learning

- [Survey on Evolutionary Deep Learning: Principles, Algorithms, Applications and Open Issues](https://arxiv.org/abs/2208.10658) — *ACM Computing Surveys 2022* · 📈114。進化計算による深層学習設計(EDL)の原理と手法を概観

### Evolutionary Feature Selection

- [Quantum-Inspired Evolutionary Algorithms for Feature Subset Selection: A Comprehensive Survey](https://arxiv.org/abs/2407.17946) — *arXiv 2024*。量子インスパイア進化的アルゴリズムによる特徴部分集合選択を網羅したサーベイ

### Evolutionary Multi-Objective Optimization

- [A Survey of Decomposition-Based Evolutionary Multi-Objective Optimization: Part I-Past and Future](https://arxiv.org/abs/2404.14571) — *IEEE TEVC 2024*。MOEA/Dを代表に分解ベース進化的多目的最適化の発展を概観したサーベイ(Part I)

### Evolutionary NAS

- [A Survey on Evolutionary Neural Architecture Search](https://arxiv.org/abs/2008.10937) — *IEEE TNNLS 2020* · 📈570。進化計算ベースのニューラルアーキテクチャ探索200本超を整理

### Evolutionary RL

- [Combining Evolution and Deep Reinforcement Learning for Policy Search: a Survey](https://arxiv.org/abs/2203.14009) — *ACM TELO 2022* · 📈66。進化計算と深層強化学習の融合手法を統一枠組みで概観

### Genetic Programming

- [A Recent Survey on the Applications of Genetic Programming in Image Processing](https://arxiv.org/abs/1901.07387) — *arXiv 2019*。画像処理における遺伝的プログラミングの応用(分類・特徴選択等)を整理したサーベイ

### Large-Scale Evolutionary Optimization

- [A Survey on Learnable Evolutionary Algorithms for Scalable Multiobjective Optimization](https://arxiv.org/abs/2206.11526) — *IEEE TEVC 2022*。スケールアップ多目的最適化向け学習可能な進化的アルゴリズムを4方向で概観

### Multi-objective Optimization

- [A Review of Evolutionary Multi-modal Multi-objective Optimization](https://arxiv.org/abs/2009.13347) — *IEEE TEVC 2020* · 📈193。進化的マルチモーダル多目的最適化をレビューした論文

### Neuroevolution

- [Neuroevolution in Deep Neural Networks: Current Trends and Future Challenges](https://arxiv.org/abs/2006.05415) — *IEEE TETCI 2020* · 📈174。深層ニューラルネットへの進化的アルゴリズム適用を概観

### Swarm Intelligence (PSO)

- [Particle Swarm Optimization: A survey of historical and recent developments with hybridization perspectives](https://arxiv.org/abs/1804.05319) — *Machine Learning and Knowledge Extraction 2018*。PSOの歴史的・最新の発展とハイブリッド化の観点を網羅したサーベイ

## 🔢 理論計算機科学

### Algorithmic Fairness Testing

- [Fairness Testing: A Comprehensive Survey and Analysis of Trends](https://arxiv.org/abs/2207.10223) — *ACM TOSEM 2022* · 📈140。ソフトウェア工学の観点で公平性テスト手法を体系化したサーベイ

### Algorithms with Predictions

- [Algorithms with Predictions](https://arxiv.org/abs/2006.09123) — *Beyond the Worst-Case Analysis of Algorithms (book chapter) 2020* · 📈306。ML予測を用いて最悪ケース解析を回避する学習拡張アルゴリズムの基礎を解説した定番サーベイ章

### Computational Social Choice

- [Preference Restrictions in Computational Social Choice: A Survey](https://arxiv.org/abs/2205.09092) — *arXiv 2022*。単峰性など制限選好領域が計算社会選択を容易化する仕組みを整理したサーベイ

### Differentiable Optimization

- [Differentiable Convex Optimization Layers in Neural Architectures: Foundations and Perspectives](https://arxiv.org/abs/2412.20679) — *arXiv 2024* · 📈2。微分可能最適化層の基礎と発展を概観したサーベイ

### ML for Combinatorial Optimization

- [Machine Learning for Combinatorial Optimization: a Methodological Tour d'Horizon](https://arxiv.org/abs/1811.06128) — *European Journal of Operational Research 2018* · 📈1784。MLとOR両分野からの組合せ最適化への機械学習活用を方法論的に俯瞰した定番サーベイ

### Streaming / Sketching Algorithms

- [Streaming and Sketching Complexity of CSPs: A survey](https://arxiv.org/abs/2205.02744) — *ICALP 2022*。ストリーミング・スケッチ計算モデルでのCSP近似解法の複雑性を概観したサーベイ

### Submodular Optimization

- [Learning with Submodular Functions: A Convex Optimization Perspective](https://arxiv.org/abs/1111.6453) — *Foundations and Trends in Machine Learning 2013*。劣モジュラ関数を凸最適化の観点から学習に結びつけた定番のモノグラフ
- [Convex Analysis and Optimization with Submodular Functions: a Tutorial](https://arxiv.org/abs/1010.4207) — *arXiv 2010*。劣モジュラ関数の凸解析と最適化を第一原理から解説したチュートリアル

## 🔬 AI for Science

### AI Drug Discovery

- [Deep Learning Methods for Small Molecule Drug Discovery: A Survey](https://arxiv.org/abs/2303.00313) — *IEEE TKDE 2023* · 📈23。低分子創薬の深層学習(生成・物性予測・逆合成)を概観

### AI Physics Simulation

- [Scientific Machine Learning through Physics-Informed Neural Networks: Where we are and What's next](https://arxiv.org/abs/2201.05624) — *Journal of Scientific Computing 2022* · 📈2297。物理情報ニューラルネット(PINN)の現状と展望を概観

### AI for Science (Overview)

- [A Survey of Deep Learning for Scientific Discovery](https://arxiv.org/abs/2003.11755) — *arXiv 2020* · 📈153。科学的発見のための深層学習を網羅的に概観したサーベイ

### AI4Science - Astronomy / Astrophysics

- [Deep Learning in Astrophysics](https://arxiv.org/abs/2510.10713) — *Annual Review of Astronomy and Astrophysics 2026* · 📈1。天体物理におけるニューラルネットの役割と物理対称性の組込みを整理したレビュー

### AI4Science - Computational Fluid Dynamics

- [Recent Advances on Machine Learning for Computational Fluid Dynamics: A Survey](https://arxiv.org/abs/2408.12171) — *arXiv 2024* · 📈63。計算流体力学への機械学習応用(2020-2024)を空力・燃焼等で整理したサーベイ

### AI4Science - Materials Discovery

- [Machine Learning-Driven Materials Discovery: Unlocking Next-Generation Functional Materials - A review](https://arxiv.org/abs/2503.18975) — *arXiv 2025* · 📈24。機械学習による材料発見手法を物性予測・新材料探索の観点で整理したレビュー

### AI4Science - Molecular Generation / Drug Design

- [A Survey of Generative AI for de novo Drug Design: New Frontiers in Molecule and Protein Generation](https://arxiv.org/abs/2402.08703) — *arXiv 2024* · 📈108。de novo創薬の生成AI(分子生成・タンパク質生成)を網羅したサーベイ

### AI4Science - Neuroscience & Deep Learning

- [A Review of Neuroscience-Inspired Machine Learning](https://arxiv.org/abs/2403.18929) — *arXiv 2024* · 📈16。神経科学に着想を得た機械学習(エネルギーベース/前向き/スパイキング)のレビュー

### AI4Science - PDE Solvers

- [Partial Differential Equations Meet Deep Neural Networks: A Survey](https://arxiv.org/abs/2211.05567) — *arXiv 2022* · 📈48。PDEを解く深層ニューラルネット手法(PINN/演算子学習等)を分類したサーベイ

### AI4Science - Protein Design

- [A Model-Centric Review of Deep Learning for Protein Design](https://arxiv.org/abs/2502.19173) — *arXiv 2025* · 📈11。タンパク質設計の深層学習をモデル中心で整理したレビュー

### AI4Science - Protein Structure Prediction

- [Deep Learning-Driven Protein Structure Prediction and Design: Key Model Developments by Nobel Laureates and Multi-Domain Applications](https://arxiv.org/abs/2504.01490) — *arXiv 2025* · 📈3。AlphaFold/RoseTTAFold等タンパク質構造予測・設計の主要モデルを体系化したレビュー

### AI4Science - Quantum Chemistry

- [Ab-initio Quantum Chemistry with Neural-Network Wavefunctions](https://doi.org/10.1038/s41570-023-00516-8) — *Nature Reviews Chemistry 2023* · 📈132。ニューラルネット波動関数によるab-initio量子化学(QMC)を俯瞰したレビュー

### AI4Science - Single-Cell Bioinformatics

- [LLM4Cell: A Survey of Large Language and Agentic Models for Single-Cell Biology](https://arxiv.org/abs/2510.07793) — *arXiv 2025* · 📈2。単一細胞生物学の基盤モデル58種を統一的に整理した初のサーベイ

### Bioinformatics Deep Learning

- [A Systematic Review of Deep Graph Neural Networks: Challenges, Classification, Architectures, Applications & Potential Utility in Bioinformatics](https://arxiv.org/abs/2311.02127) — *arXiv 2023* · 📈6。深層GNNのバイオインフォマティクス応用を系統レビュー

### Climate / Weather ML

- [Deep Learning and Foundation Models for Weather Prediction: A Survey](https://arxiv.org/abs/2501.06907) — *arXiv 2025* · 📈22。天気予測の深層学習・基盤モデルを学習パラダイムで分類
- [Interpretable Machine Learning for Weather and Climate Prediction: A Survey](https://arxiv.org/abs/2403.18864) — *arXiv 2024* · 📈11。天気・気候予測における解釈可能MLを概観したサーベイ

### Clinical NLP

- [Neural Natural Language Processing for Unstructured Data in Electronic Health Records: a Review](https://arxiv.org/abs/2107.02975) — *Computer Science Review 2021* · 📈226。電子カルテ非構造化テキストへのニューラルNLPをレビュー

### Materials Science ML

- [Advances of Machine Learning in Materials Science: Ideas and Techniques](https://arxiv.org/abs/2307.14032) — *Frontiers of Physics 2023* · 📈73。材料科学における機械学習の手法と応用を概観したレビュー

### Protein Structure Prediction

- [A Survey of Deep Learning Methods in Protein Bioinformatics and its Impact on Protein Design](https://arxiv.org/abs/2501.01477) — *arXiv 2025* · 📈2。タンパク質構造・機能予測・設計の深層学習手法を概観

## 🌟 人工知能 (全般)

### Automated Planning

- [AI Planning: A Primer and Survey (Preliminary Report)](https://arxiv.org/abs/2412.05528) — *arXiv 2024* · 📈5。AIプランニングの基礎と学習ベース手法・基盤モデル連携を俯瞰した入門サーベイ

### Commonsense Reasoning

- [Commonsense Reasoning for Natural Language Understanding: A Survey of Benchmarks, Resources, and Approaches](https://arxiv.org/abs/1904.01172) — *arXiv 2019* · 📈144。常識推論のベンチマーク・知識資源・手法を整理した定番サーベイ
- [Commonsense Knowledge Reasoning and Generation with Pre-trained Language Models: A Survey](https://arxiv.org/abs/2201.12438) — *AAAI 2022* · 📈78。事前学習言語モデルによる常識推論・生成タスクの強み弱みを整理したサーベイ

### Foundation Models

- [On the Opportunities and Risks of Foundation Models](https://arxiv.org/abs/2108.07258) — *arXiv 2021* · 📈6535。基盤モデルの能力・技術・応用・社会影響を横断的に論じたStanford大規模レポート

### Knowledge Graphs & Reasoning

- [A Survey on Knowledge Graphs: Representation, Acquisition and Applications](https://arxiv.org/abs/2002.00388) — *IEEE TNNLS 2021* · 📈2703。知識グラフの表現学習・獲得・推論・応用を網羅した高被引用サーベイ

### Mathematical Reasoning

- [A Survey of Deep Learning for Mathematical Reasoning](https://arxiv.org/abs/2212.10535) — *ACL 2023* · 📈195。数学的推論の課題・データセット・深層学習手法を10年分整理したサーベイ — [`lupantech/dl4math`](https://github.com/lupantech/dl4math) ⭐372🔴

### Neuro-Symbolic AI

- [Towards Data-and Knowledge-Driven Artificial Intelligence: A Survey on Neuro-Symbolic Computing](https://arxiv.org/abs/2210.15889) — *IEEE TPAMI 2024* · 📈62。ニューラルと記号推論を統合するニューロシンボリック計算の体系的サーベイ

### Theorem Proving & ML

- [A Survey on Deep Learning for Theorem Proving](https://arxiv.org/abs/2404.09939) — *COLM 2024* · 📈63。自動形式化・前提選択・証明探索など定理証明への深層学習応用を網羅したサーベイ — [`zhaoyu-li/DL4TP`](https://github.com/zhaoyu-li/DL4TP) ⭐224🟡

### World Models

- [Understanding World or Predicting Future? A Comprehensive Survey of World Models](https://arxiv.org/abs/2411.14499) — *ACM Computing Surveys 2025* · 📈157。世界理解と未来予測の2機能でworld modelsを体系化した包括的サーベイ — [`tsinghua-fib-lab/World-Model`](https://github.com/tsinghua-fib-lab/World-Model) ⭐738🟡

## 🧩 ニューラルネット基礎

### Activation Functions

- [Activation Functions in Deep Learning: A Comprehensive Survey and Benchmark](https://arxiv.org/abs/2109.14545) — *Neurocomputing 2022* · 📈1085。Sigmoid/ReLU/ELU/学習型など活性化関数を分類しベンチマーク比較したサーベイ
- [Three Decades of Activations: A Comprehensive Survey of 400 Activation Functions for Neural Networks](https://arxiv.org/abs/2402.09092) — *arXiv 2024* · 📈53。30年分400種類の活性化関数を網羅的に整理した大規模サーベイ

### Attention Mechanisms

- [Attention, please! A survey of Neural Attention Models in Deep Learning](https://arxiv.org/abs/2103.16775) — *Artificial Intelligence Review 2022* · 📈279。650本超を分析し各種ニューラルattention機構を横断的に整理したサーベイ

### CNN Fundamentals

- [Recent Advances in Convolutional Neural Networks](https://arxiv.org/abs/1512.07108) — *Pattern Recognition 2018* · 📈5941。層設計・活性化・損失・正則化・最適化などCNNの改良を網羅した定番総説
- [A Survey of the Recent Architectures of Deep Convolutional Neural Networks](https://arxiv.org/abs/1901.06032) — *Artificial Intelligence Review 2020* · 📈2685。深層CNNの主要アーキテクチャ革新を分類整理した高被引用サーベイ

### Capsule Networks

- [Learning with Capsules: A Survey](https://arxiv.org/abs/2206.02664) — *ACM Computing Surveys 2024* · 📈22。部分-全体階層を扱うcapsule networkの概念・ルーティング・応用を整理したサーベイ

### Diffusion Models Theory

- [Diffusion Models: A Comprehensive Survey of Methods and Applications](https://arxiv.org/abs/2209.00796) — *ACM Computing Surveys 2023* · 📈2240。DDPM/SGM/Score SDEの三定式化と効率サンプリング・尤度改善を整理した総説 — [`YangLing0818/Diffusion-Models-Papers-Survey-Taxonomy`](https://github.com/YangLing0818/Diffusion-Models-Papers-Survey-Taxonomy) ⭐3345🟡

### Efficient Transformers

- [Efficient Transformers: A Survey](https://arxiv.org/abs/2009.06732) — *ACM Computing Surveys 2022* · 📈1520。計算/メモリ効率を改善する各種効率的Transformerを整理した定番サーベイ

### Equivariant Neural Networks

- [Geometric Deep Learning and Equivariant Neural Networks](https://arxiv.org/abs/2105.13926) — *Artificial Intelligence Review 2023* · 📈111。群同変・ゲージ同変NNの数学的基礎を球面ネットワーク等で詳説したサーベイ

### Geometric Deep Learning

- [Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges](https://arxiv.org/abs/2104.13478) — *arXiv 2021* · 📈1594。対称性とゲージ原理で各種NNアーキテクチャを統一する幾何深層学習の体系的論考 — [project](https://geometricdeeplearning.com/book/)

### Implicit Neural Representations

- [Where Do We Stand with Implicit Neural Representations? A Technical and Performance Survey](https://arxiv.org/abs/2411.03688) — *arXiv 2024* · 📈54。活性化・位置符号化・構造最適化の観点でINRを技術的・性能的に比較したサーベイ

### Mixture of Experts

- [A Review of Sparse Expert Models in Deep Learning](https://arxiv.org/abs/2209.01667) — *arXiv 2022* · 📈203。MoE/Switch等のスパースエキスパートモデルを概念整理したレビュー
- [A Comprehensive Survey of Mixture-of-Experts: Algorithms, Theory, and Applications](https://arxiv.org/abs/2503.07137) — *arXiv 2025* · 📈96。MoEのアルゴリズム・理論・多モーダル応用を包括的に整理した近年のサーベイ

### Neural ODE / Differential Equations

- [Comprehensive Review of Neural Differential Equations for Time Series Analysis](https://arxiv.org/abs/2502.09885) — *IJCAI (Survey Track) 2025* · 📈21。Neural ODE/CDE/SDEを時系列解析の観点で数理・応用ごとに整理したレビュー

### Normalization Layers

- [Normalization Techniques in Training DNNs: Methodology, Analysis and Application](https://arxiv.org/abs/2009.12836) — *IEEE TPAMI 2023* · 📈437。BatchNorm等の正規化手法を最適化観点で統一的に整理した分類学サーベイ — [`huangleiBuaa/NormalizationSurvey`](https://github.com/huangleiBuaa/NormalizationSurvey) ⭐85🔴

### Physics-Informed NN

- [Physics-Informed Machine Learning: A Survey on Problems, Methods and Applications](https://arxiv.org/abs/2211.08064) — *arXiv 2023* · 📈177。物理事前知識の表現と組込み手法を軸に物理情報機械学習を体系化したサーベイ

### Quantum Machine Learning

- [A comprehensive review of Quantum Machine Learning: from NISQ to Fault Tolerance](https://arxiv.org/abs/2401.11351) — *Reports on Progress in Physics 2024* · 📈108。NISQから誤り耐性までのQML概念・アルゴリズム・統計学習理論を整理したレビュー
- [A Survey on Quantum Machine Learning: Current Trends, Challenges, Opportunities, and the Road Ahead](https://arxiv.org/abs/2310.10315) — *arXiv 2023* · 📈73。QMLアルゴリズム・データセット・ハード/ソフト基盤を網羅した動向サーベイ

### RNN / LSTM

- [Fundamentals of Recurrent Neural Network (RNN) and Long Short-Term Memory (LSTM) Network](https://arxiv.org/abs/1808.03314) — *Physica D 2020* · 📈4976。微分方程式からRNN/LSTMの正準形を導出する理論的基礎解説

### Sparse Neural Networks

- [Sparsity in Deep Learning: Pruning and growth for efficient inference and training in neural networks](https://arxiv.org/abs/2102.00554) — *JMLR 2021* · 📈966。300本超を統合し疎化(枝刈り/成長)の手法と実践を解説した大規模チュートリアル
- [A Survey on Deep Neural Network Pruning: Taxonomy, Comparison, Analysis, and Recommendations](https://arxiv.org/abs/2308.06767) — *IEEE TPAMI 2024* · 📈480。DNN枝刈りの分類学・比較・分析・推奨を提供した近年の包括的サーベイ

### Spiking Neural Networks

- [Deep Learning in Spiking Neural Networks](https://arxiv.org/abs/1804.08150) — *Neural Networks 2019* · 📈1343。深層SNNの教師あり/なし学習手法を精度・計算コスト・ハード親和性で比較した総説
- [Toward Large-scale Spiking Neural Networks: A Comprehensive Survey and Future Directions](https://arxiv.org/abs/2409.02111) — *arXiv 2024* · 📈12。大規模化と Spiking Transformer に焦点を当てた深層SNNの包括的サーベイ

### State Space Models

- [A Survey of Mamba](https://arxiv.org/abs/2408.01129) — *arXiv 2024* · 📈93。Mambaベースモデルの進展・データ適応・応用を整理した状態空間モデルのサーベイ
- [Mamba-360: Survey of State Space Models as Transformer Alternative for Long Sequence Modelling](https://arxiv.org/abs/2404.16112) — *arXiv 2024* · 📈89。Transformer代替としてのSSMを長系列モデリング観点で分類・比較したサーベイ — [`badripatro/mamba360`](https://github.com/badripatro/mamba360) ⭐71🔴

### Test-Time Adaptation

- [A Comprehensive Survey on Test-Time Adaptation under Distribution Shifts](https://arxiv.org/abs/2303.15361) — *IJCV 2025* · 📈508。分布シフト下でのテスト時適応(TTA)を試験データ形態で分類した包括的サーベイ — [`tim-learn/awesome-test-time-adaptation`](https://github.com/tim-learn/awesome-test-time-adaptation) ⭐1285🟡

### Transformer Architectures

- [A Survey of Transformers](https://arxiv.org/abs/2106.04554) — *AI Open 2022* · 📈1488。X-formerの分類体系(構造改良・事前学習・応用)を提示したTransformer総説

## 🏭 応用・横断領域

### AI x Agriculture

- [AI in Agriculture: A Survey of Deep Learning Techniques for Crops, Fisheries and Livestock](https://arxiv.org/abs/2507.22101) — *arXiv 2026* · 📈8。作物・水産・畜産にわたる農業AIの深層学習技術を網羅したサーベイ

### AI x Cybersecurity - Intrusion Detection

- [Deep Learning-based Intrusion Detection Systems: A Survey](https://arxiv.org/abs/2504.07839) — *arXiv 2025* · 📈28。侵入検知システム(IDS)の深層学習を全段階(収集~調査)で体系化したサーベイ

### AI x Education - Intelligent Tutoring

- [Large Language Models for Education: A Survey](https://arxiv.org/abs/2405.13001) — *arXiv 2024* · 📈79。教育分野(知能チュータ等)におけるLLM応用を体系化したサーベイ

### AI x Energy - Load Forecasting

- [Short-Term Electricity-Load Forecasting by Deep Learning: A Comprehensive Survey](https://arxiv.org/abs/2408.16202) — *arXiv 2025* · 📈59。短期電力負荷予測の深層学習手法を包括的に整理したサーベイ

### AI x Finance

- [Deep Learning for Financial Applications : A Survey](https://arxiv.org/abs/2002.05786) — *Applied Soft Computing 2020* · 📈498。金融応用への深層学習をサブ分野・モデル別に整理した高被引用サーベイ

### AI x Finance - Algorithmic Trading

- [Deep Reinforcement Learning in Quantitative Algorithmic Trading: A Review](https://arxiv.org/abs/2106.00123) — *arXiv 2021* · 📈56。定量的アルゴリズム取引における深層強化学習を整理したレビュー

### AI x Finance - Financial LLM

- [A Survey of Large Language Models for Financial Applications: Progress, Prospects and Challenges](https://arxiv.org/abs/2406.11903) — *arXiv 2024* · 📈150。金融応用におけるLLMの進展・展望・課題を整理したサーベイ

### AI x Finance - Fraud Detection

- [Year-over-Year Developments in Financial Fraud Detection via Deep Learning: A Systematic Literature Review](https://arxiv.org/abs/2502.00201) — *arXiv 2025* · 📈40。金融不正検知の深層学習手法を年次推移で分析した系統的文献レビュー

### AI x Healthcare

- [Deep EHR: A Survey of Recent Advances in Deep Learning Techniques for Electronic Health Record (EHR) Analysis](https://arxiv.org/abs/1706.03446) — *IEEE JBHI 2018* · 📈1436。電子カルテ解析への深層学習応用を構造・技術・臨床応用面で整理したサーベイ

### AI x Healthcare - Clinical NLP / EHR

- [A Comprehensive Survey of Electronic Health Record Modeling: From Deep Learning Approaches to Large Language Models](https://arxiv.org/abs/2507.12774) — *arXiv 2025* · 📈10。EHRモデリングを深層学習からLLMまで体系化した包括サーベイ

### AI x Healthcare - Computational Pathology

- [Artificial Intelligence for Digital and Computational Pathology](https://doi.org/10.1038/s44222-023-00096-8) — *Nature Reviews Bioengineering 2023* · 📈323。デジタル/計算病理学におけるAIの応用と課題を俯瞰したNatureレビュー

### AI x Healthcare - Digital Pathology Foundation Models

- [A New Era in Computational Pathology: A Survey on Foundation and Vision-Language Models](https://arxiv.org/abs/2408.14496) — *arXiv 2024* · 📈12。計算病理学における基盤モデルとVision-Languageモデルの最新サーベイ

### AI x Healthcare - Medical Image Segmentation

- [From CNN to Transformer: A Review of Medical Image Segmentation Models](https://arxiv.org/abs/2308.05305) — *arXiv 2023* · 📈197。医療画像セグメンテーションのCNNからTransformerへの進化を整理したレビュー

### AI x Healthcare - Medical LLM

- [A Survey on Medical Large Language Models: Technology, Application, Trustworthiness, and Future Directions](https://arxiv.org/abs/2406.03712) — *arXiv 2024* · 📈53。医療特化LLMの技術・応用・信頼性・将来方向を体系化した包括サーベイ

### AI x Healthcare - Mental Health NLP

- [A Survey on Multilingual Mental Disorders Detection from Social Media Data](https://arxiv.org/abs/2505.15556) — *arXiv 2026* · 📈4。ソーシャルメディアからの多言語メンタル疾患検出のNLPサーベイ

### AI x Healthcare - Radiology Report Generation

- [A Survey of Deep Learning-based Radiology Report Generation Using Multimodal Data](https://arxiv.org/abs/2405.12833) — *arXiv 2025* · 📈8。マルチモーダルデータを用いた放射線レポート自動生成の深層学習サーベイ

### AI x IoT/Edge - TinyML

- [From Tiny Machine Learning to Tiny Deep Learning: A Survey](https://arxiv.org/abs/2506.18927) — *arXiv 2025* · 📈31。TinyMLからTinyDLへの移行(量子化・剪定・NAS・HW)を網羅したサーベイ

### AI x Law - Legal LLM

- [Large Language Models Meet Legal Artificial Intelligence: A Survey](https://arxiv.org/abs/2509.09969) — *arXiv 2025* · 📈8。法律AIにおけるLLMモデル・フレームワーク・ベンチマークを網羅したサーベイ

### AI x Manufacturing - Anomaly Detection

- [Deep Learning for Unsupervised Anomaly Localization in Industrial Images: A Survey](https://arxiv.org/abs/2207.10298) — *arXiv 2022* · 📈245。産業画像の教師なし異常箇所特定の深層学習手法を整理したサーベイ

### AI x Manufacturing - Industrial Time Series Anomaly Detection

- [A Comprehensive Survey of Deep Transfer Learning for Anomaly Detection in Industrial Time Series: Methods, Applications, and Directions](https://arxiv.org/abs/2307.05638) — *arXiv 2024* · 📈164。産業時系列の異常検知における深層転移学習を網羅したサーベイ

### AI x Mobility - Autonomous Driving Foundation Models

- [A Survey for Foundation Models in Autonomous Driving](https://arxiv.org/abs/2402.01105) — *arXiv 2024* · 📈65。自動運転における基盤モデル(マルチモーダル/LLM等)を分類したサーベイ

### AI x Music - Deep Music Generation

- [A Comprehensive Survey on Deep Music Generation: Multi-level Representations, Algorithms, Evaluations, and Future Directions](https://arxiv.org/abs/2011.06801) — *arXiv 2020* · 📈148。深層音楽生成を多階層表現・アルゴリズム・評価の観点で網羅した包括サーベイ

### AI x Networking

- [Deep Learning in Mobile and Wireless Networking: A Survey](https://arxiv.org/abs/1803.04311) — *IEEE Communications Surveys & Tutorials 2019* · 📈1495。モバイル/無線ネットワーク研究への深層学習応用を横断的に整理した定番サーベイ

### AI x Society - Finance/Healthcare/Law

- [A Survey on Large Language Models for Critical Societal Domains: Finance, Healthcare, and Law](https://arxiv.org/abs/2405.01769) — *arXiv 2024* · 📈100。金融・医療・法律という重要社会領域でのLLM応用と倫理を横断的に整理したサーベイ

### AI x Software Engineering

- [A Survey on Deep Learning for Software Engineering](https://arxiv.org/abs/2011.14597) — *ACM Computing Surveys 2022* · 📈234。20主要会議誌の142本を分析しSEタスクへの深層学習応用を分類したサーベイ

### AI x Software Engineering - LLM Agents

- [Large Language Model-Based Agents for Software Engineering: A Survey](https://arxiv.org/abs/2409.02977) — *arXiv 2025* · 📈192。ソフトウェア工学向けLLMエージェントをSE/エージェント両視点で整理したサーベイ

### AI x Transportation - GNN

- [Graph Neural Networks in Intelligent Transportation Systems: Advances, Applications and Trends](https://arxiv.org/abs/2401.00713) — *arXiv 2024* · 📈18。知能交通システムにおけるGNN応用(予測・制御・需要等6領域)を整理したサーベイ

### Geospatial - Remote Sensing Foundation Models

- [Foundation Models for Remote Sensing and Earth Observation: A Survey](https://arxiv.org/abs/2410.16602) — *IEEE Geoscience and Remote Sensing Magazine 2025* · 📈85。リモートセンシング/地球観測の基盤モデルを網羅したサーベイ(IEEE GRSM採録)

### Geospatial - Self-Supervised GeoAI

- [Self-Supervised Representation Learning for Geospatial Objects: A Survey](https://arxiv.org/abs/2408.12133) — *arXiv 2025* · 📈17。地理空間オブジェクトの自己教師あり表現学習を整理したサーベイ

## 📊 データ中心AI・評価

### Active Learning

- [A Survey of Deep Active Learning](https://arxiv.org/abs/2009.00236) — *ACM Computing Surveys 2022* · 📈1479。深層能動学習の初の包括レビュー。クエリ戦略やラベリングコスト削減手法を整理

### Benchmark Contamination

- [A Survey on Data Contamination for Large Language Models](https://arxiv.org/abs/2502.14425) — *arXiv 2025*。データ汚染の定義・影響と汚染フリー評価手法(更新/書換/予防)を整理したサーベイ
- [Benchmark Data Contamination of Large Language Models: A Survey](https://arxiv.org/abs/2406.04244) — *arXiv 2024*。LLMのベンチマーク汚染問題と検出・緩和手法を整理したサーベイ

### Benchmark Design / Model Evaluation

- [Evaluation and Benchmarking of LLM Agents: A Survey](https://arxiv.org/abs/2507.21504) — *arXiv 2025* · 📈123。LLMエージェントの評価を評価対象と評価プロセスの2次元分類で俯瞰したサーベイ

### Coreset Selection / Data Pruning

- [A Coreset Selection of Coreset Selection Literature: Introduction and Recent Advances](https://arxiv.org/abs/2505.17799) — *arXiv 2025* · 📈18。coreset選択(データ枝刈り)を訓練不要・訓練指向・ラベル不要の3系統に統一分類したサーベイ

### Data-Centric AI

- [Data-centric Artificial Intelligence: A Survey](https://arxiv.org/abs/2303.10158) — *ACM Computing Surveys 2025* · 📈427。学習/推論データ開発とデータ保守の3目標でデータ中心AIを俯瞰したサーベイ — [`daochenzha/data-centric-AI`](https://github.com/daochenzha/data-centric-AI) ⭐1149🔴

### Dataset Distillation

- [Dataset Distillation: A Comprehensive Review](https://arxiv.org/abs/2301.07014) — *IEEE TPAMI 2024* · 📈195。合成サンプルで小規模代替データを生成するデータ蒸留の近年の進展を整理したレビュー
- [A Comprehensive Survey of Dataset Distillation](https://arxiv.org/abs/2301.05603) — *IEEE TPAMI 2024* · 📈172。データ蒸留のフレームワーク・アルゴリズム・分解型手法・応用を整理したサーベイ

### LLM-as-Judge Evaluation

- [A Survey on LLM-as-a-Judge](https://arxiv.org/abs/2411.15594) — *arXiv 2024*。LLM-as-a-Judgeの信頼性向上(一貫性・バイアス緩和等)の戦略を整理したサーベイ

### Synthetic Data Generation

- [Synthetic Data Generation Using Large Language Models: Advances in Text and Code](https://arxiv.org/abs/2503.14023) — *IEEE Access 2025*。LLMによるテキスト・コードの合成データ生成手法(プロンプト/RAG/自己改良)を概観
- [A Survey on Data Synthesis and Augmentation for Large Language Models](https://arxiv.org/abs/2410.12896) — *arXiv 2024*。LLMのライフサイクル全体にわたるデータ合成・拡張技術を整理したサーベイ

## 貢献

追加・修正は [`contributing.md`](contributing.md) を参照。サーベイ論文 (survey/review/overview) のみを対象とし、実在検証 (arXiv/DOI/GitHub) を経たもののみ掲載します。

## ライセンス

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](LICENSE) 本リスト（キュレーション）は CC0 (パブリックドメイン)。各論文の著作権は原著者に帰属します。
