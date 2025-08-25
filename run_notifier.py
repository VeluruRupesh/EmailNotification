import http.server
import socketserver
import webbrowser
import os

PORT = 8000

# Serve current directory (deployment-notifier/)
web_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(web_dir)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    url = f"http://localhost:{PORT}/index.html"
    print(f"Serving at {url}")
    webbrowser.open(url)   # automatically open browser
    httpd.serve_forever()
