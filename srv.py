import http.server as srv

if __name__ == "__main__":
        server = srv.HTTPServer(('', 8080), srv.SimpleHTTPRequestHandler)
        server.serve_forever()
