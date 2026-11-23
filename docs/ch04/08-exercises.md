---
title: 本章要点自测
outline: [2, 3]
---

# 本章要点自测

**1.** 转发与选路的区别是什么？它们分别属于哪个平面、在什么时间尺度上运作、通常用什么实现？

**2.** 为什么转发表要在每张线卡上放一份"影子副本"，而不是每个分组都去问选路处理器？

**3.** 什么是最长前缀匹配？为什么必须使用这条规则而不是"第一个匹配"？

**4.** 三种交换技术（经内存、经总线、经交叉开关）各自的带宽瓶颈是什么？交叉开关为什么被称为"无阻塞"的？

**5.** 什么是队头阻塞？它在输入排队交换机中为何会导致吞吐量在负载仅 58% 时就急剧下降？

**6.** 缓冲区大小的经验法则 $B = \text{RTT} \cdot C$ 与 $B = \text{RTT} \cdot \frac{C}{\sqrt{N}}$ 分别适用于什么情形？为什么缓冲并非越多越好？

**7.** 什么是缓冲膨胀？它与"缓冲区越大越好"的直觉冲突在哪里？

**8.** FIFO、优先级排队、轮转、加权公平排队各自的特点是什么？WFQ 如何实现按权重分配带宽？

**9.** IPv4 首部中 TTL、协议、首部校验和三个字段各起什么作用？为什么 IPv6 取消了校验和与分片？

**10.** 如何用"摘下接口"的方法判断一个网络中有几个子网？`223.1.1.0/24` 这个记法表示什么？

**11.** CIDR 与分类编址的区别是什么？路由聚合如何减少骨干路由表规模？为什么"更具体的路由"需要最长前缀匹配来配合？

**12.** DHCP 的四个步骤是什么？为什么客户最初只能用广播？

**13.** NAT 如何把内部地址映射到外部地址？它带来了哪些争议？

**14.** IPv6 的 128 比特地址、40 字节定长首部、取消分片与校验和分别带来什么好处？双栈与隧道如何帮助过渡？

**15.** "匹配加动作"抽象是什么？OpenFlow 的匹配字段与动作各有哪些？中间盒与 SDN 有什么关系？

**16.** IP 沙漏模型说明了什么？为什么"最小的承诺"反而带来"最大的通用性"？

**17.** 端到端论点的核心主张是什么？它能解释因特网的哪些设计选择？又有哪些"例外"？

# 附录 A　术语对照表

| 术语 | English | 术语 | English |
| --- | --- | --- | --- |
| 数据平面 | data plane | 控制平面 | control plane |
| 转发 | forwarding | 选路 | routing |
| 转发表 | forwarding table | 流表 | flow table |
| 输入端口 | input port | 输出端口 | output port |
| 交换结构 | switching fabric | 交叉开关 | crossbar switch |
| 选路处理器 | routing processor | 线卡 | line card |
| 最长前缀匹配 | longest prefix match | 三态内容寻址存储器 | TCAM |
| 队头阻塞 | HOL blocking | 输入排队 | input queueing |
| 弃尾 | drop-tail | 主动队列管理 | AQM |
| 随机早期检测 | RED | 缓冲膨胀 | bufferbloat |
| 先进先出 | FIFO | 优先级排队 | priority queueing |
| 轮转 | round-robin | 加权公平排队 | WFQ |
| 数据报 | datagram | 接口 | interface |
| 点分十进制 | dotted-decimal | 子网 | subnet |
| 子网掩码 | subnet mask | 无类域间选路 | CIDR |
| 路由聚合 | route aggregation | 动态主机配置 | DHCP |
| 网络地址转换 | NAT | 专用地址 | private address |
| 任播 | anycast | 流标签 | flow label |
| 双栈 | dual stack | 隧道 | tunneling |
| 广义转发 | generalized forwarding | 匹配加动作 | match-plus-action |
| 软件定义网络 | SDN | 中间盒 | middlebox |
| 窄腰沙漏 | narrow waist | 端到端论点 | end-to-end argument |

# 附录 B　常用数值与字段速查

| **项目** | **数值 / 说明** |
| --- | --- |
| IPv4 地址长度 | 32 比特（4 字节） |
| IPv4 首部长度 | 20 字节（无选项）；最长 60 字节 |
| IPv4 数据报最大长度 | 65 535 字节 |
| IPv6 地址长度 | 128 比特（16 字节） |
| IPv6 首部长度 | 固定 40 字节 |
| 协议号 6 / 17 | TCP / UDP |
| 专用地址段（RFC 1918） | `10.0.0.0/8`、`172.16.0.0/12`、`192.168.0.0/16` |
| DHCP 端口 | 服务器 67，客户 68 |
| 缓冲规模经验值 | $B = \text{RTT} \cdot C$；大量流时 $B = \text{RTT} \cdot \frac{C}{\sqrt{N}}$ |
| HOL 阻塞下的吞吐拐点 | 输入负载达 58% 时开始急剧下降 |
