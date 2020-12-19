import socket as sock
import time


opens = []
common = [20,21,22,23,25,50,51,53,67,68,69,80,110,119,123,135,136,137,139,139]

for x in range(1,):
    s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
    rst = s.connect_ex(('192.168.0.1', x))
    if rst == 0:
        opens.append(x)
        print(f'open: {x}')
    s.close()