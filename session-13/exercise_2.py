import http.server
import socketserver

PORT = 8004

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET received")

        print("Request line:" + self.requestline)
        print("     Cmd: "+self.command)
        print("     Path: "+self.path)

        c = self.requestline.split(" ")
        if c[1] == '/':
            file = open('index.html', 'r')
            content = file.read()
            file.close()
        else:
            file = open('error.html', 'r')
            content = file.read()
            file.close()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))

        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print('Serving at PORT', PORT)

    httpd.serve_forever()