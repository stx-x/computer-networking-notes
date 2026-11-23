---
title: 2.6　套接字编程：创建网络应用
outline: [2, 3]
---

# 2.6　套接字编程：创建网络应用

前面各节考察了若干应用层协议，但都是"读"协议。本节换个角度：亲手**写**网络应用。我们将用 Python 编写几个简单的客户-服务器应用，从中体会应用开发者所面对的套接字接口。

在开始之前，回顾 2.1 节的几个基本概念：一个网络应用由一对通过套接字交换报文的进程构成；套接字是应用进程与运输层之间的接口，也是应用开发者所能控制的最底层"把手"。开发者可以选择使用 UDP 还是 TCP，这一选择决定了应用能获得哪些运输层服务，也决定了编写代码的方式。

## 2.6.1　UDP 套接字编程

使用 UDP 时，两个进程之间没有"连接"：发送进程把分组附上目的地址（IP 地址与端口号）后直接送入网络，接收进程从套接字中取出分组，并可从分组中得知源地址。

图 2.22 展示了一个简单的 UDP 客户-服务器应用。服务器进程先创建一个 UDP 套接字并绑定到某个端口（例如 12000），然后循环等待客户请求；客户进程创建 UDP 套接字后，直接向服务器的地址和端口发送报文，并等待应答。

<Figure src="ch02/fig2-22.webp" caption="图 2.22　使用 UDP 的客户-服务器应用" />

服务器端代码如下：

```text
# UDPServer.py
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
```

客户端代码如下：

```text
# UDPClient.py
from socket import *

serverName = 'hostname'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
```

几点说明：`socket(AF*INET, SOCK*DGRAM)` 创建一个 UDP 套接字，`AF*INET` 表示使用 IPv4，`SOCK*DGRAM` 表示这是一个 UDP（数据报）套接字。`sendto()` 的第二个参数是目的地址二元组（主机名或 IP 地址，端口号）。`recvfrom()` 返回报文数据与源地址；注意服务器端从这个源地址中取得了客户的 IP 与端口，从而能够回送应答——这正是第 3 章将讨论的"源端口号充当回信地址"的作用。用 UDP 时，客户与服务器之间没有握手，因此若一个分组丢失，客户可能永远等不到应答。

## 2.6.2　TCP 套接字编程

使用 TCP 时，客户与服务器必须先建立连接，然后才能传输数据。TCP 提供的是**字节流**抽象：没有报文边界，应用看到的是一条连续的字节序列。

图 2.23 与图 2.24 说明了 TCP 客户-服务器应用的结构。注意一个关键区别：TCP 服务器有两个套接字——**欢迎套接字**（welcoming socket）在固定端口上等待连接请求，而 `accept()` 返回的是一个**新**套接字（连接套接字），专门用于与这个特定客户通信。这样，一个服务器进程就能同时服务多个客户。

<Figure src="ch02/fig2-23.webp" caption="图 2.23　TCPServer 进程有两个套接字" />

服务器端代码如下：

```text
# TCPServer.py
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
```

客户端代码如下：

```text
# TCPClient.py
from socket import *

serverName = 'servername'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence.decode())
clientSocket.close()
```

注意 `SOCK_STREAM` 表示这是一个 TCP 套接字；`listen(1)` 的参数指明连接请求队列的最大长度；`connect()` 触发 TCP 三次握手。与 UDP 不同，TCP 客户不需要在每次发送时都附上目的地址——连接已经"记住"了对端。

<Figure src="ch02/fig2-24.webp" caption="图 2.24　使用 TCP 的客户-服务器应用" />

## 2.6.3　QUIC 套接字编程

如 2.2.7 节所述，QUIC 提供了一种"新的运输层"接口：开发者可以像创建 TCP、UDP 套接字那样创建 QUIC 套接字，而 QUIC 子层在内部创建一个 UDP 套接字来完成实际的分组收发。

从编程接口看，QUIC 与 TCP 的相似之处在于它同样提供可靠的、按序的**流**抽象；不同之处在于一条 QUIC 连接上可以有多条相互独立的流，且连接建立更快（通常一个 RTT，甚至 0-RTT）、默认加密。因此，编写 QUIC 应用时，开发者通常先建立一个连接，再在该连接上打开一条或多条流，在流上读写数据——这与 TCP 的"一条连接一条字节流"不同。

本节的三个例子展示了网络应用开发的基本套路：创建套接字、绑定/连接、收发数据、关闭。掌握了这套接口，你就已经可以编写自己的网络应用了。章末的套接字编程作业提供了进一步练习的机会。
