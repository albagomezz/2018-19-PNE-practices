import http.server
import socketserver

PORT = 8002

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET received")

        print("Request line:" + self.requestline)
        print("     Cmd: "+self.command)
        print("     Path: "+self.path)

        c = self.requestline.split(" ")
        if c[1] == '/':
            f = open('index.html', 'r')
            contents = f.read()
            f.close()

        elif c == '/pink':
            f = open('pink.html', 'r')
            contents = f.read()
            f.close()

        elif c == '/blue':
            f = open('blue.html', 'r')
            contents = f.read()
            f.close()

        else:
            f = open('error.html', 'r')
            contents = f.read()
            f.close()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        self.wfile.write(str.encode(contents))

        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print('Serving at PORT', PORT)

    httpd.serve_forever()

