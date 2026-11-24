---
title: 附录 B　符号与公式速查
outline: [2, 3]
---

# 附录 B　符号与公式速查

| 术语 | English |
| --- | --- |
| $L$ | [分组长度（比特）] |
| $R$ | [链路传输速率（比特/秒）] |
| $N$ | [源到目的之间的链路数（因而有 $N - 1$ 台路由器）] |
| $d$ | [两台路由器之间的距离（米）] |
| $s$ | [链路的传播速度（米/秒），约 $2 \times 10^{8}$～$3 \times 10^{8}$] |
| $a$ | [分组到达队列的平均速率（分组/秒）] |
| $F$ | [文件长度（比特）] |

| **公式** | **说明** |
| --- | --- |
| $d_{\text{trans}} = \frac{L}{R}$ | 传输时延 |
| $d_{\text{prop}} = \frac{d}{s}$ | 传播时延 |
| $d_{\text{nodal}} = d_{\text{proc}} + d_{\text{queue}} + d_{\text{trans}} + d_{\text{prop}}$ | 节点时延 |
| $d_{\text{端到端}} = N \frac{L}{R}$ | 存储转发端到端时延 |
| $d_{\text{end-end}} = N(d_{\text{proc}} + d_{\text{trans}} + d_{\text{prop}})$ | 端到端时延 |
| $\text{流量强度} = L \frac{a}{R}$ | 排队时延的关键参数，应 $\le 1$ |
| $\text{吞吐量} = \text{min} \{{R_{s}, R_{c} \} \}}$ | 两链路网络的吞吐量 |
| $\text{吞吐量} = \text{min} \{{R_{1}, \cdots, R_{N} \} \}}$ | 多链路网络的吞吐量 |
| $\text{平均吞吐量} = \frac{F}{T}$ | 文件传送的平均吞吐量 |
| $\text{传送时间} \approx \frac{F}{\text{min}} \{{R_{s}, R_{c} \} \}}$ | 大文件传送时间估计 |
