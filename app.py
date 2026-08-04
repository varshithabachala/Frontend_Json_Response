"""
Simple Flask app to serve the Playbook Request Log frontend
on your office network (intranet).

SETUP:
    1. Put this file (app.py) in the SAME folder as your index.html
       (i.e. inside Frontend_Json_Response folder)
    2. Install Flask (one time):
           pip install flask --break-system-packages
    3. Run:
           python3 app.py
    4. It will print a network URL like:
           http://192.168.1.23:5000
       Share THIS URL with coworkers on the same office WiFi/LAN.

NOTE:
    - Your laptop must stay ON and this script must keep running
      for others to access it (there's no "always on" server unless
      you keep this terminal open).
    - index.html's API_BASE should still point to your Render backend
      (https://backend-26zz.onrender.com) - that stays in the cloud,
      no change needed there.
"""

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
