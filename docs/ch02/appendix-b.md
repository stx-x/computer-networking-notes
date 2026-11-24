---
title: 附录 B　常用端口与报文速查
outline: [2, 3]
---

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
