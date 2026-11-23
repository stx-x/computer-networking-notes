---
title: 2.7　小结
outline: [2, 3]
---

# 2.7　小结

本章从应用层出发，开始自顶向下地考察计算机网络。我们首先建立了网络应用的基本原理：应用体系结构（客户-服务器与 P2P）、进程与套接字、可供应用使用的运输服务（可靠数据传输、吞吐量、定时、安全性），以及因特网实际提供的两种运输服务（TCP 与 UDP）。随后详细考察了四类重要应用：Web（HTTP）、电子邮件（SMTP、POP3、IMAP）、目录服务（DNS）和流式视频（DASH 与 CDN）。最后，通过套接字编程，我们看到了应用开发者眼中的运输层。

本章的几个要点值得反复回味：

::: tip 要点

+ **应用层协议只在端系统中实现。** 网络核心设备不运行应用层协议，这一设计把复杂性推向边缘，也使得新应用的部署无需改动网络核心——这正是因特网能够迅速催生大量新应用的根本原因。
  + **应用体系结构与网络体系结构是两回事。** 前者由开发者设计（客户-服务器、P2P），后者由协议栈规定（五层模型）。
  + **选择 TCP 还是 UDP，本质上是在选择服务模型。** TCP 提供可靠、有序、带拥塞控制的字节流；UDP 提供最小化的数据报服务，把控制权交给应用。实时应用往往偏好 UDP，可靠应用偏好 TCP，而 QUIC 则试图兼得二者。
  + **HTTP 是无状态的，Cookie 在无状态之上构建了状态。** 这一组合既保持了服务器的简单与可扩展，又满足了识别用户的需求，同时也带来了隐私争议。
  + **缓存是 Web 性能的关键。** 浏览器缓存与条件 GET（`If-Modified-Since`、`304 Not Modified`）使得大量请求无需真正传输对象。
  + **DNS 是分布式数据库的经典范例。** 层次化的服务器结构、递归与迭代查询、缓存机制，共同支撑了全球规模的名称解析。
  + **视频是当今因特网流量的主体。** DASH 解决带宽异构，CDN 解决时延与骨干带宽，二者共同构成现代流媒体的基础设施。

:::

## 本章要点自测

**1.** 客户-服务器体系结构与 P2P 体系结构各有什么优缺点？为什么今天大多数应用仍采用客户-服务器结构？

**2.** 一个进程要向另一台主机上的进程发送报文，需要知道哪两项信息？各自的作用是什么？

**3.** TCP 与 UDP 各提供哪些服务？为什么 DNS 通常使用 UDP，而 HTTP/1.1 使用 TCP？

**4.** 为什么说 HTTP 是无状态协议？Cookie 的四个组成部分是什么？它如何在无状态协议之上实现用户会话？

**5.** 非持续连接与持续连接的区别是什么？在非持续连接下请求一个含 10 个对象的网页，大约需要多少个 RTT？

**6.** 条件 GET 的作用是什么？服务器返回 304 状态码意味着什么？

**7.** HTTP/2 的成帧机制如何缓解队头阻塞？为什么它无法从根本上消除 HOL 阻塞？

**8.** QUIC 为什么被称为"应用层的子层"而不是第三个运输层协议？它相对 TCP+TLS 有哪些优势？

**9.** SMTP、POP3、IMAP 各自的作用是什么？为什么 SMTP 被称为"推"协议而 HTTP 是"拉"协议？

**10.** DNS 的层次结构包括哪几类服务器？递归查询与迭代查询有何区别？

**11.** DNS 资源记录的四种主要类型（A、NS、CNAME、MX）各自的作用是什么？

**12.** DASH 如何适应不同用户的带宽？CDN 的"拉"式与"推"式分发各适合什么场景？

# 附录 A　术语对照表

| 术语 | English | 术语 | English |
| --- | --- | --- | --- |
| 应用层 | application layer | 应用体系结构 | application architecture |
| 客户-服务器 | client-server | 对等 | peer-to-peer (P2P) |
| 进程 | process | 套接字 | socket |
| 用户代理 | user agent | 邮件服务器 | mail server |
| 端口号 | port number | IP 地址 | IP address |
| 可靠数据传输 | reliable data transfer | 吞吐量 | throughput |
| 带宽敏感 | bandwidth-sensitive | 弹性应用 | elastic application |
| 无连接 | connectionless | 面向连接 | connection-oriented |
| 超文本传输协议 | HTTP | 请求行 | request line |
| 首部行 | header line | 状态码 | status code |
| 实体主体 | entity body | 持续连接 | persistent connection |
| 非持续连接 | non-persistent connection | 往返时间 | RTT |
| Cookie | cookie | 浏览器缓存 | browser caching |
| 条件 GET | conditional GET | 代理缓存 | proxy cache |
| 成帧子层 | framing sub-layer | 队头阻塞 | HOL blocking |
| 服务器推送 | server push | 多路复用 | multiplexing |
| 简单邮件传输协议 | SMTP | 邮件访问协议 | mail access protocol |
| 域名系统 | DNS | 根服务器 | root server |
| 顶级域服务器 | TLD server | 权威服务器 | authoritative server |
| 本地 DNS 服务器 | local DNS server | 递归查询 | recursive query |
| 迭代查询 | iterative query | 资源记录 | resource record |
| 规范主机名 | canonical hostname | 负载分配 | load distribution |
| 内容分发网 | CDN | 动态自适应流 | DASH |
| 告示文件 | manifest file | 用户生成内容 | UGC |
| 字节流 | byte stream | 欢迎套接字 | welcoming socket |

# 附录 B　常用端口与报文速查

| **协议** | **用途** | **默认端口** |
| --- | --- | --- |
| HTTP | Web 文档传输 | 80 |
| HTTP/3 | 基于 QUIC 的 Web 传输 | 443（UDP） |
| HTTPS | 基于 TLS 的 HTTP | 443 |
| SMTP | 邮件发送 | 25 |
| POP3 | 邮件读取（下载式） | 110 |
| IMAP | 邮件读取（服务器端维护） | 143 |
| DNS | 名称解析 | 53 |
| FTP | 文件传输（控制连接） | 21 |
| SSH | 安全远程登录 | 22 |
| Telnet | 远程登录（明文） | 23 |

| **关系式** | **说明** |
| --- | --- |
| $\text{HTTP 响应时间} \approx 2 \text{RTT} + \text{传输时间}$ | 非持续连接下请求一个对象 |
| $\text{并行连接数} \le 6$ | HTTP/1.1 浏览器的典型做法 |
| $\text{QUIC 建立时间} \approx 1 \text{RTT}$ | 首次连接（0-RTT 用于恢复） |
| $(\text{Name}, \text{Value}, \text{Type}, \text{TTL})$ | DNS 资源记录四元组 |
