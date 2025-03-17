from flask import Flask, render_template, jsonify
import nmap
import socket

app = Flask(__name__)
nm = nmap.PortScanner()

def scan_network():
    try:
        # aqui descobre o ip e ja cria o prefixo automatico
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        network_prefix = ".".join(local_ip.split(".")[:3]) + ".0/24"

        print(f"📡 Escaneando a rede: {network_prefix}")

        # roda o nmap como se fosse o cmd
        scan_result = nm.scan(hosts=network_prefix, arguments="-sn", timeout=20)

        devices = []
        for host in nm.all_hosts():
            mac_address = nm[host]["addresses"].get("mac", "Desconhecido")
            devices.append({
                "IP": host,
                "MAC": mac_address
            })

        print(f"🔍 {len(devices)} dispositivos encontrados!")
        return devices

    except Exception as e:
        print(f"❌ ERRO no escaneamento: {e}")
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan')
def scan():
    devices = scan_network()
    return jsonify(devices)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
