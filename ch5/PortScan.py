import sys
from turtle import ScrolledCanvas
from scapy.all import *
if len(sys.argv) != 3:
    print("Usage : PortScan <IP>\n eg : PortScan 192.168.1.1 80 ")
    sys.exit(1)
dst_ip = sys.argv[1]
src_port = RandShort()  # 随机使用一个端口
dst_port = int(sys.argv[2])
packet = IP(dst=dst_ip)/TCP(sport=src_port, dport=dst_port,
                            flags="S")  # flags 参数设置为“S”，表明这是一个 SYN 请求数据包
resp = sr1(packet, timeout=10)
if (str(type(resp)) == "<type NoneType>"):  # 如果此时 resp 的值为空，就表示没有收到来自目标的回应
    print("The port %s is Closed" % dst_port)

# 当收到了回应的数据包之后，需要判断一下这个数据包是“ SYN+ACK ”类型，还是“ RST ”类型的
elif (resp.haslayer(TCP)):  # 判断一个数据包是否使用了 TCP 就可以使用 haslayer(TCP)来判断
    # 使用 getlayer ( TCP ）来读取其中某个字段的内容
    if (resp.getlayer(TCP).flags == 0x12):  # 0x12 就是 "SYN+ACK"
        send_rst = sr(IP(dst=dst_ip) / TCP(sport=src_port,
                      dport=dst_port, flags="AR"), timeout=10)  # flags 参数设置为“AR”，表明这是一个 ACK 响应数据包
        print("The port %s is Open" % dst_port)
    elif (resp.getlayer(TCP).flags == 0x14):  # 0x14 就是 "RST"
        print("The port %s is Closed" % dst_port)
