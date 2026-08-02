from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import os

PORT = int(os.environ.get("HUB_PORT", "4181"))

if __name__ == "__main__":
    print(f"Hub disponible sur http://0.0.0.0:{PORT}")
    ThreadingHTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler).serve_forever()
