# 調査ノート — Awesome AI Survey Papers

本ドキュメントは収集した全サーベイ論文のメタデータ・統計・調査手法をまとめたもの。READMEは分類済みリストに徹し、ここに全調査結果を集約する。最終更新 2026-07-12。

## 調査手法と飽和判定

分野fan-out 並列収集 → 反復波で純増の逓減を観測 → 飽和で終了、という手順を採った（詳細は [`docs/best-practice.md`](best-practice.md)）。各波は分野クラスタ単位で複数の収集エージェントを並列起動し、各エージェントが arXiv abs ページの照合・`gh api` によるcompanion repo 実在確認を経た JSON を出力。親が全 raw をマージ→ arXiv ID/正規化タイトルで重複排除→ Semantic Scholar batch API で被引用数を付与した。

| 波 | 収集テーマ | 重複排除後の累計 | 純増 |
|---|---|---:|---:|
| 第1波 | 主要17分野クラスタ(CV/NLP/LLM/ML/RL/DM・DB・IR/GNN/信頼AI/AI全般 等) | 490 | +490 |
| 第2波 | 薄い分野深掘り・新興ニッチ・GitHubトピック掃き出し・応用横断・知識/DB/DM | 697 | +207 |
| 第3波 | CV深掘り・NLP/古典ML niche・causal/federated/time-series・未収録掃き出し | 889 | +192 |
| 第4波 | 残る薄い分野(tcs/web/hci/ir/evolutionary等)の最終補強・網羅性メタ監査 | 955 | +66 |

**飽和判定**: 純増が +207 → +192 → +66 と明確に逓減。第4波の網羅性監査では「必ずあるべき定番サーベイ」の未収録が24件のみで、その大半が2010年代前半の古典層（最新サーベイは既に高網羅）。rl/knowledge/llm/multimodal/multi-agent/federated/time-series/recsys 等は探索した定番候補がほぼ全て既収録で飽和に近いと判定された。**新規の良質サーベイが見つかりにくくなったため、ここで収集を一旦終了する**。

**良質な単独サーベイが構造的に乏しいテーマ**（無理に水増しせず明記）: 進化計算の細分(共進化/EDA/メメティック/品質多様性/オープンエンド進化、多くが書籍章や原著)、TCSのゼロ次最適化・微分可能プログラミング(会議録中心)、HCIのAIフェアネス×ユーザ知覚(実証研究中心で決定版サーベイ無し)、音声匿名化(手法論文中心)。

## 統計

- 総数: **955** 本
- 分野数: 30
- companion GitHub 付き: 122 件
- arXiv ID あり: 940 件
- 被引用数取得済み: 834 件
- 出版年の分布: 2008:1, 2009:3, 2010:2, 2012:1, 2013:4, 2014:2, 2015:6, 2016:9, 2017:22, 2018:30, 2019:38, 2020:78, 2021:114, 2022:125, 2023:146, 2024:231, 2025:138, 2026:5

### 分野別件数

| 分野 | 件数 | サブ分野数 |
|---|---:|---:|
| 大規模言語モデル (LLM) | 82 | 49 |
| 生成AI・拡散モデル | 30 | 23 |
| マルチモーダル・視覚言語 | 22 | 18 |
| 自然言語処理 (NLP) | 79 | 47 |
| 音声・信号処理 | 24 | 18 |
| コンピュータビジョン (CV) | 108 | 79 |
| 機械学習 (一般) | 101 | 72 |
| 学習理論 | 18 | 12 |
| 強化学習 (RL) | 34 | 26 |
| ロボティクス・身体性 | 22 | 14 |
| マルチエージェント | 21 | 18 |
| グラフニューラルネット (GNN) | 33 | 27 |
| 知識表現・知識グラフ | 30 | 24 |
| 因果推論 | 15 | 13 |
| 時系列・時空間 | 20 | 14 |
| データマイニング | 29 | 20 |
| データベース・データ管理 | 17 | 13 |
| 情報検索 (IR) | 17 | 13 |
| 推薦システム | 21 | 17 |
| Web・ソーシャル | 21 | 18 |
| 信頼できるAI (公平性・XAI・安全性) | 31 | 21 |
| 連合学習 | 19 | 15 |
| HCI・ヒューマンAI | 18 | 15 |
| 進化計算 | 13 | 13 |
| 理論計算機科学 | 18 | 15 |
| AI for Science | 20 | 19 |
| 人工知能 (全般) | 15 | 13 |
| ニューラルネット基礎 | 30 | 22 |
| 応用・横断領域 | 29 | 29 |
| データ中心AI・評価 | 18 | 13 |

## 被引用数トップ30

| 被引用 | タイトル | venue | 年 |
|---:|---|---|---:|
| 22413 | Training language models to follow instructions with human feedback | NeurIPS | 2022 |
| 17608 | Deep Learning in Neural Networks: An Overview | Neural Networks | 2015 |
| 14029 | Representation Learning: A Review and New Perspectives | IEEE TPAMI | 2013 |
| 13770 | A Survey on Deep Learning in Medical Image Analysis | Medical Image Analysis | 2017 |
| 11484 | A Comprehensive Survey on Graph Neural Networks | IEEE TNNLS | 2021 |
| 8944 | Advances and Open Problems in Federated Learning | FnT in ML | 2019 |
| 8758 | Bootstrap your own latent: A new approach to self-supervised Learning | NeurIPS | 2020 |
| 8734 | wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Repres | NeurIPS | 2020 |
| 7125 | Graph Neural Networks: A Review of Methods and Applications | AI Open | 2020 |
| 6831 | On the Opportunities and Risks of Foundation Models | arXiv | 2021 |
| 6127 | Federated Learning: Challenges, Methods, and Future Directions | IEEE Signal Processing Magazine | 2019 |
| 5992 | Recent Advances in Convolutional Neural Networks | Pattern Recognition | 2018 |
| 5801 | Variational Inference: A Review for Statisticians | JASA | 2017 |
| 5544 | Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Metho | ACM Computing Surveys | 2021 |
| 5487 | Federated Learning: Strategies for Improving Communication Efficiency | NeurIPS Workshop | 2016 |
| 5262 | Towards A Rigorous Science of Interpretable Machine Learning | arXiv | 2017 |
| 5083 | Fundamentals of Recurrent Neural Network (RNN) and Long Short-Term Mem | Physica D | 2020 |
| 5059 | A Survey of Methods for Explaining Black Box Models | ACM Computing Surveys | 2018 |
| 4664 | A Survey of Large Language Models | arXiv | 2023 |
| 4297 | A Survey of Convolutional Neural Networks: Analysis, Applications, and | TNNLS | 2022 |
| 3789 | Generative Adversarial Networks: An Overview | IEEE Signal Processing Magazine | 2018 |
| 3783 | Image Segmentation Using Deep Learning: A Survey | TPAMI | 2022 |
| 3713 | A Survey on Vision Transformer | TPAMI | 2023 |
| 3677 | Efficient Processing of Deep Neural Networks: A Tutorial and Survey | Proceedings of the IEEE | 2017 |
| 3648 | Transformers in Vision: A Survey | CSUR | 2022 |
| 3646 | Retrieval-Augmented Generation for Large Language Models: A Survey | arXiv | 2024 |
| 3581 | Deep Reinforcement Learning: A Brief Survey | IEEE Signal Processing Magazine | 2017 |
| 3459 | Object Detection in 20 Years: A Survey | Proceedings of the IEEE | 2023 |
| 3309 | Fake News Detection on Social Media: A Data Mining Perspective | ACM SIGKDD Explorations | 2017 |
| 3303 | Deep Learning for Time Series Classification: A Review | Data Mining and Knowledge Discovery | 2019 |

## companion GitHub リポジトリ（star順・実在検証済み）

| ⭐star | repo | 最終更新 | 論文 |
|---:|---|---|---|
| 17939 | [BradyFU/Awesome-Multimodal-Large-Language-Models](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models) | 2026-07-02 | A Survey on Multimodal Large Language Models |
| 12186 | [RUCAIBox/LLMSurvey](https://github.com/RUCAIBox/LLMSurvey) | 2025-03-11 | A Survey of Large Language Models |
| 8160 | [WooooDyy/LLM-Agent-Paper-List](https://github.com/WooooDyy/LLM-Agent-Paper-List) | 2025-09-12 | The Rise and Potential of Large Language Model Bas |
| 4319 | [thunlp/PromptPapers](https://github.com/thunlp/PromptPapers) | 2023-07-17 | Pre-train, Prompt, and Predict: A Systematic Surve |
| 3404 | [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) | 2026-05-20 | Unifying the Perspectives of NLP and Software Engi |
| 3354 | [YangLing0818/Diffusion-Models-Papers-Survey-Taxonomy](https://github.com/YangLing0818/Diffusion-Models-Papers-Survey-Taxonomy) | 2025-09-27 | Diffusion Models: A Comprehensive Survey of Method |
| 3240 | [Meirtz/Awesome-Context-Engineering](https://github.com/Meirtz/Awesome-Context-Engineering) | 2026-05-28 | A Survey of Context Engineering for Large Language |
| 3131 | [jingyi0000/VLM_survey](https://github.com/jingyi0000/VLM_survey) | 2025-10-14 | Vision-Language Models for Vision Tasks: A Survey |
| 2992 | [qingsongedu/time-series-transformers-review](https://github.com/qingsongedu/time-series-transformers-review) | 2024-08-08 | Transformers in Time Series: A Survey |
| 2907 | [Paitesanshi/LLM-Agent-Survey](https://github.com/Paitesanshi/LLM-Agent-Survey) | 2025-02-20 | A Survey on Large Language Model based Autonomous  |
| 2868 | [zjunlp/EasyEdit](https://github.com/zjunlp/EasyEdit) | 2026-07-09 | A Comprehensive Study of Knowledge Editing for Lar |
| 2800 | [luo-junyu/Awesome-Agent-Papers](https://github.com/luo-junyu/Awesome-Agent-Papers) | 2025-11-07 | Large Language Model Agent: A Survey on Methodolog |
| 2769 | [OpenBMB/BMTools](https://github.com/OpenBMB/BMTools) | 2023-12-05 | Tool Learning with Foundation Models |
| 2609 | [RManLuo/Awesome-LLM-KG](https://github.com/RManLuo/Awesome-LLM-KG) | 2025-05-02 | Unifying Large Language Models and Knowledge Graph |
| 2523 | [DEEP-PolyU/Awesome-GraphRAG](https://github.com/DEEP-PolyU/Awesome-GraphRAG) | 2026-06-02 | A Survey of Graph Retrieval-Augmented Generation f |
| 2302 | [ChenHsing/Awesome-Video-Diffusion-Models](https://github.com/ChenHsing/Awesome-Video-Diffusion-Models) | 2026-06-22 | A Survey on Video Diffusion Models |
| 2243 | [EgoAlpha/prompt-in-context-learning](https://github.com/EgoAlpha/prompt-in-context-learning) | 2026-05-29 | A Survey on In-context Learning |
| 2234 | [ActiveVisionLab/Awesome-LLM-3D](https://github.com/ActiveVisionLab/Awesome-LLM-3D) | 2026-04-16 | When LLMs step into the 3D World: A Survey and Met |
| 2142 | [Xnhyacinth/Awesome-LLM-Long-Context-Modeling](https://github.com/Xnhyacinth/Awesome-LLM-Long-Context-Modeling) | 2026-07-01 | A Comprehensive Survey on Long Context Language Mo |
| 2138 | [Tongji-KGLLM/RAG-Survey](https://github.com/Tongji-KGLLM/RAG-Survey) | 2024-05-08 | Retrieval-Augmented Generation for Large Language  |
| 2116 | [HCPLab-SYSU/Embodied_AI_Paper_List](https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List) | 2026-06-10 | Aligning Cyber Space with Physical World: A Compre |
| 1787 | [hymie122/RAG-Survey](https://github.com/hymie122/RAG-Survey) | 2024-08-20 | Retrieval-Augmented Generation for AI-Generated Co |
| 1692 | [asinghcsu/AgenticRAG-Survey](https://github.com/asinghcsu/AgenticRAG-Survey) | 2025-10-20 | Agentic Retrieval-Augmented Generation: A Survey o |
| 1605 | [MLGroupJLU/LLM-eval-survey](https://github.com/MLGroupJLU/LLM-eval-survey) | 2026-04-17 | A Survey on Evaluation of Large Language Models |
| 1437 | [LirongWu/awesome-graph-self-supervised-learning](https://github.com/LirongWu/awesome-graph-self-supervised-learning) | 2024-08-15 | Self-supervised Learning on Graphs: Contrastive, G |
| 1299 | [tim-learn/awesome-test-time-adaptation](https://github.com/tim-learn/awesome-test-time-adaptation) | 2025-11-14 | A Comprehensive Survey on Test-Time Adaptation und |
| 1296 | [ATH-MaaS/Awesome-Unified-Multimodal-Models](https://github.com/ATH-MaaS/Awesome-Unified-Multimodal-Models) | 2026-03-24 | Unified Multimodal Understanding and Generation Mo |
| 1295 | [Tebmer/Awesome-Knowledge-Distillation-of-LLMs](https://github.com/Tebmer/Awesome-Knowledge-Distillation-of-LLMs) | 2025-03-09 | A Survey on Knowledge Distillation of Large Langua |
| 1290 | [huybery/Awesome-Code-LLM](https://github.com/huybery/Awesome-Code-LLM) | 2024-12-10 | A Survey on Large Language Models for Code Generat |
| 1260 | [AIoT-MLSys-Lab/Efficient-LLMs-Survey](https://github.com/AIoT-MLSys-Lab/Efficient-LLMs-Survey) | 2025-06-23 | Efficient Large Language Models: A Survey |
| 1235 | [zjunlp/KnowledgeEditingPapers](https://github.com/zjunlp/KnowledgeEditingPapers) | 2026-06-25 | Editing Large Language Models: Problems, Methods,  |
| 1235 | [zjunlp/KnowledgeEditingPapers](https://github.com/zjunlp/KnowledgeEditingPapers) | 2026-06-25 | Knowledge Mechanisms in Large Language Models: A S |
| 1212 | [jwwthu/GNN4Traffic](https://github.com/jwwthu/GNN4Traffic) | 2024-08-07 | STG4Traffic: A Survey and Benchmark of Spatial-Tem |
| 1151 | [daochenzha/data-centric-AI](https://github.com/daochenzha/data-centric-AI) | 2024-06-26 | Data-centric Artificial Intelligence: A Survey |
| 1132 | [VILA-Lab/Awesome-DLMs](https://github.com/VILA-Lab/Awesome-DLMs) | 2026-05-29 | A Survey on Diffusion Language Models |
| 1127 | [weihaox/GAN-Inversion](https://github.com/weihaox/GAN-Inversion) | 2025-02-07 | GAN Inversion: A Survey |
| 1112 | [PRIV-Creation/Awesome-Controllable-T2I-Diffusion-Models](https://github.com/PRIV-Creation/Awesome-Controllable-T2I-Diffusion-Models) | 2024-12-31 | Controllable Generation with Text-to-Image Diffusi |
| 1085 | [HillZhang1999/llm-hallucination-survey](https://github.com/HillZhang1999/llm-hallucination-survey) | 2025-09-27 | Siren's Song in the AI Ocean: A Survey on Hallucin |
| 1016 | [yaotingwangofficial/Awesome-MCoT](https://github.com/yaotingwangofficial/Awesome-MCoT) | 2026-05-22 | Multimodal Chain-of-Thought Reasoning: A Comprehen |
| 1012 | [huytransformer/Awesome-Out-Of-Distribution-Detection](https://github.com/huytransformer/Awesome-Out-Of-Distribution-Detection) | 2026-04-03 | Generalized Out-of-Distribution Detection: A Surve |
| 1001 | [yyysjz1997/Awesome-TimeSeries-SpatioTemporal-Diffusion-Model](https://github.com/yyysjz1997/Awesome-TimeSeries-SpatioTemporal-Diffusion-Model) | 2026-02-05 | A Survey on Diffusion Models for Time Series and S |
| 998 | [jianzongwu/Awesome-Open-Vocabulary](https://github.com/jianzongwu/Awesome-Open-Vocabulary) | 2026-05-12 | Towards Open Vocabulary Learning: A Survey |
| 997 | [PeterGriffinJin/Awesome-Language-Model-on-Graphs](https://github.com/PeterGriffinJin/Awesome-Language-Model-on-Graphs) | 2025-03-02 | Large Language Models on Graphs: A Comprehensive S |
| 961 | [tamlhp/awesome-machine-unlearning](https://github.com/tamlhp/awesome-machine-unlearning) | 2026-07-06 | A Survey of Machine Unlearning |
| 946 | [worldbench/awesome-3d-4d-world-models](https://github.com/worldbench/awesome-3d-4d-world-models) | 2026-06-29 | 3D and 4D World Modeling: A Survey |
| 807 | [chauncygu/Safe-Reinforcement-Learning-Baselines](https://github.com/chauncygu/Safe-Reinforcement-Learning-Baselines) | 2026-03-13 | A Review of Safe Reinforcement Learning: Methods,  |
| 804 | [tjunlp-lab/Awesome-LLMs-Evaluation-Papers](https://github.com/tjunlp-lab/Awesome-LLMs-Evaluation-Papers) | 2024-05-08 | Evaluating Large Language Models: A Comprehensive  |
| 803 | [ChaofanTao/Autoregressive-Models-in-Vision-Survey](https://github.com/ChaofanTao/Autoregressive-Models-in-Vision-Survey) | 2026-05-05 | Autoregressive Models in Vision: A Survey |
| 789 | [tsinghua-fib-lab/World-Model](https://github.com/tsinghua-fib-lab/World-Model) | 2025-11-18 | Understanding World or Predicting Future? A Compre |
| 782 | [Eclipsess/Awesome-Efficient-Reasoning-LLMs](https://github.com/Eclipsess/Awesome-Efficient-Reasoning-LLMs) | 2026-02-28 | Stop Overthinking: A Survey on Efficient Reasoning |
| 764 | [EnnengYang/Awesome-Model-Merging-Methods-Theories-Applications](https://github.com/EnnengYang/Awesome-Model-Merging-Methods-Theories-Applications) | 2026-07-12 | Model Merging in LLMs, MLLMs, and Beyond: Methods, |
| 759 | [lxtGH/Awesome-Segmentation-With-Transformer](https://github.com/lxtGH/Awesome-Segmentation-With-Transformer) | 2024-08-25 | Transformer-Based Visual Segmentation: A Survey |
| 751 | [mayuelala/Awesome-Controllable-Video-Generation](https://github.com/mayuelala/Awesome-Controllable-Video-Generation) | 2026-04-13 | Controllable Video Generation: A Survey |
| 733 | [EmulationAI/awesome-large-audio-models](https://github.com/EmulationAI/awesome-large-audio-models) | 2026-06-03 | Sparks of Large Audio Models: A Survey and Outlook |
| 713 | [SiatMMLab/Awesome-Diffusion-Model-Based-Image-Editing-Methods](https://github.com/SiatMMLab/Awesome-Diffusion-Model-Based-Image-Editing-Methods) | 2025-07-15 | Diffusion Model-Based Image Editing: A Survey |
| 658 | [yhLeeee/Awesome-LLMs-in-Graph-tasks](https://github.com/yhLeeee/Awesome-LLMs-in-Graph-tasks) | 2025-03-21 | A Survey of Graph Meets Large Language Model: Prog |
| 642 | [Coder-Yu/SELFRec](https://github.com/Coder-Yu/SELFRec) | 2025-06-06 | Self-Supervised Learning for Recommender Systems:  |
| 636 | [HKUSTDial/awesome-data-agents](https://github.com/HKUSTDial/awesome-data-agents) | 2026-06-10 | A Survey of Data Agents: Emerging Paradigm or Over |
| 611 | [PointsCoder/Awesome-3D-Object-Detection-for-Autonomous-Driving](https://github.com/PointsCoder/Awesome-3D-Object-Detection-for-Autonomous-Driving) | 2023-05-04 | 3D Object Detection for Autonomous Driving: A Comp |
| 520 | [xiyuanzh/awesome-llm-time-series](https://github.com/xiyuanzh/awesome-llm-time-series) | 2024-07-26 | Large Language Models for Time Series: A Survey |
| 511 | [JindongGu/Awesome-Prompting-on-Vision-Language-Model](https://github.com/JindongGu/Awesome-Prompting-on-Vision-Language-Model) | 2025-03-18 | A Systematic Survey of Prompt Engineering on Visio |
| 505 | [withinmiaov/A-Survey-on-Mixture-of-Experts-in-LLMs](https://github.com/withinmiaov/A-Survey-on-Mixture-of-Experts-in-LLMs) | 2026-06-07 | A Survey on Mixture of Experts in Large Language M |
| 495 | [jun0wanan/awesome-large-multimodal-agents](https://github.com/jun0wanan/awesome-large-multimodal-agents) | 2024-09-25 | Large Multimodal Agents: A Survey |
| 485 | [quchangle1/LLM-Tool-Survey](https://github.com/quchangle1/LLM-Tool-Survey) | 2025-08-09 | Tool Learning with Large Language Models: A Survey |
| 462 | [jiawei-chen/RecDebiasing](https://github.com/jiawei-chen/RecDebiasing) | 2024-02-19 | Bias and Debias in Recommender System: A Survey an |
| 449 | [weijiawu/Awesome-RL-for-Multimodal-Foundation-Models](https://github.com/weijiawu/Awesome-RL-for-Multimodal-Foundation-Models) | 2026-04-28 | Reinforcement Learning for Large Model: A Survey |
| 432 | [MobileLLM/Personal_LLM_Agents_Survey](https://github.com/MobileLLM/Personal_LLM_Agents_Survey) | 2026-06-27 | Personal LLM Agents: Insights and Survey about the |
| 407 | [CroitoruAlin/Diffusion-Models-in-Vision-A-Survey](https://github.com/CroitoruAlin/Diffusion-Models-in-Vision-A-Survey) | 2023-11-26 | Diffusion Models in Vision: A Survey |
| 388 | [heshuting555/Awesome-3DGS-Applications](https://github.com/heshuting555/Awesome-3DGS-Applications) | 2026-06-17 | A Survey on 3D Gaussian Splatting Applications: Se |
| 381 | [qingsongedu/Awesome-SSL4TS](https://github.com/qingsongedu/Awesome-SSL4TS) | 2024-04-28 | Self-Supervised Learning for Time Series Analysis: |
| 380 | [ALEEEHU/World-Simulator](https://github.com/ALEEEHU/World-Simulator) | 2026-07-09 | Simulating the Real World: A Unified Survey of Mul |
| 374 | [lupantech/dl4math](https://github.com/lupantech/dl4math) | 2023-12-22 | A Survey of Deep Learning for Mathematical Reasoni |
| 374 | [taozh2017/RGBD-SODsurvey](https://github.com/taozh2017/RGBD-SODsurvey) | 2023-08-01 | RGB-D Salient Object Detection: A Survey |
| 369 | [HKUDS/Awesome-LLM4Graph-Papers](https://github.com/HKUDS/Awesome-LLM4Graph-Papers) | 2025-03-15 | A Survey of Large Language Models for Graphs |
| 365 | [Zoeyyao27/CoT-Igniting-Agent](https://github.com/Zoeyyao27/CoT-Igniting-Agent) | 2023-11-25 | Navigate through Enigmatic Labyrinth: A Survey of  |
| 365 | [EnnengYang/Awesome-Forgetting-in-Deep-Learning](https://github.com/EnnengYang/Awesome-Forgetting-in-Deep-Learning) | 2026-01-27 | A Comprehensive Survey of Forgetting in Deep Learn |
| 356 | [XiaoYee/Awesome_Efficient_LRM_Reasoning](https://github.com/XiaoYee/Awesome_Efficient_LRM_Reasoning) | 2026-01-22 | A Survey of Efficient Reasoning for Large Reasonin |
| 354 | [Lupin1998/Awesome-MIM](https://github.com/Lupin1998/Awesome-MIM) | 2025-04-23 | Masked Modeling for Self-supervised Representation |
| 340 | [thunlp/ChatEval](https://github.com/thunlp/ChatEval) | 2024-10-19 | ChatEval: Towards Better LLM-based Evaluators thro |
| 337 | [LuckyyySTA/Awesome-LLM-hallucination](https://github.com/LuckyyySTA/Awesome-LLM-hallucination) | 2024-03-11 | A Survey on Hallucination in Large Language Models |
| 333 | [Li-Zn-H/AwesomeWorldModels](https://github.com/Li-Zn-H/AwesomeWorldModels) | 2026-06-27 | A Comprehensive Survey on World Models for Embodie |
| 317 | [jishengpeng/WavChat](https://github.com/jishengpeng/WavChat) | 2024-11-28 | WavChat: A Survey of Spoken Dialogue Models |
| 312 | [IrohXu/Awesome-Multimodal-LLM-Autonomous-Driving](https://github.com/IrohXu/Awesome-Multimodal-LLM-Autonomous-Driving) | 2024-03-14 | A Survey on Multimodal Large Language Models for A |
| 311 | [qqqqqqy0227/awesome-3DGS](https://github.com/qqqqqqy0227/awesome-3DGS) | 2025-01-06 | 3D Gaussian Splatting: Survey, Technologies, Chall |
| 307 | [wusw14/GNN-in-RS](https://github.com/wusw14/GNN-in-RS) | 2022-06-25 | Graph Neural Networks in Recommender Systems: A Su |
| 286 | [YuanchenBei/Awesome-Cold-Start-Recommendation](https://github.com/YuanchenBei/Awesome-Cold-Start-Recommendation) | 2026-03-26 | Cold-Start Recommendation towards the Era of Large |
| 277 | [ZJU-LLMs/Awesome-LoRAs](https://github.com/ZJU-LLMs/Awesome-LoRAs) | 2024-08-12 | A Survey on LoRA of Large Language Models |
| 274 | [Strivin0311/long-llms-learning](https://github.com/Strivin0311/long-llms-learning) | 2024-07-30 | Advancing Transformer Architecture in Long-Context |
| 264 | [imxtx/awesome-controllable-speech-synthesis](https://github.com/imxtx/awesome-controllable-speech-synthesis) | 2026-07-07 | Towards Controllable Speech Synthesis in the Era o |
| 256 | [RayYoh/OCRM_survey](https://github.com/RayYoh/OCRM_survey) | 2024-10-04 | A Survey of Embodied Learning for Object-Centric R |
| 232 | [xiaoya-li/Instruction-Tuning-Survey](https://github.com/xiaoya-li/Instruction-Tuning-Survey) | 2025-08-10 | Instruction Tuning for Large Language Models: A Su |
| 230 | [vyokky/LLM-Brained-GUI-Agents-Survey](https://github.com/vyokky/LLM-Brained-GUI-Agents-Survey) | 2025-06-23 | Large Language Model-Brained GUI Agents: A Survey |
| 226 | [zhaoyu-li/DL4TP](https://github.com/zhaoyu-li/DL4TP) | 2025-05-28 | A Survey on Deep Learning for Theorem Proving |
| 221 | [RUCAIBox/DenseRetrieval](https://github.com/RUCAIBox/DenseRetrieval) | 2022-12-07 | Dense Text Retrieval based on Pretrained Language  |
| 210 | [dreamtheater123/Awesome-SpeechLM-Survey](https://github.com/dreamtheater123/Awesome-SpeechLM-Survey) | 2025-06-17 | Recent Advances in Speech Language Models: A Surve |
| 209 | [RUC-NLPIR/GenIR-Survey](https://github.com/RUC-NLPIR/GenIR-Survey) | 2025-04-05 | A Survey of Generative Information Retrieval |
| 205 | [tfzhou/VS-Survey](https://github.com/tfzhou/VS-Survey) | 2022-12-28 | A Survey on Deep Learning Technique for Video Segm |
| 201 | [JizhiziLi/matting-survey](https://github.com/JizhiziLi/matting-survey) | 2023-05-16 | Deep Image Matting: A Comprehensive Survey |
| 189 | [franciscoliu/Awesome-GenAI-Unlearning](https://github.com/franciscoliu/Awesome-GenAI-Unlearning) | 2026-04-22 | Machine Unlearning in Generative AI: A Survey |
| 184 | [AIoT-MLSys-Lab/Efficient-Diffusion-Model-Survey](https://github.com/AIoT-MLSys-Lab/Efficient-Diffusion-Model-Survey) | 2025-12-08 | Efficient Diffusion Models: A Comprehensive Survey |
| 184 | [AIoT-MLSys-Lab/Efficient-Diffusion-Model-Survey](https://github.com/AIoT-MLSys-Lab/Efficient-Diffusion-Model-Survey) | 2025-12-08 | Efficient Diffusion Models: A Survey |
| 158 | [vignywang/Awesome-Local-Feature-Matching](https://github.com/vignywang/Awesome-Local-Feature-Matching) | 2024-03-11 | Local Feature Matching Using Deep Learning: A Surv |
| 155 | [ShenZheng2000/LLIE_Survey](https://github.com/ShenZheng2000/LLIE_Survey) | 2024-10-09 | Low-Light Image and Video Enhancement Using Deep L |
| 137 | [PKU-Alignment/AlignmentSurvey](https://github.com/PKU-Alignment/AlignmentSurvey) | 2023-11-02 | AI Alignment: A Comprehensive Survey |
| 129 | [LAMDA-Tabular/Tabular-Survey](https://github.com/LAMDA-Tabular/Tabular-Survey) | 2026-06-10 | Representation Learning for Tabular Data: A Compre |
| 125 | [wzk1015/Awesome-Vision-to-Music-Generation](https://github.com/wzk1015/Awesome-Vision-to-Music-Generation) | 2025-08-09 | Vision-to-Music Generation: A Survey |
| 113 | [limengran98/Awesome-Literature-Graph-Learning-Challenges](https://github.com/limengran98/Awesome-Literature-Graph-Learning-Challenges) | 2025-09-25 | A Survey of Large Language Models for Data Challen |
| 111 | [niconi19/LLM-Conversation-Safety](https://github.com/niconi19/LLM-Conversation-Safety) | 2024-08-07 | Attacks, Defenses and Evaluations for LLM Conversa |
| 106 | [llm-misinformation/llm-misinformation-survey](https://github.com/llm-misinformation/llm-misinformation-survey) | 2024-11-09 | Combating Misinformation in the Age of LLMs: Oppor |
| 94 | [guikunchen/Awesome3DGS](https://github.com/guikunchen/Awesome3DGS) | 2026-01-18 | A Survey on 3D Gaussian Splatting |
| 91 | [tim-learn/Awesome-LabelFree-VLMs](https://github.com/tim-learn/Awesome-LabelFree-VLMs) | 2026-02-02 | Adapting Vision-Language Models Without Labels: A  |
| 87 | [yunfanLu/Awesome-Image-Prior](https://github.com/yunfanLu/Awesome-Image-Prior) | 2025-05-29 | Priors in Deep Image Restoration and Enhancement:  |
| 85 | [kaize0409/Awesome-Graph-OOD](https://github.com/kaize0409/Awesome-Graph-OOD) | 2024-10-28 | A Survey of Deep Graph Learning under Distribution |
| 85 | [kaize0409/Awesome-Graph-OOD](https://github.com/kaize0409/Awesome-Graph-OOD) | 2024-10-28 | Beyond Generalization: A Survey of Out-Of-Distribu |
| 84 | [huangleiBuaa/NormalizationSurvey](https://github.com/huangleiBuaa/NormalizationSurvey) | 2021-06-24 | Normalization Techniques in Training DNNs: Methodo |
| 80 | [Lsyhprum/WEAVESS](https://github.com/Lsyhprum/WEAVESS) | 2021-05-16 | A Comprehensive Survey and Experimental Comparison |
| 79 | [jindongli-Ai/Survey_on_CLIP-Powered_Domain_Generalization_and_Adaptation](https://github.com/jindongli-Ai/Survey_on_CLIP-Powered_Domain_Generalization_and_Adaptation) | 2026-03-25 | CLIP-Powered Domain Generalization and Domain Adap |
| 77 | [IPL-sharif/KD_Survey](https://github.com/IPL-sharif/KD_Survey) | 2026-06-08 | A Comprehensive Survey on Knowledge Distillation |
| 71 | [badripatro/mamba360](https://github.com/badripatro/mamba360) | 2024-05-02 | Mamba-360: Survey of State Space Models as Transfo |
| 56 | [ndrwmlnk/Awesome-Video-Diffusion-Models](https://github.com/ndrwmlnk/Awesome-Video-Diffusion-Models) | 2025-02-11 | Video Diffusion Models: A Survey |
| 18 | [Kimho666/LLM_Hardware_Survey](https://github.com/Kimho666/LLM_Hardware_Survey) | 2025-07-15 | Large Language Model Inference Acceleration: A Com |
| 8 | [larocs/offline-rl-suvey](https://github.com/larocs/offline-rl-suvey) | 2022-10-12 | A Survey on Offline Reinforcement Learning: Taxono |

## 全エントリ一覧

### 🧠 大規模言語モデル (LLM)

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| Training language models to follow instructions with human f | Long Ouyang et al. | NeurIPS | 2022 | 2203.02155 | 22413 |  |
| A Survey of Large Language Models | Wayne Xin Zhao et al. | arXiv | 2023 | 2303.18223 | 4664 | RUCAIBox/LLMSurvey |
| A Comprehensive Overview of Large Language Models | Humza Naveed et al. | arXiv | 2023 | 2307.06435 | 1773 |  |
| Large Language Models: A Survey | Shervin Minaee et al. | arXiv | 2024 | 2402.06196 | 1019 |  |
| Instruction Tuning for Large Language Models: A Survey | Shengyu Zhang et al. | arXiv | 2023 | 2308.10792 | 896 | xiaoya-li/Instruction-Tuning-Survey |
| Retrieval-Augmented Generation for AI-Generated Content: A S | Penghao Zhao et al. | arXiv | 2024 | 2402.19473 | 629 | hymie122/RAG-Survey |
| Editing Large Language Models: Problems, Methods, and Opport | Yunzhi Yao et al. | EMNLP | 2023 | 2305.13172 | 471 | zjunlp/KnowledgeEditingPapers |
| Stop Overthinking: A Survey on Efficient Reasoning for Large | Yang Sui et al. | arXiv | 2025 | 2503.16419 | 412 | Eclipsess/Awesome-Efficient-Reasoning-LLMs |
| AI Alignment: A Comprehensive Survey | Jiaming Ji et al. | arXiv | 2023 | 2310.19852 | 371 | PKU-Alignment/AlignmentSurvey |
| A Survey on Knowledge Distillation of Large Language Models | Xiaohan Xu et al. | arXiv | 2024 | 2402.13116 | 351 | Tebmer/Awesome-Knowledge-Distillation-of-LLMs |
| Personal LLM Agents: Insights and Survey about the Capabilit | Yuanchun Li et al. | arXiv | 2024 | 2401.05459 | 349 | MobileLLM/Personal_LLM_Agents_Survey |
| Automatically Correcting Large Language Models: Surveying th | Liangming Pan et al. | TACL | 2023 | 2308.03188 | 287 |  |
| Two Tales of Persona in LLMs: A Survey of Role-Playing and P | Yu-Min Tseng et al. | arXiv | 2024 | 2406.01171 | 281 |  |
| Secrets of RLHF in Large Language Models Part I: PPO | Rui Zheng et al. | arXiv | 2023 | 2307.04964 | 280 |  |
| A Comprehensive Survey of Small Language Models in the Era o | Fali Wang et al. | arXiv | 2024 | 2411.03350 | 226 |  |
| Large Language Model-Brained GUI Agents: A Survey | Chaoyun Zhang et al. | arXiv | 2024 | 2411.18279 | 181 | vyokky/LLM-Brained-GUI-Agents-Survey |
| A Survey of Text Watermarking in the Era of Large Language M | Aiwei Liu et al. | arXiv | 2023 | 2312.07913 | 174 |  |
| A Survey on LoRA of Large Language Models | Yuren Mao et al. | Frontiers of Computer Science | 2024 | 2407.11046 | 161 | ZJU-LLMs/Awesome-LoRAs |
| A Survey of Reinforcement Learning for Large Reasoning Model | Kaiyan Zhang et al. | arXiv | 2025 | 2509.08827 | 158 |  |
| A Survey of Efficient Reasoning for Large Reasoning Models:  | Xiaoye Qu et al. | arXiv | 2025 | 2503.21614 | 135 | XiaoYee/Awesome_Efficient_LRM_Reasoning |
| Datasets for Large Language Models: A Comprehensive Survey | Yang Liu et al. | arXiv | 2024 | 2402.18041 | 135 |  |
| A Comprehensive Survey on Long Context Language Modeling | Jiaheng Liu et al. | arXiv | 2025 | 2503.17407 | 124 | Xnhyacinth/Awesome-LLM-Long-Context-Modeling |
| A Survey of Graph Retrieval-Augmented Generation for Customi | Qinggang Zhang et al. | arXiv | 2025 | 2501.13958 | 123 | DEEP-PolyU/Awesome-GraphRAG |
| A Survey of Context Engineering for Large Language Models | Lingrui Mei et al. | arXiv | 2025 | 2507.13334 | 122 | Meirtz/Awesome-Context-Engineering |
| Beyond the Limits: A Survey of Techniques to Extend the Cont | Xindi Wang et al. | IJCAI | 2024 | 2402.02244 | 111 |  |
| Knowledge Mechanisms in Large Language Models: A Survey and  | Mengru Wang et al. | EMNLP Findings | 2024 | 2407.15017 | 72 | zjunlp/KnowledgeEditingPapers |
| A Survey on Diffusion Language Models | Tianyi Li et al. | arXiv | 2025 | 2508.10875 | 67 | VILA-Lab/Awesome-DLMs |
| A Survey on Sparse Autoencoders: Interpreting the Internal M | Dong Shu et al. | arXiv | 2025 | 2503.05613 | 64 |  |
| A Survey on Large Language Models for Mathematical Reasoning | Peng-Yuan Wang et al. | arXiv | 2025 | 2506.08446 | 59 |  |
| The Oscars of AI Theater: A Survey on Role-Playing with Lang | Nuo Chen et al. | arXiv | 2024 | 2407.11484 | 58 |  |
| A Survey of Small Language Models | Chien Van Nguyen et al. | arXiv | 2024 | 2410.20011 | 56 |  |
| Code to Think, Think to Code: A Survey on Code-Enhanced Reas | Dayu Yang et al. | arXiv | 2025 | 2502.19411 | 55 |  |
| Emergent Abilities in Large Language Models: A Survey | Leonardo Berti et al. | arXiv | 2025 | 2503.05788 | 53 |  |
| Knowledge Distillation and Dataset Distillation of Large Lan | Luyang Fang et al. | arXiv preprint | 2025 | 2504.14772 | 50 |  |
| The Mystery of In-Context Learning: A Comprehensive Survey o | Yuxiang Zhou et al. | EMNLP | 2023 | 2311.00237 | 48 |  |
| A Survey of Data Agents: Emerging Paradigm or Overstated Hyp | Yizhang Zhu et al. | arXiv | 2025 | 2510.23587 | 33 | HKUSTDial/awesome-data-agents |
| A Comprehensive Survey of Machine Unlearning Techniques for  | Jiahui Geng et al. | arXiv | 2025 | 2503.01854 | 32 |  |
| Reinforcement Learning Meets Large Language Models: A Survey | Keliang Liu et al. | arXiv preprint | 2025 | 2509.16679 | 29 |  |
| A Survey of Test-Time Compute: From Intuitive Inference to D | Yixin Ji et al. | arXiv | 2025 | 2501.02497 | 20 |  |
| KV Cache Compression for Inference Efficiency in LLMs: A Rev | Yanyu Liu et al. | arXiv preprint | 2025 | 2508.06297 | 12 |  |
| A Survey of Theory of Mind in Large Language Models: Evaluat | Hieu Minh Nguyen et al. | arXiv | 2025 | 2502.06470 | 9 |  |
| Reinforcement Learning Foundations for Deep Research Systems | Wenjun Li et al. | arXiv preprint | 2025 | 2509.06733 | 9 |  |
| Closer Look at Efficient Inference Methods: A Survey of Spec | Hyun Ryu et al. | arXiv preprint | 2024 | 2411.13157 | 7 |  |
| LLM Post-Training: A Deep Dive into Reasoning Large Language | Komal Kumar et al. | arXiv | 2025 | 2502.21321 |  |  |
| Safe RLHF: Safe Reinforcement Learning from Human Feedback | Josef Dai et al. | ICLR | 2024 | 2310.12773 |  |  |
| Navigate through Enigmatic Labyrinth: A Survey of Chain of T | Zheng Chu et al. | ACL | 2024 | 2309.15402 |  | Zoeyyao27/CoT-Igniting-Agent |
| A Comprehensive Survey of Hallucination Mitigation Technique | S. M. Towhidul Islam Tonm | arXiv | 2024 | 2401.01313 |  |  |
| A Survey on RAG Meeting LLMs: Towards Retrieval-Augmented La | Wenqi Fan et al. | KDD | 2024 | 2405.06211 |  |  |
| ChatEval: Towards Better LLM-based Evaluators through Multi- | Chi-Min Chan et al. | ICLR | 2024 | 2308.07201 |  | thunlp/ChatEval |
| What Are Tools Anyway? A Survey from the Language Model Pers | Zhiruo Wang et al. | COLM | 2024 | 2403.15452 |  |  |
| A Survey on Efficient Inference for Large Language Models | Zixuan Zhou et al. | arXiv | 2024 | 2404.14294 |  |  |
| LLM Inference Unveiled: Survey and Roofline Model Insights | Zhihang Yuan et al. | arXiv | 2024 | 2402.16363 |  |  |
| Parameter-Efficient Fine-Tuning for Large Models: A Comprehe | Zeyu Han et al. | TMLR | 2024 | 2403.14608 |  |  |
| The What, Why, and How of Context Length Extension Technique | Saurav Pawar et al. | arXiv | 2024 | 2401.07872 |  |  |
| Jailbreak Attacks and Defenses Against Large Language Models | Sibo Yi et al. | arXiv | 2024 | 2407.04295 |  |  |
| Attacks, Defenses and Evaluations for LLM Conversation Safet | Zhichen Dong et al. | NAACL | 2024 | 2402.09283 |  | niconi19/LLM-Conversation-Safety |
| A Survey on Large Language Models for Code Generation | Juyong Jiang et al. | arXiv | 2024 | 2406.00515 |  | huybery/Awesome-Code-LLM |
| A Survey on Mixture of Experts in Large Language Models | Weilin Cai et al. | IEEE TKDE | 2024 | 2407.06204 |  | withinmiaov/A-Survey-on-Mixture-of-Experts-in-LLMs |
| Towards Lifelong Learning of Large Language Models: A Survey | Junhao Zheng et al. | ACM Computing Surveys | 2024 | 2406.06391 |  |  |
| A Comprehensive Study of Knowledge Editing for Large Languag | Ningyu Zhang et al. | arXiv | 2024 | 2401.01286 |  | zjunlp/EasyEdit |
| A Survey on Multilingual Large Language Models: Corpora, Ali | Yuemei Xu et al. | arXiv | 2024 | 2404.00929 |  |  |
| Large Language Model Alignment: A Survey | Tianhao Shen et al. | arXiv | 2023 | 2309.15025 |  |  |
| A Survey on In-context Learning | Qingxiu Dong et al. | EMNLP | 2023 | 2301.00234 |  | EgoAlpha/prompt-in-context-learning |
| A Survey on Hallucination in Large Language Models: Principl | Lei Huang et al. | ACM TOIS | 2023 | 2311.05232 |  | LuckyyySTA/Awesome-LLM-hallucination |
| Siren's Song in the AI Ocean: A Survey on Hallucination in L | Yue Zhang et al. | arXiv | 2023 | 2309.01219 |  | HillZhang1999/llm-hallucination-survey |
| A Survey on Large Language Model based Autonomous Agents | Lei Wang et al. | Frontiers of Computer Science | 2023 | 2308.11432 |  | Paitesanshi/LLM-Agent-Survey |
| The Rise and Potential of Large Language Model Based Agents: | Zhiheng Xi et al. | arXiv | 2023 | 2309.07864 |  | WooooDyy/LLM-Agent-Paper-List |
| Tool Learning with Foundation Models | Yujia Qin et al. | ACM Computing Surveys | 2023 | 2304.08354 |  | OpenBMB/BMTools |
| A Survey on Evaluation of Large Language Models | Yupeng Chang et al. | ACM TIST | 2023 | 2307.03109 |  | MLGroupJLU/LLM-eval-survey |
| Evaluating Large Language Models: A Comprehensive Survey | Zishan Guo et al. | arXiv | 2023 | 2310.19736 |  | tjunlp-lab/Awesome-LLMs-Evaluation-Papers |
| Towards Efficient Generative LLM Serving: A Survey from Algo | Xupeng Miao et al. | ACM Computing Surveys | 2023 | 2312.15234 |  |  |
| Scaling Down to Scale Up: A Guide to Parameter-Efficient Fin | Vladislav Lialin et al. | arXiv | 2023 | 2303.15647 |  |  |
| Parameter-Efficient Fine-Tuning Methods for Pretrained Langu | Lingling Xu et al. | arXiv | 2023 | 2312.12148 |  |  |
| Advancing Transformer Architecture in Long-Context LLMs: A C | Yunpeng Huang et al. | arXiv | 2023 | 2311.12351 |  | Strivin0311/long-llms-learning |
| Trustworthy LLMs: A Survey and Guideline for Evaluating Larg | Yang Liu et al. | arXiv | 2023 | 2308.05374 |  |  |
| Large Language Models for Software Engineering: A Systematic | Xinyi Hou et al. | ACM TOSEM | 2023 | 2308.10620 |  |  |
| Unifying the Perspectives of NLP and Software Engineering: A | Ziyin Zhang et al. | TMLR | 2023 | 2311.07989 |  | codefuse-ai/Awesome-Code-LLM |
| A Survey on Model Compression for Large Language Models | Xunyu Zhu et al. | TACL | 2023 | 2308.07633 |  |  |
| Efficient Large Language Models: A Survey | Zhongwei Wan et al. | TMLR | 2023 | 2312.03863 |  | AIoT-MLSys-Lab/Efficient-LLMs-Survey |
| The Efficiency Spectrum of Large Language Models: An Algorit | Tianyu Ding et al. | arXiv | 2023 | 2312.00678 |  |  |
| Knowledge Editing for Large Language Models: A Survey | Song Wang et al. | ACM Computing Surveys | 2023 | 2310.16218 |  |  |
| Towards Reasoning in Large Language Models: A Survey | Jie Huang et al. | ACL Findings | 2022 | 2212.10403 |  |  |

### 🎨 生成AI・拡散モデル

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| NIPS 2016 Tutorial: Generative Adversarial Networks | Ian Goodfellow | NIPS Tutorial | 2016 | 1701.00160 | 1818 |  |
| Generative Adversarial Networks: Challenges, Solutions, and  | Divya Saxena et al. | ACM Computing Surveys | 2021 | 2005.00065 | 468 |  |
| Human Motion Generation: A Survey | Wentao Zhu et al. | IEEE TPAMI | 2023 | 2307.10894 | 147 |  |
| Generative Adversarial Networks in Computer Vision: A Survey | Zhengwei Wang et al. | ACM Computing Surveys | 2021 | 1906.01529 | 92 |  |
| Controllable Video Generation: A Survey | Yue Ma et al. | arXiv | 2025 | 2507.16869 | 77 | mayuelala/Awesome-Controllable-Video-Generation |
| A Survey of Multimodal-Guided Image Editing with Text-to-Ima | Xincheng Shuai et al. | arXiv | 2024 | 2406.14555 | 65 |  |
| Autoregressive Models in Vision: A Survey | Jing Xiong et al. | TMLR | 2024 | 2411.05902 | 55 | ChaofanTao/Autoregressive-Models-in-Vision-Survey |
| Diffusion Model-Based Video Editing: A Survey | Wenhao Sun et al. | arXiv | 2024 | 2407.07111 | 52 |  |
| Score-based Diffusion Models via Stochastic Differential Equ | Wenpin Tang et al. | arXiv | 2024 | 2402.07487 | 52 |  |
| Efficient Diffusion Models: A Survey | Hui Shen et al. | TMLR | 2025 | 2502.06805 | 47 | AIoT-MLSys-Lab/Efficient-Diffusion-Model-Survey |
| A Survey on Personalized Content Synthesis with Diffusion Mo | Xulu Zhang et al. | arXiv | 2024 | 2405.05538 | 41 |  |
| Simulating the Real World: A Unified Survey of Multimodal Ge | Yuqi Hu et al. | IEEE TPAMI | 2025 | 2503.04641 | 17 | ALEEEHU/World-Simulator |
| A Comprehensive Survey on Concept Erasure in Text-to-Image D | Changhoon Kim et al. | arXiv | 2025 | 2502.14896 | 10 |  |
| Vision-to-Music Generation: A Survey | Zhaokai Wang et al. | ISMIR | 2025 | 2503.21254 | 6 | wzk1015/Awesome-Vision-to-Music-Generation |
| A Survey on Pre-Trained Diffusion Model Distillations | Xuhui Fan et al. | arXiv | 2025 | 2502.08364 | 5 |  |
| Advances in 4D Generation: A Survey | Qiaowei Miao et al. | arXiv | 2025 | 2503.14501 | 0 |  |
| Efficient Diffusion Models: A Comprehensive Survey from Prin | Zhiyuan Ma et al. | TMLR | 2024 | 2410.11795 |  | AIoT-MLSys-Lab/Efficient-Diffusion-Model-Survey |
| Video Diffusion Models: A Survey | Andrew Melnik et al. | TMLR | 2024 | 2405.03150 |  | ndrwmlnk/Awesome-Video-Diffusion-Models |
| Sora as a World Model? A Complete Survey on Text-to-Video Ge | Fachrina Dewi Puspitasari | arXiv | 2024 | 2403.05131 |  |  |
| Diffusion Model-Based Image Editing: A Survey | Yi Huang et al. | IEEE TPAMI | 2024 | 2402.17525 |  | SiatMMLab/Awesome-Diffusion-Model-Based-Image-Editing-Methods |
| Controllable Generation with Text-to-Image Diffusion Models: | Pu Cao et al. | IEEE TPAMI | 2024 | 2403.04279 |  | PRIV-Creation/Awesome-Controllable-T2I-Diffusion-Models |
| Advances in 3D Generation: A Survey | Xiaoyu Li et al. | arXiv | 2024 | 2401.17807 |  |  |
| RenAIssance: A Survey into AI Text-to-Image Generation in th | Fengxiang Bie et al. | IEEE TPAMI | 2023 | 2309.00810 |  |  |
| A Survey on Video Diffusion Models | Zhen Xing et al. | ACM Computing Surveys | 2023 | 2310.10647 |  | ChenHsing/Awesome-Video-Diffusion-Models |
| Generative AI meets 3D: A Survey on Text-to-3D in AIGC Era | Chenghao Li et al. | arXiv | 2023 | 2305.06131 |  |  |
| Sparks of Large Audio Models: A Survey and Outlook | Siddique Latif et al. | arXiv | 2023 | 2308.12792 |  | EmulationAI/awesome-large-audio-models |
| A Comprehensive Survey of AI-Generated Content (AIGC): A His | Yihan Cao et al. | arXiv | 2023 | 2303.04226 |  |  |
| A Review on Generative Adversarial Networks: Algorithms, The | Jie Gui et al. | IEEE TKDE | 2020 | 2001.06937 |  |  |
| An Introduction to Variational Autoencoders | Diederik P. Kingma et al. | Foundations and Trends in ML | 2019 | 1906.02691 |  |  |
| Normalizing Flows: An Introduction and Review of Current Met | Ivan Kobyzev et al. | IEEE TPAMI | 2019 | 1908.09257 |  |  |

### 🖼️ マルチモーダル・視覚言語

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| A Survey on Multimodal Large Language Models for Autonomous  | Can Cui et al. | WACV | 2024 | 2311.12320 | 534 | IrohXu/Awesome-Multimodal-LLM-Autonomous-Driving |
| Video Understanding with Large Language Models: A Survey | Yunlong Tang et al. | arXiv | 2023 | 2312.17432 | 271 |  |
| Multimodal Chain-of-Thought Reasoning: A Comprehensive Surve | Yaoting Wang et al. | arXiv | 2025 | 2503.12605 | 195 | yaotingwangofficial/Awesome-MCoT |
| Perception, Reason, Think, and Plan: A Survey on Large Multi | Yunxin Li et al. | arXiv | 2025 | 2505.04921 | 88 |  |
| Unified Multimodal Understanding and Generation Models: Adva | Shanshan Zhao et al. | arXiv | 2025 | 2505.02567 | 72 | ATH-MaaS/Awesome-Unified-Multimodal-Models |
| Ask in Any Modality: A Comprehensive Survey on Multimodal Re | Mohammad Mahdi Abootorabi | ACL Findings | 2025 | 2502.08826 | 65 |  |
| A Survey of Mathematical Reasoning in the Era of Multimodal  | Yibo Yan et al. | ACL Findings | 2024 | 2412.11936 | 65 |  |
| A Survey of Multimodal Retrieval-Augmented Generation | Lang Mei et al. | arXiv | 2025 | 2504.08748 | 47 |  |
| When LLMs step into the 3D World: A Survey and Meta-Analysis | Xianzheng Ma et al. | arXiv | 2024 | 2405.10255 | 44 | ActiveVisionLab/Awesome-LLM-3D |
| A Survey on Mechanistic Interpretability for Multi-Modal Fou | Zihao Lin et al. | arXiv | 2025 | 2502.17516 | 36 |  |
| Adapting Vision-Language Models Without Labels: A Comprehens | Hao Dong et al. | arXiv preprint | 2025 | 2508.05547 | 7 | tim-learn/Awesome-LabelFree-VLMs |
| MM-LLMs: Recent Advances in MultiModal Large Language Models | Duzhen Zhang et al. | ACL Findings | 2024 | 2401.13601 |  |  |
| Video-Language Understanding: A Survey from Model Architectu | Thong Nguyen et al. | ACL Findings | 2024 | 2406.05615 |  |  |
| A Survey on Vision-Language-Action Models for Embodied AI | Yueen Ma et al. | arXiv | 2024 | 2405.14093 |  |  |
| Agent AI: Surveying the Horizons of Multimodal Interaction | Zane Durante et al. | arXiv | 2024 | 2401.03568 |  |  |
| Large Multimodal Agents: A Survey | Junlin Xie et al. | arXiv | 2024 | 2402.15116 |  | jun0wanan/awesome-large-multimodal-agents |
| Hallucination of Multimodal Large Language Models: A Survey | Zechen Bai et al. | arXiv | 2024 | 2404.18930 |  |  |
| A Survey on Multimodal Large Language Models | Shukang Yin et al. | National Science Review | 2023 | 2306.13549 |  | BradyFU/Awesome-Multimodal-Large-Language-Models |
| A Systematic Survey of Prompt Engineering on Vision-Language | Jindong Gu et al. | arXiv | 2023 | 2307.12980 |  | JindongGu/Awesome-Prompting-on-Vision-Language-Model |
| Vision-Language Pre-training: Basics, Recent Advances, and F | Zhe Gan et al. | Foundations and Trends in CV | 2022 | 2210.09263 |  |  |
| Document AI: Benchmarks, Models and Applications | Lei Cui et al. | arXiv | 2021 | 2111.08609 |  |  |
| Deep Audio-Visual Learning: A Survey | Hao Zhu et al. | International Journal of Automation and Computing | 2020 | 2001.04758 |  |  |

### 💬 自然言語処理 (NLP)

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| Pre-train, Prompt, and Predict: A Systematic Survey of Promp | Pengfei Liu et al. | ACM Computing Surveys | 2021 | 2107.13586 | 5544 | thunlp/PromptPapers |
| Recent Trends in Deep Learning Based Natural Language Proces | Tom Young et al. | IEEE Computational Intelligence Magazine | 2018 | 1708.02709 | 3084 |  |
| A Primer in BERTology: What We Know About How BERT Works | Anna Rogers et al. | TACL | 2020 | 2002.12327 | 1916 |  |
| Deep Learning for Sentiment Analysis: A Survey | Lei Zhang et al. | WIREs Data Mining and Knowledge Discovery | 2018 | 1801.07883 | 1911 |  |
| Pre-trained Models for Natural Language Processing: A Survey | Xipeng Qiu et al. | Science China Technological Sciences | 2020 | 2003.08271 | 1710 |  |
| Recent Advances in Natural Language Processing via Large Pre | Bonan Min et al. | ACM Computing Surveys | 2021 | 2111.01243 | 1568 |  |
| A Survey on Deep Learning for Named Entity Recognition | Jing Li et al. | IEEE TKDE | 2020 | 1812.09449 | 1482 |  |
| Deep Learning Based Text Classification: A Comprehensive Rev | Shervin Minaee et al. | ACM Computing Surveys | 2020 | 2004.03705 | 1338 |  |
| Pre-Trained Models: Past, Present and Future | Xu Han et al. | AI Open | 2021 | 2106.07139 | 1092 |  |
| A Survey of Data Augmentation Approaches for NLP | Steven Y. Feng et al. | Findings of ACL | 2021 | 2105.03075 | 993 |  |
| Survey of the State of the Art in Natural Language Generatio | Albert Gatt et al. | JAIR | 2018 | 1703.09902 | 907 |  |
| A Survey on Dialogue Systems: Recent Advances and New Fronti | Hongshen Chen et al. | ACM SIGKDD Explorations | 2017 | 1711.01731 | 771 |  |
| A Survey on Automated Fact-Checking | Zhijiang Guo et al. | TACL | 2021 | 2108.11896 | 752 |  |
| A Survey on Text Classification: From Shallow to Deep Learni | Qian Li et al. | ACM TIST | 2020 | 2008.00364 | 544 |  |
| A Survey of the State of Explainable AI for Natural Language | Marina Danilevsky et al. | AACL-IJCNLP | 2020 | 2010.00711 | 468 |  |
| Neural Machine Translation: A Review and Survey | Felix Stahlberg et al. | JAIR | 2020 | 1912.02047 | 428 |  |
| A Survey on Aspect-Based Sentiment Analysis: Tasks, Methods, | Wenxuan Zhang et al. | IEEE TKDE | 2022 | 2203.01054 | 421 |  |
| Neural Machine Translation for Low-Resource Languages: A Sur | Surangika Ranathunga et a | ACM Computing Surveys | 2021 | 2106.15115 | 372 |  |
| Recent Advances in Deep Learning Based Dialogue Systems: A S | Jinjie Ni et al. | Artificial Intelligence Review | 2021 | 2105.04387 | 348 |  |
| A Survey of Evaluation Metrics Used for NLG Systems | Ananya B. Sai et al. | ACM Computing Surveys | 2020 | 2008.12009 | 340 |  |
| Post-hoc Interpretability for Neural NLP: A Survey | Andreas Madsen et al. | ACM Computing Surveys | 2021 | 2108.04840 | 320 |  |
| Survey on Factuality in Large Language Models: Knowledge, Re | Cunxiang Wang et al. | arXiv | 2023 | 2310.07521 | 293 |  |
| Word Embeddings: A Survey | Felipe Almeida et al. | arXiv | 2019 | 1901.09069 | 246 |  |
| A Survey on Complex Knowledge Base Question Answering: Metho | Yunshi Lan et al. | IJCAI | 2021 | 2105.11644 | 209 |  |
| QA Dataset Explosion: A Taxonomy of NLP Resources for Questi | Anna Rogers et al. | ACM Computing Surveys | 2021 | 2107.12708 | 200 |  |
| An Empirical Survey on Long Document Summarization: Datasets | Huan Yee Koh et al. | ACM Computing Surveys | 2022 | 2207.00939 | 181 |  |
| A Survey on Contextual Embeddings | Qi Liu et al. | arXiv | 2020 | 2003.07278 | 180 |  |
| A Survey on Stance Detection for Mis- and Disinformation Ide | Momchil Hardalov et al. | NAACL Findings | 2021 | 2103.00242 | 174 |  |
| Topic Modelling Meets Deep Neural Networks: A Survey | He Zhao et al. | IJCAI | 2021 | 2103.00498 | 168 |  |
| Multi-document Summarization via Deep Learning Techniques: A | Congbo Ma et al. | ACM Computing Surveys | 2020 | 2011.04843 | 162 |  |
| A Survey of Large Language Models in Finance (FinLLMs) | Jean Lee et al. | arXiv | 2024 | 2402.02315 | 159 |  |
| A Survey of Code-switched Speech and Language Processing | Sunayana Sitaram et al. | arXiv | 2019 | 1904.00784 | 159 |  |
| A Survey of Deep Learning Techniques for Neural Machine Tran | Shuoheng Yang et al. | arXiv | 2020 | 2002.07526 | 153 |  |
| Explainable Automated Fact-Checking: A Survey | Neema Kotonya et al. | COLING | 2020 | 2011.03870 | 151 |  |
| Grammatical Error Correction: A Survey of the State of the A | Christopher Bryant et al. | Computational Linguistics | 2023 | 2211.05166 | 138 |  |
| A Survey on Semantic Parsing | Aishwarya Kamath et al. | AKBC | 2018 | 1812.00978 | 138 |  |
| A Comprehensive Survey on Relation Extraction: Recent Advanc | Xiaoyan Zhao et al. | ACM Computing Surveys | 2023 | 2306.02051 | 137 |  |
| A Survey on Non-Autoregressive Generation for Neural Machine | Yisheng Xiao et al. | IEEE TPAMI | 2022 | 2204.09269 | 129 |  |
| A Survey of Deep Learning Methods for Relation Extraction | Shantanu Kumar et al. | arXiv | 2017 | 1705.03645 | 123 |  |
| A Survey on Neural Topic Models: Methods, Applications, and  | Xiaobao Wu et al. | Artificial Intelligence Review | 2024 | 2401.15351 | 112 |  |
| Natural Language Processing for the Legal Domain: A Survey o | Farid Ariai et al. | ACM Computing Surveys | 2025 | 2410.21306 | 103 |  |
| SECNLP: A Survey of Embeddings in Clinical Natural Language  | Kalyan KS et al. | Journal of Biomedical Informatics | 2019 | 1903.01039 | 96 |  |
| A Short Survey of Pre-trained Language Models for Conversati | Munazza Zaib et al. | ACSW | 2020 | 2104.10810 | 83 |  |
| A Survey on Low-Resource Neural Machine Translation | Rui Wang et al. | IJCAI | 2021 | 2107.04239 | 80 |  |
| Local Interpretations for Explainable Natural Language Proce | Siwen Luo et al. | ACM Computing Surveys | 2021 | 2103.11072 | 72 |  |
| The Decades Progress on Code-Switching Research in NLP: A Sy | Genta Indra Winata et al. | ACL Findings | 2023 | 2212.09660 | 65 |  |
| Trends, Limitations and Open Challenges in Automatic Readabi | Sowmya Vajjala et al. | LREC | 2022 | 2105.00973 | 63 |  |
| Adversarial Attacks on Deep Learning Models in Natural Langu | Wei Emma Zhang et al. | ACM TIST | 2019 | 1901.06796 | 57 |  |
| Empathetic Conversational Systems: A Review of Current Advan | Aravind Sesagiri Raamkuma | IEEE Transactions on Affective Computing | 2022 | 2206.05017 | 54 |  |
| Recent Advances in Named Entity Recognition: A Comprehensive | Imed Keraghel et al. | arXiv | 2024 | 2401.10825 | 50 |  |
| Leveraging Large Language Models for NLG Evaluation: Advance | Zhen Li et al. | EMNLP | 2024 | 2401.07103 | 46 |  |
| A Neural Entity Coreference Resolution Review | Nikolaos Stylianou et al. | Expert Systems with Applications | 2019 | 1910.09329 | 43 |  |
| A Comprehensive Survey of Grammar Error Correction | Yu Wang et al. | arXiv | 2020 | 2005.06600 | 42 |  |
| Recent Trends in Personalized Dialogue Generation: A Review  | Yi-Pei Chen et al. | LREC-COLING | 2024 | 2405.17974 | 38 |  |
| A Survey on Neural Network-Based Summarization Methods | Yue Dong et al. | arXiv | 2018 | 1804.04589 | 37 |  |
| A Survey of Adversarial Defences and Robustness in NLP | Shreya Goyal et al. | ACM Computing Surveys | 2022 | 2203.06414 | 36 |  |
| "Do you follow me?": A Survey of Recent Approaches in Dialog | Leo Jacqmin et al. | SIGDIAL | 2022 | 2207.14627 | 36 |  |
| A Survey of Implicit Discourse Relation Recognition | Wei Xiang et al. | ACM Computing Surveys | 2022 | 2203.02982 | 34 |  |
| A Survey of Multimodal Sarcasm Detection | Shafkat Farabi et al. | IJCAI | 2024 | 2410.18882 | 33 |  |
| A Survey on Text Simplification | Punardeep Sikka et al. | arXiv | 2020 | 2008.08612 | 32 |  |
| A Survey on Neural Machine Reading Comprehension | Boyu Qiu et al. | arXiv | 2019 | 1906.03824 | 32 |  |
| Deep Learning Approaches to Lexical Simplification: A Survey | Kai North et al. | arXiv | 2023 | 2305.12000 | 27 |  |
| Adversarial Attacks and Defense on Texts: A Survey | Aminul Huq et al. | arXiv | 2020 | 2005.14108 | 24 |  |
| Keyphrase Generation: A Multi-Aspect Survey | Erion Cano et al. | FRUCT | 2019 | 1910.05059 | 24 |  |
| A Comprehensive Survey of Sentence Representations: From the | Abhinav Ramesh Kashyap et | EACL | 2024 | 2305.12641 | 23 |  |
| Generative Large Language Models in Automated Fact-Checking: | Ivan Vykopal et al. | arXiv | 2024 | 2407.02351 | 22 |  |
| Coreference Resolution for the Biomedical Domain: A Survey | Pengcheng Lu et al. | arXiv | 2021 | 2109.12424 | 20 |  |
| A Survey on Neural Question Generation: Methods, Application | Shasha Guo et al. | IJCAI | 2024 | 2402.18267 | 19 |  |
| A Survey of Stance Detection on Social Media: New Directions | Bowen Zhang et al. | arXiv | 2024 | 2409.15690 | 17 |  |
| Large Language Models in Argument Mining: A Survey | Hao Li et al. | arXiv | 2025 | 2506.16383 | 15 |  |
| A Survey on Lexical Ambiguity Detection and Word Sense Disam | Miuru Abeysiriwardana et  | arXiv | 2024 | 2403.16129 | 14 |  |
| Innovations in Neural Data-to-text Generation: A Survey | Mandar Sharma et al. | arXiv | 2022 | 2207.12571 | 12 |  |
| A Survey of the Usages of Deep Learning in Natural Language  | Daniel W. Otter et al. | IEEE TNNLS | 2021 | 1807.10854 | 12 |  |
| A Survey on Neural Abstractive Summarization Methods and Fac | Meng Cao et al. | arXiv | 2022 | 2204.09519 | 9 |  |
| Language Modeling for the Future of Finance: A Survey into M | Nikita Tatarinov et al. | arXiv | 2025 | 2504.07274 | 6 |  |
| Transfer Learning for Multi-lingual Tasks -- a Survey | Amir Reza Jafari et al. | arXiv | 2021 | 2110.02052 | 6 |  |
| Recent advancements in computational morphology: A comprehen | Jatayu Baxi et al. | arXiv | 2024 | 2406.05424 | 5 |  |
| A Survey of Text Style Transfer: Applications and Ethical Im | Sourabrata Mukherjee et a | arXiv | 2024 | 2407.16737 | 2 |  |
| Survey on Multi-Document Summarization: Systematic Literatur | Uswa Ihsan et al. | arXiv | 2023 | 2312.12915 | 1 |  |

### 🔊 音声・信号処理

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| wav2vec 2.0: A Framework for Self-Supervised Learning of Spe | Alexei Baevski et al. | NeurIPS | 2020 | 2006.11477 | 8734 |  |
| Supervised Speech Separation Based on Deep Learning: An Over | DeLiang Wang et al. | IEEE/ACM TASLP | 2018 | 1708.07524 | 1598 |  |
| Self-Supervised Speech Representation Learning: A Review | Abdelrahman Mohamed et al | IEEE JSTSP | 2022 | 2205.10643 | 511 |  |
| A Survey on Neural Speech Synthesis | Xu Tan et al. | arXiv | 2021 | 2106.15561 | 474 |  |
| A Review of Speaker Diarization: Recent Advances with Deep L | Tae Jin Park et al. | Computer Speech & Language | 2021 | 2101.09624 | 436 |  |
| An Overview of Voice Conversion and its Challenges: From Sta | Berrak Sisman et al. | IEEE/ACM TASLP | 2020 | 2008.03648 | 425 |  |
| A Review of Deep Learning Techniques for Speech Processing | Ambuj Mehrish et al. | Information Fusion | 2023 | 2305.00359 | 351 |  |
| End-to-End Speech Recognition: A Survey | Rohit Prabhavalkar et al. | IEEE/ACM TASLP | 2023 | 2303.03329 | 301 |  |
| Sound Event Detection: A Tutorial | Annamaria Mesaros et al. | IEEE Signal Processing Magazine | 2021 | 2107.05463 | 272 |  |
| A Survey on Spoken Language Understanding: Recent Advances a | Libo Qin et al. | IJCAI | 2021 | 2103.03095 | 124 |  |
| Recent Advances in Speech Language Models: A Survey | Wenqian Cui et al. | ACL | 2025 | 2410.03751 | 122 | dreamtheater123/Awesome-SpeechLM-Survey |
| WavChat: A Survey of Spoken Dialogue Models | Shengpeng Ji et al. | arXiv | 2024 | 2411.13577 | 109 | jishengpeng/WavChat |
| A Tutorial on Deep Learning for Music Information Retrieval | Keunwoo Choi et al. | arXiv | 2017 | 1709.04396 | 103 |  |
| A Survey on Speech Large Language Models for Understanding | Jing Peng et al. | arXiv | 2024 | 2410.18908 | 97 |  |
| A Comprehensive Survey on Multi-modal Conversational Emotion | Yuntao Shou et al. | arXiv | 2023 | 2312.05735 | 57 |  |
| A Survey of Multilingual Models for Automatic Speech Recogni | Hemant Yadav et al. | LREC | 2022 | 2202.12576 | 54 |  |
| Towards Controllable Speech Synthesis in the Era of Large La | Tianxin Xie et al. | EMNLP | 2025 | 2412.06602 | 41 | imxtx/awesome-controllable-speech-synthesis |
| Emotion Recognition and Generation: A Comprehensive Review o | Rebecca Mobbs et al. | arXiv | 2025 | 2502.06803 | 10 |  |
| Direct Speech-to-Speech Neural Machine Translation: A Survey | Mahendra Gupta et al. | arXiv | 2024 | 2411.14453 | 9 |  |
| Reimagining Speech: A Scoping Review of Deep Learning-Powere | Anders R. Bargum et al. | arXiv | 2023 | 2311.08104 | 9 |  |
| Generative Adversarial Network based Voice Conversion: Techn | Sandipan Dhar et al. | arXiv | 2025 | 2504.19197 | 7 |  |
| Advances in Small-Footprint Keyword Spotting: A Comprehensiv | Soumen Garai et al. | arXiv | 2025 | 2506.11169 | 7 |  |
| Audio-Language Models for Audio-Centric Tasks: A Systematic  | Yi Su et al. | arXiv | 2025 | 2501.15177 | 1 |  |
| Speech Recognition Using Deep Neural Networks: A Systematic  | Ali Bou Nassif et al. | IEEE Access | 2019 |  |  |  |

### 👁️ コンピュータビジョン (CV)

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| A Survey on Deep Learning in Medical Image Analysis | Geert Litjens et al. | Medical Image Analysis | 2017 | 1702.05747 | 13770 |  |
| A Survey of Convolutional Neural Networks: Analysis, Applica | Zewen Li et al. | TNNLS | 2022 | 2004.02806 | 4297 |  |
| Generative Adversarial Networks: An Overview | Antonia Creswell et al. | IEEE Signal Processing Magazine | 2018 | 1710.07035 | 3789 |  |
| Image Segmentation Using Deep Learning: A Survey | Shervin Minaee et al. | TPAMI | 2022 | 2001.05566 | 3783 |  |
| A Survey on Vision Transformer | Kai Han et al. | TPAMI | 2023 | 2012.12556 | 3713 |  |
| Transformers in Vision: A Survey | Salman Khan et al. | CSUR | 2022 | 2101.01169 | 3648 |  |
| Object Detection in 20 Years: A Survey | Zhengxia Zou et al. | Proceedings of the IEEE | 2023 | 1905.05055 | 3459 |  |
| Deep Learning for Generic Object Detection: A Survey | Li Liu et al. | IJCV | 2020 | 1809.02165 | 2820 |  |
| Deep Visual Domain Adaptation: A Survey | Mei Wang et al. | Neurocomputing | 2018 | 1802.03601 | 2321 |  |
| Deep Learning for 3D Point Clouds: A Survey | Yulan Guo et al. | TPAMI | 2021 | 1912.12033 | 2264 |  |
| Deep Learning for Person Re-identification: A Survey and Out | Mang Ye et al. | TPAMI | 2022 | 2001.04193 | 2188 |  |
| Diffusion Models in Vision: A Survey | Florinel-Alin Croitoru et | TPAMI | 2023 | 2209.04747 | 2186 | CroitoruAlin/Diffusion-Models-in-Vision-A-Survey |
| Generalizing from a Few Examples: A Survey on Few-Shot Learn | Yaqing Wang et al. | CSUR | 2020 | 1904.05046 | 2142 |  |
| Threat of Adversarial Attacks on Deep Learning in Computer V | Naveed Akhtar et al. | IEEE Access | 2018 | 1801.00553 | 2066 |  |
| Self-supervised Visual Feature Learning with Deep Neural Net | Longlong Jing et al. | IEEE TPAMI | 2021 | 1902.06162 | 2024 |  |
| Deep Learning in Remote Sensing: A Review | Xiao Xiang Zhu et al. | IEEE GRSM | 2017 | 1710.03959 | 1888 |  |
| Zero-Shot Learning -- A Comprehensive Evaluation of the Good | Yongqin Xian et al. | TPAMI | 2019 | 1707.00600 | 1853 |  |
| Deep Learning for Image Super-resolution: A Survey | Zhihao Wang et al. | TPAMI | 2021 | 1902.06068 | 1813 |  |
| A Survey on Contrastive Self-supervised Learning | Ashish Jaiswal et al. | Technologies | 2021 | 2011.00362 | 1766 |  |
| Deep Facial Expression Recognition: A Survey | Shan Li et al. | IEEE Trans. Affective Computing | 2018 | 1804.08348 | 1679 |  |
| Vision-Language Models for Vision Tasks: A Survey | Jingyi Zhang et al. | TPAMI | 2024 | 2304.00685 | 1459 | jingyi0000/VLM_survey |
| Deep Face Recognition: A Survey | Mei Wang et al. | Neurocomputing | 2021 | 1804.06655 | 1441 |  |
| A Review on Deep Learning Techniques Applied to Semantic Seg | Alberto Garcia-Garcia et  | arXiv | 2017 | 1704.06857 | 1385 |  |
| Deep Learning for Anomaly Detection: A Review | Guansong Pang et al. | CSUR | 2021 | 2007.02500 | 1374 |  |
| Transformers in Medical Imaging: A Survey | Fahad Shamshad et al. | Medical Image Analysis | 2023 | 2201.09873 | 1199 |  |
| A Survey of Deep Learning-based Object Detection | Licheng Jiao et al. | IEEE Access | 2019 | 1907.09408 | 1139 |  |
| Deep Learning-Based Human Pose Estimation: A Survey | Ce Zheng et al. | CSUR | 2023 | 2012.13392 | 967 |  |
| A Survey of Modern Deep Learning based Object Detection Mode | Syed Sahil Abbas Zaidi et | Digital Signal Processing | 2022 | 2104.11892 | 914 |  |
| A Comprehensive Survey of Deep Learning for Image Captioning | MD Zakir Hossain et al. | CSUR | 2019 | 1810.04020 | 895 |  |
| Neural Style Transfer: A Review | Yongcheng Jing et al. | TVCG | 2017 | 1705.04058 | 866 |  |
| Human Action Recognition from Various Data Modalities: A Rev | Zehua Sun et al. | TPAMI | 2023 | 2012.11866 | 799 |  |
| Salient Object Detection in the Deep Learning Era: An In-Dep | Wenguan Wang et al. | TPAMI | 2022 | 1904.09146 | 744 |  |
| Going Deeper into Action Recognition: A Survey | Samitha Herath et al. | Image and Vision Computing | 2017 | 1605.04988 | 642 |  |
| GAN Inversion: A Survey | Weihao Xia et al. | TPAMI | 2022 | 2101.05278 | 636 | weihaox/GAN-Inversion |
| Low-Light Image and Video Enhancement Using Deep Learning: A | Chongyi Li et al. | TPAMI | 2021 | 2104.10729 | 570 | ShenZheng2000/LLIE_Survey |
| A Survey on Self-supervised Learning: Algorithms, Applicatio | Jie Gui et al. | TPAMI | 2024 | 2301.05712 | 560 |  |
| Advances in Neural Rendering | Ayush Tewari et al. | Computer Graphics Forum | 2021 | 2111.05849 | 550 |  |
| Domain Adaptation for Visual Applications: A Comprehensive S | Gabriela Csurka | Springer (book chapter) | 2017 | 1702.05374 | 549 |  |
| A Survey of Visual Transformers | Yang Liu et al. | TNNLS | 2023 | 2111.06091 | 545 |  |
| Scene Text Detection and Recognition: The Deep Learning Era | Shangbang Long et al. | IJCV | 2021 | 1811.04256 | 502 |  |
| Fine-Grained Image Analysis with Deep Learning: A Survey | Xiu-Shen Wei et al. | TPAMI | 2021 | 2111.06119 | 461 |  |
| 3D Object Detection for Autonomous Driving: A Comprehensive  | Jiageng Mao et al. | IJCV | 2023 | 2206.09474 | 456 | PointsCoder/Awesome-3D-Object-Detection-for-Autonomous-Driving |
| Text-to-image Diffusion Models in Generative AI: A Survey | Chenshuang Zhang et al. | arXiv | 2023 | 2303.07909 | 432 |  |
| Deep Image Deblurring: A Survey | Kaihao Zhang et al. | IJCV | 2022 | 2201.10700 | 384 |  |
| Class-Incremental Learning: A Survey | Da-Wei Zhou et al. | TPAMI | 2023 | 2302.03648 | 375 |  |
| Deep Learning for Visual Tracking: A Comprehensive Survey | Seyed Mojtaba Marvasti-Za | IEEE T-ITS | 2022 | 1912.00535 | 360 |  |
| A Survey on 3D Gaussian Splatting | Guikun Chen et al. | TPAMI | 2024 | 2401.03890 | 351 | guikunchen/Awesome3DGS |
| Transformer-Based Visual Segmentation: A Survey | Xiangtai Li et al. | TPAMI | 2024 | 2304.09854 | 316 | lxtGH/Awesome-Segmentation-With-Transformer |
| NeRF: Neural Radiance Field in 3D Vision: A Comprehensive Re | Kyle Gao et al. | arXiv | 2022 | 2210.00379 | 306 |  |
| RGB-D Salient Object Detection: A Survey | Tao Zhou et al. | Computational Visual Media | 2020 | 2008.00230 | 304 | taozh2017/RGBD-SODsurvey |
| A Survey on Deep Learning Technique for Video Segmentation | Wenguan Wang et al. | TPAMI | 2023 | 2107.01153 | 303 | tfzhou/VS-Survey |
| Monocular Depth Estimation Based On Deep Learning: An Overvi | Chaoqiang Zhao et al. | Science China Technological Sciences | 2020 | 2003.06620 | 296 |  |
| Deep Gait Recognition: A Survey | Alireza Sepas-Moghaddam e | TPAMI | 2021 | 2102.09546 | 271 |  |
| Towards Open Vocabulary Learning: A Survey | Jianzong Wu et al. | TPAMI | 2023 | 2306.15880 | 261 | jianzongwu/Awesome-Open-Vocabulary |
| Appearance-based Gaze Estimation With Deep Learning: A Revie | Yihua Cheng et al. | TPAMI | 2021 | 2104.12668 | 251 |  |
| Video Super Resolution Based on Deep Learning: A Comprehensi | Hongying Liu et al. | Artificial Intelligence Review | 2020 | 2007.12928 | 228 |  |
| A Survey on Long-Tailed Visual Recognition | Lu Yang et al. | IJCV | 2022 | 2205.13775 | 193 |  |
| Comprehensive Review of Deep Learning-Based 3D Point Cloud C | Ben Fei et al. | IEEE T-ITS | 2022 | 2203.03311 | 192 |  |
| Video Transformers: A Survey | Javier Selva et al. | TPAMI | 2023 | 2201.05991 | 169 |  |
| Scene Graph Generation: A Comprehensive Survey | Guangming Zhu et al. | Neurocomputing | 2022 | 2201.00443 | 168 |  |
| Multimodal Alignment and Fusion: A Survey | Songtao Li et al. | arXiv | 2024 | 2411.17040 | 156 |  |
| Diffusion Models, Image Super-Resolution And Everything: A S | Brian B. Moser et al. | TNNLS | 2024 | 2401.00736 | 149 |  |
| A Comprehensive Survey on Segment Anything Model for Vision  | Chunhui Zhang et al. | arXiv | 2023 | 2305.08196 | 145 |  |
| 3D Gaussian Splatting: Survey, Technologies, Challenges, and | Yanqi Bao et al. | arXiv | 2024 | 2407.17418 | 143 | qqqqqqy0227/awesome-3DGS |
| Deep Learning for Micro-expression Recognition: A Survey | Yante Li et al. | IEEE Trans. Affective Computing | 2021 | 2107.02823 | 142 |  |
| Deep Learning for Event-based Vision: A Comprehensive Survey | Xu Zheng et al. | arXiv | 2023 | 2302.08890 | 139 |  |
| Deepfake Detection: A Comprehensive Survey from the Reliabil | Tianyi Wang et al. | ACM Computing Surveys | 2022 | 2211.10881 | 135 |  |
| Deepfake Generation and Detection: A Benchmark and Survey | Gan Pei et al. | arXiv | 2024 | 2403.17881 | 131 |  |
| Few-Shot Object Detection: A Comprehensive Survey | Mona Köhler et al. | TNNLS | 2023 | 2112.11699 | 124 |  |
| Image Colorization: A Survey and Dataset | Saeed Anwar et al. | Information Fusion | 2020 | 2008.10774 | 110 |  |
| A Survey on Open-Vocabulary Detection and Segmentation: Past | Chaoyang Zhu et al. | TPAMI | 2023 | 2307.09220 | 106 |  |
| Local Feature Matching Using Deep Learning: A Survey | Shibiao Xu et al. | Information Fusion | 2024 | 2401.17592 | 105 | vignywang/Awesome-Local-Feature-Matching |
| A Comprehensive Survey and Taxonomy on Single Image Dehazing | Jie Gui et al. | ACM Computing Surveys | 2021 | 2106.03323 | 104 |  |
| 2D Human Pose Estimation: A Survey | Haoming Chen et al. | arXiv | 2022 | 2204.07370 | 102 |  |
| Face Generation and Editing with StyleGAN: A Survey | Andrew Melnik et al. | TPAMI | 2022 | 2212.09102 | 98 |  |
| Deep Learning-based Image and Video Inpainting: A Survey | Weize Quan et al. | IJCV | 2024 | 2401.03395 | 95 |  |
| A Survey of Deep Learning Approaches for OCR and Document Un | Nishant Subramani et al. | arXiv | 2020 | 2011.13534 | 90 |  |
| Deep Learning for Visual Localization and Mapping: A Survey | Changhao Chen et al. | arXiv | 2023 | 2308.14039 | 86 |  |
| Transformers in 3D Point Clouds: A Survey | Dening Lu et al. | arXiv | 2022 | 2205.07417 | 77 |  |
| Deep Learning-Based Object Pose Estimation: A Comprehensive  | Jian Liu et al. | IJCV | 2024 | 2405.07801 | 75 |  |
| Neural Volume Rendering: NeRF And Beyond | Frank Dellaert et al. | arXiv | 2021 | 2101.05204 | 73 |  |
| A Survey on Deep Stereo Matching in the Twenties | Fabio Tosi et al. | IJCV | 2024 | 2407.07816 | 68 |  |
| A Survey of Camouflaged Object Detection and Beyond | Fengyang Xiao et al. | arXiv | 2024 | 2408.14562 | 67 |  |
| Towards Unified Deep Image Deraining: A Survey and A New Ben | Xiang Chen et al. | arXiv | 2023 | 2310.03535 | 63 |  |
| 3D and 4D World Modeling: A Survey | Lingdong Kong et al. | arXiv | 2025 | 2509.07996 | 61 | worldbench/awesome-3d-4d-world-models |
| Video Anomaly Detection in 10 Years: A Survey and Outlook | Moshira Abdalla et al. | arXiv | 2024 | 2405.19387 | 55 |  |
| A Survey of Label-Efficient Deep Learning for 3D Point Cloud | Aoran Xiao et al. | TPAMI | 2023 | 2305.19812 | 50 |  |
| Panoptic Segmentation: A Review | Omar Elharrouss et al. | arXiv | 2021 | 2111.10250 | 49 |  |
| Masked Image Modeling: A Survey | Vlad Hondru et al. | IJCV | 2025 | 2408.06687 | 48 |  |
| Optical Flow Estimation in the Deep Learning Age | Junhwa Hur et al. | arXiv | 2020 | 2004.02853 | 41 |  |
| Deep learning for 3D human pose estimation and mesh recovery | Yang Liu et al. | Neurocomputing | 2024 | 2402.18844 | 39 |  |
| Masked Modeling for Self-supervised Representation Learning  | Siyuan Li et al. | arXiv | 2024 | 2401.00897 | 35 | Lupin1998/Awesome-MIM |
| Learning-based Multi-View Stereo: A Survey | Fangjinhua Wang et al. | arXiv | 2024 | 2408.15235 | 34 |  |
| A Survey on Deep Learning-based Single Image Crowd Counting: | Haoyue Bai et al. | Neurocomputing | 2020 | 2012.15685 | 32 |  |
| Efficient Annotation and Learning for 3D Hand Pose Estimatio | Takehiko Ohkawa et al. | IJCV | 2022 | 2206.02257 | 27 |  |
| Multimodal Referring Segmentation: A Survey | Henghui Ding et al. | arXiv | 2025 | 2508.00265 | 26 |  |
| Deep Image Matting: A Comprehensive Survey | Jizhizi Li et al. | arXiv | 2023 | 2304.04672 | 22 | JizhiziLi/matting-survey |
| A Survey on 3D Gaussian Splatting Applications: Segmentation | Shuting He et al. | arXiv | 2025 | 2508.09977 | 19 | heshuting555/Awesome-3DGS-Applications |
| A Survey on Image Quality Assessment: Insights, Analysis, an | Chengqian Ma et al. | arXiv | 2025 | 2502.08540 | 15 |  |
| CLIP-Powered Domain Generalization and Domain Adaptation: A  | Jindong Li et al. | arXiv preprint | 2025 | 2504.14280 | 14 | jindongli-Ai/Survey_on_CLIP-Powered_Domain_Generalization_and_Adaptation |
| Deep Learning-Based Point Cloud Registration: A Comprehensiv | Yu-Xin Zhang et al. | IJCV | 2024 | 2404.13830 | 14 |  |
| A Survey on Deep Learning-based Spatio-temporal Action Detec | Peng Wang et al. | Int. J. Wavelets Multiresolut. Inf. Process. | 2023 | 2308.01618 | 13 |  |
| Deep Learning for Video-based Person Re-Identification: A Su | Khawar Islam et al. | arXiv | 2023 | 2303.11332 | 11 |  |
| From Pixels to Portraits: A Comprehensive Survey of Talking  | Shreyank N Gowda et al. | arXiv | 2023 | 2308.16041 | 11 |  |
| Deep Learning-Based Multi-Object Tracking: A Comprehensive S | Momir Adžemović et al. | arXiv | 2025 | 2506.13457 | 10 |  |
| A Review of Human-Object Interaction Detection | Yuxiao Wang et al. | arXiv | 2024 | 2408.10641 | 10 |  |
| Priors in Deep Image Restoration and Enhancement: A Survey | Yunfan Lu et al. | arXiv | 2022 | 2206.02070 | 9 | yunfanLu/Awesome-Image-Prior |
| Deep Learning Techniques for Video Instance Segmentation: A  | Chenhao Xu et al. | arXiv | 2023 | 2310.12393 | 5 |  |

### 📈 機械学習 (一般)

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| Representation Learning: A Review and New Perspectives | Yoshua Bengio et al. | IEEE TPAMI | 2013 | 1206.5538 | 14029 |  |
| Bootstrap your own latent: A new approach to self-supervised | Jean-Bastien Grill et al. | NeurIPS | 2020 | 2006.07733 | 8758 |  |
| Variational Inference: A Review for Statisticians | David M. Blei et al. | JASA | 2017 | 1601.00670 | 5801 |  |
| Efficient Processing of Deep Neural Networks: A Tutorial and | Vivienne Sze et al. | Proceedings of the IEEE | 2017 | 1703.09039 | 3677 |  |
| Self-supervised Learning: Generative or Contrastive | Xiao Liu et al. | IEEE TKDE | 2021 | 2006.08218 | 2198 |  |
| A tutorial on conformal prediction | Glenn Shafer et al. | JMLR | 2008 | 0706.3188 | 1688 |  |
| Deep Neural Networks and Tabular Data: A Survey | Vadim Borisov et al. | IEEE TNNLS | 2022 | 2110.01889 | 1188 |  |
| A Gentle Introduction to Conformal Prediction and Distributi | Anastasios N. Angelopoulo | arXiv | 2021 | 2107.07511 | 1151 |  |
| A survey of sparse representation: algorithms and applicatio | Zheng Zhang et al. | IEEE Access | 2015 | 1602.07017 | 1058 |  |
| A Survey of Unsupervised Deep Domain Adaptation | Garrett Wilson et al. | ACM TIST | 2020 | 1812.02849 | 1017 |  |
| Dynamic Neural Networks: A Survey | Yizeng Han et al. | TPAMI | 2022 | 2102.04906 | 933 |  |
| Kernel Mean Embedding of Distributions: A Review and Beyond | Krikamol Muandet et al. | Foundations and Trends in ML | 2017 | 1605.09522 | 899 |  |
| When Gaussian Process Meets Big Data: A Review of Scalable G | Haitao Liu et al. | IEEE TNNLS | 2018 | 1807.01065 | 871 |  |
| Multiple Instance Learning: A Survey of Problem Characterist | Marc-Andre Carbonneau et  | Pattern Recognition | 2016 | 1612.03365 | 747 |  |
| A Survey on Metric Learning for Feature Vectors and Structur | Aurelien Bellet et al. | arXiv | 2013 | 1306.6709 | 713 |  |
| Learning from positive and unlabeled data: a survey | Jessa Bekker et al. | Machine Learning | 2020 | 1811.04820 | 706 |  |
| A Survey of Optimization Methods from a Machine Learning Per | Shiliang Sun et al. | IEEE Transactions on Cybernetics | 2020 | 1906.06821 | 669 |  |
| Curriculum Learning: A Survey | Petru Soviany et al. | IJCV | 2022 | 2101.10382 | 571 |  |
| Recent Advances in Autoencoder-Based Representation Learning | Michael Tschannen et al. | NeurIPS Workshop | 2018 | 1812.05069 | 510 |  |
| A Survey of Machine Unlearning | Thanh Tam Nguyen et al. | arXiv | 2022 | 2209.02299 | 435 | tamlhp/awesome-machine-unlearning |
| Model Merging in LLMs, MLLMs, and Beyond: Methods, Theories, | Enneng Yang et al. | ACM Computing Surveys | 2024 | 2408.07666 | 269 | EnnengYang/Awesome-Model-Merging-Methods-Theories-Applications |
| Deep Clustering: A Comprehensive Survey | Yazhou Ren et al. | IEEE TNNLS | 2022 | 2210.04142 | 268 |  |
| A Unified Survey on Anomaly, Novelty, Open-Set, and Out-of-D | Mohammadreza Salehi et al | TMLR | 2022 | 2110.14051 | 246 |  |
| A Survey on Kolmogorov-Arnold Network | Shriyank Somvanshi et al. | arXiv | 2024 | 2411.06078 | 234 |  |
| Empowering Edge Intelligence: A Comprehensive Survey on On-D | Xubin Wang et al. | arXiv preprint | 2025 | 2503.06027 | 199 |  |
| Large Language Models for Generative Recommendation: A Surve | Lei Li et al. | arXiv | 2023 | 2309.01157 | 162 |  |
| Manifold learning: what, how, and why | Marina Meila et al. | Annual Review of Statistics | 2023 | 2311.03757 | 159 |  |
| A Comprehensive Survey of Forgetting in Deep Learning Beyond | Zhenyi Wang et al. | IEEE TPAMI | 2024 | 2307.09218 | 117 | EnnengYang/Awesome-Forgetting-in-Deep-Learning |
| A Survey on Diffusion Models for Time Series and Spatio-Temp | Yiyuan Yang et al. | arXiv | 2024 | 2404.18886 | 116 | yyysjz1997/Awesome-TimeSeries-SpatioTemporal-Diffusion-Model |
| A Survey on Programmatic Weak Supervision | Jieyu Zhang et al. | arXiv | 2022 | 2202.05433 | 112 |  |
| Calibration in Deep Learning: A Survey of the State-of-the-A | Cheng Wang et al. | arXiv | 2023 | 2308.01222 | 107 |  |
| Large Language Model Inference Acceleration: A Comprehensive | Jinhao Li et al. | arXiv preprint | 2024 | 2410.04466 | 83 | Kimho666/LLM_Hardware_Survey |
| A Comprehensive Survey on Knowledge Distillation | Amir M. Mansourian et al. | arXiv preprint | 2025 | 2503.12067 | 76 | IPL-sharif/KD_Survey |
| Conformal Prediction for Natural Language Processing: A Surv | Margarida M. Campos et al | TACL | 2024 | 2405.01976 | 64 |  |
| Reproducing Kernel Hilbert Space, Mercer's Theorem, Eigenfun | Benyamin Ghojogh et al. | arXiv | 2021 | 2106.08443 | 61 |  |
| Supervised Dictionary Learning and Sparse Representation-A R | Mehrdad J. Gangeh et al. | arXiv | 2015 | 1502.05928 | 59 |  |
| Efficient Training of Large Language Models on Distributed I | Jiangfei Duan et al. | arXiv preprint | 2024 | 2407.20018 | 56 |  |
| A Survey of Methods for Addressing Class Imbalance in Deep-L | Sophie Henning et al. | EACL | 2023 | 2210.04675 | 56 |  |
| Kolmogorov-Arnold Networks: A Critical Assessment of Claims, | Yuntian Hou et al. | arXiv | 2024 | 2407.11075 | 55 |  |
| A Survey on Open Set Recognition | Atefeh Mahdavi et al. | arXiv | 2021 | 2109.00893 | 53 |  |
| A Survey on Deep Tabular Learning | Shriyank Somvanshi et al. | arXiv | 2024 | 2410.12034 | 48 |  |
| Deep Learning for Multi-Label Learning: A Comprehensive Surv | Adane Nega Tarekegn et al | arXiv | 2024 | 2401.16549 | 48 |  |
| Representation Learning for Tabular Data: A Comprehensive Su | Jun-Peng Jiang et al. | arXiv | 2025 | 2504.16109 | 47 | LAMDA-Tabular/Tabular-Survey |
| Graph Foundation Models: A Comprehensive Survey | Zehong Wang et al. | arXiv | 2025 | 2505.15116 | 46 |  |
| Cognitive Edge Computing: A Comprehensive Survey on Optimizi | Xubin Wang et al. | arXiv preprint | 2025 | 2501.03265 | 33 |  |
| Foundation Models for Time Series: A Survey | Siva Rama Krishna Kottapa | arXiv | 2025 | 2504.04011 | 30 |  |
| Spectral, Probabilistic, and Deep Metric Learning: Tutorial  | Benyamin Ghojogh et al. | arXiv | 2022 | 2201.09267 | 30 |  |
| A Survey of Generative Search and Recommendation in the Era  | Yongqi Li et al. | arXiv | 2024 | 2404.16924 | 28 |  |
| Deep Gaussian Processes: A Survey | Kalvik Jakkala et al. | arXiv | 2021 | 2106.12135 | 27 |  |
| The Evolution of Dataset Distillation: Toward Scalable and G | Ping Liu et al. | arXiv preprint | 2025 | 2502.05673 | 26 |  |
| Information Compression in the AI Era: Recent Advances and F | Jun Chen et al. | arXiv | 2024 | 2406.10036 | 24 |  |
| Neural Tangent Kernel: A Survey | Eugene Golikov et al. | arXiv | 2022 | 2208.13614 | 22 |  |
| Advancing Intelligent Sequence Modeling: Evolution, Trade-of | Shriyank Somvanshi et al. | arXiv | 2025 | 2503.18970 | 18 |  |
| Hardware Acceleration of LLMs: A comprehensive survey and co | Nikoletta Koilia et al. | arXiv preprint | 2024 | 2409.03384 | 16 |  |
| A Survey on Extreme Multi-label Learning | Tong Wei et al. | arXiv | 2022 | 2210.03968 | 14 |  |
| Hyperparameter Optimization in Machine Learning | Luca Franceschi et al. | arXiv preprint | 2024 | 2410.22854 | 12 |  |
| Systems for Parallel and Distributed Large-Model Deep Learni | Kabir Nagrecha et al. | arXiv preprint | 2023 | 2301.02691 | 9 |  |
| A Survey on Ordinal Regression: Applications, Advances and P | Jinhong Wang et al. | arXiv | 2025 | 2503.00952 | 5 |  |
| Hitchhiker's guide on the relation of Energy-Based Models wi | Davide Carbone et al. | TMLR | 2025 | 2406.13661 | 5 |  |
| Hardware Acceleration for Neural Networks: A Comprehensive S | Bin Xu et al. | arXiv preprint | 2025 | 2512.23914 | 5 |  |
| GR-LLMs: Recent Advances in Generative Recommendation Based  | Zhen Yang et al. | arXiv | 2025 | 2507.06507 | 4 |  |
| Green AI: A systematic review and meta-analysis of its defin | Marcel Rojahn et al. | arXiv preprint | 2025 | 2511.07090 | 4 |  |
| Onboard Optimization and Learning: A Survey | Monirul Islam Pavel et al | arXiv preprint | 2025 | 2505.08793 | 4 |  |
| Generalized Out-of-Distribution Detection: A Survey | Jingkang Yang et al. | IJCV | 2024 | 2110.11334 |  | huytransformer/Awesome-Out-Of-Distribution-Detection |
| Neural Architecture Search: Insights from 1000 Papers | Colin White et al. | arXiv | 2023 | 2301.08727 |  |  |
| A Comprehensive Survey of Continual Learning: Theory, Method | Liyuan Wang et al. | TPAMI | 2023 | 2302.00487 |  |  |
| What-is and How-to for Fairness in Machine Learning: A Surve | Zeyu Tang et al. | ACM Computing Surveys | 2023 | 2206.04101 |  |  |
| A survey and taxonomy of loss functions in machine learning | Lorenzo Ciampiconi et al. | arXiv | 2023 | 2301.05579 |  |  |
| A Survey on Negative Transfer | Wen Zhang et al. | IEEE/CAA JAS | 2022 | 2009.00909 |  |  |
| Meta-Learning in Neural Networks: A Survey | Timothy Hospedales et al. | TPAMI | 2022 | 2004.05439 |  |  |
| Ensemble deep learning: A review | M. A. Ganaie et al. | Engineering Applications of AI | 2022 | 2104.02395 |  |  |
| Hands-on Bayesian Neural Networks -- a Tutorial for Deep Lea | Laurent Valentin Jospin e | IEEE Computational Intelligence Magazine | 2022 | 2007.06823 |  |  |
| Domain Generalization: A Survey | Kaiyang Zhou et al. | TPAMI | 2022 | 2103.02503 |  |  |
| Image Data Augmentation for Deep Learning: A Survey | Suorong Yang et al. | arXiv | 2022 | 2204.08610 |  |  |
| Learning from Noisy Labels with Deep Neural Networks: A Surv | Hwanjun Song et al. | IEEE TNNLS | 2022 | 2007.08199 |  |  |
| A Survey on Multi-Task Learning | Yu Zhang et al. | IEEE TKDE | 2021 | 1707.08114 |  |  |
| A survey on Semi-, Self- and Unsupervised Learning for Image | Lars Schmarje et al. | IEEE Access | 2021 | 2002.08721 |  |  |
| Self-Supervised Representation Learning: Introduction, Advan | Linus Ericsson et al. | IEEE Signal Processing Magazine | 2021 | 2110.09327 |  |  |
| A Review of Uncertainty Quantification in Deep Learning: Tec | Moloud Abdar et al. | Information Fusion | 2021 | 2011.06225 |  |  |
| A Survey of Uncertainty in Deep Neural Networks | Jakob Gawlikowski et al. | Artificial Intelligence Review | 2021 | 2107.03342 |  |  |
| Knowledge Distillation: A Survey | Jianping Gou et al. | IJCV | 2021 | 2006.05525 |  |  |
| Efficient Deep Learning: A Survey on Making Deep Learning Mo | Gaurav Menghani et al. | ACM Computing Surveys | 2021 | 2106.08962 |  |  |
| A Survey of Quantization Methods for Efficient Neural Networ | Amir Gholami et al. | arXiv | 2021 | 2103.13630 |  |  |
| Time Series Data Augmentation for Deep Learning: A Survey | Qingsong Wen et al. | IJCAI | 2021 | 2002.12478 |  |  |
| Interpretable Deep Learning: Interpretation, Interpretabilit | Xuhong Li et al. | Knowledge and Information Systems | 2021 | 2103.10689 |  |  |
| A Survey on Bias and Fairness in Machine Learning | Ninareh Mehrabi et al. | ACM Computing Surveys | 2021 | 1908.09635 |  |  |
| Towards Causal Representation Learning | Bernhard Schölkopf et al. | Proceedings of the IEEE | 2021 | 2102.11107 |  |  |
| AutoML: A Survey of the State-of-the-Art | Xin He et al. | Knowledge-Based Systems | 2021 | 1908.00709 |  |  |
| Model Complexity of Deep Learning: A Survey | Xia Hu et al. | Knowledge and Information Systems | 2021 | 2103.05127 |  |  |
| A Comprehensive Survey on Transfer Learning | Fuzhen Zhuang et al. | Proceedings of the IEEE | 2020 | 1911.02685 |  |  |
| Multi-Task Learning with Deep Neural Networks: A Survey | Michael Crawshaw et al. | arXiv | 2020 | 2009.09796 |  |  |
| A Brief Review of Domain Adaptation | Abolfazl Farahani et al. | arXiv | 2020 | 2010.03978 |  |  |
| A Survey of Model Compression and Acceleration for Deep Neur | Yu Cheng et al. | IEEE Signal Processing Magazine | 2020 | 1710.09282 |  |  |
| What is the State of Neural Network Pruning? | Davis Blalock et al. | MLSys | 2020 | 2003.03033 |  |  |
| Explainable Artificial Intelligence: a Systematic Review | Giulia Vilone et al. | arXiv | 2020 | 2006.00093 |  |  |
| Hyper-Parameter Optimization: A Review of Algorithms and App | Tong Yu et al. | arXiv | 2020 | 2003.05689 |  |  |
| Neural Architecture Search: A Survey | Thomas Elsken et al. | JMLR | 2019 | 1808.05377 |  |  |
| Continual Lifelong Learning with Neural Networks: A Review | German I. Parisi et al. | Neural Networks | 2019 | 1802.07569 |  |  |
| A Survey on Deep Transfer Learning | Chuanqi Tan et al. | ICANN | 2018 | 1808.01974 |  |  |
| An overview of gradient descent optimization algorithms | Sebastian Ruder et al. | arXiv | 2016 | 1609.04747 |  |  |
| A Survey on Transfer Learning | Sinno Jialin Pan et al. | IEEE TKDE | 2010 |  |  |  |

### 📐 学習理論

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| Introduction to Online Convex Optimization | Elad Hazan et al. | Foundations and Trends in Optimization | 2019 | 1909.05207 | 2299 |  |
| Introduction to Multi-Armed Bandits | Aleksandrs Slivkins et al | Foundations and Trends in ML | 2019 | 1904.07272 | 1275 |  |
| Fairness in Machine Learning: A Survey | Simon Caton et al. | ACM Computing Surveys | 2020 | 2010.04053 | 912 |  |
| Online Learning: A Comprehensive Survey | Steven C. H. Hoi et al. | Neurocomputing | 2021 | 1802.02871 | 828 |  |
| A Modern Introduction to Online Learning | Francesco Orabona et al. | arXiv | 2019 | 1912.13213 | 560 |  |
| Generalization in Deep Learning | Kenji Kawaguchi et al. | Cambridge University Press | 2022 | 1710.05468 | 501 |  |
| The Principles of Deep Learning Theory | Daniel A. Roberts et al. | Cambridge University Press | 2022 | 2106.10165 | 290 |  |
| A Primer on PAC-Bayesian Learning | Benjamin Guedj et al. | arXiv | 2019 | 1901.05353 | 241 |  |
| A Survey on Contextual Multi-armed Bandits | Li Zhou et al. | arXiv | 2016 | 1508.03326 | 145 |  |
| A Survey on Practical Applications of Multi-Armed and Contex | Djallel Bouneffouf et al. | arXiv | 2019 | 1904.10040 | 142 |  |
| The Modern Mathematics of Deep Learning | Julius Berner et al. | Cambridge University Press | 2022 | 2105.04026 | 138 |  |
| On the Implicit Bias in Deep-Learning Algorithms | Gal Vardi et al. | Communications of the ACM | 2022 | 2208.12591 | 121 |  |
| Online convex optimization and no-regret learning: Algorithm | E. Veronica Belmega et al | arXiv | 2018 | 1804.04529 | 45 |  |
| Generalization in Neural Networks: A Broad Survey | Chris Rohlfs et al. | Neurocomputing | 2022 | 2209.01610 | 36 |  |
| A Survey on Statistical Theory of Deep Learning: Approximati | Namjoon Suh et al. | Annual Review of Statistics and Its Application | 2024 | 2401.07187 | 28 |  |
| A Survey of Risk-Aware Multi-Armed Bandits | Vincent Y. F. Tan et al. | IJCAI | 2022 | 2205.05843 | 13 |  |
| Approximation Power of Deep Neural Networks: an explanatory  | Owen Davis et al. | arXiv | 2022 | 2207.09511 | 5 |  |
| A Comprehensive Guide to Differential Privacy: From Theory t | Napsu Karmitsa et al. | arXiv | 2025 | 2509.03294 | 3 |  |

### 🎮 強化学習 (RL)

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| Deep Reinforcement Learning: A Brief Survey | Kai Arulkumaran et al. | IEEE Signal Processing Magazine | 2017 | 1708.05866 | 3581 |  |
| Offline Reinforcement Learning: Tutorial, Review, and Perspe | Sergey Levine et al. | arXiv | 2020 | 2005.01643 | 2709 |  |
| Deep Reinforcement Learning: An Overview | Yuxi Li | arXiv | 2017 | 1701.07274 | 1849 |  |
| Sim-to-Real Transfer in Deep Reinforcement Learning for Robo | Wenshuai Zhao et al. | IEEE SSCI | 2020 | 2009.13303 | 1051 |  |
| An Algorithmic Perspective on Imitation Learning | Takayuki Osa et al. | Foundations and Trends in Robotics | 2018 | 1811.06711 | 1027 |  |
| Open Problems and Fundamental Limitations of Reinforcement L | Stephen Casper et al. | TMLR | 2023 | 2307.15217 | 926 |  |
| Transfer Learning in Deep Reinforcement Learning: A Survey | Zhuangdi Zhu et al. | IEEE TPAMI | 2023 | 2009.07888 | 899 |  |
| A Survey of Inverse Reinforcement Learning: Challenges, Meth | Saurabh Arora et al. | Artificial Intelligence | 2021 | 1806.06877 | 791 |  |
| Reinforcement Learning in Healthcare: A Survey | Chao Yu et al. | ACM Computing Surveys | 2021 | 1908.08796 | 784 |  |
| Curriculum Learning for Reinforcement Learning Domains: A Fr | Sanmit Narvekar et al. | JMLR | 2020 | 2003.04960 | 740 |  |
| Exploration in Deep Reinforcement Learning: A Survey | Pawel Ladosz et al. | Information Fusion | 2022 | 2205.00824 | 601 |  |
| A Practical Guide to Multi-Objective Reinforcement Learning  | Conor F. Hayes et al. | AAMAS (JAAMAS) | 2022 | 2103.09568 | 579 |  |
| A Survey on Offline Reinforcement Learning: Taxonomy, Review | Rafael Figueiredo Prudenc | IEEE TNNLS | 2023 | 2203.01387 | 420 | larocs/offline-rl-suvey |
| A Survey of Reinforcement Learning from Human Feedback | Timo Kaufmann et al. | arXiv | 2023 | 2312.14925 | 337 |  |
| A Review of Safe Reinforcement Learning: Methods, Theory and | Shangding Gu et al. | IEEE TPAMI | 2024 | 2205.10330 | 325 | chauncygu/Safe-Reinforcement-Learning-Baselines |
| A Survey of Zero-shot Generalisation in Deep Reinforcement L | Robert Kirk et al. | JAIR | 2023 | 2111.09794 | 285 |  |
| Goal-Conditioned Reinforcement Learning: Problems and Soluti | Minghuan Liu et al. | IJCAI | 2022 | 2201.08299 | 226 |  |
| A Survey on Model-based Reinforcement Learning | Fan-Ming Luo et al. | Science China Information Sciences | 2024 | 2206.09328 | 178 |  |
| A Tutorial on Meta-Reinforcement Learning | Jacob Beck et al. | Foundations and Trends in Machine Learning | 2025 | 2301.08028 | 164 |  |
| A Survey of Exploration Methods in Reinforcement Learning | Susan Amin et al. | arXiv | 2021 | 2109.00157 | 110 |  |
| A Survey of Constraint Formulations in Safe Reinforcement Le | Akifumi Wachi et al. | IJCAI | 2024 | 2402.02025 | 74 |  |
| A Survey of Temporal Credit Assignment in Deep Reinforcement | Eduardo Pignatelli et al. | arXiv | 2023 | 2312.01072 | 60 |  |
| Model-based Reinforcement Learning: A Survey | Thomas M. Moerland et al. | Foundations and Trends in Machine Learning | 2023 | 2006.16712 | 58 |  |
| Distributed Deep Reinforcement Learning: A Survey and A Mult | Qiyue Yin et al. | Machine Intelligence Research | 2024 | 2212.00253 | 37 |  |
| Reinforcement Learning for Generative AI: State of the Art,  | Giorgio Franceschelli et  | JAIR | 2024 | 2308.00031 | 37 |  |
| A Survey of In-Context Reinforcement Learning | Amir Moeini et al. | arXiv preprint | 2025 | 2502.07978 | 35 |  |
| Reward Models in Deep Reinforcement Learning: A Survey | Rui Yu et al. | IJCAI | 2025 | 2506.15421 | 30 |  |
| Reinforcement Learning for Generative AI: A Survey | Yuanjiang Cao et al. | arXiv | 2023 | 2308.14328 | 28 |  |
| A Survey of Safe Reinforcement Learning and Constrained MDPs | Ankita Kushwaha et al. | arXiv preprint | 2025 | 2505.17342 | 23 |  |
| Reinforcement Learning for Large Model: A Survey | Weijia Wu et al. | arXiv preprint | 2025 | 2508.08189 | 5 | weijiawu/Awesome-RL-for-Multimodal-Foundation-Models |
| Hierarchical Reinforcement Learning: A Comprehensive Survey | Shubham Pateria et al. | ACM Computing Surveys | 2021 |  |  |  |
| A Survey of Preference-Based Reinforcement Learning Methods | Christian Wirth et al. | JMLR | 2017 |  |  |  |
| A Comprehensive Survey on Safe Reinforcement Learning | Javier Garcia et al. | JMLR | 2015 |  |  |  |
| Bayesian Reinforcement Learning: A Survey | Mohammad Ghavamzadeh et a | Foundations and Trends in Machine Learning | 2015 | 1609.04436 |  |  |

### 🤖 ロボティクス・身体性

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| Deep Reinforcement Learning for Autonomous Driving: A Survey | B Ravi Kiran et al. | IEEE Transactions on Intelligent Transportation Systems | 2022 | 2002.00444 | 2400 |  |
| A Survey of Deep Learning Techniques for Autonomous Driving | Sorin Grigorescu et al. | Journal of Field Robotics | 2020 | 1910.07738 | 1736 |  |
| Safe Learning in Robotics: From Learning-Based Control to Sa | Lukas Brunke et al. | Annual Review of Control, Robotics, and Autonomous Systems | 2022 | 2108.06266 | 970 |  |
| Survey of Deep Reinforcement Learning for Motion Planning of | Szilard Aradi | IEEE Transactions on Intelligent Transportation Systems | 2022 | 2001.11231 | 591 |  |
| A Survey of Embodied AI: From Simulators to Research Tasks | Jiafei Duan et al. | IEEE Transactions on Emerging Topics in Computational Intelligence | 2022 | 2103.04918 | 531 |  |
| A Review of Robot Learning for Manipulation: Challenges, Rep | Oliver Kroemer et al. | JMLR | 2021 | 1907.03146 | 507 |  |
| Foundation Models in Robotics: Applications, Challenges, and | Roya Firoozi et al. | International Journal of Robotics Research | 2024 | 2312.07843 | 396 |  |
| Deep Reinforcement Learning for Robotics: A Survey of Real-W | Chunlok Lo et al. | Annual Review of Control, Robotics, and Autonomous Systems | 2025 | 2408.03539 | 381 |  |
| Aligning Cyber Space with Physical World: A Comprehensive Su | Yang Liu et al. | arXiv | 2024 | 2407.06886 | 308 | HCPLab-SYSU/Embodied_AI_Paper_List |
| Deep Learning Approaches to Grasp Synthesis: A Review | Rhys Newbury et al. | IEEE Transactions on Robotics | 2023 | 2207.02556 | 279 |  |
| A Survey of Deep RL and IL for Autonomous Driving Policy Lea | Zeyu Zhu et al. | IEEE Transactions on Intelligent Transportation Systems | 2022 | 2101.01993 | 222 |  |
| Data-driven Methods Applied to Soft Robot Modeling and Contr | Zixi Chen et al. | IEEE Transactions on Automation Science and Engineering | 2024 | 2305.12137 | 115 |  |
| A Survey of Optimization-based Task and Motion Planning: Fro | Zhigen Zhao et al. | IEEE/ASME Transactions on Mechatronics | 2024 | 2404.02817 | 84 |  |
| A Survey of Deep Reinforcement Learning Algorithms for Motio | Fei Ye et al. | IEEE IV | 2021 | 2105.14218 | 70 |  |
| A Survey of Embodied Learning for Object-Centric Robotic Man | Ying Zheng et al. | arXiv | 2024 | 2408.11537 | 46 | RayYoh/OCRM_survey |
| A Comprehensive Survey on World Models for Embodied AI | Xinqing Li et al. | arXiv | 2025 | 2510.16732 | 43 | Li-Zn-H/AwesomeWorldModels |
| A Survey on the Integration of Machine Learning with Samplin | Troy McMahon et al. | Foundations and Trends in Robotics | 2022 | 2211.08368 | 26 |  |
| World Model for Robot Learning: A Comprehensive Survey | Bohan Hou et al. | arXiv preprint | 2026 | 2605.00080 | 21 |  |
| Reinforcement Learning For Quadrupedal Locomotion: Current A | Maurya Gurram et al. | arXiv | 2024 | 2410.10438 | 4 |  |
| Deep Learning for Embodied Vision Navigation: A Survey | Fengda Zhu et al. | arXiv | 2021 | 2108.04097 | 1 |  |
| A Survey on Deep Reinforcement Learning Algorithms for Robot | Dong Han et al. | Sensors | 2023 |  |  |  |
| Reinforcement Learning in Robotics: A Survey | Jens Kober et al. | International Journal of Robotics Research | 2013 |  |  |  |

### 👥 マルチエージェント

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| Multi-Agent Reinforcement Learning: A Selective Overview of  | Kaiqing Zhang et al. | Handbook of RL and Control | 2021 | 1911.10635 | 1680 |  |
| Deep Reinforcement Learning for Multi-Agent Systems: A Revie | Thanh Thi Nguyen et al. | IEEE Transactions on Cybernetics | 2020 | 1812.11794 | 1027 |  |
| A Survey and Critique of Multiagent Deep Reinforcement Learn | Pablo Hernandez-Leal et a | AAMAS (JAAMAS) | 2019 | 1810.05587 | 729 |  |
| A Review of Cooperative Multi-Agent Deep Reinforcement Learn | Afshin Oroojlooy et al. | Applied Intelligence | 2023 | 1908.03963 | 630 |  |
| A Survey on the Memory Mechanism of Large Language Model bas | Zeyu Zhang et al. | arXiv | 2024 | 2404.13501 | 628 |  |
| Multi-Agent Collaboration Mechanisms: A Survey of LLMs | Khanh-Tung Tran et al. | arXiv | 2025 | 2501.06322 | 497 |  |
| Agentic Retrieval-Augmented Generation: A Survey on Agentic  | Aditi Singh et al. | arXiv | 2025 | 2501.09136 | 342 | asinghcsu/AgenticRAG-Survey |
| A Survey of Multi-Agent Deep Reinforcement Learning with Com | Changxi Zhu et al. | AAMAS (JAAMAS) | 2024 | 2203.08975 | 303 |  |
| Tool Learning with Large Language Models: A Survey | Changle Qu et al. | arXiv | 2024 | 2405.17935 | 293 | quchangle1/LLM-Tool-Survey |
| From Persona to Personalization: A Survey on Role-Playing La | Jiangjie Chen et al. | arXiv | 2024 | 2404.18231 | 248 |  |
| An Overview of Multi-Agent Reinforcement Learning from Game  | Yaodong Yang et al. | arXiv | 2020 | 2011.00583 | 215 |  |
| Survey on Evaluation of LLM-based Agents | Asaf Yehudai et al. | arXiv | 2025 | 2503.16416 | 189 |  |
| Large Language Model Agent: A Survey on Methodology, Applica | Junyu Luo et al. | arXiv | 2025 | 2503.21460 | 188 | luo-junyu/Awesome-Agent-Papers |
| The Landscape of Agentic Reinforcement Learning for LLMs: A  | Guibin Zhang et al. | arXiv | 2025 | 2509.02547 | 163 |  |
| A Survey of WebAgents: Towards Next-Generation AI Agents for | Liangbo Ning et al. | arXiv | 2025 | 2503.23350 | 117 |  |
| GUI Agents: A Survey | Dang Nguyen et al. | ACL Findings | 2024 | 2412.13501 | 107 |  |
| GUI Agents with Foundation Models: A Comprehensive Survey | Shuai Wang et al. | arXiv | 2024 | 2411.04890 | 105 |  |
| A Survey of Progress on Cooperative Multi-agent Reinforcemen | Lei Yuan et al. | arXiv | 2023 | 2312.01058 | 86 |  |
| Multi-Agent Reinforcement Learning: A Comprehensive Survey | Dom Huh et al. | arXiv | 2024 | 2312.10256 | 70 |  |
| A Survey on the Optimization of Large Language Model-based A | Shangheng Du et al. | arXiv | 2025 | 2503.12434 | 43 |  |
| A Survey of Multi Agent Reinforcement Learning: Federated Le | Kemboi Cheruiyot et al. | arXiv preprint | 2025 | 2507.06278 | 10 |  |

### 🕸️ グラフニューラルネット (GNN)

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| Graph Neural Networks: A Review of Methods and Applications | Jie Zhou et al. | AI Open | 2020 | 1812.08434 | 7125 |  |
| A Comprehensive Survey of Graph Embedding: Problems, Techniq | Hongyun Cai et al. | IEEE TKDE | 2018 | 1709.07604 | 1963 |  |
| Graph Embedding Techniques, Applications, and Performance: A | Palash Goyal et al. | Knowledge-Based Systems | 2018 | 1705.02801 | 1821 |  |
| Benchmarking Graph Neural Networks | Vijay Prakash Dwivedi et  | JMLR | 2023 | 2003.00982 | 1219 |  |
| Explainability in Graph Neural Networks: A Taxonomic Survey | Hao Yuan et al. | IEEE TPAMI | 2022 | 2012.15445 | 841 |  |
| Graph Self-Supervised Learning: A Survey | Yixin Liu et al. | IEEE TKDE | 2022 | 2103.00111 | 756 |  |
| Representation Learning for Dynamic Graphs: A Survey | Seyed Mehran Kazemi et al | JMLR | 2020 | 1905.11485 | 632 |  |
| Self-Supervised Learning of Graph Neural Networks: A Unified | Yaochen Xie et al. | IEEE TPAMI | 2022 | 2102.10757 | 411 |  |
| Machine Learning on Graphs: A Model and Comprehensive Taxono | Ines Chami et al. | JMLR | 2022 | 2005.03675 | 346 |  |
| Self-supervised Learning on Graphs: Contrastive, Generative, | Lirong Wu et al. | IEEE TKDE | 2023 | 2105.07342 | 333 | LirongWu/awesome-graph-self-supervised-learning |
| Graph Neural Networks for Graphs with Heterophily: A Survey | Xin Zheng et al. | IEEE TKDE | 2022 | 2202.07082 | 316 |  |
| Transformer for Graphs: An Overview from Architecture Perspe | Erxue Min et al. | arXiv | 2022 | 2202.08455 | 213 |  |
| A Systematic Survey on Deep Generative Models for Graph Gene | Xiaojie Guo et al. | IEEE TPAMI | 2020 | 2007.06686 | 199 |  |
| Graph Pooling for Graph Neural Networks: Progress, Challenge | Chuang Liu et al. | IJCAI Survey Track | 2023 | 2204.07321 | 130 |  |
| A survey of dynamic graph neural networks | Yanping Zheng et al. | Frontiers of Computer Science | 2024 | 2404.18211 | 115 |  |
| Graph Neural Networks for Temporal Graphs: State of the Art, | Antonio Longa et al. | TMLR | 2023 | 2302.01018 | 114 |  |
| Adversarial Attacks and Defenses on Graphs: A Review, A Tool | Wei Jin et al. | SIGKDD Explorations | 2020 | 2003.00653 | 107 |  |
| A Comprehensive Survey on Graph Reduction: Sparsification, C | Mohammad Hashemi et al. | IJCAI 2024 | 2024 | 2402.03358 | 105 |  |
| Deep Graph Anomaly Detection: A Survey and New Perspectives | Hezhe Qiao et al. | IEEE TKDE | 2024 | 2409.09957 | 94 |  |
| Towards Graph Contrastive Learning: A Survey and Beyond | Wei Ju et al. | arXiv | 2024 | 2405.11868 | 68 |  |
| Heterogeneous Network Representation Learning: A Unified Fra | Carl Yang et al. | IEEE TKDE | 2022 | 2004.00216 | 60 |  |
| A Comprehensive Survey on Distributed Training of Graph Neur | Haiyang Lin et al. | Proceedings of the IEEE | 2022 | 2211.05368 | 47 |  |
| Graph Condensation: A Survey | Xinyi Gao et al. | arXiv preprint | 2024 | 2401.11720 | 39 |  |
| Graph Learning under Distribution Shifts: A Comprehensive Su | Man Wu et al. | arXiv preprint | 2024 | 2402.16374 | 34 |  |
| A Systematic Literature Review of Spatio-Temporal Graph Neur | Flavio Corradini et al. | arXiv preprint | 2024 | 2410.22377 | 26 |  |
| Graph Neural Networks for the Prediction of Molecular Struct | Jan G. Rittig et al. | RSC (Machine Learning and Hybrid Modelling for Reaction Engineering) | 2022 | 2208.04852 | 21 |  |
| A Survey of Deep Graph Learning under Distribution Shifts: f | Kexin Zhang et al. | arXiv preprint | 2024 | 2410.19265 | 20 | kaize0409/Awesome-Graph-OOD |
| Recent Advances in Hypergraph Neural Networks | Murong Yang et al. | arXiv preprint | 2025 | 2503.07959 | 14 |  |
| A Survey on Graph Condensation | Hongjia Xu et al. | arXiv preprint | 2024 | 2402.02000 | 13 |  |
| Beyond Generalization: A Survey of Out-Of-Distribution Adapt | Shuhan Liu et al. | arXiv preprint | 2024 | 2402.11153 | 10 | kaize0409/Awesome-Graph-OOD |
| A Survey of Large Language Models for Data Challenges in Gra | Mengran Li et al. | arXiv preprint | 2025 | 2505.18475 | 6 | limengran98/Awesome-Literature-Graph-Learning-Challenges |
| A Survey of Graph Neural Networks for Drug Discovery: Recent | Jun Li et al. | arXiv | 2025 | 2509.07887 | 0 |  |
| Graph Neural Networks for Natural Language Processing: A Sur | Lingfei Wu et al. | Foundations and Trends in Machine Learning | 2021 | 2106.06090 | 0 |  |

### 🔗 知識表現・知識グラフ

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| Knowledge Graphs | Aidan Hogan et al. | ACM Computing Surveys | 2021 | 2003.02320 | 2575 |  |
| A Review of Relational Machine Learning for Knowledge Graphs | Maximilian Nickel et al. | Proceedings of the IEEE | 2016 | 1503.00759 | 1738 |  |
| Unifying Large Language Models and Knowledge Graphs: A Roadm | Shirui Pan et al. | IEEE TKDE | 2023 | 2306.08302 | 1570 | RManLuo/Awesome-LLM-KG |
| Graph Retrieval-Augmented Generation: A Survey | Boci Peng et al. | arXiv | 2024 | 2408.08921 | 477 |  |
| A Comprehensive Survey on Automatic Knowledge Graph Construc | Lingfeng Zhong et al. | ACM Computing Surveys | 2023 | 2302.05019 | 343 |  |
| A Survey of Knowledge Graph Reasoning on Graph Types: Static | Ke Liang et al. | IEEE TPAMI | 2022 | 2212.05767 | 308 |  |
| LLMs for Knowledge Graph Construction and Reasoning: Recent  | Yuqi Zhu et al. | World Wide Web Journal | 2023 | 2305.13168 | 285 |  |
| A Survey of Large Language Models for Graphs | Xubin Ren et al. | KDD | 2024 | 2405.08011 | 148 | HKUDS/Awesome-LLM4Graph-Papers |
| Complex Knowledge Base Question Answering: A Survey | Yunshi Lan et al. | IEEE TKDE | 2021 | 2108.06688 | 144 |  |
| From Statistical Relational to Neurosymbolic Artificial Inte | Giuseppe Marra et al. | Artificial Intelligence | 2021 | 2108.11451 | 121 |  |
| A Survey of RDF Stores & SPARQL Engines for Querying Knowled | Waqas Ali et al. | The VLDB Journal | 2021 | 2102.13027 | 120 |  |
| A Survey of Graph Meets Large Language Model: Progress and F | Yuhan Li et al. | IJCAI | 2024 | 2311.12399 | 115 | yhLeeee/Awesome-LLMs-in-Graph-tasks |
| A Benchmark and Comprehensive Survey on Knowledge Graph Enti | Rui Zhang et al. | The VLDB Journal | 2021 | 2103.15059 | 95 |  |
| A Review of Knowledge Graph Completion | Mohamad Zamini et al. | Information (MDPI) | 2022 | 2208.11652 | 93 |  |
| Construction of Knowledge Graphs: State and Challenges | Marvin Hofer et al. | arXiv | 2023 | 2302.11509 | 79 |  |
| A Survey of Knowledge Graph Embedding and Their Applications | Shivani Choudhary et al. | arXiv | 2021 | 2107.07842 | 69 |  |
| A Survey on Temporal Knowledge Graph: Representation Learnin | Li Cai et al. | arXiv | 2024 | 2403.04782 | 53 |  |
| Neurosymbolic AI for Reasoning over Knowledge Graphs: A Surv | Lauren Nicole DeLong et a | arXiv | 2023 | 2302.07200 | 50 |  |
| A Survey on Temporal Knowledge Graph Completion: Taxonomy, P | Jiapu Wang et al. | arXiv | 2023 | 2308.02457 | 42 |  |
| Large Language Models Meet Knowledge Graphs for Question Ans | Chuangtao Ma et al. | arXiv | 2025 | 2505.20099 | 36 |  |
| Neural-Symbolic Reasoning over Knowledge Graphs: A Survey fr | Lihui Liu et al. | arXiv | 2024 | 2412.10390 | 32 |  |
| Ontology Embedding: A Survey of Methods, Applications and Re | Jiaoyan Chen et al. | arXiv | 2024 | 2406.10964 | 30 |  |
| A Survey of Reinforcement Learning for Optimization in Autom | Ahmad Farooq et al. | arXiv | 2025 | 2502.09417 | 25 |  |
| Autoformalization in the Era of Large Language Models: A Sur | Ke Weng et al. | arXiv | 2025 | 2505.23486 | 20 |  |
| LLM-empowered knowledge graph construction: A survey | Haonan Bian et al. | arXiv | 2025 | 2510.20345 | 15 |  |
| Negative Sampling in Knowledge Graph Representation Learning | Tiroshan Madushanka et al | arXiv | 2024 | 2402.19195 | 15 |  |
| Temporal Knowledge Graph Question Answering: A Survey | Miao Su et al. | arXiv | 2024 | 2406.14191 | 15 |  |
| A Survey on Knowledge Graph Structure and Knowledge Graph Em | Jeffrey Sardina et al. | arXiv | 2024 | 2412.10092 | 3 |  |
| The ARC of Progress towards AGI: A Living Survey of Abstract | Sahar Vahdati et al. | arXiv | 2026 | 2603.13372 | 2 |  |
| From Provable Correctness to Probabilistic Generation: A Com | Zurabi Kobaladze et al. | arXiv | 2025 | 2508.00013 | 0 |  |

### 🎯 因果推論

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| A Survey on Causal Inference | Liuyi Yao et al. | ACM TKDD | 2021 | 2002.02770 | 684 |  |
| D'ya like DAGs? A Survey on Structure Learning and Causal Di | Matthew J. Vowels et al. | ACM Computing Surveys | 2021 | 2103.02582 | 394 |  |
| Causal Inference in Natural Language Processing: Estimation, | Amir Feder et al. | TACL | 2022 | 2109.00725 | 328 |  |
| Causal Machine Learning: A Survey and Open Problems | Jean Kaddour et al. | arXiv | 2022 | 2206.15475 | 170 |  |
| Causal Inference in Recommender Systems: A Survey and Future | Chen Gao et al. | ACM TOIS | 2022 | 2208.12397 | 166 |  |
| Survey on Causal-based Machine Learning Fairness Notions | Karima Makhlouf et al. | arXiv | 2020 | 2010.09553 | 99 |  |
| A Survey on Causal Discovery Methods for I.I.D. and Time Ser | Uzma Hasan et al. | TMLR | 2023 | 2303.15027 | 64 |  |
| Causal Inference with Large Language Model: A Survey | Jing Ma et al. | arXiv | 2024 | 2409.09822 | 46 |  |
| Robust Counterfactual Explanations in Machine Learning: A Su | Junqi Jiang et al. | IJCAI | 2024 | 2402.01928 | 42 |  |
| Causal Reinforcement Learning: A Survey | Zhihong Deng et al. | TMLR | 2023 | 2307.01452 | 42 |  |
| From Identifiable Causal Representations to Controllable Cou | Aneesh Komanduri et al. | TMLR | 2024 | 2310.11011 | 31 |  |
| Large Language Models and Causal Inference in Collaboration: | Xiaoyu Liu et al. | arXiv | 2024 | 2403.09606 | 29 |  |
| A Survey of Deep Causal Models and Their Industrial Applicat | Zongyu Li et al. | arXiv | 2022 | 2209.08860 | 21 |  |
| Causal Inference with Complex Treatments: A Survey | Yingrong Wang et al. | arXiv | 2024 | 2407.14022 | 7 |  |
| A Survey on Causal Representation Learning and Future Work f | Changjie Lu et al. | arXiv | 2022 | 2210.16034 | 0 |  |

### ⏱️ 時系列・時空間

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| Time Series Forecasting With Deep Learning: A Survey | Bryan Lim et al. | Phil. Trans. R. Soc. A | 2020 | 2004.13408 | 1983 |  |
| Transformers in Time Series: A Survey | Qingsong Wen et al. | IJCAI | 2023 | 2202.07125 | 1532 | qingsongedu/time-series-transformers-review |
| Deep learning-based electroencephalography analysis: a syste | Yannick Roy et al. | Journal of Neural Engineering | 2019 | 1901.05498 | 1351 |  |
| Deep Learning for Sensor-based Human Activity Recognition: O | Kaixuan Chen et al. | ACM Computing Surveys | 2020 | 2001.07416 | 861 |  |
| A Survey on Graph Neural Networks for Time Series: Forecasti | Ming Jin et al. | IEEE TPAMI | 2024 | 2307.03759 | 493 |  |
| Foundation Models for Time Series Analysis: A Tutorial and S | Yuxuan Liang et al. | KDD | 2024 | 2403.14735 | 432 |  |
| Self-Supervised Learning for Time Series Analysis: Taxonomy, | Kexin Zhang et al. | IEEE TPAMI | 2023 | 2306.10125 | 260 | qingsongedu/Awesome-SSL4TS |
| Large Language Models for Time Series: A Survey | Xiyuan Zhang et al. | IJCAI | 2024 | 2402.01801 | 172 | xiyuanzh/awesome-llm-time-series |
| Deep Learning for Multivariate Time Series Imputation: A Sur | Jun Wang et al. | IJCAI | 2024 | 2402.04059 | 140 |  |
| A Comprehensive Survey of Deep Learning for Time Series Fore | Jongseon Kim et al. | Artificial Intelligence Review | 2024 | 2411.05793 | 96 |  |
| A Survey of Deep Learning and Foundation Models for Time Ser | John A. Miller et al. | arXiv | 2024 | 2401.13912 | 76 |  |
| A Survey on Principles, Models and Methods for Learning from | Satya Narayan Shukla et a | arXiv | 2020 | 2012.00168 | 67 |  |
| Spatio-Temporal Graph Neural Networks: A Survey | Zahraa Al Sahili et al. | arXiv | 2023 | 2301.10569 | 60 |  |
| Universal Time-Series Representation Learning: A Survey | Patara Trirat et al. | ACM Computing Surveys | 2024 | 2401.03717 | 48 |  |
| Dive into Time-Series Anomaly Detection: A Decade Review | Paul Boniol et al. | arXiv | 2024 | 2412.20512 | 36 |  |
| Empowering Time Series Analysis with Foundation Models: A Co | Jiexia Ye et al. | arXiv | 2024 | 2405.02358 | 28 |  |
| STG4Traffic: A Survey and Benchmark of Spatial-Temporal Grap | Xunlian Luo et al. | arXiv | 2023 | 2307.00495 | 17 | jwwthu/GNN4Traffic |
| Deep Learning-Powered Electrical Brain Signals Analysis: Adv | Jiahe Li et al. | arXiv | 2025 | 2502.17213 | 8 |  |
| Bridging the Gap: A Decade Review of Time-Series Clustering  | John Paparrizos et al. | arXiv | 2024 | 2412.20582 |  |  |
| Deep learning models for price forecasting of financial time | Cheng Zhang et al. | arXiv | 2023 | 2305.04811 |  |  |

### ⛏️ データマイニング

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| A Comprehensive Survey on Graph Neural Networks | Zonghan Wu et al. | IEEE TNNLS | 2021 | 1901.00596 | 11484 |  |
| Deep Learning for Time Series Classification: A Review | Hassan Ismail Fawaz et al | Data Mining and Knowledge Discovery | 2019 | 1809.04356 | 3303 |  |
| Deep Learning for Anomaly Detection: A Survey | Raghavendra Chalapathy et | arXiv | 2019 | 1901.03407 | 1844 |  |
| A Unifying Review of Deep and Shallow Anomaly Detection | Lukas Ruff et al. | Proceedings of the IEEE | 2021 | 2009.11732 | 1059 |  |
| Educational data mining and learning analytics: An updated s | Cristobal Romero et al. | WIREs Data Mining and Knowledge Discovery | 2024 | 2402.07956 | 950 |  |
| A Comprehensive Survey on Graph Anomaly Detection with Deep  | Xiaoxiao Ma et al. | IEEE TKDE | 2023 | 2106.07178 | 824 |  |
| Deep Learning for Time Series Anomaly Detection: A Survey | Zahra Zamanzadeh Darban e | ACM Computing Surveys | 2024 | 2211.05244 | 618 |  |
| A Brief Survey of Text Mining: Classification, Clustering an | Mehdi Allahyari et al. | arXiv | 2017 | 1707.02919 | 567 |  |
| A Comprehensive Survey on Deep Graph Representation Learning | Wei Ju et al. | Neural Networks | 2024 | 2304.05055 | 332 |  |
| Large Language Models on Graphs: A Comprehensive Survey | Bowen Jin et al. | IEEE TKDE | 2024 | 2312.02783 | 315 | PeterGriffinJin/Awesome-Language-Model-on-Graphs |
| Deep Learning for Time Series Classification and Extrinsic R | Navid Mohammadi Foumani e | ACM Computing Surveys | 2024 | 2302.02515 | 288 |  |
| A Survey of Parallel Sequential Pattern Mining | Wensheng Gan et al. | ACM TKDD | 2019 | 1805.10515 | 257 |  |
| A Survey on Graph Representation Learning Methods | Shima Khoshraftar et al. | ACM TIST | 2024 | 2204.01855 | 244 |  |
| A Comprehensive Survey on Deep Clustering: Taxonomy, Challen | Sheng Zhou et al. | ACM Computing Surveys | 2024 | 2206.07579 | 215 |  |
| A Survey on Explainable Anomaly Detection | Zhong Li et al. | ACM TKDD | 2022 | 2210.06959 | 190 |  |
| Deep Learning for Predictive Business Process Monitoring: Re | Efren Rama-Maneiro et al. | IEEE TSC | 2020 | 2009.13251 | 131 |  |
| Automatic Rumor Detection on Microblogs: A Survey | Juan Cao et al. | arXiv | 2018 | 1807.03505 | 92 |  |
| A Comprehensive Survey on Deep Learning Techniques in Educat | Yuanguo Lin et al. | arXiv | 2023 | 2309.04761 | 53 |  |
| Graph Anomaly Detection in Time Series: A Survey | Thi Kieu Khanh Ho et al. | IEEE TPAMI | 2023 | 2302.00058 | 37 |  |
| Concept Drift Adaptation in Text Stream Mining Settings: A S | Cristiano Mesquita Garcia | ACM TIST | 2024 | 2312.02901 | 15 |  |
| Influence Maximization in Social Networks: A Survey | Hui Li et al. | arXiv | 2023 | 2309.04668 | 11 |  |
| Spatiotemporal Data Mining: A Survey | Arun Sharma et al. | arXiv | 2022 | 2206.12753 | 9 |  |
| Advances in Process Optimization: A Comprehensive Survey of  | Asjad Khan et al. | arXiv | 2023 | 2301.10398 | 2 |  |
| Learning from Class-Imbalanced Data: Review of Methods and A | Guo Haixiang et al. | Expert Systems with Applications | 2017 |  |  |  |
| A Survey of Heterogeneous Information Network Analysis | Chuan Shi et al. | IEEE TKDE | 2017 | 1511.04854 |  |  |
| A Survey on Concept Drift Adaptation | João Gama et al. | ACM Computing Surveys | 2014 |  |  |  |
| A Survey on Unsupervised Outlier Detection in High-Dimension | Arthur Zimek et al. | Statistical Analysis and Data Mining | 2012 |  |  |  |
| Anomaly Detection: A Survey | Varun Chandola et al. | ACM Computing Surveys | 2009 |  |  |  |
| Learning from Imbalanced Data | Haibo He et al. | IEEE TKDE | 2009 |  |  |  |

### 🗄️ データベース・データ管理

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| A Comprehensive Survey and Experimental Comparison of Graph- | Mengzhao Wang et al. | PVLDB | 2021 | 2101.12631 | 374 | Lsyhprum/WEAVESS |
| Next-Generation Database Interfaces: A Survey of LLM-based T | Zijin Hong et al. | arXiv | 2024 | 2406.08426 | 244 |  |
| Time Series Management Systems: A Survey | Soren Kejser Jensen et al | IEEE TKDE | 2017 | 1710.01077 | 203 |  |
| The Serverless Computing Survey: A Technical Primer for Desi | Zijun Li et al. | ACM Computing Surveys | 2022 | 2112.12921 | 202 |  |
| Survey of Vector Database Management Systems | James Jie Pan et al. | The VLDB Journal | 2024 | 2310.14021 | 187 |  |
| A Survey on Data Pricing: from Economics to Data Science | Jian Pei | IEEE TKDE | 2022 | 2009.04462 | 174 |  |
| Are We Ready For Learned Cardinality Estimation? | Xiaoying Wang et al. | VLDB | 2021 | 2012.06743 | 159 |  |
| Neural Networks for Entity Matching: A Survey | Nils Barlaug et al. | ACM TKDD | 2021 | 2010.11075 | 141 |  |
| A Comprehensive Survey on Vector Database: Storage and Retri | Le Ma et al. | arXiv | 2023 | 2310.11703 | 128 |  |
| A Survey on Advancing the DBMS Query Optimizer: Cardinality, | Hai Lan et al. | Data Science and Engineering | 2021 | 2101.01507 | 118 |  |
| Data Lakes: A Survey of Functions and Systems | Rihan Hai et al. | IEEE TKDE | 2021 | 2106.09592 | 112 |  |
| A Survey on Text-to-SQL Parsing: Concepts, Methods, and Futu | Bowen Qin et al. | arXiv | 2022 | 2208.13629 | 99 |  |
| End-to-End Entity Resolution for Big Data: A Survey | Vassilis Christophides et | ACM Computing Surveys | 2021 | 1905.06397 | 67 |  |
| A Survey of Learned Indexes for the Multi-dimensional Space | Abdullah Al-Mamun et al. | arXiv | 2024 | 2403.06456 | 28 |  |
| Deep Learning Driven Natural Languages Text to SQL Query Con | Ayush Kumar et al. | arXiv | 2022 | 2208.04415 | 26 |  |
| How Good Are Multi-dimensional Learned Indices? An Experimen | Qiyu Liu et al. | arXiv | 2024 | 2405.05536 | 7 |  |
| Data Cleaning: Overview and Emerging Challenges | Xu Chu et al. | SIGMOD | 2016 |  |  |  |

### 🔍 情報検索 (IR)

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| Retrieval-Augmented Generation for Large Language Models: A  | Yunfan Gao et al. | arXiv | 2024 | 2312.10997 | 3646 | Tongji-KGLLM/RAG-Survey |
| Pretrained Transformers for Text Ranking: BERT and Beyond | Jimmy Lin et al. | Synthesis Lectures (Morgan & Claypool) | 2021 | 2010.06467 | 761 |  |
| A Deep Look into Neural Ranking Models for Information Retri | Jiafeng Guo et al. | Information Processing & Management | 2019 | 1903.06902 | 383 |  |
| A Comprehensive Survey on Cross-modal Retrieval | Kaiye Wang et al. | arXiv | 2016 | 1607.06215 | 330 |  |
| Dense Text Retrieval based on Pretrained Language Models: A  | Wayne Xin Zhao et al. | ACM TOIS | 2024 | 2211.14876 | 318 | RUCAIBox/DenseRetrieval |
| A Survey on Retrieval-Augmented Text Generation | Huayang Li et al. | arXiv | 2022 | 2202.01110 | 287 |  |
| Information Retrieval: Recent Advances and Beyond | Kailash A. Hambarde et al | IEEE Access | 2023 | 2301.08801 | 165 |  |
| Conversational Information Seeking | Hamed Zamani et al. | Foundations and Trends in Information Retrieval | 2023 | 2201.08808 | 134 |  |
| Large Language Model for Table Processing: A Survey | Weizheng Lu et al. | Frontiers of Computer Science | 2024 | 2402.05121 | 104 |  |
| A Survey of Conversational Search | Fengran Mo et al. | ACM TOIS | 2025 | 2410.15576 | 54 |  |
| Explainable Information Retrieval: A Survey | Avishek Anand et al. | arXiv | 2022 | 2211.02405 | 40 |  |
| A Survey of Model Architectures in Information Retrieval | Zhichao Xu et al. | arXiv | 2025 | 2502.14822 | 27 |  |
| Pre-training Methods in Information Retrieval | Yixing Fan et al. | Foundations and Trends in Information Retrieval | 2022 | 2111.13853 | 11 |  |
| A Survey of Generative Information Retrieval | Tianyu Li et al. | ACM TOIS | 2025 | 2406.01197 | 6 | RUC-NLPIR/GenIR-Survey |
| Bridging Language Gaps: Advances in Cross-Lingual Informatio | Roksana Goworek et al. | arXiv | 2025 | 2510.00908 | 5 |  |
| An Introduction to Neural Information Retrieval | Bhaskar Mitra et al. | Foundations and Trends in Information Retrieval | 2018 |  |  |  |
| Learning to Rank for Information Retrieval | Tie-Yan Liu | Foundations and Trends in Information Retrieval | 2009 |  |  |  |

### 🛒 推薦システム

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| Graph Neural Networks in Recommender Systems: A Survey | Shiwen Wu et al. | ACM Computing Surveys | 2022 | 2011.02260 | 1808 | wusw14/GNN-in-RS |
| Deep Learning based Recommender System: A Survey and New Per | Shuai Zhang et al. | ACM Computing Surveys | 2019 | 1707.07435 | 1318 |  |
| Explainable Recommendation: A Survey and New Perspectives | Yongfeng Zhang et al. | Foundations and Trends in Information Retrieval | 2020 | 1804.11192 | 1154 |  |
| Bias and Debias in Recommender System: A Survey and Future D | Jiawei Chen et al. | ACM TOIS | 2023 | 2010.03240 | 915 | jiawei-chen/RecDebiasing |
| A Survey on Large Language Models for Recommendation | Likang Wu et al. | World Wide Web Journal | 2024 | 2305.19860 | 878 |  |
| Sequential Recommender Systems: Challenges, Progress and Pro | Shoujin Wang et al. | IJCAI | 2019 | 2001.04830 | 510 |  |
| A Survey on the Fairness of Recommender Systems | Yifan Wang et al. | ACM TOIS | 2023 | 2206.03761 | 453 |  |
| Self-Supervised Learning for Recommender Systems: A Survey | Junliang Yu et al. | IEEE TKDE | 2024 | 2203.15876 | 434 | Coder-Yu/SELFRec |
| Advances and Challenges in Conversational Recommender System | Chongming Gao et al. | AI Open | 2021 | 2101.09459 | 367 |  |
| Cross-Domain Recommendation: Challenges, Progress, and Prosp | Feng Zhu et al. | IJCAI | 2021 | 2103.01696 | 298 |  |
| Graph Learning based Recommender Systems: A Review | Shoujin Wang et al. | IJCAI | 2021 | 2105.06339 | 245 |  |
| Multimodal Recommender Systems: A Survey | Qidong Liu et al. | ACM Computing Surveys | 2024 | 2302.03883 | 180 |  |
| Deep Learning for Click-Through Rate Estimation | Weinan Zhang et al. | IJCAI | 2021 | 2104.10584 | 134 |  |
| AutoML for Deep Recommender Systems: A Survey | Ruiqi Zheng et al. | ACM TOIS | 2023 | 2203.13922 | 99 |  |
| A Survey of Deep Reinforcement Learning in Recommender Syste | Xiaocong Chen et al. | arXiv | 2021 | 2109.03540 | 74 |  |
| A Comprehensive Survey on Multimodal Recommender Systems: Ta | Hongyu Zhou et al. | arXiv | 2023 | 2302.04473 | 70 |  |
| Cold-Start Recommendation towards the Era of Large Language  | Weizhi Zhang et al. | arXiv | 2025 | 2501.01945 | 59 | YuanchenBei/Awesome-Cold-Start-Recommendation |
| A Survey on LLM-powered Agents for Recommender Systems | Qiyao Peng et al. | arXiv preprint | 2025 | 2502.10050 | 53 |  |
| Deep Learning for Sequential Recommendation: Algorithms, Inf | Hui Fang et al. | ACM TOIS | 2020 | 1905.01997 | 47 |  |
| Foundation Models for Recommender Systems: A Survey and New  | Chengkai Huang et al. | arXiv | 2024 | 2402.11143 | 18 |  |
| A Survey on Generative Recommendation: Data, Model, and Task | Min Hou et al. | arXiv preprint | 2025 | 2510.27157 | 14 |  |

### 🌐 Web・ソーシャル

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| Fake News Detection on Social Media: A Data Mining Perspecti | Kai Shu et al. | ACM SIGKDD Explorations | 2017 | 1708.01967 | 3309 |  |
| A Comprehensive Survey on Community Detection with Deep Lear | Xing Su et al. | IEEE TNNLS | 2024 | 2105.12584 | 452 |  |
| A Survey of Graph Neural Networks for Social Recommender Sys | Kartik Sharma et al. | ACM Computing Surveys | 2022 | 2212.04481 | 301 |  |
| Combating Misinformation in the Age of LLMs: Opportunities a | Canyu Chen et al. | AI Magazine | 2024 | 2311.05656 | 210 | llm-misinformation/llm-misinformation-survey |
| Towards generalisable hate speech detection: a review on obs | Wenjie Yin et al. | PeerJ Computer Science | 2021 | 2102.08886 | 209 |  |
| Fairness and Diversity in Recommender Systems: A Survey | Yuying Zhao et al. | ACM TIST | 2023 | 2307.04644 | 123 |  |
| A Survey on Fairness-aware Recommender Systems | Di Jin et al. | Information Fusion | 2023 | 2306.00403 | 81 |  |
| A Survey on Expert Recommendation in Community Question Answ | Xianzhi Wang et al. | Journal of Computer Science and Technology | 2018 | 1807.05540 | 75 |  |
| Data-driven Computational Social Science: A Survey | Bin Zhao et al. | Big Data Research | 2021 | 2008.12372 | 66 |  |
| Web Table Extraction, Retrieval and Augmentation: A Survey | Shuo Zhang et al. | ACM TIST | 2020 | 2002.00207 | 65 |  |
| A Technical Survey on Statistical Modelling and Design Metho | Yuan Jin et al. | Artificial Intelligence | 2018 | 1812.02736 | 43 |  |
| Fake News Detection Through Graph-based Neural Networks: A S | Shuzhi Gong et al. | arXiv | 2023 | 2307.12639 | 26 |  |
| Toxic Memes: A Survey of Computational Perspectives on the D | Delfina Sol Martinez Pand | arXiv | 2024 | 2406.07353 | 19 |  |
| Detection of Rumors and Their Sources in Social Networks: A  | Otabek Sattarov et al. | arXiv | 2025 | 2501.05292 | 12 |  |
| Toxicity in Online Platforms and AI Systems: A Survey of Nee | Smita Khapre et al. | arXiv | 2025 | 2509.25539 | 9 |  |
| A Survey on Automatic Online Hate Speech Detection in Low-Re | Susmita Das et al. | arXiv | 2024 | 2411.19017 | 9 |  |
| Social Bots: Detection and Challenges | Kai-Cheng Yang et al. | Handbook of Computational Social Science | 2023 | 2312.17423 | 7 |  |
| Heterogeneity in Entity Matching: A Survey and Experimental  | Mohammad Hossein Moslemi  | arXiv | 2025 | 2508.08076 | 4 |  |
| Social Media Bot Detection Research: Review of Literature | Blaž Rodič et al. | arXiv | 2025 | 2503.22838 | 2 |  |
| Quality Control in Open-Ended Crowdsourcing: A Survey | Lei Chai et al. | arXiv | 2024 | 2412.03991 | 1 |  |
| A Survey of Link Prediction Algorithms | Vivian Feng et al. | arXiv | 2023 | 2306.12970 |  |  |

### 🛡️ 信頼できるAI (公平性・XAI・安全性)

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| Towards A Rigorous Science of Interpretable Machine Learning | Finale Doshi-Velez et al. | arXiv | 2017 | 1702.08608 | 5262 |  |
| A Survey of Methods for Explaining Black Box Models | Riccardo Guidotti et al. | ACM Computing Surveys | 2018 | 1802.01933 | 5059 |  |
| Concrete Problems in AI Safety | Dario Amodei et al. | arXiv | 2016 | 1606.06565 | 3268 |  |
| Adversarial Examples: Attacks and Defenses for Deep Learning | Xiaoyong Yuan et al. | IEEE TNNLS | 2017 | 1712.07107 | 1826 |  |
| DeepFakes and Beyond: A Survey of Face Manipulation and Fake | Ruben Tolosana et al. | Information Fusion | 2020 | 2001.00179 | 1109 |  |
| Interpretable Machine Learning: Fundamental Principles and 1 | Cynthia Rudin et al. | Statistics Surveys | 2021 | 2103.11251 | 973 |  |
| A Survey on the Explainability of Supervised Machine Learnin | Nadia Burkart et al. | JAIR | 2021 | 2011.07876 | 962 |  |
| The Creation and Detection of Deepfakes: A Survey | Yisroel Mirsky et al. | ACM Computing Surveys | 2020 | 2004.11138 | 880 |  |
| Backdoor Learning: A Survey | Yiming Li et al. | IEEE TNNLS | 2020 | 2007.08745 | 837 |  |
| Opportunities and Challenges in Explainable Artificial Intel | Arun Das et al. | arXiv | 2020 | 2006.11371 | 768 |  |
| Adversarial Attacks and Defenses in Images, Graphs and Text: | Han Xu et al. | IJAC | 2019 | 1909.08072 | 755 |  |
| From Anecdotal Evidence to Quantitative Evaluation Methods:  | Meike Nauta et al. | ACM Computing Surveys | 2022 | 2201.08164 | 702 |  |
| Membership Inference Attacks on Machine Learning: A Survey | Hongsheng Hu et al. | ACM Computing Surveys | 2021 | 2103.07853 | 696 |  |
| One Explanation Does Not Fit All: A Toolkit and Taxonomy of  | Vijay Arya et al. | arXiv | 2019 | 1909.03012 | 472 |  |
| The Frontiers of Fairness in Machine Learning | Alexandra Chouldechova et | arXiv | 2018 | 1810.08810 | 438 |  |
| A Survey of Privacy Attacks in Machine Learning | Maria Rigaki et al. | ACM Computing Surveys | 2020 | 2007.07646 | 342 |  |
| Counterfactual Explanations and Algorithmic Recourses for Ma | Sahil Verma et al. | ACM Computing Surveys | 2020 | 2010.10596 | 315 |  |
| Differential Privacy and Machine Learning: a Survey and Revi | Zhanglong Ji et al. | arXiv | 2014 | 1412.7584 | 294 |  |
| Backdoor Attacks and Countermeasures on Deep Learning: A Com | Yansong Gao et al. | arXiv | 2020 | 2007.10760 | 290 |  |
| Bias Mitigation for Machine Learning Classifiers: A Comprehe | Max Hort et al. | ACM JRC | 2022 | 2207.07068 | 289 |  |
| Worldwide AI Ethics: a review of 200 guidelines and recommen | Nicholas Kluge Correa et  | Patterns | 2022 | 2206.11922 | 261 |  |
| Wild Patterns Reloaded: A Survey of Machine Learning Securit | Antonio Emanuele Cina et  | ACM Computing Surveys | 2022 | 2205.01992 | 203 |  |
| Privacy-Preserving Machine Learning: Methods, Challenges and | Runhua Xu et al. | arXiv | 2021 | 2108.04417 | 164 |  |
| Against The Achilles' Heel: A Survey on Red Teaming for Gene | Lizhi Lin et al. | arXiv preprint | 2024 | 2404.00629 | 61 |  |
| Machine Unlearning in Generative AI: A Survey | Zheyuan Liu et al. | arXiv preprint | 2024 | 2407.20516 | 58 | franciscoliu/Awesome-GenAI-Unlearning |
| Towards Possibilities & Impossibilities of AI-generated Text | Soumya Suvra Ghosal et al | arXiv preprint | 2023 | 2310.15264 | 57 |  |
| Machine Unlearning: A Comprehensive Survey | Weiqi Wang et al. | arXiv preprint | 2024 | 2405.07406 | 56 |  |
| A Survey of AI-generated Text Forensic Systems: Detection, A | Tharindu Kumarage et al. | arXiv preprint | 2024 | 2403.01152 | 33 |  |
| Are AI Detectors Good Enough? A Survey on Quality of Dataset | German Gritsai et al. | arXiv preprint | 2024 | 2410.14677 | 20 |  |
| Building Safe GenAI Applications: An End-to-End Overview of  | Alberto Purpura et al. | arXiv preprint | 2025 | 2503.01742 | 14 |  |
| Watermarking for AI Content Detection: A Review on Text, Vis | Lele Cao et al. | ICLR 2025 Workshop (GenAI Watermarking) | 2025 | 2504.03765 | 9 |  |

### 📡 連合学習

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| Advances and Open Problems in Federated Learning | Peter Kairouz et al. | FnT in ML | 2019 | 1912.04977 | 8944 |  |
| Federated Learning: Challenges, Methods, and Future Directio | Tian Li et al. | IEEE Signal Processing Magazine | 2019 | 1908.07873 | 6127 |  |
| Federated Learning: Strategies for Improving Communication E | Jakub Konecny et al. | NeurIPS Workshop | 2016 | 1610.05492 | 5487 |  |
| Federated Learning on Non-IID Data: A Survey | Hangyu Zhu et al. | Neurocomputing | 2021 | 2106.06843 | 1338 |  |
| Towards Personalized Federated Learning | Alysa Ziying Tan et al. | IEEE TNNLS | 2021 | 2103.00710 | 1284 |  |
| Threats to Federated Learning: A Survey | Lingjuan Lyu et al. | arXiv | 2020 | 2003.02133 | 544 |  |
| Federated Learning for Medical Image Analysis: A Survey | Hao Guan et al. | Pattern Recognition | 2024 | 2306.05980 | 432 |  |
| Asynchronous Federated Learning on Heterogeneous Devices: A  | Chenhao Xu et al. | arXiv | 2021 | 2109.04269 | 386 |  |
| Federated Learning for Generalization, Robustness, Fairness: | Wenke Huang et al. | IEEE TPAMI | 2023 | 2311.06750 | 245 |  |
| A Comprehensive Survey of Incentive Mechanism for Federated  | Rongfei Zeng et al. | arXiv | 2021 | 2106.15406 | 129 |  |
| A Survey on Heterogeneous Federated Learning | Dashan Gao et al. | arXiv | 2022 | 2210.04505 | 90 |  |
| Federated Graph Machine Learning: A Survey of Concepts, Tech | Xingbo Fu et al. | SIGKDD Explorations | 2022 | 2207.11812 | 69 |  |
| Decentralized Deep Learning for Multi-Access Edge Computing: | Yuwei Sun et al. | IEEE TAI | 2021 | 2108.03980 | 55 |  |
| A Survey on Decentralized Federated Learning | Edoardo Gabrielli et al. | arXiv | 2023 | 2308.04604 | 49 |  |
| A Survey on Vertical Federated Learning: From a Layered Pers | Liu Yang et al. | arXiv | 2023 | 2304.01829 | 48 |  |
| Federated Large Language Models: Current Progress and Future | Yuhang Yao et al. | arXiv | 2024 | 2409.15723 | 36 |  |
| A Survey on Federated Fine-tuning of Large Language Models | Yebo Wu et al. | arXiv | 2025 | 2503.12016 | 29 |  |
| Non-IID data in Federated Learning: A Survey with Taxonomy,  | Daniel M. Jimenez G. et a | arXiv | 2024 | 2411.12377 | 29 |  |
| A Survey on Group Fairness in Federated Learning: Challenges | Teresa Salazar et al. | arXiv | 2024 | 2410.03855 | 6 |  |

### 🖐️ HCI・ヒューマンAI

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| A Survey of Human-in-the-loop for Machine Learning | Xingjiao Wu et al. | Future Generation Computer Systems | 2021 | 2108.00941 | 771 |  |
| How should my chatbot interact? A survey on human-chatbot in | Ana Paula Chaves et al. | International Journal of Human-Computer Interaction | 2019 | 1904.02743 | 557 |  |
| Human-Centered Explainable AI (XAI): From Algorithms to User | Q. Vera Liao et al. | arXiv | 2021 | 2110.10790 | 339 |  |
| A Survey of Visual Analytics Techniques for Machine Learning | Jun Yuan et al. | Computational Visual Media | 2020 | 2008.09632 | 275 |  |
| Towards a Science of Human-AI Decision Making: A Survey of E | Vivian Lai et al. | arXiv | 2021 | 2112.11471 | 242 |  |
| Towards Human-centered Explainable AI: A Survey of User Stud | Yao Rong et al. | IEEE TPAMI | 2022 | 2210.11584 | 237 |  |
| Quality Control in Crowdsourcing: A Survey of Quality Attrib | Florian Daniel et al. | ACM Computing Surveys | 2018 | 1801.02546 | 196 |  |
| UX Research on Conversational Human-AI Interaction: A Litera | Qingxiao Zheng et al. | CHI | 2022 | 2202.09895 | 118 |  |
| The Value, Benefits, and Concerns of Generative AI-Powered A | Zhuoyan Li et al. | CHI | 2024 | 2403.12004 | 110 |  |
| Co-Writing with AI, on Human Terms: Aligning Research with U | Mohi Reza et al. | arXiv | 2025 | 2504.12488 | 46 |  |
| Generative AI and Creativity: A Systematic Literature Review | Niklas Holzner et al. | arXiv | 2025 | 2505.17241 | 24 |  |
| How Human-Centered Explainable AI Interface Are Designed and | Thu Nguyen et al. | arXiv | 2024 | 2403.14496 | 19 |  |
| A Survey of AI Reliance | Sven Eckhardt et al. | arXiv | 2024 | 2408.03948 | 16 |  |
| A Survey on Human-AI Collaboration with Large Foundation Mod | Vanshika Vats et al. | arXiv | 2024 | 2403.04931 | 14 |  |
| Trust, distrust, and appropriate reliance in (X)AI: a survey | Roel Visser et al. | arXiv | 2023 | 2312.02034 | 14 |  |
| Concerns and Values in Human-Robot Interactions: A Focus on  | Giulio Antonio Abbo et al | arXiv | 2025 | 2501.05628 | 13 |  |
| Towards Human-centered Design of Explainable Artificial Inte | Shuai Ma et al. | arXiv | 2024 | 2410.21183 | 8 |  |
| Advancing Human-Machine Teaming: Concepts, Challenges, and A | Dian Chen et al. | arXiv | 2025 | 2503.16518 | 4 |  |

### 🧬 進化計算

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| A Tutorial on Bayesian Optimization | Peter I. Frazier et al. | arXiv | 2018 | 1807.02811 | 2392 |  |
| A Survey on Evolutionary Neural Architecture Search | Yuqiao Liu et al. | IEEE TNNLS | 2020 | 2008.10937 | 587 |  |
| Particle Swarm Optimization: A survey of historical and rece | Saptarshi Sengupta et al. | Machine Learning and Knowledge Extraction | 2018 | 1804.05319 | 485 |  |
| A Review of Evolutionary Multi-modal Multi-objective Optimiz | Ryoji Tanabe et al. | IEEE TEVC | 2020 | 2009.13347 | 193 |  |
| Neuroevolution in Deep Neural Networks: Current Trends and F | Edgar Galvan et al. | IEEE TETCI | 2020 | 2006.05415 | 176 |  |
| Survey on Evolutionary Deep Learning: Principles, Algorithms | Nan Li et al. | ACM Computing Surveys | 2022 | 2208.10658 | 120 |  |
| A Survey on Learnable Evolutionary Algorithms for Scalable M | Songbai Liu et al. | IEEE TEVC | 2022 | 2206.11526 | 105 |  |
| Evolutionary Multitask Optimization: a Methodological Overvi | Eneko Osaba et al. | Cognitive Computation | 2021 | 2102.02558 | 84 |  |
| Bridging Evolutionary Algorithms and Reinforcement Learning: | Pengyi Li et al. | IEEE TEVC | 2024 | 2401.11963 | 78 |  |
| Combining Evolution and Deep Reinforcement Learning for Poli | Olivier Sigaud et al. | ACM TELO | 2022 | 2203.14009 | 67 |  |
| A Recent Survey on the Applications of Genetic Programming i | Asifullah Khan et al. | arXiv | 2019 | 1901.07387 | 38 |  |
| Quantum-Inspired Evolutionary Algorithms for Feature Subset  | Yelleti Vivek et al. | arXiv | 2024 | 2407.17946 | 18 |  |
| A Survey of Decomposition-Based Evolutionary Multi-Objective | Ke Li et al. | IEEE TEVC | 2024 | 2404.14571 | 0 |  |

### 🔢 理論計算機科学

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| Convex Optimization: Algorithms and Complexity | Sébastien Bubeck | Foundations and Trends in Machine Learning | 2015 | 1405.4980 | 2175 |  |
| Machine Learning for Combinatorial Optimization: a Methodolo | Yoshua Bengio et al. | European Journal of Operational Research | 2018 | 1811.06128 | 1831 |  |
| Learning with Submodular Functions: A Convex Optimization Pe | Francis Bach et al. | Foundations and Trends in Machine Learning | 2013 | 1111.6453 | 527 |  |
| Algorithms with Predictions | Michael Mitzenmacher et a | Beyond the Worst-Case Analysis of Algorithms (book chapter) | 2020 | 2006.09123 | 321 |  |
| End-to-End Constrained Optimization Learning: A Survey | James Kotary et al. | IJCAI | 2021 | 2103.16378 | 263 |  |
| Fairness Testing: A Comprehensive Survey and Analysis of Tre | Zhenpeng Chen et al. | ACM TOSEM | 2022 | 2207.10223 | 147 |  |
| Fair Division of Indivisible Goods: A Survey | Georgios Amanatidis et al | IJCAI | 2022 | 2202.07551 | 98 |  |
| A Survey of Distributed Optimization Methods for Multi-Robot | Trevor Halsted et al. | arXiv | 2021 | 2103.12840 | 63 |  |
| A Comprehensive Survey on Spectral Clustering with Graph Str | Kamal Berahmand et al. | arXiv | 2025 | 2501.13597 | 62 |  |
| Preference Restrictions in Computational Social Choice: A Su | Edith Elkind et al. | arXiv | 2022 | 2205.09092 | 49 |  |
| Fair Division: The Computer Scientist's Perspective | Toby Walsh | IJCAI | 2020 | 2005.04855 | 41 |  |
| Convex Analysis and Optimization with Submodular Functions:  | Francis Bach et al. | arXiv | 2010 | 1010.4207 | 40 |  |
| Empirical Game-Theoretic Analysis: A Survey | Michael P. Wellman et al. | JAIR | 2025 | 2403.04018 | 38 |  |
| Survey of Distributed Algorithms for Resource Allocation ove | Mohammadreza Doostmohamma | arXiv | 2024 | 2401.15607 | 35 |  |
| Streaming and Sketching Complexity of CSPs: A survey | Madhu Sudan et al. | ICALP | 2022 | 2205.02744 | 10 |  |
| Review of Mathematical Optimization in Federated Learning | Shusen Yang et al. | arXiv | 2024 | 2412.01630 | 6 |  |
| Differentiable Convex Optimization Layers in Neural Architec | Calder Katyal et al. | arXiv | 2024 | 2412.20679 | 3 |  |
| Differential Privacy in Machine Learning: A Survey from Symb | Francisco Aguilera-Martín | arXiv | 2025 | 2506.11687 | 2 |  |

### 🔬 AI for Science

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| Scientific Machine Learning through Physics-Informed Neural  | Salvatore Cuomo et al. | Journal of Scientific Computing | 2022 | 2201.05624 | 2447 |  |
| Integrating Scientific Knowledge with Machine Learning for E | Jared Willard et al. | ACM Computing Surveys | 2022 | 2003.04919 | 718 |  |
| Neural Natural Language Processing for Unstructured Data in  | Irene Li et al. | Computer Science Review | 2021 | 2107.02975 | 232 |  |
| A Survey of Deep Learning for Scientific Discovery | Maithra Raghu et al. | arXiv | 2020 | 2003.11755 | 154 |  |
| Ab-initio Quantum Chemistry with Neural-Network Wavefunction | Jan Hermann et al. | Nature Reviews Chemistry | 2023 | 2208.12590 | 137 |  |
| A Survey of Generative AI for de novo Drug Design: New Front | Xiangru Tang et al. | arXiv | 2024 | 2402.08703 | 117 |  |
| Advances of Machine Learning in Materials Science: Ideas and | Sue Sin Chong et al. | Frontiers of Physics | 2023 | 2307.14032 | 79 |  |
| Recent Advances on Machine Learning for Computational Fluid  | Haixin Wang et al. | arXiv | 2024 | 2408.12171 | 68 |  |
| Partial Differential Equations Meet Deep Neural Networks: A  | Shudong Huang et al. | arXiv | 2022 | 2211.05567 | 51 |  |
| Machine Learning-Driven Materials Discovery: Unlocking Next- | Dilshod Nematov et al. | arXiv | 2025 | 2503.18975 | 28 |  |
| Deep Learning and Foundation Models for Weather Prediction:  | Jimeng Shi et al. | arXiv | 2025 | 2501.06907 | 25 |  |
| Deep Learning Methods for Small Molecule Drug Discovery: A S | Wenhao Hu et al. | IEEE TKDE | 2023 | 2303.00313 | 23 |  |
| A Review of Neuroscience-Inspired Machine Learning | Alexander Ororbia et al. | arXiv | 2024 | 2403.18929 | 17 |  |
| A Model-Centric Review of Deep Learning for Protein Design | Gregory W. Kyro et al. | arXiv | 2025 | 2502.19173 | 13 |  |
| Interpretable Machine Learning for Weather and Climate Predi | Ruyi Yang et al. | arXiv | 2024 | 2403.18864 | 11 |  |
| A Systematic Review of Deep Graph Neural Networks: Challenge | Adil Mudasir Malla et al. | arXiv | 2023 | 2311.02127 | 6 |  |
| LLM4Cell: A Survey of Large Language and Agentic Models for  | Sajib Acharjee Dip et al. | arXiv | 2025 | 2510.07793 | 4 |  |
| Deep Learning-Driven Protein Structure Prediction and Design | Wanqing Yang et al. | arXiv | 2025 | 2504.01490 | 3 |  |
| Deep Learning in Astrophysics | Yuan-Sen Ting et al. | Annual Review of Astronomy and Astrophysics | 2026 | 2510.10713 | 2 |  |
| A Survey of Deep Learning Methods in Protein Bioinformatics  | Weihang Dai et al. | arXiv | 2025 | 2501.01477 | 2 |  |

### 🌟 人工知能 (全般)

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| On the Opportunities and Risks of Foundation Models | Rishi Bommasani et al. | arXiv | 2021 | 2108.07258 | 6831 |  |
| A Survey on Knowledge Graphs: Representation, Acquisition an | Shaoxiong Ji et al. | IEEE TNNLS | 2021 | 2002.00388 | 2777 |  |
| A Survey of Deep Learning for Mathematical Reasoning | Pan Lu et al. | ACL | 2023 | 2212.10535 | 201 | lupantech/dl4math |
| Understanding World or Predicting Future? A Comprehensive Su | Jingtao Ding et al. | ACM Computing Surveys | 2025 | 2411.14499 | 187 | tsinghua-fib-lab/World-Model |
| Commonsense Reasoning for Natural Language Understanding: A  | Shane Storks et al. | arXiv | 2019 | 1904.01172 | 144 |  |
| Commonsense Knowledge Reasoning and Generation with Pre-trai | Prajjwal Bhargava et al. | AAAI | 2022 | 2201.12438 | 78 |  |
| Neuro-Symbolic AI in 2024: A Systematic Review | Brandon C. Colelough et a | arXiv | 2025 | 2501.05435 | 74 |  |
| A Survey on Self-Evolution of Large Language Models | Zhengwei Tao et al. | arXiv | 2024 | 2404.14387 | 72 |  |
| A Survey on Deep Learning for Theorem Proving | Zhaoyu Li et al. | COLM | 2024 | 2404.09939 | 69 | zhaoyu-li/DL4TP |
| Towards Data-and Knowledge-Driven Artificial Intelligence: A | Wenguan Wang et al. | IEEE TPAMI | 2024 | 2210.15889 | 67 |  |
| Machine Learning Methods in Solving the Boolean Satisfiabili | Wenxuan Guo et al. | Machine Intelligence Research | 2022 | 2203.04755 | 53 |  |
| LLMs as Planning Formalizers: A Survey for Leveraging Large  | Marcus Tantakoun et al. | arXiv | 2025 | 2503.18971 | 44 |  |
| Computational Argumentation-based Chatbots: a Survey | Federico Castagna et al. | JAIR | 2024 | 2401.03454 | 21 |  |
| AI Planning: A Primer and Survey (Preliminary Report) | Dillon Z. Chen et al. | arXiv | 2024 | 2412.05528 | 5 |  |
| Approaches to Artificial General Intelligence: An Analysis | Soumil Rathi | arXiv | 2022 | 2202.03153 | 4 |  |

### 🧩 ニューラルネット基礎

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| Deep Learning in Neural Networks: An Overview | Juergen Schmidhuber | Neural Networks | 2015 | 1404.7828 | 17608 |  |
| Recent Advances in Convolutional Neural Networks | Jiuxiang Gu et al. | Pattern Recognition | 2018 | 1512.07108 | 5992 |  |
| Fundamentals of Recurrent Neural Network (RNN) and Long Shor | Alex Sherstinsky | Physica D | 2020 | 1808.03314 | 5083 |  |
| A Survey of the Recent Architectures of Deep Convolutional N | Asifullah Khan et al. | Artificial Intelligence Review | 2020 | 1901.06032 | 2725 |  |
| Diffusion Models: A Comprehensive Survey of Methods and Appl | Ling Yang et al. | ACM Computing Surveys | 2023 | 2209.00796 | 2310 | YangLing0818/Diffusion-Models-Papers-Survey-Taxonomy |
| Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, a | Michael M. Bronstein et a | arXiv | 2021 | 2104.13478 | 1651 |  |
| Efficient Transformers: A Survey | Yi Tay et al. | ACM Computing Surveys | 2022 | 2009.06732 | 1568 |  |
| A Survey of Transformers | Tianyang Lin et al. | AI Open | 2022 | 2106.04554 | 1521 |  |
| Deep Learning in Spiking Neural Networks | Amirhossein Tavanaei et a | Neural Networks | 2019 | 1804.08150 | 1372 |  |
| Activation Functions in Deep Learning: A Comprehensive Surve | Shiv Ram Dubey et al. | Neurocomputing | 2022 | 2109.14545 | 1130 |  |
| Sparsity in Deep Learning: Pruning and growth for efficient  | Torsten Hoefler et al. | JMLR | 2021 | 2102.00554 | 983 |  |
| Recent Advances in Recurrent Neural Networks | Hojjat Salehinejad et al. | arXiv | 2018 | 1801.01078 | 740 |  |
| A Comprehensive Survey on Test-Time Adaptation under Distrib | Jian Liang et al. | IJCV | 2025 | 2303.15361 | 552 | tim-learn/awesome-test-time-adaptation |
| A Survey on Deep Neural Network Pruning: Taxonomy, Compariso | Hongrong Cheng et al. | IEEE TPAMI | 2024 | 2308.06767 | 512 |  |
| Normalization Techniques in Training DNNs: Methodology, Anal | Lei Huang et al. | IEEE TPAMI | 2023 | 2009.12836 | 452 | huangleiBuaa/NormalizationSurvey |
| Attention, please! A survey of Neural Attention Models in De | Alana de Santana Correia  | Artificial Intelligence Review | 2022 | 2103.16775 | 291 |  |
| A Review of Sparse Expert Models in Deep Learning | William Fedus et al. | arXiv | 2022 | 2209.01667 | 208 |  |
| Physics-Informed Machine Learning: A Survey on Problems, Met | Zhongkai Hao et al. | arXiv | 2023 | 2211.08064 | 187 |  |
| Survey of Dropout Methods for Deep Neural Networks | Alex Labach et al. | arXiv | 2019 | 1904.13310 | 176 |  |
| A comprehensive review of Quantum Machine Learning: from NIS | Yunfei Wang et al. | Reports on Progress in Physics | 2024 | 2401.11351 | 119 |  |
| Geometric Deep Learning and Equivariant Neural Networks | Jan E. Gerken et al. | Artificial Intelligence Review | 2023 | 2105.13926 | 113 |  |
| A Comprehensive Survey of Mixture-of-Experts: Algorithms, Th | Siyuan Mu et al. | arXiv | 2025 | 2503.07137 | 112 |  |
| A Survey of Mamba | Haohao Qu et al. | arXiv | 2024 | 2408.01129 | 97 |  |
| Mamba-360: Survey of State Space Models as Transformer Alter | Badri Narayana Patro et a | arXiv | 2024 | 2404.16112 | 90 | badripatro/mamba360 |
| A Survey on Quantum Machine Learning: Current Trends, Challe | Kamila Zaman et al. | arXiv | 2023 | 2310.10315 | 78 |  |
| Where Do We Stand with Implicit Neural Representations? A Te | Amer Essakine et al. | arXiv | 2024 | 2411.03688 | 59 |  |
| Three Decades of Activations: A Comprehensive Survey of 400  | Vladimir Kunc et al. | arXiv | 2024 | 2402.09092 | 55 |  |
| Comprehensive Review of Neural Differential Equations for Ti | YongKyung Oh et al. | IJCAI (Survey Track) | 2025 | 2502.09885 | 30 |  |
| Learning with Capsules: A Survey | Fabio De Sousa Ribeiro et | ACM Computing Surveys | 2024 | 2206.02664 | 22 |  |
| Toward Large-scale Spiking Neural Networks: A Comprehensive  | Yangfan Hu et al. | arXiv | 2024 | 2409.02111 | 15 |  |

### 🏭 応用・横断領域

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| Deep Learning in Mobile and Wireless Networking: A Survey | Chaoyun Zhang et al. | IEEE Communications Surveys & Tutorials | 2019 | 1803.04311 | 1524 |  |
| Deep EHR: A Survey of Recent Advances in Deep Learning Techn | Benjamin Shickel et al. | IEEE JBHI | 2018 | 1706.03446 | 1475 |  |
| Deep Learning for Financial Applications : A Survey | Ahmet Murat Ozbayoglu et  | Applied Soft Computing | 2020 | 2002.05786 | 508 |  |
| Artificial Intelligence for Digital and Computational Pathol | Andrew H. Song et al. | Nature Reviews Bioengineering | 2023 | 2401.06148 | 345 |  |
| Deep Learning for Unsupervised Anomaly Localization in Indus | Xian Tao et al. | arXiv | 2022 | 2207.10298 | 260 |  |
| A Survey on Deep Learning for Software Engineering | Yanming Yang et al. | ACM Computing Surveys | 2022 | 2011.14597 | 237 |  |
| Large Language Model-Based Agents for Software Engineering:  | Junwei Liu et al. | arXiv | 2025 | 2409.02977 | 210 |  |
| From CNN to Transformer: A Review of Medical Image Segmentat | Wenjian Yao et al. | arXiv | 2023 | 2308.05305 | 210 |  |
| A Comprehensive Survey of Deep Transfer Learning for Anomaly | Peng Yan et al. | arXiv | 2024 | 2307.05638 | 186 |  |
| A Survey of Large Language Models for Financial Applications | Yuqi Nie et al. | arXiv | 2024 | 2406.11903 | 159 |  |
| A Comprehensive Survey on Deep Music Generation: Multi-level | Shulei Ji et al. | arXiv | 2020 | 2011.06801 | 149 |  |
| A Survey on Large Language Models for Critical Societal Doma | Zhiyu Zoey Chen et al. | arXiv | 2024 | 2405.01769 | 108 |  |
| Foundation Models for Remote Sensing and Earth Observation:  | Aoran Xiao et al. | IEEE Geoscience and Remote Sensing Magazine | 2025 | 2410.16602 | 99 |  |
| Large Language Models for Education: A Survey | Hanyi Xu et al. | arXiv | 2024 | 2405.13001 | 85 |  |
| Short-Term Electricity-Load Forecasting by Deep Learning: A  | Qi Dong et al. | arXiv | 2025 | 2408.16202 | 70 |  |
| A Survey for Foundation Models in Autonomous Driving | Haoxiang Gao et al. | arXiv | 2024 | 2402.01105 | 67 |  |
| A Survey on Medical Large Language Models: Technology, Appli | Lei Liu et al. | arXiv | 2024 | 2406.03712 | 57 |  |
| Deep Reinforcement Learning in Quantitative Algorithmic Trad | Tidor-Vlad Pricope et al. | arXiv | 2021 | 2106.00123 | 57 |  |
| From Tiny Machine Learning to Tiny Deep Learning: A Survey | Shriyank Somvanshi et al. | arXiv | 2025 | 2506.18927 | 42 |  |
| Year-over-Year Developments in Financial Fraud Detection via | Yisong Chen et al. | arXiv | 2025 | 2502.00201 | 41 |  |
| Deep Learning-based Intrusion Detection Systems: A Survey | Zhiwei Xu et al. | arXiv | 2025 | 2504.07839 | 33 |  |
| Graph Neural Networks in Intelligent Transportation Systems: | Hourun Li et al. | arXiv | 2024 | 2401.00713 | 21 |  |
| Self-Supervised Representation Learning for Geospatial Objec | Yile Chen et al. | arXiv | 2025 | 2408.12133 | 20 |  |
| A New Era in Computational Pathology: A Survey on Foundation | Dibaloke Chanda et al. | arXiv | 2024 | 2408.14496 | 14 |  |
| A Survey of Deep Learning-based Radiology Report Generation  | Xinyi Wang et al. | arXiv | 2025 | 2405.12833 | 9 |  |
| A Comprehensive Survey of Electronic Health Record Modeling: | Weijieying Ren et al. | arXiv | 2025 | 2507.12774 | 9 |  |
| AI in Agriculture: A Survey of Deep Learning Techniques for  | Umair Nawaz et al. | arXiv | 2026 | 2507.22101 | 8 |  |
| Large Language Models Meet Legal Artificial Intelligence: A  | Zhitian Hou et al. | arXiv | 2025 | 2509.09969 | 8 |  |
| A Survey on Multilingual Mental Disorders Detection from Soc | Ana-Maria Bucur et al. | arXiv | 2026 | 2505.15556 | 6 |  |

### 📊 データ中心AI・評価

| タイトル | 著者 | venue | 年 | arXiv | 📈 | github |
|---|---|---|---:|---|---:|---|
| A Survey on LLM-as-a-Judge | Jiawei Gu et al. | arXiv | 2024 | 2411.15594 | 1528 |  |
| A Survey of Deep Active Learning | Pengzhen Ren et al. | ACM Computing Surveys | 2022 | 2009.00236 | 1514 |  |
| Data-centric Artificial Intelligence: A Survey | Daochen Zha et al. | ACM Computing Surveys | 2025 | 2303.10158 | 452 | daochenzha/data-centric-AI |
| On LLMs-Driven Synthetic Data Generation, Curation, and Eval | Lin Long et al. | ACL Findings | 2024 | 2406.15126 | 339 |  |
| Machine Learning for Synthetic Data Generation: A Review | Yingzhou Lu et al. | arXiv | 2023 | 2302.04062 | 291 |  |
| Dataset Distillation: A Comprehensive Review | Ruonan Yu et al. | IEEE TPAMI | 2024 | 2301.07014 | 206 |  |
| A Comprehensive Survey of Dataset Distillation | Shiye Lei et al. | IEEE TPAMI | 2024 | 2301.05603 | 186 |  |
| Evaluation and Benchmarking of LLM Agents: A Survey | Mahmoud Mohammadi et al. | arXiv | 2025 | 2507.21504 | 157 |  |
| A Survey on Deep Active Learning: Recent Advances and New Fr | Dongyuan Li et al. | IEEE TNNLS | 2024 | 2405.00334 | 149 |  |
| Benchmark Data Contamination of Large Language Models: A Sur | Cheng Xu et al. | arXiv | 2024 | 2406.04244 | 131 |  |
| Graph Data Augmentation for Graph Machine Learning: A Survey | Tong Zhao et al. | IEEE Data Engineering Bulletin | 2022 | 2202.08871 | 112 |  |
| Detecting and Understanding Harmful Memes: A Survey | Shivam Sharma et al. | IJCAI | 2022 | 2205.04274 | 112 |  |
| Comprehensive Exploration of Synthetic Data Generation: A Su | André Bauer et al. | arXiv | 2024 | 2401.02524 | 106 |  |
| Synthetic Data Generation Using Large Language Models: Advan | Mihai Nadas et al. | IEEE Access | 2025 | 2503.14023 | 96 |  |
| Can We Trust AI Benchmarks? An Interdisciplinary Review of C | Maria Eriksson et al. | arXiv | 2025 | 2502.06559 | 67 |  |
| A Survey on Data Synthesis and Augmentation for Large Langua | Ke Wang et al. | arXiv | 2024 | 2410.12896 | 50 |  |
| A Survey on Data Contamination for Large Language Models | Yuxing Cheng et al. | arXiv | 2025 | 2502.14425 | 32 |  |
| A Coreset Selection of Coreset Selection Literature: Introdu | Brian B. Moser et al. | arXiv | 2025 | 2505.17799 | 21 |  |
