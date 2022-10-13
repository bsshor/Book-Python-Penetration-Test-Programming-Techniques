# 使用scapy实现使用tcp检测主机状态

import sys
if len(sys.argv) != 3:
    print(" Usage: tcpPing < IP >\n eg: arpPing2 192.168.1.1 80")
    sys .exit(1)

from scapy.all import sr, IP, TCP   # type: ignore
# ） 此处 flags 设置为“S”，也就 SYN。 另外，TCP 并没有目标地址和源地址，所以需要在 IP 层进行设置
ans, unans = sr(IP(dst=sys.argv[1]) / TCP(dport=int(sys.argv[2]), flags="S"))
for snd, rcv in ans:
    print(rcv.sprintf("%IP.src% is alive"))  # type: ignore
