import SimpleHTTPServer
import SocketServer

#python3 -m http.server 8000

#python2 -m SimpleHTTPServer 8000

port = 8000

handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("",port), handler)

print("Serving at port",port)
httpd.serve_forever()