import nmap3
import socket
import eel
import threading

global canl
canl = False

def start():
    eel.init('www')
    eel.start('index.html', mode='msedge') 

hosts = []

nmap = nmap3.NmapScanTechniques()    
nmp = nmap3.Nmap()
#db_port = open('fl.txt', 'r')

@eel.expose
def scan(ADDRESS):
    hosts = []
    print('Scanning.......\n')
    rst = nmap.nmap_ping_scan(ADDRESS)
    results = nmap.scan_top_ports(ADDRESS)
    for x in rst:
        global check
        global mac 
        try:
            mac =  x['addresses'][1]['addr']
            check = True
        except IndexError:
            check = False
            pass
        if canl == True:
            break
        #    print(x)
        #print(x)
        print(x['addresses'][0]['addr'])
        mc = mac if check else 'Not Found'
    #    print(x['addresses'][0]['addr'], mc)
        
        hosts.append([x['addresses'][0]['addr'], mc])
    #db_port = db_port.read()
   # ports = db_port.split('\n')
    #print(hosts)
    discovered = []
    for x in hosts:
        opn = []
        try:
            for i in results[x[0]]:
                print(i)
                if i['state'] == 'open':
                    opn.append(f"{i['portid']}:{i['service']['name']}")
        except KeyError:
            pass
        discovered.append({
            'ip': x[0],
            'mac': x[1],
            'ports': opn
            })
    print('Done')
    eel.prnt(discovered)

#print(discovered)
#if len(hosts) > 0:
#    print(hosts)
#    for addr in hosts:
#        print(addr)
#        print(addr[0], addr[1])
#        for x in ports:
#            INFO = (addr[0], int(x))
#            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#            status_tcp = s.connect_ex(INFO)
#            s.close()
#            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#            status_udp = s.connect_ex(INFO)
#            s.close()
#            val_tcp = status_tcp == 0
#            tcp = 'TCP: open' if val_tcp else 'TCP: closed'
#            val_udp = status_tcp == 0
#            udp = 'UDP: open' if val_udp else 'UDP: closed'
#            print(f'    {x}: {tcp}')# {udp}')

@eel.expose
def ssockets(ip, lbid):
    print('Scanning Sockets')
    open_ports = []
    ports = [20,21,22,23,25,53,80,110,119,123,143,161,194,443,3389,989,389,135,136,137,138,139,60,67,68,53,50,51]
    for x in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        check = s.connect_ex((ip,x));
        s.close()
        if check == 0:
            print(ip,check,x)
            open_ports.append(x)
            print(open_ports, lbid)
    if len(open_ports) > 0:
        eel.showports(open_ports, lbid)
    else:
        eel.showports(['No ports found'], lbid)

@eel.expose
def startscan(ip, lbid):
    x = threading.Thread(target=ssockets, args=(ip, lbid))
    x.start()

if __name__ == '__main__':
    start()