"""
Netflix Data Intelligence Platform — Backend Server & Web Application
Zero-dependency HTTP server utilizing Python's built-in http.server,
providing a responsive web dashboard and REST API endpoints.
"""
import os
import sys
import json
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

# Add backend directory to sys.path
backend_dir = Path(__file__).resolve().parent.parent
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

from app.routes.titles import handle_search_titles, handle_get_title
from app.routes.insights import handle_get_overview, handle_get_top_countries, handle_get_top_genres, handle_get_ratings
from app.routes.recommendations import handle_get_recommendations
from app.routes.predictions import handle_classify_content
from app.routes.dashboard import handle_get_dashboard_summary

STATIC_DIR = Path(__file__).resolve().parent / "static"

class NetflixRequestHandler(BaseHTTPRequestHandler):
    def send_json(self, data: dict, status: int = 200):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        # Serve Dashboard Web App
        if path == "/" or path == "/index.html":
            html_file = STATIC_DIR / "index.html"
            if html_file.exists():
                with open(html_file, "rb") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(content)))
                self.end_headers()
                self.wfile.write(content)
            else:
                self.send_error(404, "Dashboard HTML not found")
            return

        # API Routes
        if path == "/api/health":
            self.send_json({"status": "healthy", "service": "Netflix Data Intelligence Platform"})
        elif path == "/api/dashboard/summary":
            self.send_json(handle_get_dashboard_summary())
        elif path == "/api/insights/overview":
            self.send_json(handle_get_overview())
        elif path == "/api/insights/countries":
            limit = int(query.get("limit", [10])[0])
            self.send_json(handle_get_top_countries(limit=limit))
        elif path == "/api/insights/genres":
            limit = int(query.get("limit", [10])[0])
            self.send_json(handle_get_top_genres(limit=limit))
        elif path == "/api/insights/ratings":
            self.send_json(handle_get_ratings())
        elif path == "/api/titles":
            q = query.get("query", [""])[0]
            ctype = query.get("type", [""])[0]
            limit = int(query.get("limit", [20])[0])
            self.send_json(handle_search_titles(query=q, content_type=ctype, limit=limit))
        elif path == "/api/recommendations":
            title = query.get("title", [""])[0]
            n = int(query.get("n", [10])[0])
            self.send_json(handle_get_recommendations(title=title, n=n))
        else:
            self.send_json({"status": "error", "message": f"Route '{path}' not found"}, status=404)

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        content_length = int(self.headers.get("Content-Length", 0))
        body_bytes = self.rfile.read(content_length)

        try:
            payload = json.loads(body_bytes.decode("utf-8")) if body_bytes else {}
        except Exception:
            payload = {}

        if path == "/api/predictions/classify":
            self.send_json(handle_classify_content(payload))
        else:
            self.send_json({"status": "error", "message": f"Endpoint '{path}' not found"}, status=404)

    def log_message(self, format, *args):
        # Concise logging
        pass

def run_server(port: int = 8000):
    server = HTTPServer(("127.0.0.1", port), NetflixRequestHandler)
    print(f"🚀 Netflix Data Intelligence Platform running at http://127.0.0.1:{port}")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.server_close()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    run_server(port=port)

