---
title: 第 05 章　网络层：控制平面
outline: false
---

<ChapterHero num="05" title="网络层：控制平面" blurb="LS/DV、OSPF、BGP 与 SDN 控制器" pages="11" />

上一章考察了网络层的**数据平面**——即网络层中"逐路由器"的那部分功能：一个数据报到达路由器后，如何根据首部字段查表、被送到某条出链路。这一章补上网络层的另一半：**控制平面**。它是网络范围的逻辑，不仅控制一个数据报如何沿源主机到目的主机的端到端路径被选路，也控制网络层组件与服务如何被配置和管理。

5.2 节讲传统的路由算法——在图中计算最小代价路径；这些算法是两种广泛部署的因特网路由协议的基础：5.3 节的 OSPF 与 5.4 节的 BGP。OSPF 在一家 ISP 的网络内部运行；BGP 则把因特网中所有网络互联起来，因而常被称为把因特网黏合在一起的"胶水"。传统上，控制平面的路由协议与数据平面的转发功能是一体化地（monolithically）实现在路由器内部的。而**软件定义网络**（SDN）明确地把数据平面与控制平面分开，把控制平面功能实现为一个独立的"控制器"服务——它独立于、且远程于它所控制的路由器的转发组件。SDN 控制器见 5.5 节。

5.6、5.7 节讲管理一个 IP 网络的一些"螺母与螺栓"：ICMP（因特网控制报文协议）与 SNMP（简单网络管理协议）。

## 本章目录

<ChapterLink href="/ch05/5-1.html" title="5.1　导论" />
<ChapterLink href="/ch05/5-2.html" title="5.2　路由算法" />
<ChapterLink href="/ch05/5-3.html" title="5.3　因特网中的自治系统内部选路：OSPF" />
<ChapterLink href="/ch05/5-4.html" title="5.4　ISP 之间的选路：BGP" />
<ChapterLink href="/ch05/5-5.html" title="5.5　SDN 控制平面" />
<ChapterLink href="/ch05/5-6.html" title="5.6　ICMP：因特网控制报文协议" />
<ChapterLink href="/ch05/5-7.html" title="5.7　网络管理与 SNMP、NETCONF/YANG" />
<ChapterLink href="/ch05/5-8.html" title="5.8　小结" />
<ChapterLink href="/ch05/exercises.html" title="复习题" />
<ChapterLink href="/ch05/appendix-a.html" title="附录 A　术语对照表" />
<ChapterLink href="/ch05/appendix-b.html" title="附录 B　协议与数值速查" />
