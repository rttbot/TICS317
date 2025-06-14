from flask import Flask, request, Response, jsonify
import requests
import random

app = Flask(__name__)

# Lista de servidores backend
BACKENDS = [
    'http://server1:5001',
    'http://server2:5002'
]

# Estado de los servidores
server_status = {url: True for url in BACKENDS}

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'backends': server_status})

@app.route('/status')
def status():
    return jsonify({'backends': server_status})

@app.route('/', defaults={'path': ''}, methods=["GET", "POST", "PUT", "DELETE"])
@app.route('/<path:path>', methods=["GET", "POST", "PUT", "DELETE"])
def proxy(path):
    # Selección aleatoria de servidores disponibles
    available = [url for url, ok in server_status.items() if ok]
    tried = set()
    for _ in range(len(BACKENDS)):
        if not available:
            return Response('No backends available', status=503)
        backend = random.choice(available)
        url = f"{backend}/{path}"
        try:
            resp = requests.request(
                method=request.method,
                url=url,
                headers={key: value for key, value in request.headers if key != 'Host'},
                data=request.get_data(),
                cookies=request.cookies,
                allow_redirects=False,
                timeout=2
            )
            # Si el backend responde, devolvemos la respuesta
            server_status[backend] = True
            excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
            headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
            return Response(resp.content, resp.status_code, headers)
        except Exception as e:
            # Si falla, marcamos el backend como caído y probamos otro
            server_status[backend] = False
            tried.add(backend)
            available = [url for url in BACKENDS if url not in tried and server_status[url]]
    return Response('All backends failed', status=502)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
