import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('Connected by', self.client_address)
        client = self.request

        client.sendall('RiSTCTF{nc_problems_tutorial}\n'.encode())

if __name__ == "__main__":
    HOST, PORT = "", 1001
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()