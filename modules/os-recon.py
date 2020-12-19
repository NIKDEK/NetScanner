import nmap3
import platform
import socket
import eel


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('192.168.0.10',20))

s.accept()

nmap = nmap3.Nmap()
#rst = nmap.scan_top_ports('192.168.0.1/24')

def os_scan(address):
    rs = nmap.nmap_version_detection(address)
    return rs

#k = str(rst.keys())[11:-2].split("'")
#ls = []

#for x in k:
#    if len(x) > 2:
#        ls.append(x)

#for x in ls:
#    if x == 'runtime':
#        break
#    print('\n',x,'\n')
#    for y in rst[x]:
#        print(f"    {y['portid']}: {y['state']}")

print(os_scan('192.168.0.'))