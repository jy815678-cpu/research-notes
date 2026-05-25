# 报告A：PACE 背景知识与技能进阶路线图

> **目标读者**：具备量子光学实验背景、希望系统掌握光芯片（Photonic IC）设计到系统集成全流程的研究者
> **覆盖范围**：从理论基础 → 设计工具 → 工艺制造 → 系统集成 → 技能进阶路径

---

## 第零章：前置说明——PACE 是什么？

Lightelligence 的 **PACE**（Photonic Arithmetic Computing Engine）是目前公开报道中最先进的光子计算加速器之一：

| 参数 | PACE | PACE2 |
|------|------|-------|
| 矩阵规模 | 64 × 64 MZI mesh | 128 × 128 |
| 离散光子器件数 | >12,000 | >48,000 |
| 系统时钟 | 1 GHz | 2 GHz |
| 光学计算延迟 | 150 ps | ~100 ps |
| 集成方式 | 3D Flip-Chip 键合（PIC + EIC） | 同左 |
| 应用场景 | Ising 求解器、AI 推理 | 大规模优化问题 |

核心思想：用 **马赫-曾德尔干涉仪（MZI）网格** 实现矩阵-向量乘法（MVM），将神经网络的权重矩阵编码到光路中，输入向量通过电光调制加载，输出通过光电探测器读取。

---

## 第1章：知识地图总览

### 1.1 从量子光学到 PACE 的完整知识链条

```
量子光学实验背景
        │
        ▼
┌─────────────────────────────────────────────────────────────────────┐
│  理论基础层（第2章）                                                   │
│  ├─ 电磁学与波导理论        ← 你的 MZI 经验直接迁移                      │
│  ├─ 半导体物理与器件                                                  │
│  ├─ 集成电路设计基础（模拟/混合信号）                                    │
│  ├─ 信号处理与控制系统                                                 │
│  └─ 机器学习与优化算法                                                  │
├─────────────────────────────────────────────────────────────────────┤
│  设计工具层（第3章）                                                   │
│  ├─ 光子设计工具链（Lumerical, IPKISS, GDSFactory）                   │
│  ├─ 电子设计自动化（Cadence Virtuoso, Spectre）                       │
│  ├─ 封装与热仿真                                                       │
│  └─ 算法仿真与验证（Neurophox, MEEP）                                  │
├─────────────────────────────────────────────────────────────────────┤
│  工艺与制造层（第4章）                                                   │
│  ├─ 硅光子代工厂与 PDK（AIM, AMF, CORNERSTONE）                       │
│  ├─ CMOS 工艺节点选择                                                   │
│  ├─ 封装工艺（2.5D/3D, Flip-Chip, 混合键合）                          │
│  └─ 测试与良率管理                                                       │
├─────────────────────────────────────────────────────────────────────┤
│  系统集成层（第5章）                                                   │
│  ├─ 硬件-软件协同设计                                                   │
│  ├─ 控制系统（FPGA, DAC/ADC 阵列）                                    │
│  └─ 算法到硬件的映射（ONNX → MZI 配置）                                │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.2 各阶段所需技能一览表

| 阶段 | 核心技能 | 工具/平台 | 时间投入（全职） |
|------|---------|----------|----------------|
| 理论基础 | 波导理论、半导体物理、电路设计 | 教材、在线课程 | 3-6 个月 |
| 设计实践 | 版图设计、仿真验证、DRC/LVS | Lumerical, KLayout, GDSFactory | 3-6 个月 |
| 电子设计 | TIA/ADC/DAC 设计、CMOS 布局 | Cadence Virtuoso | 6-12 个月 |
| 系统集成 | FPGA 控制、校准算法、接口协议 | Xilinx Vivado, Python | 3-6 个月 |
| 工艺制造 | PDK 使用、流片流程、封装测试 | 代工厂 PDK, 测试设备 | 6-12 个月 |

---

## 第2章：理论基础层

### 2.1 电磁学与波导理论

| 主题 | 重要性 | 核心概念 | 与你现有知识的关联 |
|------|--------|---------|-----------------|
| **介质波导模式** | ★★★★★ | TE/TM 偏振、有效折射率、模式限制 | 自由空间 MZI → 导波 MZI，物理本质相同 |
| **高折射率对比波导** | ★★★★★ | SOI 平台（220 nm Si / 2-3 μm SiO₂），n_Si~3.45 | 限制机制从自由空间变为波导边界 |
| **耦合模理论（CMT）** | ★★★★★ | 定向耦合器、功率转移、耦合长度 | 分束比设计的关键 |
| **转移矩阵法（TMM）** | ★★★★☆ | 级联器件分析、S 参数提取 | 从单器件到系统的桥梁 |
| **弯曲损耗与辐射** | ★★★★☆ | 最小弯曲半径（~5 μm）、欧拉弯曲 | 版图面积优化的核心 |
| **色散工程** | ★★★☆☆ | 群速度色散（GVD）、相位匹配 | WDM 系统设计 |

**关键洞察**：你在自由空间 MZI 中积累的相位控制经验（压电陶瓷、环境隔振）将直接帮助你理解片上热调相的稳定性挑战——只是控制对象从机械位移变为温度场。

### 2.2 半导体物理与器件

| 主题 | 应用场景 | 物理机制 |
|------|---------|---------|
| **PN 结电光效应** | 高速硅调制器（载流子耗尽/注入） | 等离子色散效应：Δn ∝ ΔN_e, ΔN_h |
| **Franz-Keldysh / QCSE** | Ge 电吸收调制器 | 电场调制带边吸收 |
| **光电探测机制** | Ge-on-Si 光电探测器 | 带隙工程：Ge 带隙 ~0.67 eV（C 波段敏感） |
| **热光效应** | 热相位调谐器 | dn/dT ~ 1.8×10⁻⁴ K⁻¹（硅） |
| **等离子色散效应** | 载流子注入型调制器 | Δn = -8.8×10⁻²² ΔN_e - 8.5×10⁻¹⁸ (ΔN_h)^0.8 |

### 2.3 集成电路设计基础（模拟/混合信号）

PACE 的电子芯片（EIC）需要以下模拟电路模块：

| 模块 | 功能 | 设计挑战 |
|------|------|---------|
| **跨阻放大器（TIA）** | 光电流 → 电压 | 噪声-带宽权衡、输入电容补偿 |
| **限幅放大器 / AGC** | 信号整形 | 增益控制、失调消除 |
| **调制器驱动器** | 驱动光调制器 | 摆幅（2-4V for PN 结）、带宽 |
| **DAC** | 数字权重 → 模拟相移电压 | 分辨率（8-16 bit）、线性度 |
| **ADC** | 光电探测输出数字化 | 速度 vs 功耗、有效位数（ENOB） |
| **带隙基准 / LDO** | 温度稳定偏置 | 电源抑制比（PSR） |

**推荐教材**：Razavi《Design of Analog CMOS Integrated Circuits》（模拟设计圣经）、《Design of Integrated Circuits for Optical Communications》（光通信专用）。

### 2.4 信号处理与控制系统

| 主题 | 应用场景 |
|------|---------|
| **反馈控制环路** | MZI 偏置稳定、热漂移补偿 |
| **卡尔曼滤波 / 状态估计** | 实时相位误差跟踪 |
| **自适应滤波** | 工艺偏差补偿 |
| **数字 PWM** | 热调相器的时分复用控制 |

### 2.5 机器学习与优化算法

| 算法 | 应用 |
|------|------|
| **梯度下降 / SGD** | 编程 MZI 网格权重矩阵 |
| **原位反向传播（In-situ BP）** | 在芯片上训练光子神经网络 |
| **Haar 初始化** | 加速大型 MZI 网格收敛（Stanford） |
| **物理感知训练（PAT）** | 将硬件非理想性纳入训练 |
| **随机优化** | 同时扰动所有相移器（2 次计算/迭代 vs 2N） |

---

## 第3章：设计工具层

### 3.1 光子设计工具链

| 工具 | 类型 | 用途 | 获取成本 |
|------|------|------|---------|
| **Lumerical FDTD** | 物理仿真（时域有限差分） | 器件级电磁仿真：波导模式、光栅耦合器、弯曲损耗 | 商业（$$$$） |
| **Lumerical MODE / EME** | 物理仿真（本征模/特征模展开） | 模式求解、波导传播分析 | 商业（$$$$） |
| **Lumerical INTERCONNECT** | 电路仿真 | 基于 S 参数的 PIC 系统仿真 | 商业（$$$$） |
| **IPKISS (Luceda)** | 参数化设计框架 | Python 驱动版图、层次化 PCell、多视图（版图/网表/3D） | 商业（$$$） |
| **GDSFactory** | 开源版图 | Python 参数化单元、布线、PDK 集成 | 免费 |
| **SiEPIC-Tools (KLayout)** | 开源版图 + 验证 | 波导布线、DRC、网表提取、电路仿真 | 免费 |
| **MEEP** | 开源 FDTD | Lumerical FDTD 的免费替代 | 免费 |

**推荐工作流**：
```
IPKISS / GDSFactory（版图）
        ↓
Lumerical FDTD / EME（器件仿真）
        ↓
S 参数提取
        ↓
Lumerical INTERCONNECT / Caphe（电路仿真）
        ↓
GDSII 导出 → 代工厂
```

### 3.2 电子设计自动化（EDA）

| 工具/流程 | 用途 |
|-----------|------|
| **Cadence Virtuoso** | 模拟/混合信号 IC 设计（原理图、版图、仿真） |
| **Synopsys Custom Compiler** | 替代模拟设计平台 |
| **Spectre / HSPICE** | 电路仿真 |
| **Innovus / ICC2** | 数字布局布线 |
| **Calibre** | 物理验证（DRC, LVS, PEX） |

### 3.3 封装与热仿真

| 挑战 | 解决方案 |
|------|---------|
| 热光漂移 | 主动 TEC 控制、闭环反馈 |
| 相移器间热串扰 | 矩阵寻址 + 集成二极管 + PWM 控制 |
| CPO 与 GPU/ASIC 的热耦合 | 与计算散热协同设计、AlN 衬底 |
| 激光器发热 | 独立温控区、衬底挖槽隔热 |

### 3.4 算法仿真与验证

| 工具 | 用途 | 链接 |
|------|------|------|
| **Neurophox** | MZI 网格仿真与训练 | https://github.com/solgaardlab/neurophox |
| **PyTorch / TensorFlow** | 神经网络定义与训练 | — |
| **ONNX** | 模型交换格式 | 硬件编译器的输入 |

---

## 第4章：工艺与制造层

### 4.1 硅光子代工厂与 PDK

| 平台 | SOI 厚度 | 光刻 | 关键特性 |
|------|---------|------|---------|
| **AIM Photonics (SUNY Poly)** | 220 nm | 300 mm, 193 nm 浸没 | 最先进、完整 PDK |
| **AMF (Singapore)** | 220 nm SOI / 400 nm SiN | 193 nm (Si) / 248 nm (SiN) | 多材料平台 |
| **CORNERSTONE (UK)** | 220 nm | 200 mm, DUV | 学术导向 |
| **IMEC (Belgium)** | 220 nm | 200 mm | 通过 ePIXfab 联盟 |
| **IHP (Germany)** | 220 nm | 248 nm | 兼容 BiCMOS |
| **GlobalFoundries** | 170 nm | 300 mm | 商业批量 |

### 4.2 CMOS 工艺节点选择

| 节点 | 应用 | 说明 |
|------|------|------|
| **180 nm / 130 nm** | TIA、限幅放大器、偏置电路 | 成熟、低成本，许多光应用足够 |
| **65 nm / 45 nm** | 高速调制器驱动器、SerDes | >25 Gbps 必需 |
| **28 nm / 16 nm** | ADC/DAC、数字信号处理 | 先进 DSP 和控制 |
| **FinFET (7 nm+)** | 数字逻辑、存储 | 未来单片集成 |

### 4.3 封装工艺（2.5D/3D）

| 技术 | 描述 | 用例 |
|------|------|------|
| **2.5D（硅中介层）** | PIC + EIC 通过 TSV 在 Si 中介层上 | 当前主流（TSMC COUPE, Intel EMIB） |
| **3D Flip-Chip** | 微凸点垂直堆叠 | Lightelligence PACE 方案 |
| **混合键合** | 低温下直接 Cu-Cu 键合 | 未来高密度集成 |
| **光子引线键合（PWB）** | 3D 打印自由曲面光波导 | 光纤到芯片、芯片间光路由 |

### 4.4 测试与良率管理

| 阶段 | 设备 | 目的 |
|------|------|------|
| **晶圆级** | EXFO OPAL-MD, ficonTEC WLT | 自动化光电探针、光栅/边缘耦合 |
| **芯片级** | 可调激光器、偏振控制器、功率计 | 光谱响应、插入损耗、消光比 |
| **封装模块** | 误码率测试仪（BERT）、示波器 | 端到端链路表征 |
| **系统级** | FPGA + DAC/ADC 测试平台 | 算法验证、校准 |

---

## 第5章：技能进阶路径

### 5.1 入门阶段（3-6 个月）

*充分利用你的量子光学背景*

| 资源 | 主题 | 优先级 |
|------|------|--------|
| **Yariv & Yeh, "Photonics: Optical Electronics in Modern Communications" (6th ed.)** | 集成光学理论、波导、CMT | ★★★★★ |
| **Reed & Knights, "Silicon Photonics: An Introduction"** | 硅特定波导性质、工艺 | ★★★★★ |
| **Chrostowski & Hochberg, "Silicon Photonics Design: From Devices to Systems"** | 实用设计流程、PDK、代工厂就绪设计 | ★★★★★ |
| **edX: UBC "Silicon Photonics Design, Fabrication and Data Analysis"** | 带实际流片的动手课程 | ★★★★★ |

**阶段目标**：理解 SOI 波导与自由空间光学的核心差异；能使用 KLayout + SiEPIC-Tools 绘制简单版图。

### 5.2 进阶阶段（6-12 个月）

| 资源 | 技能 |
|------|------|
| **Lumerical FDTD/MODE/INTERCONNECT 教程** | 器件和电路仿真 |
| **GDSFactory + KLayout + SiEPIC-Tools** | 开源版图和验证 |
| **IPKISS 教程 (Luceda)** | 参数化设计（如有访问权限） |
| **Neurophox (GitHub: solgaardlab/neurophox)** | 仿真和训练基于 MZI 的光神经网络 |

**阶段目标**：完成一个完整的光神经网络仿真项目（从 PyTorch 模型 → MZI 网格配置 → INTERCONNECT 验证）。

### 5.3 电子与控制（并行 4-8 个月）

| 资源 | 主题 |
|------|------|
| **Razavi, "Design of Analog CMOS Integrated Circuits" (2nd Ed.)** | 模拟 CMOS 基础 |
| **Razavi, "Design of Integrated Circuits for Optical Communications" (2nd Ed.)** | TIA、限幅放大器、调制器驱动器 |
| **Razavi, "Analysis and Design of Data Converters" (2023)** | ADC/DAC 架构 |
| **UBC ELEC 506: Photonic ICs (Dr. Sudip Shekhar)** | CMOS-光子协同设计 |

**阶段目标**：理解 TIA 和 DAC 的噪声-带宽权衡；能用 Spectre 仿真一个简单的接收机链路。

### 5.4 系统与流片（6-18 个月）

| 资源 | 主题 |
|------|------|
| **Colorado State University 论文: "Hardware-software codesign of silicon photonic AI accelerators"** | 完整协同设计方法论 |
| **FPGA 开发 (Xilinx Zynq, Vivado)** | 控制系统实现 |
| **MIT INPRIS 架构论文** | 大规模相移器控制、串扰 |
| **Ghent University 矩阵寻址论文** | PWM 控制、扩展到 1000+ 相移器 |
| **AIM Photonics / CORNERSTONE / ePIXfab MPW 流片** | 实际制造经验 |
| **PHIX Photonics Assembly 资源** | 封装最佳实践 |
| **Marvell / Intel / TSMC CPO 白皮书** | 2.5D/3D 集成 |

**阶段目标**：提交一次 MPW 流片（即使只是简单的测试结构）；搭建一个 FPGA + DAC 的相移器控制原型。

### 5.5 关键开源工具清单

| 工具 | 用途 | 链接 |
|------|------|------|
| **GDSFactory** | PIC 版图 | https://gdsfactory.github.io/gdsfactory/ |
| **SiEPIC-Tools** | KLayout 硅光子插件 | https://github.com/SiEPIC/SiEPIC-Tools |
| **Neurophox** | MZI 网格仿真与训练 | https://github.com/solgaardlab/neurophox |
| **MEEP** | 开源 FDTD | https://meep.readthedocs.io/ |

---

## 附录：关键成功因素

1. **从仿真开始**：在接触任何制造之前，先在 Lumerical INTERCONNECT + Neurophox 中搭建一个完整的类 PACE 仿真系统。

2. **先原型化控制**：使用 FPGA + DAC 评估板配合商用硅光子芯片（如 SiEPICfab 或 AIM Photonics）验证控制算法。

3. **尽早提交 MPW**：即使是简单的测试结构（光栅耦合器、直波导、MZI），通过 CORNERSTONE 或 AIM Photonics 的实际流片经验将远超数月的阅读。

4. **拥抱硬件-软件协同设计**：光学部分只占挑战的 ~30%。电子控制、校准和算法映射同等关键。

5. **加入社区**：SiEPIC、AIM Photonics、ePIXfab 有活跃的用户社区。GDSFactory Slack 和 Luceda 论坛 invaluable。

---

*本报告为技能路线图，侧重"知道什么"和"如何学习"。具体技术细节和参数会随工艺节点和设计目标变化，建议以目标代工厂的 PDK 文档为准。*
