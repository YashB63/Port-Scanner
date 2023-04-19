from socket import *

def connectionScan(targetHost, targetPort):
    try:
        connectionSocket = socket(AF_INET, SOCK_STREAM)
        connectionSocket.connect((targetHost, targetPort))
        print('[+]%d/TCP Open'%targetPort)
        connectionSocket.close()
    except:
        print('[-]%d/TCP Closed'%targetPort)


def portScan(targetHost, targetPorts):
    try:
        targetIP = gethostbyname(targetHost)
    except:
        print('[-] Cannot Resolve %s '%targetHost)
        return 
    try:
        targetName = gethostbyaddr(targetIP)
        print('\n[+] Scan Result of: %s '%targetName[0])
    except:
        print('\n[+] Scan Result of: %s '%targetIP)
    setdefaulttimeout(1)
    for targetPort in targetPorts:
        print('Scanning Port: %d'% targetPort)
        connectionScan(targetHost, int(targetPort))

if __name__ == '__main__':
    portScan('facebook.com', [80, 33])







