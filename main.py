from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/log_ip', methods=['POST'])
def log_ip():
    ip_address = request.remote_addr
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("IPs.txt", "a") as file:
        file.write(f"{timestamp} - {ip_address}\n")
    return "IP Logged", 200

if __name__ == '__main__':
    app.run(debug=True)
