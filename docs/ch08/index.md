---
title: 第 08 章　计算机网络安全
outline: false
---

<ChapterHero num="08" title="计算机网络安全" blurb="密码学、TLS 1.3、IPsec 与防火墙" pages="13" />

早在 1.6 节，我们描述过几类较为常见且危害较大的因特网攻击，包括恶意软件攻击、拒绝服务、嗅探、源伪装，以及报文的修改与删除。此后我们学到了大量关于计算机网络的知识，但还没有考察如何保护网络免遭这些攻击。如今，带着新获得的计算机网络与因特网协议专长，我们深入研习安全通信——特别是计算机网络如何防御那些坏家伙。

先介绍 Alice 与 Bob：两人想通信，并且希望"安全地"通信。既然这是一本网络教材，我们应当说明：Alice 与 Bob 可以是两台想安全交换路由表的路由器，可以是两个想建立安全运输连接的客户端与服务器，也可以是两个想交换安全电子邮件的应用——这些都是本章后面要考察的案例。Alice 与 Bob 是安全界众所周知的固定角色，也许因为他们的名字比"想与实体 B 安全通信的实体 A"更有趣。爱情、战时通信与商业交易是人们常引用的安全通信的人类需求；相比后两者，我们更喜欢第一个，于是乐于用 Alice 与 Bob 作为发送方与接收方，并想象他们处于第一种场景。

我们说 Alice 与 Bob 想"安全地"通信，但这究竟意味着什么？我们将会看到，安全（就像爱情）是件多姿多彩的事，也就是说，安全有许多侧面。当然，Alice 与 Bob 希望他们通信的内容对窃听者保密；他们大概也希望确保自己在与对方通信时，对方确实是对方，而且如果通信被窃听者篡改，这种篡改能被检测出来。本章第一部分讲支撑加密通信、鉴别通信对方以及保证报文完整性的基础密码学技术。

本章第二部分考察如何用基础密码学原理构造安全的网络协议。我们再次采取自顶向下的方法，考察（上面四个）每一层中的安全协议，从应用层开始：如何保护电子邮件、如何保护 TCP 连接、如何在网络层提供"全覆盖"安全，以及如何保护无线局域网。本章第三部分讨论**运行安全**（operational security），即保护组织网络免遭攻击；我们将仔细考察防火墙与入侵检测系统如何增强组织网络的安全性。

## 本章目录

<ChapterLink href="/ch08/8-1.html" title="8.1　什么是网络安全？" />
<ChapterLink href="/ch08/8-2.html" title="8.2　密码学原理" />
<ChapterLink href="/ch08/8-3.html" title="8.3　报文完整性与数字签名" />
<ChapterLink href="/ch08/8-4.html" title="8.4　端点鉴别" />
<ChapterLink href="/ch08/8-5.html" title="8.5　保护电子邮件" />
<ChapterLink href="/ch08/8-6.html" title="8.6　保护 TCP 与 HTTP 连接：TLS" />
<ChapterLink href="/ch08/8-7.html" title="8.7　网络层安全：IPsec 与虚拟专用网" />
<ChapterLink href="/ch08/8-8.html" title="8.8　保护无线局域网与 4G/5G 蜂窝网" />
<ChapterLink href="/ch08/8-9.html" title="8.9　运行安全：防火墙与入侵检测系统" />
<ChapterLink href="/ch08/8-10.html" title="8.10　小结" />
<ChapterLink href="/ch08/exercises.html" title="复习题" />
<ChapterLink href="/ch08/appendix-a.html" title="附录 A　术语对照表" />
<ChapterLink href="/ch08/appendix-b.html" title="附录 B　数值与公式速查" />
