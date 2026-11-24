---
title: 第 03 章　运输层
outline: false
---

<ChapterHero num="03" title="运输层" blurb="rdt 状态机、TCP 拥塞控制与 QUIC" pages="12" />

运输层位于应用层与网络层之间，是分层网络体系结构中承上启下的核心一环。它的关键职责，是**直接为运行在不同主机上的应用进程提供通信服务**。本章沿用的教学思路是：在"运输层原理"与"这些原理在现有协议中的实现"之间来回切换；一如既往，重点放在因特网协议上，尤其是 TCP 与 UDP 这两个运输层协议。

我们首先讨论运输层与网络层之间的关系，为考察运输层的第一个关键功能作铺垫——把网络层提供的**主机到主机**交付服务，扩展为运行在端系统上的**进程到进程**交付服务。这一功能将在因特网的无连接运输协议 UDP 中得到具体体现。

随后我们回到原理，直面计算机网络中最基本的问题之一：两个实体如何在可能丢失和损坏数据的介质上**可靠地**通信？我们将沿着由简到繁（也越来越接近真实）的场景，逐步搭建起运输协议解决该问题所用的整套技术，然后再看这些原理如何体现在因特网的面向连接运输协议 TCP 之中。

接下来是第二个根本性问题：如何控制运输层实体的发送速率，以避免网络内部出现拥塞，或在拥塞发生后从中恢复。我们会分析拥塞的成因与代价，介绍常用的拥塞控制技术；在建立起对拥塞控制问题的扎实理解之后，再考察 TCP 各种"变体"所采用的不同拥塞控制方案。

<AsideCard title="本章脉络">

3.1 运输层做什么 → 3.2 进程到进程的交付（复用/分解）→ 3.3 最简的运输协议 UDP → 3.4 可靠数据传输的原理（rdt 系列）→ 3.5 TCP 如何实现这些原理 → 3.6 拥塞控制的原理 → 3.7 TCP 的拥塞控制 → 3.8 运输层功能的演进（QUIC）。

</AsideCard>

## 本章目录

<ChapterLink href="/ch03/3-1.html" title="3.1　引言与运输层服务" />
<ChapterLink href="/ch03/3-2.html" title="3.2　多路复用与多路分解" />
<ChapterLink href="/ch03/3-3.html" title="3.3　无连接运输：UDP" />
<ChapterLink href="/ch03/3-4.html" title="3.4　可靠数据传输原理" />
<ChapterLink href="/ch03/3-5.html" title="3.5　面向连接的运输：TCP" />
<ChapterLink href="/ch03/3-6.html" title="3.6　拥塞控制原理" />
<ChapterLink href="/ch03/3-7.html" title="3.7　TCP 拥塞控制" />
<ChapterLink href="/ch03/3-8.html" title="3.8　运输层功能的演进" />
<ChapterLink href="/ch03/3-9.html" title="3.9　小结" />
<ChapterLink href="/ch03/exercises.html" title="习题" />
<ChapterLink href="/ch03/appendix-a.html" title="附录 A　术语对照表" />
<ChapterLink href="/ch03/appendix-b.html" title="附录 B　符号与公式速查" />
