# Awesome AI Survey Papers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> AI関連分野のトップ会議・トップジャーナル・arXiv で公開された**サーベイ論文 (survey / review / overview)** の厳選キュレーション。研究サーベイの出発点として、良質で網羅的なレビュー論文へ最短で辿り着くことを目的とします。

**490 本のサーベイ論文** / 30 分野 / companion リポジトリ 65 件付き。最終更新 2026-06-05。

各項目は `[タイトル](論文URL) — *venue 年* · 📈被引用数。説明 — [`companion repo`](github) ⭐star🟢鮮度 · [project](ページ)` の形式。

凡例: 📈 被引用数 (Semantic Scholar) · ⭐ GitHub star · 鮮度 🟢直近6ヶ月 / 🟡18ヶ月内 / 🔴それ以前（サーベイ companion は鮮度が低くても網羅性・権威性で価値があります）。

> 📑 収集の全メタデータ・統計・調査手法は [`docs/research-notes.md`](docs/research-notes.md) を参照。

## 目次

- [🧠 大規模言語モデル (LLM)](#-大規模言語モデル-llm) (47)
- [🎨 生成AI・拡散モデル](#-生成ai拡散モデル) (14)
- [🖼️ マルチモーダル・視覚言語](#-マルチモーダル視覚言語) (10)
- [💬 自然言語処理 (NLP)](#-自然言語処理-nlp) (42)
- [🔊 音声・信号処理](#-音声信号処理) (9)
- [👁️ コンピュータビジョン (CV)](#-コンピュータビジョン-cv) (51)
- [📈 機械学習 (一般)](#-機械学習-一般) (48)
- [📐 学習理論](#-学習理論) (7)
- [🎮 強化学習 (RL)](#-強化学習-rl) (31)
- [🤖 ロボティクス・身体性](#-ロボティクス身体性) (19)
- [👥 マルチエージェント](#-マルチエージェント) (8)
- [🕸️ グラフニューラルネット (GNN)](#-グラフニューラルネット-gnn) (21)
- [🔗 知識表現・知識グラフ](#-知識表現知識グラフ) (10)
- [🎯 因果推論](#-因果推論) (6)
- [⏱️ 時系列・時空間](#-時系列時空間) (10)
- [⛏️ データマイニング](#-データマイニング) (17)
- [🗄️ データベース・データ管理](#-データベースデータ管理) (9)
- [🔍 情報検索 (IR)](#-情報検索-ir) (10)
- [🛒 推薦システム](#-推薦システム) (19)
- [🌐 Web・ソーシャル](#-webソーシャル) (4)
- [🛡️ 信頼できるAI (公平性・XAI・安全性)](#-信頼できるai-公平性xai安全性) (22)
- [📡 連合学習](#-連合学習) (8)
- [🖐️ HCI・ヒューマンAI](#-hciヒューマンai) (7)
- [🧬 進化計算](#-進化計算) (6)
- [🔢 理論計算機科学](#-理論計算機科学) (2)
- [🔬 AI for Science](#-ai-for-science) (9)
- [🌟 人工知能 (全般)](#-人工知能-全般) (9)
- [🧩 ニューラルネット基礎](#-ニューラルネット基礎) (27)
- [🏭 応用・横断領域](#-応用横断領域) (4)
- [📊 データ中心AI・評価](#-データ中心ai評価) (4)

## 🧠 大規模言語モデル (LLM)

### Code LLM

- [Large Language Models for Software Engineering: A Systematic Literature Review](https://arxiv.org/abs/2308.10620) — *ACM TOSEM 2023* · 📈988。395論文を分析したソフトウェア工学向けLLMの系統的文献レビュー
- [A Survey on Large Language Models for Code Generation](https://arxiv.org/abs/2406.00515) — *arXiv 2024* · 📈943。コード生成LLMのデータ・手法・評価・倫理を体系化したサーベイ — [`huybery/Awesome-Code-LLM`](https://github.com/huybery/Awesome-Code-LLM) ⭐1285🔴
- [Unifying the Perspectives of NLP and Software Engineering: A Survey on Language Models for Code](https://arxiv.org/abs/2311.07989) — *TMLR 2023* · 📈113。70+モデル・900+研究を整理したコード言語モデルの包括的サーベイ — [`codefuse-ai/Awesome-Code-LLM`](https://github.com/codefuse-ai/Awesome-Code-LLM) ⭐3373🟢

### Compression / Quantization

- [A Survey on Model Compression for Large Language Models](https://arxiv.org/abs/2308.07633) — *TACL 2023* · 📈445。量子化・枝刈り・蒸留を軸にLLM圧縮を整理したTACLサーベイ
- [Efficient Large Language Models: A Survey](https://arxiv.org/abs/2312.03863) — *TMLR 2023* · 📈232。モデル/データ/フレームワークの3視点でLLM効率化を網羅した総説 — [`AIoT-MLSys-Lab/Efficient-LLMs-Survey`](https://github.com/AIoT-MLSys-Lab/Efficient-LLMs-Survey) ⭐1260🟡
- [The Efficiency Spectrum of Large Language Models: An Algorithmic Survey](https://arxiv.org/abs/2312.00678) — *arXiv 2023* · 📈37。スケーリング則から推論までLLM効率のアルゴリズム的側面を俯瞰

### Continual Learning

- [Towards Lifelong Learning of Large Language Models: A Survey](https://arxiv.org/abs/2406.06391) — *ACM Computing Surveys 2024* · 📈94。内部/外部知識の12シナリオでLLMの生涯学習を分類したサーベイ

### Efficient Inference / KV Cache

- [A Survey on Efficient Inference for Large Language Models](https://arxiv.org/abs/2404.14294) — *arXiv 2024* · 📈228。データ/モデル/システムの3層でLLM効率推論を整理し比較実験も実施
- [LLM Inference Unveiled: Survey and Roofline Model Insights](https://arxiv.org/abs/2402.16363) — *arXiv 2024* · 📈185。Rooflineモデルでボトルネックを可視化したLLM推論効率化サーベイ
- [Towards Efficient Generative LLM Serving: A Survey from Algorithms to Systems](https://arxiv.org/abs/2312.15234) — *ACM Computing Surveys 2023* · 📈155。アルゴリズムからシステムまでLLMサービングの効率化技術を俯瞰

### Hallucination

- [A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions](https://arxiv.org/abs/2311.05232) — *ACM TOIS 2023* · 📈2940。幻覚の原理・分類・課題を網羅した代表的ハルシネーションサーベイ — [`LuckyyySTA/Awesome-LLM-hallucination`](https://github.com/LuckyyySTA/Awesome-LLM-hallucination) ⭐335🔴
- [Siren's Song in the AI Ocean: A Survey on Hallucination in Large Language Models](https://arxiv.org/abs/2309.01219) — *arXiv 2023* · 📈1014。入力矛盾・文脈矛盾・事実矛盾の分類でLLM幻覚を整理したサーベイ — [`HillZhang1999/llm-hallucination-survey`](https://github.com/HillZhang1999/llm-hallucination-survey) ⭐1086🟡
- [A Comprehensive Survey of Hallucination Mitigation Techniques in Large Language Models](https://arxiv.org/abs/2401.01313) — *arXiv 2024* · 📈449。RAG等32種超の幻覚緩和手法を分類・比較したミティゲーション専門サーベイ

### In-Context Learning

- [A Survey on In-context Learning](https://arxiv.org/abs/2301.00234) — *EMNLP 2023* · 📈1044。文脈内学習の定義・手法・分析を体系化した定番サーベイ — [`EgoAlpha/prompt-in-context-learning`](https://github.com/EgoAlpha/prompt-in-context-learning) ⭐2239🟢

### Instruction Tuning

- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) — *NeurIPS 2022* · 📈21350。InstructGPT論文。人間フィードバックによる指示追従学習の基礎を確立
- [Instruction Tuning for Large Language Models: A Survey](https://arxiv.org/abs/2308.10792) — *arXiv 2023* · 📈878。指示チューニング(SFT)の手法・データ構築・応用を整理した代表的サーベイ — [`xiaoya-li/Instruction-Tuning-Survey`](https://github.com/xiaoya-li/Instruction-Tuning-Survey) ⭐232🟡

### Knowledge Editing

- [Knowledge Editing for Large Language Models: A Survey](https://arxiv.org/abs/2310.16218) — *ACM Computing Surveys 2023* · 📈253。知識編集(KME)技術の分類・評価・課題を整理した代表的サーベイ
- [A Comprehensive Study of Knowledge Editing for Large Language Models](https://arxiv.org/abs/2401.01286) — *arXiv 2024* · 📈160。外部/パラメータ/内部の3分類とKnowEditベンチを提案した知識編集研究 — [`zjunlp/EasyEdit`](https://github.com/zjunlp/EasyEdit) ⭐2836🟢

### LLM Agents

- [A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432) — *Frontiers of Computer Science 2023* · 📈3008。LLM自律エージェントの構築統一枠組・応用・評価を整理した代表的サーベイ — [`Paitesanshi/LLM-Agent-Survey`](https://github.com/Paitesanshi/LLM-Agent-Survey) ⭐2901🟡
- [The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/abs/2309.07864) — *arXiv 2023* · 📈1769。脳・知覚・行動の枠組で単体/マルチエージェントと社会を俯瞰した大規模総説 — [`WooooDyy/LLM-Agent-Paper-List`](https://github.com/WooooDyy/LLM-Agent-Paper-List) ⭐8142🟡
- [ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate](https://arxiv.org/abs/2308.07201) — *ICLR 2024* · 📈924。複数LLMの討論で評価精度を高めるマルチエージェント評価枠組 — [`thunlp/ChatEval`](https://github.com/thunlp/ChatEval) ⭐335🔴

### LLM Evaluation

- [A Survey on Evaluation of Large Language Models](https://arxiv.org/abs/2307.03109) — *ACM TIST 2023* · 📈3399。何を/どこで/どう評価するかの3軸でLLM評価を整理した定番サーベイ — [`MLGroupJLU/LLM-eval-survey`](https://github.com/MLGroupJLU/LLM-eval-survey) ⭐1600🟢
- [Evaluating Large Language Models: A Comprehensive Survey](https://arxiv.org/abs/2310.19736) — *arXiv 2023* · 📈311。知識能力・整合性・安全性の3分類でLLM評価を網羅したサーベイ — [`tjunlp-lab/Awesome-LLMs-Evaluation-Papers`](https://github.com/tjunlp-lab/Awesome-LLMs-Evaluation-Papers) ⭐803🔴

### LLM General

- [A Survey of Large Language Models](https://arxiv.org/abs/2303.18223) — *arXiv 2023* · 📈4514。事前学習・適応・利用・評価の4側面でLLMを俯瞰した定番大規模サーベイ(144頁) — [`RUCAIBox/LLMSurvey`](https://github.com/RUCAIBox/LLMSurvey) ⭐12169🟡
- [A Comprehensive Overview of Large Language Models](https://arxiv.org/abs/2307.06435) — *arXiv 2023* · 📈1657。アーキテクチャ・学習・微調整・マルチモーダル等を広く整理したLLM総説
- [Large Language Models: A Survey](https://arxiv.org/abs/2402.06196) — *arXiv 2024* · 📈970。主要LLMファミリと構築・評価・データセットを概観した総説
- [Datasets for Large Language Models: A Comprehensive Survey](https://arxiv.org/abs/2402.18041) — *arXiv 2024* · 📈133。事前学習・指示・選好・評価データ444件を体系化したデータセットサーベイ

### Long Context

- [Advancing Transformer Architecture in Long-Context LLMs: A Comprehensive Survey](https://arxiv.org/abs/2311.12351) — *arXiv 2023* · 📈121。長文コンテキスト処理のTransformer改良を網羅した長文LLMサーベイ — [`Strivin0311/long-llms-learning`](https://github.com/Strivin0311/long-llms-learning) ⭐274🔴
- [The What, Why, and How of Context Length Extension Techniques in Large Language Models](https://arxiv.org/abs/2401.07872) — *arXiv 2024* · 📈47。コンテキスト長拡張技術を体系的にレビューし評価課題を整理

### Mixture-of-Experts

- [A Survey on Mixture of Experts in Large Language Models](https://arxiv.org/abs/2407.06204) — *IEEE TKDE 2024* · 📈313。LLMにおけるMoEのアルゴリズム・システム・応用を整理した専門サーベイ — [`withinmiaov/A-Survey-on-Mixture-of-Experts-in-LLMs`](https://github.com/withinmiaov/A-Survey-on-Mixture-of-Experts-in-LLMs) ⭐504🟡

### Multilingual LLM

- [A Survey on Multilingual Large Language Models: Corpora, Alignment, and Bias](https://arxiv.org/abs/2404.00929) — *arXiv 2024* · 📈127。多言語LLMのコーパス・アラインメント・バイアスを整理したサーベイ

### Parameter-Efficient Fine-Tuning

- [Parameter-Efficient Fine-Tuning for Large Models: A Comprehensive Survey](https://arxiv.org/abs/2403.14608) — *TMLR 2024* · 📈934。LoRA系を含むPEFTの分類・アルゴリズム・システム実装を網羅した総説
- [Parameter-Efficient Fine-Tuning Methods for Pretrained Language Models: A Critical Review and Assessment](https://arxiv.org/abs/2312.12148) — *arXiv 2023* · 📈344。PEFT手法を批判的にレビューしパラメータ/メモリ効率を実験評価
- [Scaling Down to Scale Up: A Guide to Parameter-Efficient Fine-Tuning](https://arxiv.org/abs/2303.15647) — *arXiv 2023* · 📈276。50件超のPEFTを分類し15手法を実験比較した実践ガイド型サーベイ

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

### Safety / Jailbreak

- [Trustworthy LLMs: A Survey and Guideline for Evaluating Large Language Models' Alignment](https://arxiv.org/abs/2308.05374) — *arXiv 2023* · 📈542。信頼性7カテゴリ29サブカテゴリでLLMの安全性評価指針を提示
- [Jailbreak Attacks and Defenses Against Large Language Models: A Survey](https://arxiv.org/abs/2407.04295) — *arXiv 2024* · 📈274。ジェイルブレイク攻撃と防御の分類体系を整理した専門サーベイ
- [Attacks, Defenses and Evaluations for LLM Conversation Safety: A Survey](https://arxiv.org/abs/2402.09283) — *NAACL 2024* · 📈160。会話安全の攻撃・防御・評価を3分類で整理したNAACLサーベイ — [`niconi19/LLM-Conversation-Safety`](https://github.com/niconi19/LLM-Conversation-Safety) ⭐111🔴

### Tool Use

- [Tool Learning with Foundation Models](https://arxiv.org/abs/2304.08354) — *ACM Computing Surveys 2023* · 📈397。基盤モデルのツール学習を体系化し18種ツールで実証した代表的サーベイ — [`OpenBMB/BMTools`](https://github.com/OpenBMB/BMTools) ⭐2775🔴
- [What Are Tools Anyway? A Survey from the Language Model Perspective](https://arxiv.org/abs/2403.15452) — *COLM 2024* · 📈64。LM視点でツールを定義し利用効果と効率を実証分析したツール利用サーベイ

## 🎨 生成AI・拡散モデル

### 3D Generation

- [Generative AI meets 3D: A Survey on Text-to-3D in AIGC Era](https://arxiv.org/abs/2305.06131) — *arXiv 2023* · 📈102。忠実度・効率・一貫性等の観点でテキスト3D生成を整理したサーベイ
- [Advances in 3D Generation: A Survey](https://arxiv.org/abs/2401.17807) — *arXiv 2024* · 📈91。3D表現・生成手法・データ・応用を俯瞰した3D生成サーベイ

### AIGC General

- [A Comprehensive Survey of AI-Generated Content (AIGC): A History of Generative AI from GAN to ChatGPT](https://arxiv.org/abs/2303.04226) — *arXiv 2023* · 📈796。GANからChatGPTまで生成AIの歴史と単一/マルチモーダル生成を俯瞰

### Audio / Music Generation

- [Sparks of Large Audio Models: A Survey and Outlook](https://arxiv.org/abs/2308.12792) — *arXiv 2023* · 📈63。音声認識・TTS・音楽生成等の大規模音声モデルを概観したサーベイ — [`EmulationAI/awesome-large-audio-models`](https://github.com/EmulationAI/awesome-large-audio-models) ⭐731🟢

### Controllable Generation

- [Controllable Generation with Text-to-Image Diffusion Models: A Survey](https://arxiv.org/abs/2403.04279) — *IEEE TPAMI 2024* · 📈94。特定条件・複数条件・汎用制御の3分類で制御可能T2I生成を整理 — [`PRIV-Creation/Awesome-Controllable-T2I-Diffusion-Models`](https://github.com/PRIV-Creation/Awesome-Controllable-T2I-Diffusion-Models) ⭐1113🟡

### Diffusion Acceleration

- [Efficient Diffusion Models: A Comprehensive Survey from Principles to Practices](https://arxiv.org/abs/2410.11795) — *TMLR 2024* · 📈53。アーキ・学習・高速推論・展開の効率視点で拡散モデルを俯瞰したサーベイ — [`AIoT-MLSys-Lab/Efficient-Diffusion-Model-Survey`](https://github.com/AIoT-MLSys-Lab/Efficient-Diffusion-Model-Survey) ⭐184🟢

### GAN

- [A Review on Generative Adversarial Networks: Algorithms, Theory, and Applications](https://arxiv.org/abs/2001.06937) — *IEEE TKDE 2020* · 📈1108。GANのアルゴリズム・理論・応用を体系的に俯瞰した代表的レビュー

### Image Editing

- [Diffusion Model-Based Image Editing: A Survey](https://arxiv.org/abs/2402.17525) — *IEEE TPAMI 2024* · 📈263。学習戦略・入力条件・タスク別に拡散ベース画像編集を整理したサーベイ — [`SiatMMLab/Awesome-Diffusion-Model-Based-Image-Editing-Methods`](https://github.com/SiatMMLab/Awesome-Diffusion-Model-Based-Image-Editing-Methods) ⭐713🟡

### Normalizing Flow

- [Normalizing Flows: An Introduction and Review of Current Methods](https://arxiv.org/abs/1908.09257) — *IEEE TPAMI 2019* · 📈58。正規化フローの構築法と最新手法を整理した代表的レビュー

### Text-to-Image

- [RenAIssance: A Survey into AI Text-to-Image Generation in the Era of Large Model](https://arxiv.org/abs/2309.00810) — *IEEE TPAMI 2023* · 📈78。大規模モデル時代のテキスト画像生成を5節で俯瞰したTPAMIサーベイ

### Text-to-Video

- [A Survey on Video Diffusion Models](https://arxiv.org/abs/2310.10647) — *ACM Computing Surveys 2023* · 📈277。動画生成・編集・理解の3領域で動画拡散モデルを整理した代表的サーベイ — [`ChenHsing/Awesome-Video-Diffusion-Models`](https://github.com/ChenHsing/Awesome-Video-Diffusion-Models) ⭐2293🟢
- [Sora as a World Model? A Complete Survey on Text-to-Video Generation](https://arxiv.org/abs/2403.05131) — *arXiv 2024* · 📈72。250件超を世界モデルの観点で整理したテキスト動画生成サーベイ
- [Video Diffusion Models: A Survey](https://arxiv.org/abs/2405.03150) — *TMLR 2024* · 📈45。時間的一貫性や入力モダリティ別に動画拡散モデルを分類したサーベイ — [`ndrwmlnk/Awesome-Video-Diffusion-Models`](https://github.com/ndrwmlnk/Awesome-Video-Diffusion-Models) ⭐56🟡

### VAE

- [An Introduction to Variational Autoencoders](https://arxiv.org/abs/1906.02691) — *Foundations and Trends in ML 2019* · 📈3045。VAEの理論と実装を体系的に解説した定番の入門・総説

## 🖼️ マルチモーダル・視覚言語

### Audio-Visual

- [Deep Audio-Visual Learning: A Survey](https://arxiv.org/abs/2001.04758) — *International Journal of Automation and Computing 2020* · 📈191。分離・対応・生成・表現学習の4分野で音響視覚学習を整理した代表的サーベイ

### Document AI

- [Document AI: Benchmarks, Models and Applications](https://arxiv.org/abs/2111.08609) — *arXiv 2021* · 📈97。文書理解のベンチマーク・モデル・応用を俯瞰したDocument AIサーベイ

### Embodied Multimodal

- [A Survey on Vision-Language-Action Models for Embodied AI](https://arxiv.org/abs/2405.14093) — *arXiv 2024* · 📈266。身体化AI向けVision-Language-Action(VLA)モデルを整理したサーベイ
- [Agent AI: Surveying the Horizons of Multimodal Interaction](https://arxiv.org/abs/2401.03568) — *arXiv 2024* · 📈250。環境に接地したマルチモーダルエージェントAIの地平を俯瞰した総説

### Multimodal Agents

- [Large Multimodal Agents: A Survey](https://arxiv.org/abs/2402.15116) — *arXiv 2024* · 📈111。大規模マルチモーダルエージェント(LMA)の構成要素と協調枠組を整理 — [`jun0wanan/awesome-large-multimodal-agents`](https://github.com/jun0wanan/awesome-large-multimodal-agents) ⭐491🔴

### Multimodal Hallucination

- [Hallucination of Multimodal Large Language Models: A Survey](https://arxiv.org/abs/2404.18930) — *arXiv 2024* · 📈392。MLLMの視覚と不整合な出力(幻覚)の原因・評価・緩和を整理したサーベイ

### Multimodal LLM

- [A Survey on Multimodal Large Language Models](https://arxiv.org/abs/2306.13549) — *National Science Review 2023* · 📈1385。MLLMのアーキ・学習・データ・評価を整理した最も参照される代表的サーベイ — [`BradyFU/Awesome-Multimodal-Large-Language-Models`](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models) ⭐17857🟢
- [MM-LLMs: Recent Advances in MultiModal Large Language Models](https://arxiv.org/abs/2401.13601) — *ACL Findings 2024* · 📈423。126種MM-LLMの設計枠組と学習技術を分類したACLサーベイ — [project](https://mm-llms.github.io)

### Video-Language

- [Video-Language Understanding: A Survey from Model Architecture, Model Training, and Data Perspectives](https://arxiv.org/abs/2406.05615) — *ACL Findings 2024* · 📈42。アーキ・学習・データの3視点で動画言語理解を整理したACLサーベイ

### Vision-Language Pretraining

- [Vision-Language Pre-training: Basics, Recent Advances, and Future Trends](https://arxiv.org/abs/2210.09263) — *Foundations and Trends in CV 2022* · 📈214。画像テキスト・コアCV・動画テキストでVLP手法を俯瞰した大規模総説(102頁)

## 💬 自然言語処理 (NLP)

### Adversarial Attacks (NLP)

- [Adversarial Attacks on Deep Learning Models in Natural Language Processing: A Survey](https://arxiv.org/abs/1901.06796) — *ACM TIST 2019* · 📈57。テキストへの敵対的サンプル生成手法を網羅した定番サーベイ
- [A Survey of Adversarial Defences and Robustness in NLP](https://arxiv.org/abs/2203.06414) — *ACM Computing Surveys 2022* · 📈36。NLPの敵対的防御・頑健性手法を新分類学で整理
- [Adversarial Attacks and Defense on Texts: A Survey](https://arxiv.org/abs/2005.14108) — *arXiv 2020* · 📈24。テキスト敵対的攻撃を文字・単語・文・複数レベルで分類

### Coreference Resolution

- [A Neural Entity Coreference Resolution Review](https://arxiv.org/abs/1910.09329) — *Expert Systems with Applications 2019* · 📈43。ニューラル共参照解析の進展・データ・評価指標を整理

### Data Augmentation (NLP)

- [A Survey of Data Augmentation Approaches for NLP](https://arxiv.org/abs/2105.03075) — *Findings of ACL 2021* · 📈979。NLPのデータ拡張手法を体系的に整理した代表的サーベイ

### Dialogue Systems

- [A Survey on Dialogue Systems: Recent Advances and New Frontiers](https://arxiv.org/abs/1711.01731) — *ACM SIGKDD Explorations 2017* · 📈766。タスク指向型・非タスク指向型対話システムを概観した定番サーベイ
- [Recent Advances in Deep Learning Based Dialogue Systems: A Systematic Survey](https://arxiv.org/abs/2105.04387) — *Artificial Intelligence Review 2021* · 📈342。深層学習ベース対話システムを体系的に整理した大規模サーベイ
- [A Short Survey of Pre-trained Language Models for Conversational AI - A New Age in NLP](https://arxiv.org/abs/2104.10810) — *ACSW 2020* · 📈82。会話AIにおける事前学習言語モデル活用を簡潔に整理

### Evaluation & Benchmarks

- [A Survey of Evaluation Metrics Used for NLG Systems](https://arxiv.org/abs/2008.12009) — *ACM Computing Surveys 2020* · 📈329。NLG評価指標の発展(ヒューリスティック〜学習型)を整理
- [Survey on Factuality in Large Language Models: Knowledge, Retrieval and Domain-Specificity](https://arxiv.org/abs/2310.07521) — *arXiv 2023* · 📈286。LLMの事実性(factuality)を知識・検索・ドメイン観点で整理

### Explainability (NLP)

- [A Survey of the State of Explainable AI for Natural Language Processing](https://arxiv.org/abs/2010.00711) — *AACL-IJCNLP 2020* · 📈461。NLPの説明可能AI技術を概観した代表的サーベイ
- [Post-hoc Interpretability for Neural NLP: A Survey](https://arxiv.org/abs/2108.04840) — *ACM Computing Surveys 2021* · 📈312。ニューラルNLPの事後解釈手法を分類・検証法とともに整理
- [Local Interpretations for Explainable Natural Language Processing: A Survey](https://arxiv.org/abs/2103.11072) — *ACM Computing Surveys 2021* · 📈69。局所的解釈手法に焦点を当てた説明可能NLPのサーベイ

### Low-Resource & Multilingual

- [Neural Machine Translation for Low-Resource Languages: A Survey](https://arxiv.org/abs/2106.15115) — *ACM Computing Surveys 2021* · 📈359。低資源言語NMTの研究進展を定量分析付きで概観
- [A Survey on Low-Resource Neural Machine Translation](https://arxiv.org/abs/2107.04239) — *IJCAI 2021* · 📈75。低資源NMTの補助データ活用手法を3分類で整理

### Machine Translation

- [Neural Machine Translation: A Review and Survey](https://arxiv.org/abs/1912.02047) — *JAIR 2020* · 📈423。NMTのモデル・学習・推論を網羅した定番の包括的レビュー
- [A Survey of Deep Learning Techniques for Neural Machine Translation](https://arxiv.org/abs/2002.07526) — *arXiv 2020* · 📈153。ニューラル機械翻訳の深層学習技術を体系的に整理した入門的サーベイ
- [A Survey on Non-Autoregressive Generation for Neural Machine Translation and Beyond](https://arxiv.org/abs/2204.09269) — *IEEE TPAMI 2022* · 📈126。非自己回帰生成によるNMT高速化手法を整理したサーベイ

### Named Entity Recognition

- [A Survey on Deep Learning for Named Entity Recognition](https://arxiv.org/abs/1812.09449) — *IEEE TKDE 2020* · 📈1457。深層学習によるNERの定番サーベイ(分散表現・文脈エンコーダ等)
- [Recent Advances in Named Entity Recognition: A Comprehensive Survey and Comparative Study](https://arxiv.org/abs/2401.10825) — *arXiv 2024* · 📈47。Transformer/LLM時代のNER最新手法と比較実験を含むサーベイ

### Pretrained Language Models (BERT)

- [A Primer in BERTology: What We Know About How BERT Works](https://arxiv.org/abs/2002.12327) — *TACL 2020* · 📈1868。BERTの内部挙動に関する知見をまとめた定番BERTologyサーベイ
- [Pre-trained Models for Natural Language Processing: A Survey](https://arxiv.org/abs/2003.08271) — *Science China Technological Sciences 2020* · 📈1688。NLP事前学習モデルを4視点の分類学で整理した高被引用サーベイ
- [Recent Advances in Natural Language Processing via Large Pre-Trained Language Models: A Survey](https://arxiv.org/abs/2111.01243) — *ACM Computing Surveys 2021* · 📈1521。大規模事前学習モデルによるNLPの最近の進展を整理
- [Pre-Trained Models: Past, Present and Future](https://arxiv.org/abs/2106.07139) — *AI Open 2021* · 📈1064。事前学習モデルの過去・現在・未来を俯瞰した大規模レビュー

### Prompting

- [Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing](https://arxiv.org/abs/2107.13586) — *ACM Computing Surveys 2021* · 📈5397。プロンプト手法を体系化した最重要サーベイ(prompt paradigm) — [`thunlp/PromptPapers`](https://github.com/thunlp/PromptPapers) ⭐4313🔴

### Question Answering

- [A Survey on Complex Knowledge Base Question Answering: Methods, Challenges and Solutions](https://arxiv.org/abs/2105.11644) — *IJCAI 2021* · 📈206。複雑な知識ベースQA(KBQA)の手法と課題を整理
- [QA Dataset Explosion: A Taxonomy of NLP Resources for Question Answering and Reading Comprehension](https://arxiv.org/abs/2107.12708) — *ACM Computing Surveys 2021* · 📈196。QA/読解の大量データセットを分類学として体系化
- [A Survey on Neural Machine Reading Comprehension](https://arxiv.org/abs/1906.03824) — *arXiv 2019* · 📈32。ニューラル機械読解(MRC)の手法とデータセットを整理

### Relation Extraction

- [A Comprehensive Survey on Relation Extraction: Recent Advances and New Frontiers](https://arxiv.org/abs/2306.02051) — *ACM Computing Surveys 2023* · 📈127。関係抽出を表現・文脈・トリプル予測の3視点で整理した新分類学
- [A Survey of Deep Learning Methods for Relation Extraction](https://arxiv.org/abs/1705.03645) — *arXiv 2017* · 📈123。関係抽出における各種深層学習モデルの初期サーベイ

### Sentiment Analysis

- [Deep Learning for Sentiment Analysis: A Survey](https://arxiv.org/abs/1801.07883) — *WIREs Data Mining and Knowledge Discovery 2018* · 📈1886。感情分析への深層学習適用を概観した高被引用サーベイ
- [A Survey on Aspect-Based Sentiment Analysis: Tasks, Methods, and Challenges](https://arxiv.org/abs/2203.01054) — *IEEE TKDE 2022* · 📈407。アスペクトベース感情分析(ABSA)のタスク・手法・課題を体系化

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

### Word & Sentence Embeddings

- [A Survey on Contextual Embeddings](https://arxiv.org/abs/2003.07278) — *arXiv 2020* · 📈177。文脈化単語埋め込み(ELMo/BERT系)の手法と応用を整理
- [A Comprehensive Survey of Sentence Representations: From the BERT Epoch to the ChatGPT Era and Beyond](https://arxiv.org/abs/2305.12641) — *EACL 2024* · 📈21。文表現学習をBERT期からChatGPT期まで包括的に整理

## 🔊 音声・信号処理

### Automatic Speech Recognition (ASR)

- [A Review of Deep Learning Techniques for Speech Processing](https://arxiv.org/abs/2305.00359) — *Information Fusion 2023* · 📈338。音声処理全般の深層学習技術を網羅的に概観したレビュー
- [End-to-End Speech Recognition: A Survey](https://arxiv.org/abs/2303.03329) — *IEEE/ACM TASLP 2023* · 📈287。エンドツーエンドASRのモデル分類と古典HMM系との関係を整理

### Music Information Retrieval

- [A Tutorial on Deep Learning for Music Information Retrieval](https://arxiv.org/abs/1709.04396) — *arXiv 2017* · 📈102。音楽情報処理(MIR)への深層学習適用を解説したチュートリアル兼レビュー

### Self-Supervised Speech (wav2vec)

- [wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations](https://arxiv.org/abs/2006.11477) — *NeurIPS 2020* · 📈8392。自己教師あり音声表現学習の代表的基盤モデル(分野の基礎参照)
- [Self-Supervised Speech Representation Learning: A Review](https://arxiv.org/abs/2205.10643) — *IEEE JSTSP 2022* · 📈492。自己教師あり音声表現学習(wav2vec/HuBERT系)を網羅した定番レビュー

### Speaker Recognition & Diarization

- [A Review of Speaker Diarization: Recent Advances with Deep Learning](https://arxiv.org/abs/2101.09624) — *Computer Speech & Language 2021* · 📈427。話者ダイアライゼーションの深層学習による進展を整理した定番レビュー

### Speech Enhancement & Separation

- [Supervised Speech Separation Based on Deep Learning: An Overview](https://arxiv.org/abs/1708.07524) — *IEEE/ACM TASLP 2018* · 📈1583。深層学習による教師あり音声分離・強調を網羅した定番オーバービュー

### Speech Translation

- [Direct Speech-to-Speech Neural Machine Translation: A Survey](https://arxiv.org/abs/2411.14453) — *arXiv 2024* · 📈7。直接音声対音声翻訳(S2ST)のモデル・データ・評価を整理したサーベイ

### Text-to-Speech (TTS)

- [A Survey on Neural Speech Synthesis](https://arxiv.org/abs/2106.15561) — *arXiv 2021* · 📈466。ニューラル音声合成(テキスト解析・音響モデル・ボコーダ)の定番サーベイ

## 👁️ コンピュータビジョン (CV)

### 3D Object Detection

- [3D Object Detection for Autonomous Driving: A Comprehensive Survey](https://arxiv.org/abs/2206.09474) — *IJCV 2023* · 📈438。自動運転向け3D物体検出(LiDAR/カメラ/マルチモーダル)の包括サーベイ — [`PointsCoder/Awesome-3D-Object-Detection-for-Autonomous-Driving`](https://github.com/PointsCoder/Awesome-3D-Object-Detection-for-Autonomous-Driving) ⭐609🔴

### 3D Vision / Point Cloud

- [Deep Learning for 3D Point Clouds: A Survey](https://arxiv.org/abs/1912.12033) — *TPAMI 2021* · 📈2211。点群の分類/検出/セグメンテーションを網羅した定番サーベイ
- [Transformers in 3D Point Clouds: A Survey](https://arxiv.org/abs/2205.07417) — *arXiv 2022* · 📈73。3D点群解析へのTransformer適用を分類・整理した初の包括サーベイ

### Action Recognition

- [Human Action Recognition from Various Data Modalities: A Review](https://arxiv.org/abs/2012.11866) — *TPAMI 2023* · 📈773。RGB/骨格/深度など多様なモダリティでの行動認識を整理
- [Going Deeper into Action Recognition: A Survey](https://arxiv.org/abs/1605.04988) — *Image and Vision Computing 2017* · 📈640。行動認識の手作り表現から深層手法までの進化を俯瞰した定番サーベイ

### Adversarial Robustness

- [Threat of Adversarial Attacks on Deep Learning in Computer Vision: A Survey](https://arxiv.org/abs/1801.00553) — *IEEE Access 2018* · 📈2050。CVにおける敵対的攻撃と防御を初めて包括的に整理した定番サーベイ

### Anomaly Detection

- [Deep Learning for Anomaly Detection: A Review](https://arxiv.org/abs/2007.02500) — *CSUR 2021* · 📈1325。深層異常検知の手法を体系的な分類で整理したCSURレビュー

### Depth Estimation

- [Monocular Depth Estimation Based On Deep Learning: An Overview](https://arxiv.org/abs/2003.06620) — *Science China Technological Sciences 2020* · 📈294。単眼深度推定の深層手法・損失・学習戦略を概観したサーベイ

### Domain Adaptation

- [Deep Visual Domain Adaptation: A Survey](https://arxiv.org/abs/1802.03601) — *Neurocomputing 2018* · 📈2291。視覚タスク向け深層ドメイン適応をシナリオ別に分類した定番サーベイ

### Face Recognition

- [Deep Face Recognition: A Survey](https://arxiv.org/abs/1804.06655) — *Neurocomputing 2021* · 📈1421。深層顔認識のアルゴリズム/損失関数/データセットを網羅した定番サーベイ

### Few-Shot Learning

- [Generalizing from a Few Examples: A Survey on Few-Shot Learning](https://arxiv.org/abs/1904.05046) — *CSUR 2020* · 📈2117。少数ショット学習をデータ/モデル/アルゴリズム観点で整理した定番サーベイ
- [Few-Shot Object Detection: A Comprehensive Survey](https://arxiv.org/abs/2112.11699) — *TNNLS 2023* · 📈117。少数ショット物体検出手法の包括的な分類とサーベイ

### Foundation Models / Segmentation

- [A Comprehensive Survey on Segment Anything Model for Vision and Beyond](https://arxiv.org/abs/2305.08196) — *arXiv 2023* · 📈142。基盤モデルSAMの応用・限界を視覚分野横断で整理した初の包括サーベイ

### Image Captioning

- [A Comprehensive Survey of Deep Learning for Image Captioning](https://arxiv.org/abs/1810.04020) — *CSUR 2019* · 📈884。画像キャプション生成の深層手法・データセット・評価を整理したCSURサーベイ

### Image Classification / Backbone

- [A Survey of Convolutional Neural Networks: Analysis, Applications, and Prospects](https://arxiv.org/abs/2004.02806) — *TNNLS 2022* · 📈4169。CNNの歴史・代表モデル・応用を俯瞰したバックボーンサーベイ

### Image Generation (Diffusion)

- [Diffusion Models in Vision: A Survey](https://arxiv.org/abs/2209.04747) — *TPAMI 2023* · 📈2108。視覚タスクへの拡散モデル応用を理論・実装両面で整理 — [`CroitoruAlin/Diffusion-Models-in-Vision-A-Survey`](https://github.com/CroitoruAlin/Diffusion-Models-in-Vision-A-Survey) ⭐407🔴
- [Text-to-image Diffusion Models in Generative AI: A Survey](https://arxiv.org/abs/2303.07909) — *arXiv 2023* · 📈423。テキストから画像への拡散モデル生成と応用を整理したサーベイ

### Image Generation (GAN)

- [Generative Adversarial Networks: An Overview](https://arxiv.org/abs/1710.07035) — *IEEE Signal Processing Magazine 2018* · 📈3730。画像合成等を含むGANの学習・構築手法を概観した定番オーバービュー
- [GAN Inversion: A Survey](https://arxiv.org/abs/2101.05278) — *TPAMI 2022* · 📈632。実画像編集を支えるGANインバージョン手法のサーベイ — [`weihaox/GAN-Inversion`](https://github.com/weihaox/GAN-Inversion) ⭐1126🟡

### Image Restoration

- [Priors in Deep Image Restoration and Enhancement: A Survey](https://arxiv.org/abs/2206.02070) — *arXiv 2022* · 📈8。画像復元・強調における事前分布(prior)の観点で手法を整理 — [`yunfanLu/Awesome-Image-Prior`](https://github.com/yunfanLu/Awesome-Image-Prior) ⭐87🟡

### Medical Image Analysis

- [A Survey on Deep Learning in Medical Image Analysis](https://arxiv.org/abs/1702.05747) — *Medical Image Analysis 2017* · 📈13399。医用画像解析への深層学習応用を300本超で整理した古典的定番サーベイ
- [Transformers in Medical Imaging: A Survey](https://arxiv.org/abs/2201.09873) — *Medical Image Analysis 2023* · 📈1141。医用画像のセグメンテーション/分類/再構成等へのTransformer応用を整理

### Neural Rendering / NeRF

- [NeRF: Neural Radiance Field in 3D Vision: A Comprehensive Review](https://arxiv.org/abs/2210.00379) — *arXiv 2022* · 📈304。NeRFのアーキテクチャ/応用/性能を体系化した包括的レビュー
- [Neural Volume Rendering: NeRF And Beyond](https://arxiv.org/abs/2101.05204) — *arXiv 2021* · 📈71。ニューラルボリュームレンダリング(NeRF)の俯瞰レビュー

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

### Optical Flow

- [Optical Flow Estimation in the Deep Learning Age](https://arxiv.org/abs/2004.02853) — *arXiv 2020* · 📈41。古典的エネルギー最小化からCNNまでのオプティカルフロー推定を整理

### Person Re-identification

- [Deep Learning for Person Re-identification: A Survey and Outlook](https://arxiv.org/abs/2001.04193) — *TPAMI 2022* · 📈2133。人物再同定をclosed/open-world双方の観点で整理した定番サーベイ

### Pose Estimation

- [Deep Learning-Based Human Pose Estimation: A Survey](https://arxiv.org/abs/2012.13392) — *CSUR 2023* · 📈930。2D/3D人体姿勢推定の深層手法を250本超で整理したCSURサーベイ
- [2D Human Pose Estimation: A Survey](https://arxiv.org/abs/2204.07370) — *arXiv 2022* · 📈99。2D人体姿勢推定をネットワーク設計/学習/後処理の観点で整理

### Remote Sensing

- [Deep Learning in Remote Sensing: A Review](https://arxiv.org/abs/1710.03959) — *IEEE GRSM 2017* · 📈1845。リモートセンシングデータ解析への深層学習応用を整理した定番レビュー

### Salient Object Detection

- [Salient Object Detection in the Deep Learning Era: An In-Depth Survey](https://arxiv.org/abs/1904.09146) — *TPAMI 2022* · 📈728。深層学習時代の顕著性物体検出を体系的にベンチマーク・整理

### Self-Supervised Learning

- [A Survey on Contrastive Self-supervised Learning](https://arxiv.org/abs/2011.00362) — *Technologies 2021* · 📈1732。対照学習を中心とした自己教師あり学習のサーベイ
- [A Survey on Self-supervised Learning: Algorithms, Applications, and Future Trends](https://arxiv.org/abs/2301.05712) — *TPAMI 2024* · 📈519。自己教師あり学習のアルゴリズム/応用/動向を多角的に整理
- [Masked Image Modeling: A Survey](https://arxiv.org/abs/2408.06687) — *IJCV 2025* · 📈43。マスク画像モデリング(MIM)による自己教師あり事前学習のサーベイ

### Semantic Segmentation

- [Image Segmentation Using Deep Learning: A Survey](https://arxiv.org/abs/2001.05566) — *TPAMI 2022* · 📈3715。意味的/インスタンスセグメンテーションの深層手法を網羅した定番サーベイ
- [A Review on Deep Learning Techniques Applied to Semantic Segmentation](https://arxiv.org/abs/1704.06857) — *arXiv 2017* · 📈1380。意味的セグメンテーションの深層手法・データセット・評価を整理した初期定番
- [Transformer-Based Visual Segmentation: A Survey](https://arxiv.org/abs/2304.09854) — *TPAMI 2024* · 📈297。DETR系メタアーキを軸にしたTransformerベースのセグメンテーションサーベイ — [`lxtGH/Awesome-Segmentation-With-Transformer`](https://github.com/lxtGH/Awesome-Segmentation-With-Transformer) ⭐760🔴

### Super-Resolution

- [Deep Learning for Image Super-resolution: A Survey](https://arxiv.org/abs/1902.06068) — *TPAMI 2021* · 📈1788。画像超解像の深層手法を教師あり/なし/ドメイン特化で整理した定番サーベイ

### Video Segmentation

- [A Survey on Deep Learning Technique for Video Segmentation](https://arxiv.org/abs/2107.01153) — *TPAMI 2023* · 📈294。動画オブジェクト/意味セグメンテーションの深層手法を整理 — [`tfzhou/VS-Survey`](https://github.com/tfzhou/VS-Survey) ⭐204🔴

### Video Understanding

- [Video Transformers: A Survey](https://arxiv.org/abs/2201.05991) — *TPAMI 2023* · 📈165。動画モデリング向けTransformerの効率化と自己教師あり戦略を整理

### Vision Transformer

- [A Survey on Vision Transformer](https://arxiv.org/abs/2012.12556) — *TPAMI 2023* · 📈3572。Vision Transformerをタスク別に整理した高被引用サーベイ
- [Transformers in Vision: A Survey](https://arxiv.org/abs/2101.01169) — *CSUR 2022* · 📈3543。視覚タスク全般へのTransformer応用を網羅したACM CSURサーベイ
- [A Survey of Visual Transformers](https://arxiv.org/abs/2111.06091) — *TNNLS 2023* · 📈531。分類/検出/セグメンテーション軸で100超のViTを整理

### Vision-Language Models

- [Vision-Language Models for Vision Tasks: A Survey](https://arxiv.org/abs/2304.00685) — *TPAMI 2024* · 📈1369。視覚認識タスク向けVLMの事前学習/転移/蒸留を体系的に整理 — [`jingyi0000/VLM_survey`](https://github.com/jingyi0000/VLM_survey) ⭐3124🟡

### Zero-Shot Learning

- [Zero-Shot Learning -- A Comprehensive Evaluation of the Good, the Bad and the Ugly](https://arxiv.org/abs/1707.00600) — *TPAMI 2019* · 📈1831。ゼロショット学習の統一ベンチマーク・評価を提示した定番サーベイ

## 📈 機械学習 (一般)

### AutoML

- [AutoML: A Survey of the State-of-the-Art](https://arxiv.org/abs/1908.00709) — *Knowledge-Based Systems 2021* · 📈1793。データ準備からNASまでAutoMLパイプライン全体を概観したサーベイ

### Batch Normalization

- [How Does Batch Normalization Help Optimization?](https://arxiv.org/abs/1805.11604) — *NeurIPS 2018* · 📈1722。BatchNormが最適化地形を平滑化することを示した重要論文

### Bayesian Deep Learning

- [Hands-on Bayesian Neural Networks -- a Tutorial for Deep Learning Users](https://arxiv.org/abs/2007.06823) — *IEEE Computational Intelligence Magazine 2022* · 📈877。ベイズ深層学習の実践的チュートリアル兼概説

### Causal Machine Learning

- [Towards Causal Representation Learning](https://arxiv.org/abs/2102.11107) — *Proceedings of the IEEE 2021* · 📈358。因果性と表現学習の融合を論じた影響力の大きい概説

### Continual Learning

- [Continual Lifelong Learning with Neural Networks: A Review](https://arxiv.org/abs/1802.07569) — *Neural Networks 2019* · 📈3499。破滅的忘却と継続学習手法を整理した定番レビュー
- [A Comprehensive Survey of Continual Learning: Theory, Method and Application](https://arxiv.org/abs/2302.00487) — *TPAMI 2023* · 📈1391。継続学習を理論/手法/応用の3層で網羅した近年の包括サーベイ

### Data Augmentation

- [Time Series Data Augmentation for Deep Learning: A Survey](https://arxiv.org/abs/2002.12478) — *IJCAI 2021* · 📈821。時系列データ拡張手法を整理したサーベイ
- [Image Data Augmentation for Deep Learning: A Survey](https://arxiv.org/abs/2204.08610) — *arXiv 2022* · 📈388。画像データ拡張手法を体系的に分類したサーベイ

### Domain Adaptation

- [A Brief Review of Domain Adaptation](https://arxiv.org/abs/2010.03978) — *arXiv 2020* · 📈785。ドメイン適応の主要手法を簡潔に整理したレビュー

### Domain Generalization

- [Domain Generalization: A Survey](https://arxiv.org/abs/2103.02503) — *TPAMI 2022* · 📈1537。ドメイン汎化の手法分類とベンチマークを整理したサーベイ

### Dynamic Networks

- [Dynamic Neural Networks: A Survey](https://arxiv.org/abs/2102.04906) — *TPAMI 2022* · 📈897。入力依存で計算を変える動的ニューラルネットを整理したサーベイ

### Ensemble Learning

- [Ensemble deep learning: A review](https://arxiv.org/abs/2104.02395) — *Engineering Applications of AI 2022* · 📈1951。アンサンブル深層学習(bagging/boosting/stacking等)を概観したレビュー

### Explainable AI

- [Interpretable Deep Learning: Interpretation, Interpretability, Trustworthiness, and Beyond](https://arxiv.org/abs/2103.10689) — *Knowledge and Information Systems 2021* · 📈489。解釈/解釈可能性/信頼性の概念整理と手法分類を行ったサーベイ
- [Explainable Artificial Intelligence: a Systematic Review](https://arxiv.org/abs/2006.00093) — *arXiv 2020* · 📈316。XAI手法を体系的レビューで分類した網羅的サーベイ

### Fairness

- [A Survey on Bias and Fairness in Machine Learning](https://arxiv.org/abs/1908.09635) — *ACM Computing Surveys 2021* · 📈5855。機械学習のバイアスと公平性の定義/対策を網羅した高被引用サーベイ
- [What-is and How-to for Fairness in Machine Learning: A Survey, Reflection, and Perspective](https://arxiv.org/abs/2206.04101) — *ACM Computing Surveys 2023* · 📈40。公平性の定義と実現手法を反省的視点で整理したサーベイ

### Generalization

- [Understanding deep learning requires rethinking generalization](https://arxiv.org/abs/1611.03530) — *ICLR 2017* · 📈5121。ランダムラベル暗記実験で従来の汎化理論を覆した記念碑的論文(ICLR best paper)
- [Model Complexity of Deep Learning: A Survey](https://arxiv.org/abs/2103.05127) — *Knowledge and Information Systems 2021* · 📈392。深層学習のモデル複雑度と汎化の関係を整理したサーベイ

### Hyperparameter Optimization

- [Hyper-Parameter Optimization: A Review of Algorithms and Applications](https://arxiv.org/abs/2003.05689) — *arXiv 2020* · 📈676。ハイパーパラメータ最適化アルゴリズムを整理したレビュー

### Knowledge Distillation

- [Knowledge Distillation: A Survey](https://arxiv.org/abs/2006.05525) — *IJCV 2021* · 📈4212。知識蒸留の知識種別/スキーム/アルゴリズムを網羅した定番サーベイ

### Kolmogorov-Arnold Networks

- [KAN: Kolmogorov-Arnold Networks](https://arxiv.org/abs/2404.19756) — *ICLR 2024* · 📈1719。辺に学習可能活性化を置く新アーキテクチャKANの原論文 — [`KindXiaoming/pykan`](https://github.com/KindXiaoming/pykan) ⭐16299🟡
- [A Survey on Kolmogorov-Arnold Network](https://arxiv.org/abs/2411.06078) — *arXiv 2024* · 📈207。KANの理論/変種/応用を整理した近年のサーベイ

### Label-Noise Learning

- [Learning from Noisy Labels with Deep Neural Networks: A Survey](https://arxiv.org/abs/2007.08199) — *IEEE TNNLS 2022* · 📈1359。ノイズラベル下の頑健学習手法を体系化した定番サーベイ

### Meta-Learning

- [Meta-Learning in Neural Networks: A Survey](https://arxiv.org/abs/2004.05439) — *TPAMI 2022* · 📈2642。メタ学習の統一的分類法を提示した定番サーベイ

### Model Compression

- [A Survey of Model Compression and Acceleration for Deep Neural Networks](https://arxiv.org/abs/1710.09282) — *IEEE Signal Processing Magazine 2020* · 📈1234。枝刈り/量子化/蒸留など圧縮高速化手法を概観した高被引用サーベイ
- [Efficient Deep Learning: A Survey on Making Deep Learning Models Smaller, Faster, and Better](https://arxiv.org/abs/2106.08962) — *ACM Computing Surveys 2021* · 📈616。効率的深層学習の手法/インフラ/ハードを横断的に整理したサーベイ

### Multi-Task Learning

- [A Survey on Multi-Task Learning](https://arxiv.org/abs/1707.08114) — *IEEE TKDE 2021* · 📈2907。マルチタスク学習の手法を体系的に分類した定番サーベイ
- [Multi-Task Learning with Deep Neural Networks: A Survey](https://arxiv.org/abs/2009.09796) — *arXiv 2020* · 📈785。深層マルチタスク学習のアーキテクチャと最適化を整理したサーベイ

### Neural Architecture Search

- [Neural Architecture Search: Insights from 1000 Papers](https://arxiv.org/abs/2301.08727) — *arXiv 2023* · 📈219。1000本超の論文からNAS研究全体を俯瞰した近年の包括的サーベイ
- [Neural Architecture Search: A Survey](https://arxiv.org/abs/1808.05377) — *JMLR 2019*。探索空間/探索戦略/性能推定の3軸でNASを整理した代表的サーベイ

### Optimization

- [An overview of gradient descent optimization algorithms](https://arxiv.org/abs/1609.04747) — *arXiv 2016* · 📈6929。SGD/Momentum/Adam等の勾配降下最適化手法を概説した高被引用記事
- [A survey and taxonomy of loss functions in machine learning](https://arxiv.org/abs/2301.05579) — *arXiv 2023* · 📈51。機械学習における損失関数を網羅的に分類した近年のサーベイ

### Out-of-Distribution Detection

- [Generalized Out-of-Distribution Detection: A Survey](https://arxiv.org/abs/2110.11334) — *IJCV 2024* · 📈1391。OOD検出/異常検知/新規性検出を統一的枠組みで整理したサーベイ

### Pruning

- [The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks](https://arxiv.org/abs/1803.03635) — *ICLR 2019* · 📈4231。疎な訓練可能部分網の存在を示した宝くじ仮説の定番論文(ICLR best paper)
- [What is the State of Neural Network Pruning?](https://arxiv.org/abs/2003.03033) — *MLSys 2020* · 📈1254。枝刈り研究の評価不統一を指摘しメタ分析した重要サーベイ

### Quantization

- [A Survey of Quantization Methods for Efficient Neural Network Inference](https://arxiv.org/abs/2103.13630) — *arXiv 2021* · 📈1558。ニューラルネット量子化手法を体系的に整理した定番サーベイ

### Representation Learning

- [Recent Advances in Autoencoder-Based Representation Learning](https://arxiv.org/abs/1812.05069) — *NeurIPS Workshop 2018* · 📈504。オートエンコーダによる表現学習の最新進展を整理した概説

### Scaling Laws

- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) — *arXiv 2020* · 📈8125。モデル/データ/計算量に対する損失のべき乗則を示した記念碑的論文

### Self-Supervised Learning

- [Bootstrap your own latent: A new approach to self-supervised Learning](https://arxiv.org/abs/2006.07733) — *NeurIPS 2020* · 📈8575。負例なしで自己教師あり学習を達成したBYOLの代表論文
- [Self-Supervised Representation Learning: Introduction, Advances and Challenges](https://arxiv.org/abs/2110.09327) — *IEEE Signal Processing Magazine 2021* · 📈392。自己教師あり表現学習の入門と最新動向を整理した概説

### Semi-Supervised Learning

- [A survey on Semi-, Self- and Unsupervised Learning for Image Classification](https://arxiv.org/abs/2002.08721) — *IEEE Access 2021* · 📈187。半教師/自己教師/教師なし学習を横断的に比較したサーベイ

### State Space Models

- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) — *COLM 2023* · 📈7320。選択的状態空間で線形時間系列モデリングを実現したMambaの原論文 — [`state-spaces/mamba`](https://github.com/state-spaces/mamba) ⭐18373🟢

### Tabular Deep Learning

- [Deep Neural Networks and Tabular Data: A Survey](https://arxiv.org/abs/2110.01889) — *IEEE TNNLS 2022* · 📈1121。表形式データ向け深層学習手法を体系的に整理したサーベイ

### Transfer Learning

- [A Comprehensive Survey on Transfer Learning](https://arxiv.org/abs/1911.02685) — *Proceedings of the IEEE 2020* · 📈5774。転移学習の手法を機構別に分類した高被引用サーベイ
- [A Survey on Deep Transfer Learning](https://arxiv.org/abs/1808.01974) — *ICANN 2018* · 📈2897。深層転移学習を4カテゴリに分類した簡潔なサーベイ
- [A Survey on Negative Transfer](https://arxiv.org/abs/2009.00909) — *IEEE/CAA JAS 2022* · 📈357。転移学習で性能低下を招く負の転移を体系化したサーベイ

### Uncertainty Estimation

- [A Review of Uncertainty Quantification in Deep Learning: Techniques, Applications and Challenges](https://arxiv.org/abs/2011.06225) — *Information Fusion 2021* · 📈2574。深層学習の不確実性定量化技術を網羅した高被引用レビュー
- [A Survey of Uncertainty in Deep Neural Networks](https://arxiv.org/abs/2107.03342) — *Artificial Intelligence Review 2021* · 📈1764。DNNの不確実性の源泉と推定/較正手法を体系化したサーベイ

## 📐 学習理論

### Bandits

- [Introduction to Multi-Armed Bandits](https://arxiv.org/abs/1904.07272) — *Foundations and Trends in ML 2019* · 📈1248。多腕バンディットの理論を体系的にまとめた定番教科書/概説

### Deep Learning Theory

- [The Principles of Deep Learning Theory](https://arxiv.org/abs/2106.10165) — *Cambridge University Press 2022* · 📈285。有効場理論的アプローチで深層学習を解析した体系的教科書/概説
- [The Modern Mathematics of Deep Learning](https://arxiv.org/abs/2105.04026) — *Cambridge University Press 2022* · 📈134。深層学習理論(汎化/最適化/表現力)を数学的に俯瞰した包括的概説

### Generalization Bounds

- [Generalization in Deep Learning](https://arxiv.org/abs/1710.05468) — *Cambridge University Press 2022* · 📈499。深層学習の汎化に関する理論的洞察を整理した概説

### Neural Tangent Kernel

- [Neural Tangent Kernel: Convergence and Generalization in Neural Networks](https://arxiv.org/abs/1806.07572) — *NeurIPS 2018* · 📈4035。無限幅NNの学習を記述するNTKを導入した記念碑的論文

### Online Learning

- [Online Learning: A Comprehensive Survey](https://arxiv.org/abs/1802.02871) — *Neurocomputing 2021* · 📈811。オンライン学習の理論と手法を網羅した包括的サーベイ

### Optimization Theory

- [A Convergence Theory for Deep Learning via Over-Parameterization](https://arxiv.org/abs/1811.03962) — *ICML 2019* · 📈1629。過剰パラメータ化下でのSGDの大域収束を示した重要な理論論文

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

### Safe RL

- [A Review of Safe Reinforcement Learning: Methods, Theory and Applications](https://arxiv.org/abs/2205.10330) — *IEEE TPAMI 2024* · 📈322。2H3Wの観点で手法・理論・応用・ベンチマークを整理した近年の安全RLレビュー — [`chauncygu/Safe-Reinforcement-Learning-Baselines`](https://github.com/chauncygu/Safe-Reinforcement-Learning-Baselines) ⭐794🟢
- [A Survey of Constraint Formulations in Safe Reinforcement Learning](https://arxiv.org/abs/2402.02025) — *IJCAI 2024* · 📈65。安全RLの制約定式化を代表的アルゴリズムと数理的関係から整理したサーベイ
- [A Comprehensive Survey on Safe Reinforcement Learning](https://jmlr.org/papers/v16/garcia15a.html) — *JMLR 2015*。安全RLの最適性基準修正と探索修正アプローチを整理した古典的サーベイ

### Sim-to-Real

- [Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey](https://arxiv.org/abs/2009.13303) — *IEEE SSCI 2020* · 📈1008。ドメインランダム化・適応等のsim-to-real手法を概観したサーベイ

### Transfer Learning

- [Transfer Learning in Deep Reinforcement Learning: A Survey](https://arxiv.org/abs/2009.07888) — *IEEE TPAMI 2023* · 📈876。転移知識の形式と転移様式で深層RLの転移学習を分類したサーベイ

## 🤖 ロボティクス・身体性

### Autonomous Driving

- [Deep Reinforcement Learning for Autonomous Driving: A Survey](https://arxiv.org/abs/2002.00444) — *IEEE Transactions on Intelligent Transportation Systems 2022* · 📈2324。自動運転タスクへの(深層)RL適用を分類し展開上の課題を整理した定番サーベイ
- [A Survey of Deep Learning Techniques for Autonomous Driving](https://arxiv.org/abs/1910.07738) — *Journal of Field Robotics 2020* · 📈1698。知覚・計画・制御からEnd2Endまで自動運転の深層学習技術を概観した定番サーベイ
- [Survey of Deep Reinforcement Learning for Motion Planning of Autonomous Vehicles](https://arxiv.org/abs/2001.11231) — *IEEE Transactions on Intelligent Transportation Systems 2022* · 📈581。自動運転車の階層的運動計画問題に対する深層RLを整理したサーベイ
- [A Survey of Deep RL and IL for Autonomous Driving Policy Learning](https://arxiv.org/abs/2101.01993) — *IEEE Transactions on Intelligent Transportation Systems 2022* · 📈215。自動運転の方策学習における深層RLと深層模倣学習を整理したサーベイ
- [A Survey of Deep Reinforcement Learning Algorithms for Motion Planning and Control of Autonomous Vehicles](https://arxiv.org/abs/2105.14218) — *IEEE IV 2021* · 📈69。自動運転車の運動計画・制御に向けた深層RL手法を整理したサーベイ

### Embodied AI

- [A Survey of Embodied AI: From Simulators to Research Tasks](https://arxiv.org/abs/2103.04918) — *IEEE Transactions on Emerging Topics in Computational Intelligence 2022* · 📈511。シミュレータと探索・ナビ・EQAタスクを軸にEmbodied AIを概観

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

## 👥 マルチエージェント

### Cooperative MARL

- [A Review of Cooperative Multi-Agent Deep Reinforcement Learning](https://arxiv.org/abs/1908.03963) — *Applied Intelligence 2023* · 📈613。独立学習・価値分解・通信学習等5アプローチで協調MARLを整理
- [A Survey of Progress on Cooperative Multi-agent Reinforcement Learning in Open Environment](https://arxiv.org/abs/2312.01058) — *arXiv 2023* · 📈76。オープン環境での協調MARLの進展を整理した近年のサーベイ

### Emergent Communication

- [A Survey of Multi-Agent Deep Reinforcement Learning with Communication](https://arxiv.org/abs/2203.08975) — *AAMAS (JAAMAS) 2024* · 📈278。DIAL/CommNet等の通信付きMARL 41モデルを設計次元で分類

### Game Theory & Learning

- [An Overview of Multi-Agent Reinforcement Learning from Game Theoretical Perspective](https://arxiv.org/abs/2011.00583) — *arXiv 2020* · 📈216。ゲーム理論の視点でMARLの基礎から最前線までを自己完結的に整理

### MARL (deep)

- [Deep Reinforcement Learning for Multi-Agent Systems: A Review of Challenges, Solutions and Applications](https://arxiv.org/abs/1812.11794) — *IEEE Transactions on Cybernetics 2020* · 📈1008。非定常性・部分観測等のMADRL課題と解決策・応用を整理したサーベイ
- [A Survey and Critique of Multiagent Deep Reinforcement Learning](https://arxiv.org/abs/1810.05587) — *AAMAS (JAAMAS) 2019* · 📈707。MARLと深層RLの構成要素を結びつけ実践指針を示した定番サーベイ

### MARL (general)

- [Multi-Agent Reinforcement Learning: A Comprehensive Survey](https://arxiv.org/abs/2312.10256) — *arXiv 2024* · 📈64。ゲーム理論と機械学習を結びつけMARLの課題を体系化した包括サーベイ

### MARL (theory)

- [Multi-Agent Reinforcement Learning: A Selective Overview of Theories and Algorithms](https://arxiv.org/abs/1911.10635) — *Handbook of RL and Control 2021* · 📈1629。理論的裏付けのあるMARLアルゴリズムを選択的に概観したサーベイ

## 🕸️ グラフニューラルネット (GNN)

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

### Graph Contrastive Learning

- [Towards Graph Contrastive Learning: A Survey and Beyond](https://arxiv.org/abs/2405.11868) — *arXiv 2024* · 📈62。グラフ対照学習をデータ拡張・対照モード・最適化目的の観点で網羅

### Graph Generation

- [A Systematic Survey on Deep Generative Models for Graph Generation](https://arxiv.org/abs/2007.06686) — *IEEE TPAMI 2020* · 📈197。グラフ生成の深層生成モデルを体系的に整理したサーベイ

### Graph Pooling

- [Graph Pooling for Graph Neural Networks: Progress, Challenges, and Opportunities](https://arxiv.org/abs/2204.07321) — *IJCAI Survey Track 2023* · 📈124。GNNのグラフプーリング手法を分類し進展と課題を整理したサーベイ

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

### Molecular / Drug Discovery

- [Graph Neural Networks for the Prediction of Molecular Structure-Property Relationships](https://arxiv.org/abs/2208.04852) — *RSC (Machine Learning and Hybrid Modelling for Reaction Engineering) 2022* · 📈19。分子構造-物性予測のためのGNNを化学工学視点で解説したレビュー
- [A Survey of Graph Neural Networks for Drug Discovery: Recent Developments and Challenges](https://arxiv.org/abs/2509.07887) — *arXiv 2025* · 📈0。創薬向けGNNの最新動向（分子物性・DTI・DDI・新薬設計）を整理

### Scalable GNN

- [A Comprehensive Survey on Distributed Training of Graph Neural Networks](https://arxiv.org/abs/2211.05368) — *Proceedings of the IEEE 2022* · 📈44。大規模グラフ向けGNN分散学習手法を網羅的に整理したサーベイ

## 🔗 知識表現・知識グラフ

### Graph + LLM

- [A Survey of Large Language Models for Graphs](https://arxiv.org/abs/2405.08011) — *KDD 2024* · 📈136。グラフ向けLLM手法を分類したKDD24サーベイ（コンパニオンawesomeリスト付） — [`HKUDS/Awesome-LLM4Graph-Papers`](https://github.com/HKUDS/Awesome-LLM4Graph-Papers) ⭐370🟡
- [A Survey of Graph Meets Large Language Model: Progress and Future Directions](https://arxiv.org/abs/2311.12399) — *IJCAI 2024* · 📈108。LLMをenhancer/predictor/alignmentの役割で分類したサーベイ（awesomeリスト付） — [`yhLeeee/Awesome-LLMs-in-Graph-tasks`](https://github.com/yhLeeee/Awesome-LLMs-in-Graph-tasks) ⭐657🟡

### Knowledge Graph + LLM

- [Unifying Large Language Models and Knowledge Graphs: A Roadmap](https://arxiv.org/abs/2306.08302) — *IEEE TKDE 2023* · 📈1462。LLMとKGの統合をKG強化LLM/LLM強化KG/協調の3視点で整理した定番ロードマップ — [`RManLuo/Awesome-LLM-KG`](https://github.com/RManLuo/Awesome-LLM-KG) ⭐2598🟡
- [LLMs for Knowledge Graph Construction and Reasoning: Recent Capabilities and Future Opportunities](https://arxiv.org/abs/2305.13168) — *World Wide Web Journal 2023* · 📈271。LLMによるKG構築・推論の能力と課題を実験的に評価した論文

### Knowledge Graph Completion

- [A Review of Knowledge Graph Completion](https://arxiv.org/abs/2208.11652) — *Information (MDPI) 2022* · 📈92。知識グラフ補完（リンク予測）の手法を分類・比較した近年レビュー

### Knowledge Graph Embedding

- [A Review of Relational Machine Learning for Knowledge Graphs](https://arxiv.org/abs/1503.00759) — *Proceedings of the IEEE 2016* · 📈1724。知識グラフ向け関係機械学習（潜在変数・グラフ特徴）の古典的定番レビュー
- [A Survey of Knowledge Graph Embedding and Their Applications](https://arxiv.org/abs/2107.07842) — *arXiv 2021* · 📈69。翻訳ベースから拡張ベースまでKG埋め込み手法と応用を整理したサーベイ

### Knowledge Graph General

- [Knowledge Graphs](https://arxiv.org/abs/2003.02320) — *ACM Computing Surveys 2021* · 📈2456。知識グラフの定義・スキーマ・推論・品質を網羅した教科書的大著

### Knowledge Graph Reasoning

- [A Survey of Knowledge Graph Reasoning on Graph Types: Static, Dynamic, and Multimodal](https://arxiv.org/abs/2212.05767) — *IEEE TPAMI 2022* · 📈288。静的・動的・マルチモーダルの観点で知識グラフ推論を整理したサーベイ

### Neurosymbolic AI

- [From Statistical Relational to Neurosymbolic Artificial Intelligence: a Survey](https://arxiv.org/abs/2108.11451) — *Artificial Intelligence 2021* · 📈118。統計的関係学習からニューロシンボリックAIへの統合を整理したサーベイ

## 🎯 因果推論

### Causal Discovery

- [D'ya like DAGs? A Survey on Structure Learning and Causal Discovery](https://arxiv.org/abs/2103.02582) — *ACM Computing Surveys 2021* · 📈388。構造学習・因果発見手法を網羅的に整理した定番サーベイ
- [A Survey on Causal Discovery Methods for I.I.D. and Time Series Data](https://arxiv.org/abs/2303.15027) — *TMLR 2023* · 📈61。i.i.d.データと時系列データ双方の因果発見手法・ツールを整理した近年サーベイ

### Causal Inference

- [A Survey on Causal Inference](https://arxiv.org/abs/2002.02770) — *ACM TKDD 2021* · 📈672。潜在的結果枠組みの因果推論手法を伝統的・ML手法で整理した定番サーベイ

### Causality + LLM

- [Causal Inference with Large Language Model: A Survey](https://arxiv.org/abs/2409.09822) — *arXiv 2024* · 📈40。LLMを用いた因果推論（発見・効果推定）の最新研究を整理したサーベイ

### Treatment Effect Estimation

- [A Survey of Deep Causal Models and Their Industrial Applications](https://arxiv.org/abs/2209.08860) — *arXiv 2022* · 📈20。反実仮想に基づく深層因果モデルと産業応用を時系列・分類軸で整理
- [Causal Inference with Complex Treatments: A Survey](https://arxiv.org/abs/2407.14022) — *arXiv 2024* · 📈6。多値・連続・バンドル等の複雑な処置に対する因果推論手法を整理

## ⏱️ 時系列・時空間

### Spatio-Temporal Forecasting

- [Spatio-Temporal Graph Neural Networks: A Survey](https://arxiv.org/abs/2301.10569) — *arXiv 2023* · 📈55。時空間グラフニューラルネットの手法・応用・課題を整理したサーベイ

### Time Series Forecasting

- [Time Series Forecasting With Deep Learning: A Survey](https://arxiv.org/abs/2004.13408) — *Phil. Trans. R. Soc. A 2020* · 📈1885。深層学習による時系列予測（1段/多段・確率的予測）を整理した定番サーベイ
- [Transformers in Time Series: A Survey](https://arxiv.org/abs/2202.07125) — *IJCAI 2023* · 📈1452。時系列Transformerを予測・異常検知・分類で整理した定番サーベイ（リスト付） — [`qingsongedu/time-series-transformers-review`](https://github.com/qingsongedu/time-series-transformers-review) ⭐2985🔴
- [A Comprehensive Survey of Deep Learning for Time Series Forecasting: Architectural Diversity and Open Challenges](https://arxiv.org/abs/2411.05793) — *Artificial Intelligence Review 2024* · 📈88。MLP/CNN/RNN/GNN/Transformer/拡散/基盤モデル/Mambaを比較した網羅的サーベイ

### Time Series Foundation Models

- [Foundation Models for Time Series Analysis: A Tutorial and Survey](https://arxiv.org/abs/2403.14735) — *KDD 2024* · 📈390。時系列解析向け基盤モデルの設計・事前学習・応用を解説したKDD24チュートリアル
- [A Survey of Deep Learning and Foundation Models for Time Series Forecasting](https://arxiv.org/abs/2401.13912) — *arXiv 2024* · 📈69。深層学習と基盤モデルによる時系列予測を知識・言語モデルの観点で整理
- [Empowering Time Series Analysis with Foundation Models: A Comprehensive Survey](https://arxiv.org/abs/2405.02358) — *arXiv 2024* · 📈26。他モダリティ事前学習モデルの時系列適応を網羅的に整理したサーベイ

### Time Series Representation Learning

- [Self-Supervised Learning for Time Series Analysis: Taxonomy, Progress, and Prospects](https://arxiv.org/abs/2306.10125) — *IEEE TPAMI 2023* · 📈245。時系列SSLを生成・対照・敵対的に分類し10サブカテゴリで整理したサーベイ
- [Universal Time-Series Representation Learning: A Survey](https://arxiv.org/abs/2401.03717) — *ACM Computing Surveys 2024* · 📈45。汎用時系列表現学習の手法を3要素の新分類体系で整理したサーベイ

### Traffic Forecasting

- [STG4Traffic: A Survey and Benchmark of Spatial-Temporal Graph Neural Networks for Traffic Prediction](https://arxiv.org/abs/2307.00495) — *arXiv 2023* · 📈15。交通予測向け時空間GNNのサーベイ兼ベンチマーク（コンパニオンリスト付） — [`jwwthu/GNN4Traffic`](https://github.com/jwwthu/GNN4Traffic) ⭐1206🔴

## ⛏️ データマイニング

### Anomaly Detection

- [A Unifying Review of Deep and Shallow Anomaly Detection](https://arxiv.org/abs/2009.11732) — *Proceedings of the IEEE 2021* · 📈1026。深層・浅層の異常検知手法を統一的枠組みで整理した定番レビュー
- [Anomaly Detection: A Survey](https://doi.org/10.1145/1541880.1541882) — *ACM Computing Surveys 2009*。異常検知研究の体系を確立した古典的サーベイ(被引用1万超)

### Clustering

- [A Comprehensive Survey on Deep Clustering: Taxonomy, Challenges, and Future Directions](https://arxiv.org/abs/2206.07579) — *ACM Computing Surveys 2024* · 📈203。深層クラスタリングの分類体系と課題・将来方向を整理

### Frequent Pattern Mining

- [A Survey of Parallel Sequential Pattern Mining](https://arxiv.org/abs/1805.10515) — *ACM TKDD 2019* · 📈256。並列系列パターンマイニングの手法とフレームワークを概観

### Graph Anomaly Detection

- [A Comprehensive Survey on Graph Anomaly Detection with Deep Learning](https://arxiv.org/abs/2106.07178) — *IEEE TKDE 2023* · 📈799。グラフ上の深層異常検知をワンストップで整理した包括サーベイ

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

### Stream Mining

- [A Survey on Concept Drift Adaptation](https://doi.org/10.1145/2523813) — *ACM Computing Surveys 2014*。ストリーム学習における概念ドリフト適応の定番サーベイ

### Time Series Anomaly Detection

- [Deep Learning for Time Series Anomaly Detection: A Survey](https://arxiv.org/abs/2211.05244) — *ACM Computing Surveys 2024* · 📈560。時系列異常検知の深層モデルを体系的に分類した近年の包括サーベイ

### Time Series Mining

- [Deep Learning for Time Series Classification: A Review](https://arxiv.org/abs/1809.04356) — *Data Mining and Knowledge Discovery 2019* · 📈3243。時系列分類の深層アーキテクチャを大規模実証評価した定番レビュー
- [Deep Learning for Time Series Classification and Extrinsic Regression: A Current Survey](https://arxiv.org/abs/2302.02515) — *ACM Computing Surveys 2024* · 📈270。時系列分類・回帰の深層手法を最新状況まで整理

## 🗄️ データベース・データ管理

### Approximate Nearest Neighbor Search

- [A Comprehensive Survey and Experimental Comparison of Graph-Based Approximate Nearest Neighbor Search](https://arxiv.org/abs/2101.12631) — *PVLDB 2021* · 📈360。13のグラフベースANNS手法を統一分類・実験比較した定番サーベイ — [`Lsyhprum/WEAVESS`](https://github.com/Lsyhprum/WEAVESS) ⭐80🔴

### Cloud and Serverless

- [The Serverless Computing Survey: A Technical Primer for Design Architecture](https://arxiv.org/abs/2112.12921) — *ACM Computing Surveys 2022* · 📈197。サーバレス計算の設計アーキテクチャを技術的に総覧したサーベイ

### Data Cleaning

- [Data Cleaning: Overview and Emerging Challenges](https://doi.org/10.1145/2882903.2912574) — *SIGMOD 2016*。データクリーニングの分類体系と統計的推定枠組みを提示した定番チュートリアル

### Data Pricing

- [A Survey on Data Pricing: from Economics to Data Science](https://arxiv.org/abs/2009.04462) — *IEEE TKDE 2022* · 📈172。経済学からデータサイエンスまでデータ価格付けを横断的に整理

### Entity Resolution

- [End-to-End Entity Resolution for Big Data: A Survey](https://arxiv.org/abs/1905.06397) — *ACM Computing Surveys 2021* · 📈67。ブロッキングからマッチングまでER全工程を網羅した定番サーベイ

### Learned Index

- [The Case for Learned Index Structures](https://arxiv.org/abs/1712.01208) — *SIGMOD 2018* · 📈1229。インデックスをモデルと捉える学習型インデックスを提唱した起点論文
- [A Survey of Learned Indexes for the Multi-dimensional Space](https://arxiv.org/abs/2403.06456) — *arXiv 2024* · 📈24。多次元空間向け学習型インデックスを分類整理したサーベイ

### ML for Query Optimization

- [A Survey on Advancing the DBMS Query Optimizer: Cardinality, Cost Model, and Plan Enumeration](https://arxiv.org/abs/2101.01507) — *Data Science and Engineering 2021* · 📈115。学習型のカーディナリティ推定・コストモデル・プラン列挙を概観

### Vector Database

- [Survey of Vector Database Management Systems](https://arxiv.org/abs/2310.14021) — *The VLDB Journal 2024* · 📈173。20超の商用ベクトルDBの記憶・索引戦略を整理した包括サーベイ

## 🔍 情報検索 (IR)

### Conversational Search

- [Conversational Information Seeking](https://arxiv.org/abs/2201.08808) — *Foundations and Trends in Information Retrieval 2023* · 📈128。対話的情報探索の定義・設計・評価を網羅した包括的モノグラフ
- [A Survey of Conversational Search](https://arxiv.org/abs/2410.15576) — *ACM TOIS 2025* · 📈44。クエリ再定式化・明確化・検索・応答生成と LLM 統合を網羅した会話検索サーベイ

### Dense Retrieval

- [Dense Text Retrieval based on Pretrained Language Models: A Survey](https://arxiv.org/abs/2211.14876) — *ACM TOIS 2024* · 📈304。アーキテクチャ・学習・索引・統合の4軸でdense retrievalを整理 — [`RUCAIBox/DenseRetrieval`](https://github.com/RUCAIBox/DenseRetrieval) ⭐221🔴

### Generative Retrieval

- [A Survey of Generative Information Retrieval](https://arxiv.org/abs/2406.01197) — *ACM TOIS 2025* · 📈5。クエリからDocIDを直接生成する生成型検索を体系的に整理 — [`RUC-NLPIR/GenIR-Survey`](https://github.com/RUC-NLPIR/GenIR-Survey) ⭐207🟡

### Learning to Rank

- [Learning to Rank for Information Retrieval](https://doi.org/10.1561/1500000016) — *Foundations and Trends in Information Retrieval 2009*。pointwise/pairwise/listwiseを整理したランキング学習の定番教科書的サーベイ

### Neural IR

- [Pre-training Methods in Information Retrieval](https://arxiv.org/abs/2111.13853) — *Foundations and Trends in Information Retrieval 2022* · 📈11。IR各コンポーネントへの事前学習手法適用を体系的に整理
- [An Introduction to Neural Information Retrieval](https://doi.org/10.1561/1500000061) — *Foundations and Trends in Information Retrieval 2018*。ニューラルIRの基礎を古典手法と対比して解説した入門サーベイ

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

### Graph-based Recommendation

- [Graph Neural Networks in Recommender Systems: A Survey](https://arxiv.org/abs/2011.02260) — *ACM Computing Surveys 2022* · 📈1768。GNNベース推薦を情報種別とタスクで分類した定番サーベイ — [`wusw14/GNN-in-RS`](https://github.com/wusw14/GNN-in-RS) ⭐307🔴
- [Graph Learning based Recommender Systems: A Review](https://arxiv.org/abs/2105.06339) — *IJCAI 2021* · 📈241。グラフ学習ベース推薦を初めて体系的に整理したレビュー

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

### Computational Social Science

- [Data-driven Computational Social Science: A Survey](https://arxiv.org/abs/2008.12372) — *Big Data Research 2021* · 📈66。個人・関係・集団の3視点で計算社会科学の人間ダイナミクス研究を整理

### Fake News Detection

- [Fake News Detection on Social Media: A Data Mining Perspective](https://arxiv.org/abs/1708.01967) — *ACM SIGKDD Explorations 2017* · 📈3243。データマイニング視点でフェイクニュース検出を整理した高被引用サーベイ

### Misinformation Detection

- [Combating Misinformation in the Age of LLMs: Opportunities and Challenges](https://arxiv.org/abs/2311.05656) — *AI Magazine 2024* · 📈201。LLM時代の誤情報生成・検出の機会と課題を整理したサーベイ — [`llm-misinformation/llm-misinformation-survey`](https://github.com/llm-misinformation/llm-misinformation-survey) ⭐106🔴

### Social Network Analysis

- [A Comprehensive Survey on Community Detection with Deep Learning](https://arxiv.org/abs/2105.12584) — *IEEE TNNLS 2024* · 📈439。コミュニティ検出の深層手法を分類体系で整理した包括サーベイ

## 🛡️ 信頼できるAI (公平性・XAI・安全性)

### AI Fairness / Bias

- [The Frontiers of Fairness in Machine Learning](https://arxiv.org/abs/1810.08810) — *arXiv 2018* · 📈436。ML公平性の未解決問題と研究フロンティアを整理した展望論文
- [Bias Mitigation for Machine Learning Classifiers: A Comprehensive Survey](https://arxiv.org/abs/2207.07068) — *ACM JRC 2022* · 📈275。分類器のバイアス緩和手法341本を網羅した包括的サーベイ

### AI Governance / Ethics

- [Worldwide AI Ethics: a review of 200 guidelines and recommendations for AI governance](https://arxiv.org/abs/2206.11922) — *Patterns 2022* · 📈244。世界の200のAI倫理ガイドラインをメタ分析した大規模レビュー

### AI Safety

- [Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565) — *arXiv 2016* · 📈3140。AI安全性の具体的課題を提起した分野定義的論文

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

### Membership Inference

- [Membership Inference Attacks on Machine Learning: A Survey](https://arxiv.org/abs/2103.07853) — *ACM Computing Surveys 2021* · 📈681。メンバーシップ推論攻撃と防御を初めて包括的に分類したサーベイ

### Model Interpretability

- [Towards A Rigorous Science of Interpretable Machine Learning](https://arxiv.org/abs/1702.08608) — *arXiv 2017* · 📈5099。解釈可能MLの定義と評価枠組みを提起した影響力の高い論文
- [Interpretable Machine Learning: Fundamental Principles and 10 Grand Challenges](https://arxiv.org/abs/2103.11251) — *Statistics Surveys 2021* · 📈947。解釈可能MLの基本原則と10の重要課題を提示した必読サーベイ

### Privacy-Preserving ML

- [A Survey of Privacy Attacks in Machine Learning](https://arxiv.org/abs/2007.07646) — *ACM Computing Surveys 2020* · 📈328。MLに対するプライバシー攻撃を網羅的に分類したサーベイ
- [Privacy-Preserving Machine Learning: Methods, Challenges and Directions](https://arxiv.org/abs/2108.04417) — *arXiv 2021* · 📈163。プライバシー保護MLの手法・課題・研究ロードマップを整理

### XAI Evaluation

- [From Anecdotal Evidence to Quantitative Evaluation Methods: A Systematic Review on Evaluating Explainable AI](https://arxiv.org/abs/2201.08164) — *ACM Computing Surveys 2022* · 📈674。XAI評価の12特性を提案し300本超の評価実践を系統レビュー

## 📡 連合学習

### Communication Efficiency

- [Federated Learning: Strategies for Improving Communication Efficiency](https://arxiv.org/abs/1610.05492) — *NeurIPS Workshop 2016* · 📈5409。連合学習の通信効率改善手法を提案した基礎論文

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

## 🖐️ HCI・ヒューマンAI

### AI-Assisted Decision Making

- [Towards a Science of Human-AI Decision Making: A Survey of Empirical Studies](https://arxiv.org/abs/2112.11471) — *arXiv 2021* · 📈235。AI支援意思決定の実証研究100本超を設計軸で整理したサーベイ

### Crowdsourcing (HCOMP)

- [Quality Control in Crowdsourcing: A Survey of Quality Attributes, Assessment Techniques and Assurance Actions](https://arxiv.org/abs/1801.02546) — *ACM Computing Surveys 2018* · 📈194。クラウドソーシングの品質管理を属性・評価・保証で体系化

### Explainability & HCI

- [Human-Centered Explainable AI (XAI): From Algorithms to User Experiences](https://arxiv.org/abs/2110.10790) — *arXiv 2021* · 📈325。人間中心XAIをアルゴリズムからUXまで概観した書籍章サーベイ
- [Towards Human-centered Explainable AI: A Survey of User Studies for Model Explanations](https://arxiv.org/abs/2210.11584) — *IEEE TPAMI 2022* · 📈219。XAIのユーザ研究97本を信頼・理解・協調の観点で系統レビュー

### Human-AI Interaction

- [A Survey on Human-AI Collaboration with Large Foundation Models](https://arxiv.org/abs/2403.04931) — *arXiv 2024* · 📈14。基盤モデル時代の人間-AI協調を設計・倫理・応用で概観

### Human-in-the-loop

- [A Survey of Human-in-the-loop for Machine Learning](https://arxiv.org/abs/2108.00941) — *Future Generation Computer Systems 2021* · 📈749。human-in-the-loop機械学習をデータ視点で整理したサーベイ

### Visualization for ML

- [A Survey of Visual Analytics Techniques for Machine Learning](https://arxiv.org/abs/2008.09632) — *Computational Visual Media 2020* · 📈272。機械学習向けビジュアルアナリティクス259本を分類したサーベイ

## 🧬 進化計算

### Black-box Optimization

- [A Tutorial on Bayesian Optimization](https://arxiv.org/abs/1807.02811) — *arXiv 2018* · 📈2332。ベイズ最適化(ブラックボックス最適化)の定番チュートリアル

### Evolutionary Deep Learning

- [Survey on Evolutionary Deep Learning: Principles, Algorithms, Applications and Open Issues](https://arxiv.org/abs/2208.10658) — *ACM Computing Surveys 2022* · 📈114。進化計算による深層学習設計(EDL)の原理と手法を概観

### Evolutionary NAS

- [A Survey on Evolutionary Neural Architecture Search](https://arxiv.org/abs/2008.10937) — *IEEE TNNLS 2020* · 📈570。進化計算ベースのニューラルアーキテクチャ探索200本超を整理

### Evolutionary RL

- [Combining Evolution and Deep Reinforcement Learning for Policy Search: a Survey](https://arxiv.org/abs/2203.14009) — *ACM TELO 2022* · 📈66。進化計算と深層強化学習の融合手法を統一枠組みで概観

### Multi-objective Optimization

- [A Review of Evolutionary Multi-modal Multi-objective Optimization](https://arxiv.org/abs/2009.13347) — *IEEE TEVC 2020* · 📈193。進化的マルチモーダル多目的最適化をレビューした論文

### Neuroevolution

- [Neuroevolution in Deep Neural Networks: Current Trends and Future Challenges](https://arxiv.org/abs/2006.05415) — *IEEE TETCI 2020* · 📈174。深層ニューラルネットへの進化的アルゴリズム適用を概観

## 🔢 理論計算機科学

### Algorithmic Fairness Testing

- [Fairness Testing: A Comprehensive Survey and Analysis of Trends](https://arxiv.org/abs/2207.10223) — *ACM TOSEM 2022* · 📈140。ソフトウェア工学の観点で公平性テスト手法を体系化したサーベイ

### Differentiable Optimization

- [Differentiable Convex Optimization Layers in Neural Architectures: Foundations and Perspectives](https://arxiv.org/abs/2412.20679) — *arXiv 2024* · 📈2。微分可能最適化層の基礎と発展を概観したサーベイ

## 🔬 AI for Science

### AI Drug Discovery

- [Deep Learning Methods for Small Molecule Drug Discovery: A Survey](https://arxiv.org/abs/2303.00313) — *IEEE TKDE 2023* · 📈23。低分子創薬の深層学習(生成・物性予測・逆合成)を概観

### AI Physics Simulation

- [Scientific Machine Learning through Physics-Informed Neural Networks: Where we are and What's next](https://arxiv.org/abs/2201.05624) — *Journal of Scientific Computing 2022* · 📈2297。物理情報ニューラルネット(PINN)の現状と展望を概観

### AI for Science (Overview)

- [A Survey of Deep Learning for Scientific Discovery](https://arxiv.org/abs/2003.11755) — *arXiv 2020* · 📈153。科学的発見のための深層学習を網羅的に概観したサーベイ

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

### AI x Finance

- [Deep Learning for Financial Applications : A Survey](https://arxiv.org/abs/2002.05786) — *Applied Soft Computing 2020* · 📈498。金融応用への深層学習をサブ分野・モデル別に整理した高被引用サーベイ

### AI x Healthcare

- [Deep EHR: A Survey of Recent Advances in Deep Learning Techniques for Electronic Health Record (EHR) Analysis](https://arxiv.org/abs/1706.03446) — *IEEE JBHI 2018* · 📈1436。電子カルテ解析への深層学習応用を構造・技術・臨床応用面で整理したサーベイ

### AI x Networking

- [Deep Learning in Mobile and Wireless Networking: A Survey](https://arxiv.org/abs/1803.04311) — *IEEE Communications Surveys & Tutorials 2019* · 📈1495。モバイル/無線ネットワーク研究への深層学習応用を横断的に整理した定番サーベイ

### AI x Software Engineering

- [A Survey on Deep Learning for Software Engineering](https://arxiv.org/abs/2011.14597) — *ACM Computing Surveys 2022* · 📈234。20主要会議誌の142本を分析しSEタスクへの深層学習応用を分類したサーベイ

## 📊 データ中心AI・評価

### Active Learning

- [A Survey of Deep Active Learning](https://arxiv.org/abs/2009.00236) — *ACM Computing Surveys 2022* · 📈1479。深層能動学習の初の包括レビュー。クエリ戦略やラベリングコスト削減手法を整理

### Data-Centric AI

- [Data-centric Artificial Intelligence: A Survey](https://arxiv.org/abs/2303.10158) — *ACM Computing Surveys 2025* · 📈427。学習/推論データ開発とデータ保守の3目標でデータ中心AIを俯瞰したサーベイ — [`daochenzha/data-centric-AI`](https://github.com/daochenzha/data-centric-AI) ⭐1149🔴

### Dataset Distillation

- [Dataset Distillation: A Comprehensive Review](https://arxiv.org/abs/2301.07014) — *IEEE TPAMI 2024* · 📈195。合成サンプルで小規模代替データを生成するデータ蒸留の近年の進展を整理したレビュー
- [A Comprehensive Survey of Dataset Distillation](https://arxiv.org/abs/2301.05603) — *IEEE TPAMI 2024* · 📈172。データ蒸留のフレームワーク・アルゴリズム・分解型手法・応用を整理したサーベイ

## 貢献

追加・修正は [`contributing.md`](contributing.md) を参照。サーベイ論文 (survey/review/overview) のみを対象とし、実在検証 (arXiv/DOI/GitHub) を経たもののみ掲載します。

## ライセンス

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](LICENSE) 本リスト（キュレーション）は CC0 (パブリックドメイン)。各論文の著作権は原著者に帰属します。
