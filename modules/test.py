import netifaces as nf

def mac(ip):
    print('st')
    print(nf.interfaces())
    for i in nf.interfaces():
        addr = nf.ifaddresses(i)
        try:
            if_mac = addr[nf.AF_LINK][0]['addr']
            if_ip = addr[nf.AF_INET][0]['addr']
            print(if_ip)
        except IndexError and KeyError:
            if_mac = if_ip = None
        if if_ip == ip:
            print(if_mac)

mac('192.168.0.1')