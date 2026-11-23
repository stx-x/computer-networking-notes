---
title: 习题
outline: [2, 3]
---

# 习题

## 复习题

### 3.1～3.3 节

**R1.** 假设网络层提供如下服务：源主机中的网络层从运输层接收一个最大长度为 1200 字节的报文段和一个目的主机地址，然后保证把该报文段交付给目的主机中的运输层。假设目的主机上可以运行许多网络应用进程。

1. 设计一个尽可能简单的运输层协议，把应用数据送到目的主机上期望的进程。假定目的主机的操作系统已为每个运行中的应用进程分配了一个 4 字节的端口号。
1. 修改该协议，使其能为目的进程提供一个"回信地址"。
1. 在你的协议中，运输层是否"必须做点什么"才能提供其服务？在计算机网络的核心中呢？

**R2.** 考虑这样一颗行星：每个人都属于一个六口之家，每个家庭住在自己的房子里，每座房子有唯一地址，同一座房子里的每个人都有唯一的名字。假设这颗行星有一种邮件服务，把信件从源房子投递到目的房子。邮件服务要求：(1) 信件必须装在信封里；(2) 信封上必须清楚地写明目的房子的地址（仅此而已）。假设每个家庭有一名代表，负责为其他家庭成员收集和分发信件。信件本身不一定标明收信人。

1. 借鉴上面 R1 的解法，描述一种代表们可用来把信件从某个发送方家庭成员送到某个接收方家庭成员的协议。
1. 在你的协议中，邮件服务是否曾经需要打开信封、检查信件内容才能提供服务？

**R3.** 考虑主机 A 与主机 B 之间的一条 TCP 连接。假设从 A 发往 B 的 TCP 报文段的源端口号为 $x$、目的端口号为 $y$，那么从 B 发往 A 的报文段的源端口号和目的端口号分别是什么？

**R4.** 说明应用开发者为什么会选择在 UDP 而不是 TCP 之上运行应用。

**R5.** 在当今的因特网中，为什么语音和视频流量常常通过 TCP 而不是 UDP 发送？（提示：我们所期待的答案与 TCP 的拥塞控制机制无关。）

**R6.** 应用运行在 UDP 之上时，是否仍可能获得可靠数据传输？如果可以，怎么做？

**R7.** 假设主机 C 中某个进程有一个端口号为 6789 的 UDP 套接字。假设主机 A 和主机 B 都向主机 C 发送目的端口号为 6789 的 UDP 报文段。这两个报文段会被导向主机 C 的同一个套接字吗？如果是，主机 C 中的进程如何知道这两个报文段来自两台不同的主机？

**R8.** 假设主机 C 在端口 80 上运行一个 Web 服务器，该服务器使用持久连接，当前正在接收来自两台不同主机 A 和 B 的请求。所有这些请求都通过主机 C 的同一个套接字发送吗？如果它们通过不同的套接字传递，那么这两个套接字的端口号都是 80 吗？请讨论并解释。

### 3.4 节

**R9.** 在我们的 rdt 协议中，为什么需要引入序号？

**R10.** 在我们的 rdt 协议中，为什么需要引入定时器？

**R11.** 假设发送方与接收方之间的往返时延恒定，且发送方已知该值。在假定分组可能丢失的前提下，rdt3.0 协议中是否仍然需要定时器？请解释。

**R12.** 访问配套网站上的 Go-Back-N 交互式动画。

1. 让发送方发送五个分组，然后在任何一个分组到达目的地之前暂停动画；接着"杀死"第一个分组并继续播放。描述发生了什么。
1. 重复该实验，但这次让第一个分组到达目的地，并"杀死"第一个确认。再次描述发生了什么。
1. 最后，试着发送六个分组。会发生什么？

**R13.** 重复 R12，但改用选择重传交互式动画。选择重传与回退 N 步有何不同？

### 3.5 节

**R14.** 判断正误。

1. 主机 A 通过一条 TCP 连接向主机 B 发送一个大文件。假定主机 B 没有数据要发给 A。由于主机 B 无法把确认捎带在数据上，它将不会向主机 A 发送确认。
1. TCP 的 rwnd 大小在连接持续期内从不改变。
1. 假设主机 A 通过一条 TCP 连接向主机 B 发送一个大文件，则 A 发送的未确认字节数不能超过接收缓冲区的大小。
1. 假设主机 A 通过一条 TCP 连接向主机 B 发送一个大文件。若该连接中某个报文段的序号为 $m$，则下一个报文段的序号必然是 $m + 1$。
1. TCP 报文段首部中有一个用于 rwnd 的字段。
1. 假设某 TCP 连接中最近一次的 SampleRTT 等于 1 秒，则该连接当前的 TimeoutInterval 必然 $\ge 1$ 秒。
1. 假设主机 A 通过一条 TCP 连接向主机 B 发送一个序号为 38、含 4 字节数据的报文段，则在同一报文段中，确认号必然是 42。

**R15.** 假设主机 A 通过一条 TCP 连接向主机 B 背靠背发送两个 TCP 报文段，第一个的序号为 90，第二个的序号为 110。

1. 第一个报文段中有多少数据？
1. 假设第一个报文段丢失，而第二个报文段到达了 B。在主机 B 发给主机 A 的确认中，确认号是多少？

**R16.** 考虑 3.5 节讨论的 Telnet 例子。在用户键入字母 'C' 几秒之后，用户又键入了字母 'R'。键入 'R' 之后，共发送多少个报文段？这些报文段的序号字段和确认号字段中分别填入了什么？

### 3.7 节

**R17.** 假设有两条 TCP 连接经过某条速率为 $R$ bps 的瓶颈链路，两条连接都有巨大的文件要发送（沿瓶颈链路的同一方向），且文件传输同时开始。TCP 愿意给这两条连接各分配多大的传输速率？

**R18.** 判断正误：考虑 TCP 中的拥塞控制，当发送方定时器超时时，ssthresh 的值被置为其原值的一半。

**R19.** 在 3.7 节关于 TCP 分接（TCP splitting）的专栏中曾断言：采用 TCP 分接时的响应时间约为 $4 \cdot \text{RTT}_{\text{FE}} + \text{RTT}_{\text{BE}} + \text{处理时间}$。请论证这一断言。

说明：原书本章还给出 58 道计算与分析题（P1–P58，原书第 272–283 页），涉及 rdt 协议设计、GBN/SR 窗口分析、TCP 序号与超时计算、拥塞控制建模等。这些题目与正文各节的推导一一对应，建议配合本节复习题一并练习。

# 附录 A　术语对照表

| 术语 | English | 术语 | English |
| --- | --- | --- | --- |
| 运输层 | transport layer | 多路复用 | multiplexing |
| 逻辑通信 | logical communication | 多路分解 | demultiplexing |
| 报文段 | segment | 套接字 | socket |
| 数据报 | datagram | 端口号 | port number |
| 周知端口号 | well-known port number | 无连接 | connectionless |
| 面向连接 | connection-oriented | 全双工 | full-duplex |
| 可靠数据传输 | reliable data transfer | 流量控制 | flow control |
| 拥塞控制 | congestion control | 拥塞窗口 | congestion window |
| 尽力而为交付 | best-effort delivery | 接收窗口 | receive window |
| 停等协议 | stop-and-wait | 肯定确认 | positive acknowledgment |
| 否定确认 | negative acknowledgment | 自动重传请求 | ARQ |
| 序号 | sequence number | 确认号 | acknowledgment number |
| 累积确认 | cumulative acknowledgment | 选择确认 | selective acknowledgment |
| 重复 ACK | duplicate ACK | 快速重传 | fast retransmit |
| 回退 N 步 | Go-Back-N | 选择重传 | selective repeat |
| 滑动窗口 | sliding window | 窗口长度 | window size |
| 带宽时延积 | bandwidth-delay product | 瓶颈链路 | bottleneck link |
| 有限状态机 | finite-state machine | 扩展有限状态机 | extended FSM |
| 校验和 | checksum | 反码 | 1s complement |
| 回卷 | wraparound | 端到端原则 | end-end principle |
| 最大报文段长度 | MSS | 最大传输单元 | MTU |
| 发送缓冲区 | send buffer | 接收缓冲区 | receive buffer |
| 慢启动 | slow start | 拥塞避免 | congestion avoidance |
| 快速恢复 | fast recovery | 慢启动阈值 | ssthresh |
| 加性增乘性减 | AIMD | 带宽探测 | bandwidth probing |
| 三次握手 | three-way handshake | 半开连接 | half-open connection |
| SYN 洪泛攻击 | SYN flood attack | 重置报文段 | reset segment |
| 显式拥塞通知 | ECN | 阻流分组 | choke packet |
| 队头阻塞 | HOL blocking | 往返时间 | RTT |
| 超时间隔 | timeout interval | 指数加权移动平均 | EWMA |
| 拥塞崩溃 | congestion collapse | 公平性 | fairness |
| 流 | stream | 面向报文的 | message-oriented |

# 附录 B　符号与公式速查

| 术语 | English |
| --- | --- |
| $L$ | [分组长度（比特）] |
| $R$ | [链路传输速率（比特/秒）] |
| $d_{\text{trans}}$ | [传输时延，$d_{\text{trans}} = \frac{L}{R}$] |
| $\text{RTT}$ | [往返时间] |
| $\text{MSS}$ | [最大报文段长度（应用层数据字节数）] |
| $\text{cwnd}$ | [拥塞窗口（字节）] |
| $\text{rwnd}$ | [接收窗口（字节）] |
| $\text{RcvBuffer}$ | [接收缓冲区大小（字节）] |
| $\text{SendBase}$ | [最早的未确认字节的序号] |
| $\text{NextSeqNum}$ | [下一个待发字节的序号] |
| $\text{ssthresh}$ | [慢启动阈值] |
| $W$ | [丢包事件发生时的窗口大小] |
| $\alpha$ | [EstimatedRTT 的权重，推荐 $\frac{1}{8}$] |
| $\beta$ | [DevRTT 的权重，推荐 $\frac{1}{4}$] |
| $N$ | [GBN/SR 的窗口长度] |

| **公式** | **说明** |
| --- | --- |
| $U_{\text{sender}} = \frac{\frac{L}{R}}{\text{RTT} + \frac{L}{R}}$ | 停等协议的发送方利用率 |
| $\text{EstimatedRTT} = (1 - \alpha) \text{EstimatedRTT} + \alpha \text{SampleRTT}$ | RTT 的指数加权移动平均 |
| $\text{DevRTT} = (1 - \beta) \text{DevRTT} + \beta \lvert \text{SampleRTT} - \text{EstimatedRTT} \rvert$ | RTT 偏差 |
| $\text{TimeoutInterval} = \text{EstimatedRTT} + 4 \text{DevRTT}$ | 重传超时间隔 |
| $\text{LastByteSent} - \text{LastByteAcked} \le \text{min}(\text{cwnd}, \text{rwnd})$ | 未确认数据量的上界 |
| $\text{rwnd} = \text{RcvBuffer} - [\text{LastByteRcvd} - \text{LastByteRead}]$ | 接收窗口 |
| $\text{发送速率} \approx \frac{\text{cwnd}}{\text{RTT}}$ | TCP 的平均发送速率 |
| $\text{平均吞吐量} = 0.75 \frac{W}{\text{RTT}}$ | TCP Reno 的宏观吞吐量 |
