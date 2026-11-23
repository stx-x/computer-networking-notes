---
title: 8.10　小结
outline: [2, 3]
---

# 8.10　小结

本章考察了我们的秘密恋人 Bob 与 Alice 可以用来安全通信的各种机制。我们看到，Bob 与 Alice 关心**机密性**（只有他们两人能理解所传报文的内容）、**端点鉴别**（他们确信自己在与对方说话）与**报文完整性**（他们确信报文在途中未被改动）。当然，安全通信的需求并不限于秘密恋人。事实上，8.5 至 8.8 节表明，安全性可以用在网络体系结构的各个层次上，以抵御手头握有大量可能攻击手段的坏人。

本章前半部分给出了安全通信背后的各种原理。8.2 节讨论了加解密数据的密码学技术，包括对称密钥密码学与公钥密码学，并以 DES 与 RSA 作为当今网络所用两大类密码学技术的具体案例加以考察。

8.3 节考察了提供报文完整性的两种途径：报文鉴别码（MAC）与数字签名。这两种途径有许多相似之处：都用密码散列函数，都能让我们验证报文的来源以及报文本身的完整性。一个重要差别是 MAC 不依赖加密，而数字签名需要一套公钥基础设施。这两种技术在实践中的应用都很广泛，8.5 至 8.8 节已经看到。此外，数字签名被用来创建数字证书，而数字证书对验证公钥的有效性至关重要。8.4 节考察了端点鉴别，并引入 nonce 来防范重放攻击。

8.5 至 8.8 节考察了若干在实践中被广泛使用的安全网络协议。我们看到，对称密钥密码学是 PGP、TLS、IPsec 与无线安全的核心；公钥密码学对 PGP 与 TLS 都至关重要；PGP 用数字签名提供报文完整性，而 TLS 与 IPsec 用 MAC。我们还探讨了无线网络的安全性，包括 WiFi 网络与 4G/5G 蜂窝网络。既然已经理解了密码学的基本原理，又研究了这些原理实际如何被使用，你现在就有能力设计自己的安全网络协议了！

有了 8.2 至 8.8 节的技术，Bob 与 Alice 就能安全通信了。但机密性只是网络安全图景的一小部分。如 8.9 节所学，网络安全的焦点正日益转向保护网络基础设施，以抵御坏人的潜在猛攻。因此本章后半部分讨论了防火墙与 IDS 系统，它们检查进出组织网络的分组。

# 复习题

par(spacing: 0.56em)

8.1–8.2 节

**R1.** 报文机密性与报文完整性有何区别？可以有机密性而无完整性吗？可以有完整性而无机密性吗？说明理由。

**R2.** 因特网实体（路由器、交换机、DNS 服务器、Web 服务器、用户端系统等等）常常需要安全通信。给出三对具体的、可能想安全通信的因特网实体。

**R3.** 从服务角度看，对称密钥系统与公钥系统的一个重要区别是什么？

**R4.** 假设入侵者手里有一条加密报文以及该报文的解密版本。他能实施唯密文攻击、已知明文攻击还是选择明文攻击？

**R5.** 考虑一个 8 比特块密码。该密码有多少种可能的输入块？有多少种可能的映射？若把每种映射视为一把密钥，则该密码有多少把可能的密钥？

**R6.** 假设 $N$ 个人想用对称密钥加密与其余 $N - 1$ 个人分别通信。任意两人 $i$ 与 $j$ 之间的所有通信对这群 $N$ 人中的其他所有人都可见，而这群人中其他任何人都不应能解码他们的通信。整个系统需要多少把密钥？现在假设改用公钥加密，此时需要多少把密钥？

**R7.** 假设 $n = 10 \, 000$、$a = 10 \, 023$、$b = 10 \, 004$。用一条模运算恒等式心算 $(a \cdot b) \bmod n$。

**R8.** 假设你想通过加密"与报文对应的十进制数"来加密报文 10101111。该十进制数是多少？

8.3–8.4 节

**R9.** 与检验和（例如因特网检验和）相比，散列在哪些方面提供了更好的报文完整性检查？

**R10.** 你能"解密"报文的散列以得到原始报文吗？解释你的回答。

**R11.** 考虑 MAC 算法（图 8.9）的一种变体：发送方发送 $(m, H(m) + s)$，其中 $H(m) + s$ 是 $H(m)$ 与 $s$ 的拼接。这种变体有漏洞吗？为什么有或为什么没有？

**R12.** 一份经签名的文档"可验证且不可伪造"是什么意思？

**R13.** 与"用公钥加密整条报文"相比，"用公钥加密报文散列"在哪些方面提供了更好的数字签名？

**R14.** 假设 certifier.com 为 foo.com 签发了一份证书。通常，整份证书会用 certifier.com 的公钥加密。对还是错？

**R15.** 假设 Alice 有一条报文，准备发给任何索要的人。成千上万的人都想得到 Alice 的报文，但每人都想确信报文的完整性。在此语境下，你认为基于 MAC 还是基于数字签名的完整性方案更合适？为什么？

**R16.** 在端点鉴别协议中，nonce 的作用是什么？

**R17.** 说一个 nonce 是"一生只用一次"的值，是什么意思？在谁的一生中？

**R18.** 基于 HMAC 的报文完整性方案容易遭受重放攻击吗？若容易，如何把 nonce 纳入该方案以消除这种易受攻击性？

8.5–8.8 节

**R19.** 假设 Bob 收到 Alice 发来的一条 PGP 报文。Bob 如何确知这条报文是 Alice（而不是比如 Trudy）创建的？PGP 用 MAC 提供报文完整性吗？

**R20.** TLS 记录中有一个用于存放 TLS 序号的字段。对还是错？

**R21.** TLS 握手中那些随机 nonce 的作用是什么？

**R22.** 假设某个 TLS 会话采用带 CBC 的块密码。对还是错：服务器把 IV 以明文形式发给客户。

**R23.** 假设 Bob 向冒充 Alice 的 Trudy 发起一条 TCP 连接。在握手期间，Trudy 把 Alice 的证书发给了 Bob。在 TLS 握手算法的哪一步，Bob 会发现他并没有在与 Alice 通信？

**R24.** 考虑用 IPsec 从主机 A 向主机 B 发送一个分组流。通常，流中每发送一个分组都会建立一个新的 SA。对还是错？

**R25.** 假设 TCP 运行在图 8.28 中总部与分支机构之间的 IPsec 之上。若 TCP 重传同一个分组，则 R1 发出的两个相应分组在 ESP 首部中会有相同的序号。对还是错？

**R26.** IKE SA 与 IPsec SA 是同一回事。对还是错？

**R27.** 考虑 802.11 的 WEP。假设数据是 10101100、密钥流是 11110000，所得密文是什么？

8.9 节

**R28.** 状态分组过滤器维护两个数据结构。说出它们的名称并简要描述其作用。

**R29.** 考虑一台传统（无状态）分组过滤器。这台分组过滤器可以依据 TCP 标志比特以及其他首部字段来过滤分组。对还是错？

**R30.** 在传统分组过滤器中，每个接口可以有自己的访问控制列表。对还是错？

**R31.** 应用网关为什么必须与路由器过滤器配合工作才有效？

**R32.** 基于特征的 IDS 与 IPS 会检查 TCP 与 UDP 报文段的载荷内部。对还是错？

par(spacing: 0.8em)

# 附录 A　术语对照表

| 英文 | 中文 |
| --- | --- |
| network security | 网络安全 |
| confidentiality | 机密性 |
| message integrity | 报文完整性 |
| end-point authentication | 端点鉴别 |
| non-repudiation | 不可否认性 |
| plaintext / ciphertext | 明文／密文 |
| cipher | 密码（加密方法） |
| key | 密钥 |
| symmetric key cryptography | 对称密钥密码学 |
| public key cryptography | 公钥密码学 |
| Caesar cipher | 凯撒密码 |
| monoalphabetic cipher | 单表替换密码 |
| polyalphabetic encryption | 多表替换加密 |
| ciphertext-only attack | 唯密文攻击 |
| known-plaintext attack | 已知明文攻击 |
| chosen-plaintext attack | 选择明文攻击 |
| block cipher | 块密码 |
| DES / 3DES / AES | 数据加密标准／三重 DES／高级加密标准 |
| CBC | 密码块链接 |
| initialization vector (IV) | 初始化向量 |
| RSA | RSA 公钥算法 |
| session key | 会话密钥 |
| Diffie-Hellman key agreement | Diffie-Hellman 密钥协商 |
| cryptographic hash function | 密码散列函数 |
| message digest | 报文摘要 |
| MD5 / SHA-1 | MD5／SHA-1 散列算法 |
| message authentication code (MAC) | 报文鉴别码 |
| authentication key | 鉴别密钥 |
| HMAC | 基于散列的消息鉴别码 |
| digital signature | 数字签名 |
| public key infrastructure (PKI) | 公钥基础设施 |
| certification authority (CA) | 认证机构 |
| certificate | 证书 |
| X.509 | X.509 证书标准 |
| distinguished name (DN) | 可分辨名称 |
| IP spoofing | IP 欺骗 |
| playback attack | 重放攻击 |
| nonce | 一次性随机数 |
| authentication protocol (ap) | 鉴别协议 |
| web of trust | 信任网 |
| key-signing party | 密钥签名会 |
| PGP / OpenPGP | PGP／OpenPGP 安全邮件 |
| TLS | 运输层安全协议 |
| SSL | 安全套接字层 |
| master secret (MS) | 主秘密 |
| encrypted master secret (EMS) | 加密主秘密 |
| cipher suite | 密码套件 |
| AEAD | 带关联数据的认证加密 |
| ephemeral key | 临时密钥 |
| connection replay attack | 连接重放攻击 |
| truncation attack | 截断攻击 |
| IPsec | IP 安全协议 |
| AH | 鉴别首部协议 |
| ESP | 封装安全载荷协议 |
| security association (SA) | 安全关联 |
| security parameter index (SPI) | 安全参数索引 |
| security association database (SAD) | 安全关联数据库 |
| security policy database (SPD) | 安全策略数据库 |
| tunnel mode / transport mode | 隧道模式／运输模式 |
| ESP trailer | ESP 尾部 |
| IKE | 因特网密钥交换 |
| virtual private network (VPN) | 虚拟专用网 |
| WPA3-Personal | Wi-Fi 保护接入 3 个人版 |
| WPA3-Enterprise | Wi-Fi 保护接入 3 企业版 |
| SAE | 对等实体同时鉴别 |
| Dragonfly key exchange | Dragonfly 密钥交换 |
| pairwise master key (PMK) | 成对主密钥 |
| 802.1X | 802.1X 接入控制标准 |
| EAP | 可扩展鉴别协议 |
| EAPoL | 局域网上的 EAP |
| EAP-TTLS | 隧道化 TLS 的 EAP |
| RADIUS / DIAMETER | RADIUS／DIAMETER 鉴别协议 |
| EAP-AKA' | EAP 鉴别与密钥协商（5G） |
| SEAF / AUSF / UDM | 安全锚功能／鉴别服务器功能／统一数据管理 |
| authentication vector (AV) | 鉴别向量 |
| XRES | 期望响应 |
| anchor key | 锚密钥 |
| firewall | 防火墙 |
| packet filter | 分组过滤器 |
| stateful filter | 状态过滤器 |
| connection table | 连接表 |
| access control list (ACL) | 访问控制列表 |
| application gateway | 应用网关 |
| demilitarized zone (DMZ) | 非军事区 |
| deep packet inspection | 深度分组检查 |
| intrusion detection system (IDS) | 入侵检测系统 |
| intrusion prevention system (IPS) | 入侵防御系统 |
| signature-based IDS | 基于特征的 IDS |
| anomaly-based IDS | 基于异常的 IDS |
| Snort | Snort 开源 IDS |
| TOR | TOR 匿名网络 |

# 附录 B　数值与公式速查

par(first-line-indent: 0em, leading: 1.45em)

下表列出本章的密钥长度、算法参数与常用公式，便于答题时速查。

| **项目** | **数值／公式** | **说明** |
| --- | --- | --- |
| DES 块长 / 密钥 | 64 / 56 比特 | 名义 64 比特含校验位 |
| AES 块长 / 密钥 | 128 / 128–256 比特 | 取代 DES 的现行标准 |
| MD5 / SHA-1 输出 | 128 / 160 比特 | SHA-1 为美国联邦标准 |
| RSA 模长 / DH 参数 | $\ge 2 \, 048$ 比特 | 分解 / 离散对数困难 |
| RSA 加解密 | $c = m^{e} \bmod n$ | $m = c^{d} \bmod n$，$n = p q$ |
| DH 公开值 | $K_{A}^{+} = g^{S_{A}} \bmod p$ | 共享秘密 $(K_{B}^{+})^{S_{A}}$ |
| MAC 定义 | $H(s + m)$ | $s$ 为鉴别密钥 |
| 数字签名 | $K_{B}^{-}(H(m))$ | 先取散列再签，省算力 |
| TLS 会话密钥 | 4 把 | $E_{B}, M_{B}, E_{A}, M_{A}$ |
| TLS 1.3 握手 | 1 个 RTT | QUIC 下可为 0 |
| IPsec 协议号 | 50（ESP）/ 51（AH） | 外层 IPv4 首部字段 |
| IPsec SA 数 | $2(n + 2)$ | 总部 + 分支 + $n$ 台 |
| SPI / ESP 序号 | 均 32 比特 | 标识 SA / 防重放 |
| WEP 密文 | 数据 $\oplus$ 密钥流 | 见复习题 R27 |
| 802.11 信道 | 11 个（2.4 GHz） | 非重叠仅 {1, 6, 11} |

par(first-line-indent: 0em, leading: 1.45em)

最后把几类完整性／鉴别手段并列对照。选型时先问：双方是否已共享密钥？是否需要向第三方证明？

| **手段** | **需要什么** | **提供什么** | **典型用处** |
| --- | --- | --- | --- |
| 检验和 | 无 | 差错检测 | IP/TCP/UDP |
| CRC | 无 | 突发差错检测 | 链路层帧尾 |
| MAC / HMAC | 共享密钥 | 完整性 + 来源 | OSPF、TLS 等 |
| 数字签名 | 公私钥 + PKI | 完整 + 来源 + 不可否认 | PGP、证书 |
| AEAD | 会话密钥 | 机密 + 完整 | TLS 1.3 数据 |
