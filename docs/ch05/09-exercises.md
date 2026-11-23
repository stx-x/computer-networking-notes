---
title: 5.8　小结
outline: [2, 3]
---

# 5.8　小结

至此，我们完成了深入网络核心的两章旅程——它始于第 4 章对网络层数据平面的学习，止于本章对网络层控制平面的学习。我们学到，控制平面是网络范围的逻辑，它不仅控制一个数据报如何沿源主机到目的主机的端到端路径在各路由器之间被转发，也控制网络层组件与服务如何被配置和管理。

我们学到，构建控制平面有两大途径：传统的**逐路由器控制**（路由算法在每台路由器中运行，路由器中的选路组件与其他路由器中的选路组件通信）与**软件定义网络**（SDN）控制（逻辑集中的控制器计算并分发每台路由器要使用的转发表）。5.2 节研究了在图中计算最小代价路径的两种基本路由算法——链路状态选路与距离向量选路；这两种算法在逐路由器控制与 SDN 控制中都有应用。它们是两种广泛部署的因特网路由协议 OSPF 与 BGP 的基础，5.3、5.4 节分别讨论了这两个协议。5.5 节讨论了网络层控制平面的 SDN 途径，考察了 SDN 网络控制应用、SDN 控制器，以及控制器与 SDN 控制设备之间通信的 OpenFlow 协议。5.6、5.7 节讨论了管理一个 IP 网络的一些"螺母与螺栓"：ICMP（因特网控制报文协议），以及使用 SNMP 与 NETCONF/YANG 的网络管理。

完成了对网络层的学习，我们的旅程现在沿协议栈再往下走一步，即走向链路层。与网络层一样，链路层也是每一台联网设备的一部分。但下一章会看到，链路层承担的任务要局部得多：在同一链路或局域网上的节点之间移动分组。虽然这项任务表面上比网络层的任务简单，但我们会看到，链路层涉及许多重要而迷人的问题，足以让我们忙上很久。

# 复习题

par(first-line-indent: 0em, leading: 1.5em)

以下 R1–R23 为原书第 5 章复习题全译。复习题用于检验对概念的理解，答案均可直接在本章正文中找到。

5.1 节

1. 什么是基于**逐路由器控制**的控制平面？在这种情形下，当我们说网络控制平面与数据平面是"一体化"（monolithically）实现时，指的是什么？
1. 什么是基于**逻辑集中式控制**的控制平面？在这种情形下，数据平面与控制平面是实现在同一设备中，还是实现在分离的设备中？请解释。
1. 比较并对照集中式路由算法与分布式路由算法的性质。各举一个采取集中式与分散式途径的路由协议的例子。

5.2 节

1. 比较并对照链路状态与距离向量路由算法。
1. 距离向量选路中的"无穷计数"（count to infinity）问题是什么？
1. 每个自治系统是否有必要使用相同的 AS 内部路由算法？为什么？

5.3–5.4 节

1. 因特网中为什么要使用不同的 AS 间与 AS 内路由协议？
1. 判断正误：当一台 OSPF 路由器发送其链路状态信息时，它只发给直接相连的邻居节点。请解释。
1. OSPF 自治系统中的**区域**（area）是什么意思？为什么要引入区域这个概念？
1. 定义并对照以下术语：**子网**、**前缀**、**BGP 路由**。
1. BGP 如何使用 NEXT-HOP 属性？它如何使用 AS-PATH 属性？
1. 描述一家上层 ISP 的网络管理员在配置 BGP 时可以如何实施策略。
1. 判断正误：当一台 BGP 路由器从邻居收到一条通告的路径时，它必须把自己的标识加到收到的路径上，然后把这条新路径发送给它的所有邻居。请解释。

5.5 节

1. 描述 SDN 控制器中通信层、网络范围状态管理层与网络控制应用层的主要作用。
1. 假设你想在 SDN 控制平面中实现一个新的路由协议。你会把该协议实现在哪一层？请解释。
1. 哪些类型的报文流过 SDN 控制器的北向与南向 API？控制器跨南向接口发出的报文，其接收者是谁？跨北向接口向控制器发送报文的又是谁？
1. 描述两种（任选）从被控设备发往控制器的 OpenFlow 报文的用途。描述两种（任选）从控制器发往被控设备的 OpenFlow 报文的用途。
1. OpenDaylight SDN 控制器中服务抽象层的作用是什么？

5.6–5.7 节

1. 列举四种不同类型的 ICMP 报文。
1. 在执行 **Traceroute** 程序的发送主机上，会收到哪两种类型的 ICMP 报文？
1. 在 SNMP 语境下定义以下术语：**管理服务器**、**被管设备**、**网络管理代理**、**MIB**。
1. SNMP 的 GetRequest 与 SetRequest 报文各有什么用途？
1. SNMP trap 报文的用途是什么？

# 附录 A　术语对照表

| 英文 | 中文 |
| --- | --- |
| control plane | 控制平面 |
| data plane | 数据平面 |
| per-router control | 逐路由器控制 |
| logically centralized control | 逻辑集中式控制 |
| control agent (CA) | 控制代理 |
| routing algorithm | 路由算法 |
| centralized routing algorithm | 集中式路由算法 |
| decentralized routing algorithm | 分散式路由算法 |
| static / dynamic routing | 静态／动态路由 |
| load-sensitive / -insensitive | 负载敏感／不敏感 |
| link-state (LS) algorithm | 链路状态算法 |
| distance-vector (DV) algorithm | 距离向量算法 |
| Dijkstra's algorithm | Dijkstra 算法 |
| Bellman-Ford equation | Bellman-Ford 方程 |
| route oscillation | 路由振荡 |
| count-to-infinity problem | 无穷计数问题 |
| poisoned reverse | 毒性逆转 |
| quiescent state | 静止状态 |
| autonomous system (AS) | 自治系统 |
| AS number (ASN) | 自治系统号 |
| intra-AS routing protocol | AS 内部路由协议 |
| inter-AS routing protocol | AS 间路由协议 |
| OSPF | 开放最短路径优先 |
| IS-IS | 中间系统到中间系统 |
| area | 区域 |
| backbone area | 骨干区域 |
| area border router | 区域边界路由器 |
| HELLO message | HELLO 报文 |
| BGP | 边界网关协议 |
| BGP connection | BGP 连接 |
| eBGP / iBGP | 外部／内部 BGP |
| gateway router | 网关路由器 |
| internal router | 内部路由器 |
| prefix | 前缀 |
| AS-PATH | AS 路径属性 |
| NEXT-HOP | 下一跳属性 |
| hot potato routing | 热土豆选路 |
| route-selection algorithm | 路由选择算法 |
| local preference | 本地偏好 |
| IP-anycast | IP 任播 |
| multi-homed | 多宿 |
| stub network | 端网络 |
| transit traffic | 过境流量 |
| peering | 对等 |
| SDN | 软件定义网络 |
| SDN controller | SDN 控制器 |
| network-control application | 网络控制应用 |
| northbound interface | 北向接口 |
| southbound interface | 南向接口 |
| flow table | 流表 |
| match-plus-action | 匹配加动作 |
| OpenFlow | OpenFlow 协议 |
| ONOS | 开放网络操作系统 |
| Orion | Orion 控制器 |
| network information base (NIB) | 网络信息库 |
| intent-based networking | 基于意图的网络 |
| NFV | 网络功能虚拟化 |
| ICMP | 因特网控制报文协议 |
| Traceroute | 路由追踪程序 |
| SNMP | 简单网络管理协议 |
| MIB | 管理信息库 |
| SMI | 管理信息结构 |
| PDU | 协议数据单元 |
| trap | 陷阱报文 |
| NETCONF | 网络配置协议 |
| YANG | YANG 数据建模语言 |
| managing server | 管理服务器 |
| managed device | 被管设备 |
| network management agent | 网络管理代理 |

# 附录 B　协议与数值速查

| **项目** | **数值** | **说明** |
| --- | --- | --- |
| OSPF | IP 协议号 89 | IP 直接承载，自行实现可靠传输 |
| OSPF 刷新周期 | ≤ 30 分钟 | 即使状态未变也周期性通告 |
| BGP | TCP 端口 179 | eBGP／iBGP 共用同一条连接 |
| OpenFlow | TCP 端口 6653 | 控制器与交换机之间的南向协议 |
| OpenFlow 1.0 | 11 个字段 | 运输层、网络层、链路层首部 |
| ICMP | IP 协议号 1 | 作为 IP 载荷承载 |
| SNMP | UDP 161 / 162 | 161 为代理，162 为 trap 接收 |
| NETCONF | TCP 830 | 基于 TLS 的安全会话 |

| **算法／协议** | **复杂度或规模** | **备注** |
| --- | --- | --- |
| LS（Dijkstra） | $O(\lvert N \rvert {}^{2})$ | 用堆可降到 $O(\lvert N \rvert \log \lvert N \rvert)$ |
| LS 报文数 | $O(\lvert N \rvert \lvert E \rvert)$ | 链路状态泛洪 |
| DV | 迭代收敛 | 可能慢收敛、出现环路 |
| DV 报文 | 邻居之间 | 仅当距离向量变化时才发送 |
| BGP 路由表规模 | > 50 万条 | 前缀加属性 |

| **BGP 路由选择规则（依次施加）** | **依据** |
| --- | --- |
| 1. 本地偏好最高 | 策略 |
| 2. AS-PATH 最短 | AS 跳数 |
| 3. 热土豆（NEXT-HOP 最近） | AS 内代价 |
| 4. BGP 标识符 | 打破平局 |
