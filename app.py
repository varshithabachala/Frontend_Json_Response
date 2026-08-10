import socket
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder=".", static_url_path="")


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


def get_local_ip():
    """Find this machine's LAN IP address (the one others on office network use)."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


if __name__ == "__main__":
    local_ip = get_local_ip()
    port = 5000
    print("=" * 60)
    print(f"Server starting...")
    print(f"On THIS machine open:   http://localhost:{port}")
    print(f"On OFFICE NETWORK open: http://{local_ip}:{port}")
    print("Share the second link with coworkers on the same network.")
    print("=" * 60)
    app.run(host="0.0.0.0", port=port)
