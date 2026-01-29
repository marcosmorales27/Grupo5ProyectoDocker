from flask import Flask, request, jsonify

app = Flask(__name__)

USERS = {
    "admin": "1234",
    "estudiante": "pass123",
    "docente": "admin123"
}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data:
        return jsonify({"status": "error", "message": "Faltan datos (JSON)"}), 400

    user = data.get("username")
    password = data.get("password")
    
    if USERS.get(user) == password:
        return jsonify({
            "status": "success", 
            "message": "Autenticado correctamente",
            "token": "token-simulado-12345" 
        }), 200
    
    return jsonify({"status": "error", "message": "Credenciales inválidas"}), 401

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({
        "service": "Servicio de Autenticación",
        "status": "activo",
        "port": 5000
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)