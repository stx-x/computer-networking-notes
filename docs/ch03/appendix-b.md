---
title: 附录 B　符号与公式速查
outline: [2, 3]
---

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
