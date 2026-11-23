---
title: 7.7　小结
outline: [2, 3]
---

# 7.7　小结

无线移动网络最初彻底改变了电话，如今在计算机网络世界中也正产生日益深刻的影响。联网的无线用户已是有线用户的五倍以上，加上随时随地、无拘无束地接入全球网络基础设施，无线网络正提供近乎无处不在的无线因特网连通性，并促成了一组令人兴奋的新移动、位置相关服务。鉴于无线与移动网络的重要性，我们用整整一章（本章）讨论这个主题。

本章从无线与移动网络导论开始，随后自底向上研究其原理与实践。尽管我们强烈偏好自顶向下的教学方法，但我们认为尽早掌握底层无线电信道是理解无线网络几乎其他所有方面的前提。因此 7.2 节从研究无线电信道的独特特性开始深入研究，随后学习比特如何被编码为符号、符号又如何被调制、发送并在该信道上接收。7.3 节转向无线接入网，涵盖共享无线信道、网络发现与设备附着、帧传输调度与节能等技术；在 7.3 节全篇我们用 WiFi 与 5G 网络说明所学原理如何付诸实践。7.4 节讲了移动核心网——蜂窝网络的关键体系结构组件，为全球身份、移动性与服务订购提供支持，而这些服务在传统有线因特网中通常没有。移动性是无线网络如此独特的特征，我们用整整一节（7.5 节）讨论它。本章主要聚焦 5G 与 WiFi 网络，但 7.6 节也简要介绍了另外三种重要的无线网络体系结构——蓝牙、卫星与 IoT 无线网络。

尽管我们用整整一章研究无线与移动网络，要充分探索这个令人兴奋且快速扩张的领域仍需要一整本书（甚至更多）！这个主题本身足以开一门完整的课——本书作者之一确实开了这样一门课 [Kurose 2025]。我们鼓励读者查阅本章提到的众多资源，更深入地钻研这个领域。

# 复习题

par(first-line-indent: 0em, leading: 1.5em)

以下 R1–R50 为原书第 7 章复习题全译。答案均可直接在本章正文中找到。

7.1 节

1. 回答以下关于无线接入网与无线核心网的复习题。这两者中哪一个包含用户设备？哪一个附着到更大的因特网？哪一个包含把用户设备连入无线网络的无线链路？
1. 一个无线网络工作在"基础设施模式"是什么意思？若网络不工作在基础设施模式，它工作在什么模式？该模式与基础设施模式有何不同？

7.2 节

1. 描述电磁波的幅度、频率与相位各指什么。这三个特征中你会用哪一个来确定波长？
1. 无线电信号的带宽与经无线信道传输的比特每秒数是一回事吗？
1. 列举两个在发送方与接收方之间的无线电信道中引入噪声的来源。
1. 无线信号传输与接收中，路径损耗与多径效应有何不同？
1. "隐藏终端"问题的两个成因是什么？
1. 对接收方所收到的发送信号，"相干时间"指什么？
1. MIMO 空间分集与 MIMO 空间复用有何不同？
1. "波束成形"指什么？
1. 许可频谱与免许可频谱有何不同？5G 主要工作在许可还是免许可频谱？WiFi 呢？
1. 物理层中编码与调制有何不同？
1. 无线电信号有哪三个可被调制以把信息编码进信号的特性？（提示：见复习题 R3。）
1. 正交幅度调制（QAM）中调制的是无线电信号的哪些特性？
1. 当移动节点离基站越来越远时，基站可以采取哪两项动作来确保所发帧的丢失概率不上升？

7.3 节

1. FDM、OFDM 与 OFDMA 之间的共同点与差别是什么？
1. 在 CSMA/CA 中，想发送帧的站会做载波侦听吗？会做冲突检测吗？
1. 在 CSMA/CA 中，请求发送（RTS）与允许发送（CTS）报文的作用／目的是什么？
1. 假设 IEEE 802.11 的 RTS 与 CTS 帧与标准 DATA、ACK 帧一样长。使用 CTS 与 RTS 帧还有任何好处吗？为什么？
1. 为什么 802.11 中使用确认，而有线以太网中不用？
1. "密集部署"的 WiFi 网络指什么？它与比如因特网咖啡馆中的 WiFi 部署有何不同？
1. 5G RAN 中资源单元与资源块之间是什么关系？
1. 按带宽从宽到窄排列 5G 中的以下结构：信道、频段、子信道。
1. 用一句话分别简述 5G RAN 中无线资源控制（RRC）、服务数据适配协议（SDAP）、分组数据汇聚协议（PDCP）与无线链路控制（RLC）的作用。
1. 在 5G RAN 语境下，"解绑"（disaggregation）指什么？
1. 网络发现中"信标"报文的作用是什么？
1. 对信标的主动扫描与被动扫描有何不同？
1. 802.11 关联请求帧的用途是什么？
1. 下列 MAC 帧调度准则中，哪些在做调度决策时考虑了收发双方的信道特性：轮询（RR）、最大吞吐量（MT）、盲式等吞吐（BET）、比例公平（PF）？
1. 下列 MAC 帧调度准则中，哪些在做调度决策时考虑了用户间的公平：轮询（RR）、最大吞吐量（MT）、盲式等吞吐（BET）、比例公平（PF）？
1. 在协调式睡眠／唤醒的节能途径中，被协调的是哪些网络元素的行为？

7.4 节

1. 控制平面与数据平面。下列哪句话最好地描述了控制平面与数据平面之间的区别？

- a. 控制平面与数据平面在不同网络层执行相同的功能。
  - b. 控制平面生成数据，而数据平面为数据选路。
  - c. 数据平面负责转发含用户数据的分组，而控制平面负责管理（配置、监视）执行该转发的网络基础设施。
  - d. 控制平面基于硬件，而数据平面基于软件。

1. 说 5G 核心采用"服务化体系结构"是什么意思？
1. 5G 核心中用户平面功能的作用是什么？
1. 5G 核心中接入与移动性管理功能（AMF）执行的两个关键功能是什么？
1. 5G 核心的用户平面中为什么要用隧道？
1. 蜂窝 SIM 卡中存储的五项信息是什么？
1. 判断正误：是否接纳一台到达设备加入 5G 网络的决定，总是完全由该到达设备所要加入的网络独自做出。
1. 软件化。网络软件化的首要目标是什么？

- a. 减小网络硬件的物理尺寸
  - b. 通过软件方案提高网络的灵活性与可编程性
  - c. 用软件取代所有网络硬件
  - d. 增强网络设备的安全性

7.5 节

1. 移动用户设备可能被从一台基站切换到另一台基站的两个原因是什么？
1. 判断正误：5G 会执行从一台基站到另一台基站的切换，而 WiFi 不具备从一台基站切换到另一台基站的这种能力。
1. 在 5G 中，设备切换是由用户设备、源基站还是目标基站发起的？
1. 判断正误：5G 切换过程中，目的地为设备的数据平面数据报将始终只经过恰好一台基站。
1. 判断正误：5G 切换过程中及切换之后，设备在 RAN 与核心之间隧道的端点不会改变。

7.6 节

1. 你认为蓝牙的设计者为何选择从一个时隙到下一个时隙使用跳频，而不是像 WiFi 那样使用固定频率信道？
1. 蓝牙中逻辑链路控制与适配（L2CAP）层的作用是什么？
1. 判断正误：蓝牙中通信只发生在中心节点与外围节点之间；外围节点之间没有直接通信。
1. 考虑 GEO 与 LEO 卫星网络。这两类网络中"地面—卫星—地面"的往返时延有何不同？在这两类网络中，哪一类里卫星与地面站的相对位置会变化？
1. 经 LEO 卫星网络的"弯管"式端到端路径指什么？
1. 考虑三类 IoT 网络：短距离低功耗（WiFi、低功耗蓝牙）、广域低功耗（LoRaWAN）与传统蜂窝（LTE-M）。这三类中哪一类往往数据率最低？哪一类往往地理足迹最小？哪一类往往能耗最高？

# 附录 A　术语对照表

| 英文 | 中文 |
| --- | --- |
| wireless access network | 无线接入网 |
| wireless core network | 无线核心网 |
| base station | 基站 |
| access point (AP) | 接入点 |
| gNB / eNB | 5G／4G 基站（3GPP 术语） |
| user equipment (UE) | 用户设备 |
| infrastructure / ad hoc mode | 基础设施／自组织模式 |
| handover (handoff) | 切换 |
| amplitude / wavelength | 幅度／波长 |
| phase | 相位 |
| carrier frequency | 载波频率 |
| power spectral density | 功率谱密度 |
| signal bandwidth | 信号带宽 |
| signal-to-noise ratio (SNR) | 信噪比 |
| Shannon capacity | 香农容量 |
| path loss / attenuation | 路径损耗／衰减 |
| hidden terminal problem | 隐藏终端问题 |
| multipath | 多径 |
| coherence time | 相干时间 |
| MIMO | 多输入多输出 |
| spatial diversity | 空间分集 |
| spatial multiplexing | 空间复用 |
| beamforming | 波束成形 |
| MU-MIMO | 多用户 MIMO |
| licensed / unlicensed spectrum | 许可／免许可频谱 |
| coding | 编码 |
| modulation | 调制 |
| ASK / FSK / PSK | 幅移／频移／相移键控 |
| QPSK | 正交相移键控 |
| constellation diagram | 星座图 |
| QAM | 正交幅度调制 |
| adaptive modulation | 自适应调制 |
| bit error rate (BER) | 比特差错率 |
| OFDM | 正交频分多路复用 |
| guard band | 保护带 |
| OFDMA | 正交频分多址 |
| resource element (RE) | 资源单元 |
| resource block (RB) | 资源块 |
| resource unit (RU) | 资源单元（WiFi） |
| CSMA/CA | 带冲突避免的载波侦听多路访问 |
| DIFS / SIFS | 分布式／短帧间间隔 |
| RTS / CTS | 请求发送／允许发送 |
| basic service set (BSS) | 基本服务集 |
| extended service set (ESS) | 扩展服务集 |
| SSID | 服务集标识符 |
| beacon | 信标 |
| association request/response | 关联请求／响应 |
| MU-RTS | 多用户 RTS |
| MAC scheduler | MAC 调度器 |
| channel quality indication (CQI) | 信道质量指示 |
| received signal strength indicator (RSSI) | 接收信号强度指示 |
| round robin (RR) | 轮询调度 |
| maximum throughput (MT) | 最大吞吐量调度 |
| blind equal throughput (BET) | 盲式等吞吐调度 |
| proportional fairness (PF) | 比例公平调度 |
| DRX | 非连续接收 |
| target wake time (TWT) | 目标唤醒时间 |
| traffic indication map (TIM) | 业务指示图 |
| service-based architecture (SBA) | 服务化体系结构 |
| network function (NF) | 网元功能 |
| user plane function (UPF) | 用户平面功能 |
| access and mobility management function (AMF) | 接入与移动性管理功能 |
| session management function (SMF) | 会话管理功能 |
| unified data management (UDM) | 统一数据管理 |
| unified data repository (UDR) | 统一数据存储库 |
| network exposure function (NEF) | 网络开放功能 |
| authentication server function (AUSF) | 鉴别服务器功能 |
| security edge protection proxy (SEPP) | 安全边缘保护代理 |
| network repository function (NRF) | 网络存储库功能 |
| policy control function (PCF) | 策略控制功能 |
| network slicing | 网络切片 |
| reference point (N1/N2) | 参考点 |
| GTP | GPRS 隧道协议 |
| registration | 注册 |
| PDU session establishment | PDU 会话建立 |
| SIM / eSIM | 用户身份模块／嵌入式 SIM |
| IMSI | 国际移动用户身份 |
| MCC / MNC / MSIN | 移动国家码／移动网络码／用户识别号 |
| roaming | 漫游 |
| tracking area update | 跟踪区更新 |
| paging | 寻呼 |
| Mobile IP | 移动 IP |
| Bluetooth / piconet | 蓝牙／微微网 |
| FHSS | 跳频扩频 |
| L2CAP | 逻辑链路控制与适配协议 |
| GEO / LEO satellite | 地球静止／低地球轨道卫星 |
| footprint | 足迹 |
| inter-satellite link (ISL) | 星间链路 |
| bent pipe | 弯管（架构） |
| LoRaWAN | 远距离广域网 |
| NB-IoT / LTE-M | 窄带 IoT／机器型 LTE |
| BLE / Zigbee | 低功耗蓝牙／Zigbee |

# 附录 B　数值与公式速查

| **项目** | **数值／公式** | **说明** |
| --- | --- | --- |
| 光速 | $3 \times 10^{8}$ m/s | 电磁波传播速度（近似） |
| SNR（dB） | $10 \log _{10}(\frac{S}{N})$ | WiFi 下限约 20 dB；LTE 为 −5～18 dB |
| 香农容量 | $C = B \log _{2}(1 + \frac{S}{N})$ | 带宽与 SNR 决定容量上界 |
| 路径损耗指数 | 2 / 3 / 4+ | 自由空间／城市／室内 |
| WiFi 2.4 GHz 信道 | 11 个 × 20 MHz | 1、6、11 为唯一三信道组合 |
| 最小信道带宽（WiFi） | 20 MHz | 更高带宽靠绑定相邻 20 MHz |
| 802.11 载荷上限 | 2 312 字节 | 通常小于 1 500 字节 |
| 802.11 地址字段 | 4 个 × 6 字节 | 基础设施模式用前三个 |
| 802.11 CRC | 32 比特 | 比特差错在无线中更常见 |
| RE（4G/5G） | 15 kHz × 66.6 μs | WiFi 为 78 kHz × 12.8 μs |
| RB（4G） | 84 个符号 | 12 子载波 × 7 微时隙 |
| 4G 信道带宽 | 1.4–20 MHz | 5G 扩展到 100 MHz |
| 4G/5G 调度周期 | 1 ms | WiFi 6 可更短 |
| DRX 最大 TWT | 约 4 年 5 个月 | WiFi 6 的睡眠协商上限 |
| LEO 轨道高度 | 500–1 200 km | 往返时延约 30 ms |
| GEO 轨道高度 | 约 35 000 km | 往返时延约 800 ms |
| LEO 卫星足迹 | 直径约 15 英里 | 地面站停留约 10 分钟 |
| LEO 卫星速度 | 27 000 km/h | 相对地面 |
| 蓝牙信道／时隙 | 79 个 × 625 μs | 跳频扩频（FHSS） |
| 蓝牙微微网 | 最多 8 个活跃设备 | 1 个中心 + 至多 7 个外围 |

| **调制方式** | **每符号比特数** |
| --- | --- |
| QPSK（4-QAM） | 2 |
| 16-QAM | 4 |
| 64-QAM | 6 |
| 256-QAM | 8 |
| 1024-QAM / 4096-QAM | 10 / 12（WiFi 6/7） |
