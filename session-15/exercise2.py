import http.server
import socketserver
import termcolor

# we are using http library (always from now on)
# Define the Server's port
PORT = 8003

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        if self.path.startswith("/main-page") or self.path == "/":
            f = open("form3.html", "r")
            contents = f.read()
        elif self.path.startswith("/myserver"):
            msg = self.path.split("=")
            ff = open("echo.html", "r")
            contents = ff.read()
            if "on" in msg:
                contents += msg[1].upper()
                contents = contents[:-4]
            elif "on" not in msg:
                contents += msg[1]
            contents += """</p>
                                        <a href="main-page">The main page</a>

                                    </body>
                                    </html>
                                    """

        else:
            fff = open("error.html", "r")
            contents = fff.read()
        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')  # this header is crucial
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")