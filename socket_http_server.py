import socket
import sys
import signal
from datetime import datetime

def start_server(port, log=False):
    port = str(port)
    if log:
        print('redirecting stdout to ' + log)
        sys.stdout = open(log, 'a')
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('port ' + port)
    tcp.bind(('', int(port)))
    tcp.listen(1)
    print('* listening')
    def signal_handler(sig, frame):
        tcp.close()
        print('stopping listener')
        exit(0)
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        try:
            con, (host, portr) = tcp.accept()
            msg = con.recv(65000)
            print('* [' + datetime.now().strftime('%d/%m/%Y %H:%M:%S') + '] connection from: ' + host)
            print(msg.decode())
            # requestline = msg.decode().split('\r\n')[0]
            # path = re.sub('\s+HTTP.[0-9\.]+\s*$', '', re.sub('^[a-zA-Z]+\s+', '', requestline))[1:]
            con.send(b'HTTP/1.1 200 OK\r\nConnection: close\r\n\r\n')
            # print(path)
            # except Exception as e:
            #     print('error on communication with client ' + e)
            con.close()
            if log:
                sys.stdout.flush()
        except socket.timeout as t:
            pass
        except Exception as e:
            print('- error ' + str(e))

port = 8080
if len(sys.argv) > 1:
    port = sys.argv[1]
    
start_server(port, 'http.log')