import socketserver
#import socket

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('Connected by', self.client_address)
        client = self.request

        def argument_n(name):
            client.sendall(('No argument required for "'+ name +'"\n').encode('utf-8'))
        
        client.sendall('Hello! This shell is "RiShell" (RiSh)!\nPlease input some commands!\n'.encode('utf-8'))
        while 1:
            client.sendall('RiSTCTF $ '.encode('utf-8'))
            data = self.request.recv(1024)
            if not data:
                break

            cmd = list(map(str, data.decode().strip().split()))
            if cmd == []:
                continue
            #client.sendall(data)
            #'''

            if cmd[0] == 'exit': #exit
                if len(cmd) < 2:
                    break
                else:
                    argument_n(cmd[0])

            elif cmd[0] == 'flag':
                if len(cmd) < 2:
                    client.sendall('RiSTCTF{RiSh_1s_7h3_ex313n7_5h3ll}\n'.encode('utf-8'))
                else:
                    argument_n(cmd[0])

            elif cmd[0] == 'help':
                if len(cmd) < 2:
                    client.sendall('These are all of commands.\nexit flag help ls \n'.encode('utf-8'))
                else:
                    argument_n(cmd[0])

            elif cmd[0] == 'ls':
                if len(cmd) < 2:
                    client.sendall('flag.txt\n'.encode('utf-8'))
                else:
                    argument_n(cmd[0])

            else:
                client.sendall(('RiSh: ' + cmd[0] + ' is unknown command. Please check "help" command.\n').encode('utf-8'))
            #'''
    

if __name__ == "__main__":
    HOST, PORT = "", 2001
    with socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()