
---

# 太空算力与光芯片

## 深度调研报告

---

**摘要**：随着低轨卫星巨型星座的加速部署，太空正从"通信中继站"演变为"分布式计算节点"。本报告系统梳理了太空算力产业的驱动因素、技术挑战、全球竞争格局，并深入分析了光芯片（Photonic Chip）在太空环境中的独特优势——从抗辐射特性到低功耗、高带宽密度、轻量化与热不敏感性。报告覆盖近地轨道计算星座、深空探测光通信、太空-地面协同计算等前沿方向，为产业决策与技术投资提供参考。

---

## 第1章：太空算力概述

### 1.1 什么是太空算力？

**太空算力（Space Computing / Orbital Computing）** 指在地球轨道及深空环境中部署计算资源，使卫星不再仅仅是"信号中继器"，而是具备数据存储、处理、分析与决策能力的"轨道数据中心"。

传统卫星采用"弯管式"（Bent-pipe）架构——地面站发送信号，卫星放大后转发给另一地面站，所有计算都在地面完成。这种模式在通信时代尚可应对，但在遥感数据爆炸、实时决策需求激增的今天，已成为严重的瓶颈。

太空算力的核心范式转变体现在三个层面：

| 层级 | 传统模式 | 太空算力模式 |
|:---|:---|:---|
| **数据流** | 采集 → 全量下传 → 地面处理 | 采集 → 在轨处理 → 只传结果 |
| **延迟** | 分钟至小时级（取决于地面站覆盖） | 毫秒至秒级（边缘计算） |
| **自主性** | 地面遥控为主 | 星上自主决策 |

太空算力的技术形态包括：
- **星上边缘计算（On-board Edge Computing）**：在卫星上运行 AI 推理模型，实时筛选、压缩、分析遥感图像
- **轨道数据中心（Orbital Data Center）**：将数据中心级 GPU/AI 加速器部署到太空，执行模型训练等高负载任务
- **星间计算网络（Inter-Satellite Computing Mesh）**：通过激光链路互联的卫星集群，形成分布式计算网络

### 1.2 需求驱动：从通信到计算

太空算力的崛起并非偶然，而是由多重需求叠加驱动的必然结果。

**（一）数据洪流与下行带宽瓶颈**

现代遥感卫星产生的数据量呈指数级增长。以欧洲哨兵（Sentinel）系列为例，单颗卫星每天产生约 1.5 TB 数据。若采用传统全量下传模式，需要庞大的地面站网络支撑，且大量数据（如云层覆盖图像）本就不具备下传价值。

研究表明，通过在轨 AI 处理，可将下行带宽需求降低 **85%** ——卫星只将"有价值"的洞察传回地面，而非原始像素。这种"数据精简"（Data Reduction）能力是太空算力的首要价值。

**（二）低延迟边缘计算需求**

对于国防侦察、海事监控、灾害应急等场景，"实时性"意味着生死。传统模式下，卫星图像需经过下传、地面处理、分发，延迟可达数十分钟。而星上边缘计算可在秒级内完成目标检测、变化识别和告警生成。

例如，在野火监测中，星上 AI 可在卫星过顶瞬间识别火点并触发告警，为消防响应争取宝贵时间。

**（三）自主导航与深空任务**

深空探测面临与地面通信的巨大延迟。火星任务中，信号单程传输需 **4-24 分钟**，使得地面实时遥控不可能。探测器必须具备自主导航、自主避障、自主科学决策能力——这本质上是太空算力问题。

NASA 的"自主科学航天器实验"（Autonomous Sciencecraft Experiment）早在 2000 年代就验证了星上自主目标识别与重规划能力。未来的载人火星任务将需要更强大的星上计算支持。

**（四）AI 时代的算力饥渴**

地球数据中心的电力消耗正成为制约 AI 发展的瓶颈。2023 年，美国数据中心消耗了全国约 **4.4%** 的电力，预计到 2028 年将增至 **6.7%-12%**。在此背景下，太空——拥有近乎无限的太阳能和天然的辐射冷却——被视为潜在的算力释放空间。

### 1.3 市场规模与增长预测

太空算力市场正处于爆发前夜，不同研究机构给出了差异化的规模估算，反映了定义边界的差异：

| 细分市场 | 2024-2025 估值 | 复合年增长率（CAGR） | 2034-2035 预测 |
|:---|:---|:---|:---|
| 太空在轨计算平台（Space On-Board Computing Platform） | 15.5 亿美元 | 11.95% | 47.9 亿美元 |
| 太空边缘计算（Space-Based Edge Computing，狭义） | 38 亿美元 | 19.3% | 186 亿美元 |
| 太空云计算（Space Cloud Computing，欧洲） | 13.8 亿欧元 | — | 56.4 亿欧元 |
| 太空边缘计算（广义，含地面基础设施） | 1689 亿美元 | 8.26% | 3450 亿美元 |

> 注：广义估算将地面站、网络基础设施和下游应用纳入统计，而狭义估算仅统计星上计算硬件与软件。

**关键增长驱动因素**：

1. **LEO 巨型星座扩张**：截至 2025 年底，在轨活跃卫星超过 **12,000 颗**，其中 LEO 卫星占比 **88%-93%**。预计到 2034 年将超过 **25,000 颗**。

2. **国防投入激增**：美国太空发展局（SDA）已承诺到 2030 年投入超过 **130 亿美元**用于"扩散型作战人员太空架构"（PWSA）。

3. **发射成本断崖式下降**：SpaceX 猎鹰 9 号（Falcon 9）复用发射成本已降至约 **1,500-2,940 美元/千克**，而星舰（Starship）的目标是将这一数字推向 **100 美元/千克以下**。

4. **软件定义卫星**：可编程载荷使单颗卫星可动态切换任务，提升了计算资源的利用率。

---

## 第2章：太空环境与技术挑战

太空并非友好环境。在轨计算系统必须面对地面数据中心无需考虑的极端条件。

### 2.1 辐射效应

太空辐射是电子系统面临的首要威胁。辐射环境由三部分组成：

| 辐射源 | 成分 | 能量范围 | 主要影响 |
|:---|:---|:---|:---|
| **地球辐射带** | 被地磁场捕获的电子和质子 | 电子：keV-MeV；质子：MeV-GeV | 长期累积损伤 |
| **银河宇宙射线（GCR）** | 高能质子、α粒子、重离子 | 高达 10¹² eV | 单粒子事件 |
| **太阳粒子事件（SPE）** | 太阳耀斑和日冕物质抛射产生的高能粒子 | 10-100 MeV | 短期高强度暴露 |

辐射对电子器件的损害分为两大类：

**（一）总电离剂量（Total Ionizing Dose, TID）**

TID 是长期累积效应，由辐射在绝缘层（如栅氧化层）中产生电子-空穴对并导致电荷俘获引起。对 CMOS 器件的影响包括：
- 阈值电压漂移（数十至数百毫伏）
- 漏电流增加（可达数个数量级）
- 时序特性退化
- 功耗上升

典型空间任务的 TID 要求为 **100 krad(Si)** 量级。商业级 CMOS 器件在数十 Gy 剂量下即开始退化，而航天级器件可耐受 100-300 krad(Si)。

**（二）单粒子效应（Single Event Effects, SEEs）**

SEE 是瞬态、随机事件，由单个高能粒子 strike 产生。分为：

| 非破坏性效应 | 破坏性效应 |
|:---|:---|
| 单粒子翻转（SEU）——比特翻转 | 单粒子闩锁（SEL） |
| 单粒子瞬态（SET） | 单粒子烧毁（SEB） |
| 多比特翻转（MBU） | 单粒子栅击穿（SEGR） |
| 单粒子功能中断（SEFI） | — |

随着工艺节点缩小，器件对 SEE 的敏感性反而增加——更小的电容意味着更少的电荷即可翻转一个节点。

### 2.2 热管理

卫星在轨经历极端的温度循环：

| 工况 | 温度范围 |
|:---|:---|
| 阳光直射面 | 最高可达 **+121°C** |
| 地球阴影区（日食） | 最低可达 **-157°C** |
| LEO 典型轨道（每 90 分钟一圈） | 总波动约 **220°C** |

由于太空是真空环境，**对流散热完全不存在**，热量只能通过辐射方式散失。这带来了独特的热管理挑战：

- **散热器面积需求**：在 20°C 表面温度下，每平方米散热器仅能排散约 600-700 W 热量
- **热管技术**：回路热管（Loop Heat Pipe, LHP）是卫星热管理的核心，工作范围覆盖 **-160°C 至 +120°C**
- **相变材料（PCM）**：作为"热电池"在热相吸收热量、冷相释放热量
- **多层隔热（MLI）**：防止过度散热

对于高功率计算载荷，热管理尤为严峻。Starcloud 等轨道数据中心公司声称太空的辐射冷却具有优势，但实际上，在真空中排散 1 MW 热量需要约 **1,200 平方米**的散热器面积——相当于 4 个网球场。

### 2.3 功耗与能源限制

卫星的能源主要来自太阳能电池板，但可用功率严格受限：

| 卫星类型 | 典型功率 |
|:---|:---|
| CubeSat（立方星） | 1-10 W |
| 小型通信卫星 | 100-500 W |
| Starlink V2 Mini | ~2-3 kW |
| Starlink V3（预计） | 更高功率 |
| 大型遥感卫星 | 5-15 kW |

功率预算必须分配给通信、姿态控制、热管理和计算。对于计算载荷，每增加 1 W 计算功耗，可能需要额外 0.3-0.5 W 用于散热。

### 2.4 重量与发射成本

尽管发射成本已大幅下降，但重量仍是关键约束：

| 发射系统 | LEO 成本（美元/千克） | 备注 |
|:---|:---|:---|
| 猎鹰 9 号（复用） | 1,500-2,940 | 当前主流 |
| 猎鹰重型（复用） | ~1,500 | 大载荷 |
| 星舰（初期目标） | 100-500 | 完全复用 |
| 星舰（长期目标） | 10-67 | 高频次发射 |

对于巨型星座，单颗卫星的重量直接决定发射总成本。Starlink V2 Mini 单颗重约 800 kg，而 V3 预计更重。计算载荷的增加会直接影响星座部署的经济性。

---

## 第3章：国内外布局

### 3.1 美国：SpaceX 星链、Amazon Kuiper、NASA

**（一）SpaceX 星链（Starlink）与星盾（Starshield）**

SpaceX 的星链是全球最大的卫星星座，截至 2025 年底在轨活跃卫星超过 **7,000 颗**，占全球活跃卫星总数的约 60%。

星链卫星的计算能力经历了代际跃升：

| 指标 | V2 Mini | V3（预计 2026 年） |
|:---|:---|:---|
| 下行容量 | ~100 Gbps | **1 Tbps** |
| 上行容量 | ~7 Gbps | **160 Gbps** |
| RF + 激光回程总容量 | 较低 | ~4 Tbps |
| 单星算力 | 有限 | 支持轨道数据中心 |

星链 V3 卫星将搭载新一代计算系统、先进调制解调器和复杂的波束成形与交换能力，并配备高速星间激光链路，形成 mesh 网络。

**星盾（Starshield）** 是 SpaceX 面向美国军方的星链变体，已签署多项重大合同：
- 2024 年 3 月：与美国国家侦察局（NRO）签署 **18 亿美元**合同，部署数百颗侦察卫星
- 2025 年 12 月：与美国太空军合作开发 **约 480 颗卫星**的 MILNET 军事通信星座
- 星盾具备增强加密、抗干扰通信和星上安全数据处理能力

**（二）Amazon Project Kuiper**

Amazon 的 Kuiper 星座计划部署 **3,236 颗卫星**，2025 年 4 月完成首批商业发射。

Kuiper 的技术亮点在于其自研芯片：
- **"Prometheus" 处理器**：集成 5G 调制解调器、蜂窝基站和微波回传天线功能，单颗卫星可处理 **1 Tbps** 数据
- **AWS Graviton 衍生边缘计算**：将 Amazon 云端的自研芯片能力延伸至太空
- 架构支持"再生式中继"——卫星可解调、路由、再编码信号，而非简单放大转发

Kuiper 与 AWS 深度整合，企业客户可通过 Kuiper 将偏远设施（石油平台、矿场、农村站点）直连 AWS 云基础设施。

**（三）NASA 与新兴企业**

- **Starcloud（2024 年成立）**：2025 年 11 月发射 Starcloud-1 卫星，搭载 **NVIDIA H100 GPU**，在 325 km 轨道完成史上首次太空 LLM 训练（NanoGPT）和推理（Google Gemma/Gemini）。2026 年 3 月完成 **1.7 亿美元 A 轮融资**，估值 11 亿美元，成为最快达到独角兽地位的 YC 企业（17 个月）。
- **HPE Spaceborne Computer-2**：部署于国际空间站，验证在轨边缘处理
- **Azure Space**：微软的太空云计划，扩展在轨 AI 合作伙伴关系

### 3.2 欧洲：ESA、OneWeb

**（一）欧洲航天局（ESA）**

ESA 在太空计算和光通信领域布局深远：

- **Phi-Lab 和 FAST 项目**：推进在轨数据处理
- **欧洲数据中继系统（EDRS）**： nicknamed "太空数据高速公路"，是世界上首个商业化的光学卫星通信系统
  - EDRS-A（2016 年发射）和 EDRS-C（2019 年发射）位于地球静止轨道
  - 激光通信终端（LCT）数据速率达 **1.8 Gbps**
  - 截至 2024 年 10 月，已完成 **80,000 余次**成功激光连接，可靠性达 **99.53%**
  - 累计下传数据超过 **2.5 PB**

- **欧几里得（Euclid）任务**：ESA 的暗能量/暗物质探测望远镜，2023 年 7 月发射。使用传统 X 波段和 K 波段射频通信（非激光），K 波段下行速率约 55-74 Mbps。

- **昴宿星（Pleiades Neo）**：Airbus 的地球观测星座，配备 Tesat Spacecom 激光通信终端，通过 EDRS 实现近实时数据中继。

**（二）OneWeb**

OneWeb 第一代星座已完成 **634 颗 LEO 卫星**部署，被 Eutelsat 收购后更名为 Eutelsat OneWeb。

ESA 与 OneWeb 的合作重点：
- **Sunrise 合作伙伴计划**：开发 JoeySat 演示卫星（2023 年 5 月发射），测试数字波束成形、跳波束和再生处理
- **Copernicus 数据枢纽**：在非洲等偏远地区部署配备 OneWeb 用户终端和专用处理单元的数据枢纽
- **5G-Advanced NR-NTN**：2025 年实现全球首个基于 OneWeb LEO 卫星的 Rel-19 5G-Advanced 非地面网络连接

### 3.3 中国：卫星互联网星座、商业航天

**（一）GW 星座（国网星座）**

GW 星座是中国国家主导的 LEO 卫星互联网项目，由中国卫星网络集团（China SatNet）运营：

| 参数 | 规格 |
|:---|:---|
| 规划卫星总数 | **12,992 颗** |
| GW-A59 子星座 | 6,080 颗（<500 km 极低轨道） |
| GW-A2 子星座 | 6,912 颗（1,145 km 轨道） |
| ITU 申报时间 | 2020 年 9 月 |

2024-2025 年发射进展：
- 2024 年 12 月 16 日：长征五号 B/远征二号首次批量组网发射（一箭十星），标志星座建设正式启动
- 2025 年：发射节奏从"每月一次"加速至"每三天一组"，截至 2025 年底累计完成 **17 次组网发射**，**136 颗卫星**在轨
- 2029 年 9 月 ITU 截止：需部署约 **1,300 颗卫星**（总量的 10%）以保留频谱/轨道资源

**（二）千帆星座（G60 星链）**

上海垣信卫星运营的千帆星座规划 **15,000 颗卫星**：
- 2024 年 8 月首批发射
- 2024 年融资 **67 亿元**
- 规划 2025 年部署一期 **648 颗**

**（三）银河航天（Galaxy Space）**

- 中国商业航天首家独角兽公司，估值约 **115 亿元**
- 2024 年发射卫星超 **50 颗**
- 建成**全球最大商业卫星工厂**，实现百颗卫星量产能力
- 单颗卫星成本降至传统方案的 **1/6**
- 2024 年 5 月完成**泰国首次低轨宽带卫星互联网测试**

**（四）时空道宇（Spacemore）**

- 吉利控股集团旗下商业航天企业，估值超 **百亿元**
- 全球首个深度融合航天制造与汽车制造能力的卫星量产工厂
- 2024 年实现**前装车载卫星通信终端产品规模化应用落地**——全球率先
- 开创"卫星制造 + 车联网应用"的商业闭环

**（五）中国太空光通信进展**

| 时间 | 卫星/项目 | 速率 | 里程碑 |
|:---|:---|:---|:---|
| 2011 年 | 海洋二号 | 504 Mbps | 国内首次星地激光通信在轨试验 |
| 2016 年 | 墨子号 | 5.12 Gbps | 国内首个低轨卫星对地相干激光通信 |
| 2017 年 | 实践十三号 | 5 Gbps | 国际首次高轨卫星与地面双向高速激光通信 |
| 2019-2020 年 | **实践二十号** | **10 Gbps** | **国际首个 QPSK 相干体制，创世界纪录** |
| 2020 年 | 行云二号 | 100 Mbps | 中国首次低轨星间激光通信实验 |
| 2023 年 | 吉林一号 MF02A04 | 10 Gbps | 首次面向业务化应用的星地激光高速通信 |
| 2024 年底 | 吉林一号平台 02A02 | **100 Gbps** | 国内首次星地激光 100Gbps 超高速传输 |
| 2025 年 3 月 | 光传 01/02 试验星 | **400 Gbps** | 国内首次在轨星间 400Gbps 超高速激光通信 |

### 3.4 其他：日本、印度、俄罗斯

**（一）日本（JAXA）**

JAXA 目前**没有**专门的卫星互联网宽带星座计划，但正在推进：
- **LEO PNT 星座**：规划 240 颗卫星（2030 年）至 480 颗（2035 年），用于 GNSS 增强（定位精度提升至约 10 cm），而非互联网宽带

**（二）印度（ISRO）**

印度**没有** ISRO 主导的卫星互联网星座，但采取"民营主导"策略：
- Ananth Technologies 获 IN-SPACe 批准，计划 2028 年推出印度首个私营卫星宽带服务（300 亿卢比项目，地球静止轨道）
- ISRO 为外国星座提供商业发射服务（如 2025 年底为 AST SpaceMobile 发射 BlueBird 卫星）
- 现有卫星互联网由 Hughes Communications India、OneWeb（Bharti 合作）、Jio-SES 等提供

**（三）俄罗斯**

俄罗斯正加速建设自主卫星互联网，受地缘政治压力驱动：
- **Skif 星座**：2025 年开始部署，原型星 Skif-D 于 2022 年 10 月发射
- **Rassvet（黎明）星座**：2025 年 3 月政府批准，规划 292 颗工作星 + 91 颗备份星
- 2025-2030 年拨款 **1,160 亿卢布**用于卫星互联网发展
- 目标：2027 年向公众提供服务

---

## 第4章：光芯片在太空中的优势

光芯片（Photonic Integrated Circuit, PIC），又称光子集成电路，将激光器、调制器、波导、探测器等光学元件集成在单一芯片上。与传统电子芯片相比，光芯片在太空环境中展现出独特的优势。

### 4.1 抗辐射特性

光芯片最根本的优势在于其信息载体——**光子（Photon）** 不受电磁场直接影响。

**电子 vs 光子的辐射响应差异**：

| 特性 | 电子（传统 CMOS） | 光子（光芯片） |
|:---|:---|:---|
| 信息载体 | 电子电荷 | 光子（无电荷） |
| SEU 敏感性 | **极高**——单粒子即可翻转比特 | **本质免疫**——光子不受单粒子 strike 影响 |
| TID 机制 | 氧化层电荷俘获，阈值漂移 | 无氧化层，无阈值概念 |
| 主要损伤机制 | 电离损伤 + 位移损伤 | 主要为位移损伤（晶格原子位移） |
| EMI 敏感性 | 高 | **免疫** |

**实验验证**：

2023 年，Soria-Gómez 等人在 SPIE/ICSO 会议上发表了 InP 基光芯片的辐射硬度评估结果：
- 测试器件：SOA（半导体光放大器）、电光相位调制器、波导、MMI 耦合器、光电探测器
- 伽马射线剂量：最高 **106 krad**
- 质子辐照：最高 **1.5 × 10¹¹ p⁺/cm²**
- **结论**：所有基础器件在典型空间任务剂量范围内均表现出辐射硬度，未观察到系统性退化

**里程碑式的在轨实验**：

2024 年发表在 *Science Advances* 上的研究报道了首次在 LEO 真实空间环境中对硅光芯片进行为期 **325 天**的暴露实验（MISSE-FF 平台，ISS 外部，>2,000 km 轨道）：

| 参数 | 结果 |
|:---|:---|
| 载流子迁移率 | **无变化** |
| 自由载流子寿命 | 降低约 55%（500 ps → 226 ps） |
| 电光调制效率 | **保持不变** |
| 光电带宽 | **扩大**（因载流子寿命降低） |
| 消光比（MRM） | 从 24 dB 降至 14 dB（仍 >10 dB，满足通信需求） |
| 有源波导损耗 | 增加 **+20 dB/cm** |

关键发现：地面高剂量 X 射线/伽马射线测试与实际空间粒子辐射产生的损伤机制**完全不同**。实际空间辐射下，载流子迁移率和调制效率未受影响——这与地面测试的预测截然相反。

### 4.2 低功耗

光计算的核心优势之一是**光传播的"免费"加法**。

在传统电子计算中，矩阵乘法等操作需要大量晶体管开关，每个开关都消耗能量并产生热量。而在光域中：
- 光信号的叠加（干涉）是**被动过程**，几乎不消耗能量
- 波分复用（Wavelength Division Multiplexing, WDM）可在单根光纤中同时传输数十至数百个波长的信号，每个波长独立承载数据
- 光互连的能耗可低至 **每比特亚皮焦（sub-pJ/bit）**

对于太空应用，低功耗意味着：
- 更小的太阳能电池板面积
- 更少的热管理负担
- 更长的任务寿命

2024 年清华大学发布的 **"太极"（Taichi）光芯片**实现了 **160 TOPS/W** 的能效，远超现有电子 AI 加速器（如 NVIDIA H100 约为 30-60 TOPS/W）。

### 4.3 高带宽密度

WDM 技术使光芯片能够在极小的物理空间内实现极高的带宽密度：

| 技术 | 带宽密度 |
|:---|:---|
| 铜缆电互连 | ~10 Gbps/mm |
| 单模光纤 | ~100 Tbps（使用 WDM） |
| 光芯片波导 | 可在 mm² 面积内容纳数十条波导，每条支持 100+ Gbps |

NASA 的 TBIRD（TeraByte InfraRed Delivery）任务在 2022 年展示了 **200 Gbps** 的星地激光通信速率，使用 WDM + 双偏振 QPSK 调制，单次过顶传输 **4.8 TB** 无误码数据。这一速率是传统射频通信的 **1,000 倍**。

### 4.4 轻量化

光互连的物理载体——光纤——比铜缆轻得多：

| 对比项 | 铜缆 | 光纤 |
|:---|:---|:---|
| 重量（同带宽） | 重 5-10 倍 | 轻 |
| 直径 | 粗 | 细（单模光纤芯径 9 μm） |
| 弯曲半径 | 较大 | 小 |
| 电磁屏蔽需求 | 需要 | 不需要 |

对于卫星内部互连，光芯片可将收发器、波导和调制器集成在单一芯片上，大幅减小体积和重量。EDRS 的激光通信终端重量约 **50 kg**，而传统射频终端达到同等数据率可能需要数倍重量。

### 4.5 热不敏感性（非相干架构的温度鲁棒性）

光芯片存在相干（Coherent）与非相干（Incoherent）两种架构，后者在温度稳定性方面具有显著优势：

| 特性 | 相干光计算 | 非相干光计算 |
|:---|:---|:---|
| 工作原理 | 保持光相位关系，需精确相位控制 | 基于光强度/功率，不依赖相位 |
| 温度敏感性 | **极高**——相位强依赖温度 | **显著更低**——强度受温度影响小 |
| 热管理开销 | 可能成为系统功耗的重要组成 | 最小化或无需 |
| 系统复杂度 | 高（需 TEC、反馈控制） | 简单，更具成本效益 |

硅材料的热光系数约为 **1.86 × 10⁻⁴ K⁻¹**，是二氧化硅的约 10 倍。这意味着温度变化会显著改变硅波导的折射率和物理尺寸，导致谐振波长漂移。

然而，**非相干架构**通过使用光强度而非相位来编码信息，从根本上规避了这一问题。此外，**氮化硅（Si₃N₄）**平台因其更低的热光系数，成为温度敏感应用的理想选择——具备高热稳定性和低热光系数，同时保持超低光损耗（<1 dB/cm）。

研究表明，采用 MZI（马赫-曾德尔干涉仪）自补偿设计的波导可在 **>50°C** 范围内实现零净温度灵敏度，为太空宽温环境应用提供了可行路径。

---

## 第5章：光计算太空化的技术路线

### 5.1 太空光通信（已有成熟应用）

太空光通信是光芯片在太空中最成熟的应用方向，已从技术验证走向商业运营。

**（一）NASA 光通信项目**

| 项目 | 时间 | 轨道/距离 | 数据速率 | 里程碑意义 |
|:---|:---|:---|:---|:---|
| **LCRD** | 2021 年 12 月发射 | GEO（35,786 km） | 1.2 Gbps | NASA 首个双向端到端光学中继系统 |
| **TBIRD** | 2022 年 5 月发射 | LEO（482 km） | **200 Gbps** | 单次过顶传输 4.8 TB，速率是 RF 的 1,000 倍 |
| **ILLUMA-T** | 2023 年 11 月发射 | ISS | 1.2 Gbps | 首个载人航天光学通信系统 |
| **DSOC** | 2023 年 10 月发射 | 深空（Psyche 任务） | 267 Mbps（最近点） | 2024 年 12 月创纪录地从 **3.07 亿英里**（4.94 亿公里）传输数据 |
| **O2O** | 计划 2026 年 | 月球轨道 | — | 阿尔忒弥斯 II 任务，支持 4K 超高清视频 |

DSOC 的成就尤为突出：在相当于地球-火星最大距离的位置，实现了 267 Mbps 的数据传输，证明了激光通信在深空的可行性。

**（二）ESA EDRS**

EDRS 是迄今为止最成功的商业化太空光通信系统：
- 两颗 GEO 卫星（EDRS-A 于 2016 年，EDRS-C 于 2019 年）
- 激光终端由 Tesat Spacecom 制造，数据率 **1.8 Gbps**
- 最大链路距离 **80,000 公里**
- 服务哨兵系列、国际空间站、军事/安全用户
- 截至 2024 年 10 月：**80,000+ 成功激光连接，99.53% 可靠性，2.5+ PB 数据下传**

**（三）中国实践二十号**

实践二十号卫星（2019 年 12 月发射）是中国太空光通信的里程碑：
- **10 Gbps** QPSK 相干体制星地激光通信
- **国际首个** QPSK 相干体制星地激光链路
- 地面站：丽江光学地面站

后续进展迅速：
- 2024 年底：吉林一号实现 **100 Gbps** 星地激光传输
- 2025 年 3 月：光传试验星实现 **400 Gbps** 星间激光通信

### 5.2 太空光计算（前沿探索）

太空光计算目前处于早期探索阶段，技术成熟度（TRL）约为 2-3 级。

**（一）光神经网络加速器**

2024-2025 年的关键突破：

| 成果 | 年份 | 特性 | 太空相关性 |
|:---|:---|:---|:---|
| **Taichi 光芯片**（清华大学） | 2024 | 160 TOPS/W，大规模光子集成 | 超高能效，对功率受限卫星至关重要 |
| **光谱 CNN 芯片**（Cui 等） | 2025 | 直接处理非相干自然光 | 无需相干激光源，简化太空系统 |
| **ROSA 架构** | 2025 | 鲁棒型微环光神经网络 | 提升恶劣环境下的可靠性 |
| **TRON 架构** | 2025 | 可训练、可重构随机光网络 | 适应变化的任务需求 |

**（二）太空光计算路线图**

2025 年发布的一篇关于系外行星高对比度成像的路线图首次明确规划了光计算加速器进入太空的时间表：

| 时间 | 里程碑 |
|:---|:---|
| **2025-2030 年** | 地基望远镜部署光计算协处理器，实现 >5 kHz 的自适应光学闭环带宽 |
| **2030-2035 年** | **空间站搭载光子人工智能加速器**，完成在轨系外行星大气成分分析 |
| **2040 年后** | 光子神经形态芯片与量子传感器融合，用于宇宙原恒星系统的分子谱线成像 |

**（三）在轨 AI 计算的现状**

当前在轨计算仍以电子加速器为主：
- Starcloud-1（2025 年 11 月）：搭载 NVIDIA H100，在 325 km 轨道完成 LLM 训练和推理
- SpaceX 星链 V3：计划支持轨道数据中心，利用高速激光链路形成分布式计算网络

光计算芯片尚未进入太空，但地面进展迅速。预计 **2030-2035 年**将出现首个太空光计算演示任务。

### 5.3 技术差距与突破点

| 差距 | 现状 | 突破方向 |
|:---|:---|:---|
| **规模化** | 演示系统 <3 层、数百神经元 | 大规模集成、多层网络 |
| **非线性激活** | 需光电混合实现 | 全光非线性器件 |
| **精度与校准** | 模拟计算精度受限 | 主动误差校正、数字辅助 |
| **太空鉴定** | 尚无光 NN 加速器通过飞行鉴定 | 辐射硬化、热真空测试 |
| **与航天器系统集成** | 电源、数据接口、软件栈未标准化 | 制定标准、开发配套生态 |
| **成本** | 光芯片制造成本高 | 开放式多项目晶圆（MPW）、规模化生产 |

---

## 第6章：前景与展望

### 6.1 近地轨道计算星座

LEO 计算星座是太空算力最现实的近期应用场景。

**SpaceX 的轨道数据中心愿景**：

Elon Musk 已明确表示："通过扩展具有高速激光链路的 Starlink V3 卫星，可以实现轨道数据中心。SpaceX 将这样做。"

SpaceX 分析的轨道数据中心优势：
- 太阳能：单位面积接收能量是地面的 **5 倍**
- 冷却效率：辐射冷却无需水，PUE 可低至 **1.02-1.05**（地面最佳约 1.2-1.5）
- 10 年期 40 MW 集群成本：约 **820 万美元** vs 地面约 **1.67 亿美元**

**竞争格局**：

| 公司 | 项目 | 状态 | 时间表 |
|:---|:---|:---|:---|
| **Starcloud** | 轨道数据中心 | H100 已入轨 | Starcloud-2：2026 年底（Blackwell B200） |
| **SpaceX** | Starlink 扩展 | 已申请百万卫星星座 | 5 年计划 |
| **Google** | Project Suncatcher | 开发中 | 原型发射：2027 年 |
| **Blue Origin** | TeraWave | 2025 年底宣布 | 政府客户优先 |
| **中国/国星宇航** | 三体计算星座 | 12 颗卫星已发射（2025 年 5 月） | 2030 年 2,800 颗 |

**光芯片在 LEO 计算星座中的角色**：

- **星间光互连**：WDM 激光链路提供 Tbps 级带宽，连接计算节点
- **光计算加速**：用于 AI 推理、图像处理等任务的低功耗加速
- **光存储互连**：替代铜缆，减轻重量、降低功耗

### 6.2 深空探测中的光计算

深空任务对计算和通信提出了最极端的要求。

**通信延迟挑战**：

| 目标 | 单向延迟 |
|:---|:---|
| 月球 | 1.3 秒 |
| 火星（最近） | 4 分钟 |
| 火星（最远） | 24 分钟 |
| 木星 | 32 分钟 |
| 土星 | 1 小时 |

如此长的延迟使得地面实时控制不可能，航天器必须具备完全自主的决策能力。

**光计算的优势**：

1. **辐射硬度**：深空辐射环境比 LEO 更恶劣，光芯片的抗辐射特性尤为珍贵
2. **低功耗**：深空航天器能源极其有限（依赖太阳能或放射性同位素电源），光计算的高能效可延长任务寿命
3. **高带宽通信**：DSOC 已证明在深空距离上可实现 267 Mbps 的激光通信，未来光计算可与光通信无缝集成

**应用场景**：
- 自主导航与避障（如 NASA 的自主科学航天器）
- 实时科学数据分析（如识别感兴趣的地质特征并自主调整观测计划）
- 航天器健康监测与故障自主诊断

### 6.3 太空-地面协同计算

太空算力并非要取代地面数据中心，而是与地面形成**协同计算架构**。

**协同模式**：

| 模式 | 描述 | 示例 |
|:---|:---|:---|
| **数据预处理** | 卫星执行数据清洗、压缩、筛选，只传有价值数据 | 遥感图像去云、去噪后下传 |
| **模型推理** | 星上运行训练好的 AI 模型，地面负责训练 | Starcloud 在轨运行 Gemma 模型 |
| **联邦学习** | 多颗卫星分布式训练，只传模型更新 | 未来星座级分布式 AI |
| **任务卸载** | 根据延迟/带宽需求，动态分配计算任务 | 低延迟任务在星上，复杂分析在地面 |

**光芯片在协同架构中的价值**：

- **高速星地链路**：TBIRD 的 200 Gbps 速率使大规模模型更新传输成为可能
- **光互连降低星座内部延迟**：激光星间链路（OISL）延迟仅毫秒级
- **边缘-云端无缝衔接**：光通信的高带宽使"太空边缘 + 地面云"的协同模式流畅运行

---

## 结语

太空算力正站在从"概念验证"到"规模部署"的历史转折点上。光芯片——凭借其抗辐射、低功耗、高带宽、轻量化和温度鲁棒性——为太空计算提供了独特的技术路径。

当前，太空光通信已进入商业化运营阶段（EDRS、中国实践二十号/吉林一号系列），而太空光计算仍处于实验室向工程化过渡的早期。预计 2030-2035 年将迎来光计算芯片的首次太空演示，2040 年后可能实现与量子传感器融合的先进光子智能系统。

对于产业参与者而言，关键投资方向包括：
1. **辐射硬化光芯片**：针对空间环境优化材料和设计
2. **非相干光计算架构**：降低温度敏感性，简化太空系统
3. **星间光互连标准**：推动 WDM 激光链路的互操作性
4. **太空-地面协同软件栈**：使光计算资源可被地面应用无缝调用

太空算力与光芯片的结合，不仅是技术的融合，更是人类计算边界向最终 frontier 的拓展。

---

**参考来源**：

- [Space-Based Edge Computing Market Size, Share, Forecast, 2034](https://www.fortunebusinessinsights.com/space-based-edge-computing-market-108137)
- [Space On Board Computing Platform Market Size to Hit USD 4.79 Billion by 2034](https://www.precedenceresearch.com/space-on-board-computing-platform-market)
- [AMD Chips Power SpaceX Starlink Satellites](https://gearmusk.com/2024/10/30/amd-chips-power-spacex-starlink-satellites/)
- [SpaceX V3 Starlink Satellites: 20x More Powerful](https://gearmusk.com/2025/01/01/spacex-v3-starlink-satellites/)
- [Musk Pushes Starlink Into Space-Based Computing](https://www.tmtpost.com/7748367.html)
- [Starcloud Raises $170M Series A at $1.1bn Valuation](https://lasvegassun.com/news/2026/mar/30/starcloud-raises-170m-series-a-at-11bn-valuation-led-by-benchmark-and-eqt-ventures/)
- [Starcloud Becomes First to Train LLMs in Space Using NVIDIA H100](https://analyticsindiamag.com/ai-news-updates/starcloud-becomes-first-to-train-llms-in-space-using-nvidia-h100/)
- [U.S. Space Force and SpaceX Partner to Develop 480-Satellite MILNET Constellation](https://satnews.com/2025/12/29/u-s-space-force-and-spacex-partner-to-develop-480-satellite-milnet-constellation/)
- [Amazon's Project Kuiper vs. Starlink](https://www.techtarget.com/whatis/feature/Amazons-Project-Kuiper-vs-Starlink-How-do-they-compare)
- [Space & Defense Semiconductors — Sector Supply Chain](https://semiconductorx.com/sector-space-military.html)
- [China SatNet GW Constellation](https://baike.baidu.com/en/item/China%20SatNet%20GW%20Constellation/1477932)
- [China adds new satellites to Guowang constellation](https://spacenews.com/china-adds-new-satellites-to-guowang-constellation-eyes-accelerated-launch-rate/)
- [GuoWang - Overview of the Chinese State-Owned LEO SatCom Constellation](https://www.skylinker.io/p/guowang-xingwang-gw-a59-china-satnet-chinese-leo-satcom-constellation-overview-eng)
- [2024年中国商业航天发展回顾与展望](https://www.spacejournal.cn/zght/article/id/0bf6d04d-d14d-4c45-a386-bb590b61f3a1)
- [银河航天：中国商业航天首家独角兽](https://tiu.taibo.cn/p/558)
- [中国商业航天的前景趋势与促进举措](http://paper.people.com.cn/rmlt/pc/content/202507/01/content_30087745.html)
- [Russia to start deploying Skif satellite constellation](https://tass.com/science/1535097)
- [ISRO to Launch AST SpaceMobile's BlueBird Satellite in Late 2025](https://hammermindset.com/isro-to-launch-ast-spacemobiles-bluebird-satellite-in-late-2025/)
- [NASA LCRD Overview](https://www.nasa.gov/missions/tech-demonstration/laser-communications-relay-demonstration-lcrd-overview/)
- [NASA TBIRD Mission](https://www.ll.mit.edu/r-d/projects/laser-communications-relay-demonstration)
- [NASA DSOC Mission](https://www.jpl.nasa.gov/missions/deep-space-optical-communications-dsoc/)
- [NASA laser comms demo achieves record data transmission from deep space](https://spacenews.com/nasa-laser-comms-demo-achieves-record-data-transmission-from-deep-space/)
- [European Data Relay System (EDRS)](https://connectivity.esa.int/archives/partnership-projects/european-data-relay-system-edrs)
- [Space Data Highway | European Data Relay System](https://www.airbus.com/en/products-services/defence/military-space/space-data-highway)
- [First European Data Relay System Satellite Forges 20,000 Successful Laser Links](https://spacenews.com/first-european-data-relay-system-satellite-forges-20000-successful-laser-links/)
- [实践二十号卫星激光通信通过在轨验证](https://www.spacechina.com/n25/n2014789/n2014804/c2885351/content.html)
- [超高速激光通信技术在实践二十号卫星完成验证](https://www.laserfair.com/yingyong/202005/14/76867.html)
- [国内外卫星激光通信进展](https://pibaojiameng.com/ccefdc2d73e96d8d/98cd42c161ceec87.html)
- [Space Qualifying Silicon Photonic Modulators and Circuits](https://pmc.ncbi.nlm.nih.gov/articles/PMC10776012/)
- [Evaluation of radiation hardness of InP-based photonic integrated circuits for space applications](https://ui.adsabs.harvard.edu/abs/2023SPIE12777E..6FP/abstract)
- [Photonic Integrated Circuits for Optical Satellite Links: A Review](https://onlinelibrary.wiley.com/doi/full/10.1002/sat.1552)
- [How do photonic chips perform in space environments?](https://www.photondelta.com/blog/how-do-photonic-chips-perform-in-space-environments/)
- [What is the difference between coherent and incoherent photonic chips?](https://www.photondelta.com/blog/what-is-the-difference-between-coherent-and-incoherent-photonic-chips/)
- [Thermal Stability and Optical Behavior of Porous Silicon Photonic Crystals](https://www.mdpi.com/2304-6732/12/2/94)
- [Spacecraft Thermal Control in Extreme Environments](https://www.electronics-cooling.com/2026/01/spacecraft-thermal-control-in-extreme-environments-surviving-lunar-night-and-martian-dust/)
- [Core Heat Dissipation Methods in Space](https://www.assembtek.com/blogs/insight/core-heat-dissipation-methods-in-space-how-do-orbital-data-centers-thermal-management)
- [Space Launch Cost Comparison 2026](https://spacenexus.us/guide/space-launch-cost-comparison)
- [SpaceX Starship: The True Cost Per Kilogram](https://posvirtual.fapam.edu.br/fapam-news/spacex-starship-the-true-cost-per-kilogram-1764800565)
- [Orbital Data Center & Space-Based AI Computing Market Research Report 2034](https://marketintelo.com/report/orbital-data-center-space-based-ai-computing-market)
- [Data Centers in Space Aren't as Wild as They Sound](https://www.scientificamerican.com/article/data-centers-in-space/)
- [Realities of Space-Based Compute](https://www.peraspera.us/realities-of-space-based-compute/)
- [Edge Computing in Space: Enhancing Data Processing and Communication](https://www.ijtsrd.com/papers/ijtsrd64541.pdf)
- [Space edge computing: Shaping the future of space operations](https://stlpartners.com/articles/edge-computing/space-edge-computing/)
- [How Many Satellites Are Orbiting Earth in 2025?](https://orbitalxploration.com/how-many-satellites-are-orbiting-earth-in-2025-latest-facts-and-surprising-insights)
- [Number of active satellites by year 2024](https://www.statista.com/statistics/897719/number-of-active-satellites-by-year/)
- [Optical Neural Networks: Principles, Challenges, and Future Prospects](http://www.ati.ac.cn/en/article/pdf/preview/10.61977/ati2025031.pdf)
- [Roadmap for Exoplanet High-Contrast Imaging](https://www.mdpi.com/2304-6732/12/10/1030)
- [SpaceMoE: Towards Orbital General Intelligence](https://arxiv.org/html/2605.16849v1)
- [Total Ionizing Dose (TID) Effects on Electronics](https://radiationtestsolutions.com/blogs/total-ionizing-dose-tid-effects-on-electronics/)
- [What is the TID Effect?](https://www.laser2cots.com/en/article/7.TID.html)
- [NASA Small Spacecraft Systems Virtual Institute - Thermal Control](https://www.nasa.gov/smallsat-institute/sst-soa/thermal-control/)
- [Loop Heat Pipes Technology for Satellites](https://www.arquimea.com/blog/satellites-loop-heat-pipes-technology/)
- [ESA, GeoVille and Eutelsat OneWeb to deliver connectivity](https://connectivity.esa.int/news/esa-geoville-and-eutelsat-oneweb-deliver-connectivity-distribute-earth-observation-data-across-africa)
- [OneWeb, Astroscale, UK Space Agency and ESA partner to launch space junk servicer ELSA-M](https://www.ukspace.org/oneweb-astroscale-uksa-esa-launch-space-junk-servicer-elsam/)
- [D-Orbit signs contract with OneWeb in the frame of ESA project Sunrise](https://www.spacedaily.com/reports/D_Orbit_signs_contract_with_OneWeb_in_the_frame_of_ESA_project_Sunrise_999.html)
- [Starshield](https://www.spacex.com/starshield/)
- [SpaceX's Starshield shapes the Earth observation and national security industries](https://spacesecurity.wse.jhu.edu/2024/09/23/spacexs-starshield-shapes-the-earth-observation-and-national-security-industries/)
- [Orbital Data Centers: The Complete Guide to Space-Based AI Infrastructure](https://introl.com/blog/orbital-data-centers-space-ai-infrastructure-guide-2025)
- [What Are Orbital Data Centers?](https://builtin.com/articles/orbital-data-centers-ai)
- [AI in Orbit? Starcloud's $170M Raise Pushes the Idea Forward](https://orbitaltoday.com/2026/04/01/ai-in-orbit-starclouds-170m-raise-pushes-the-idea-forward/)
- [SpaceX Files for Million-Satellite Orbital Data Center](https://introl.com/blog/spacex-million-satellite-orbital-data-center-2026)

---

*报告完成日期：2026 年 5 月 25 日*
