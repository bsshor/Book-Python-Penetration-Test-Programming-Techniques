# 使用scapy实现使用icmp检测主机状态

import sys
if len(sys. argv) != 2:
    print("Usage : icmpPing <IP>\n eg: icmpPing 192.168.1.1 ")
    sys . exit(1)
from scapy . all import sr, IP, ICMP  # type: ignore
ans, unans = sr(IP(dst=sys . argv[1])/ICMP())
for snd, rcv in ans:
    print(rcv.sprintf("%IP.src% is alive"))  # type: ignore
