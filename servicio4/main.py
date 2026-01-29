from flask import Flask, request, jsonify

app = Flask(__name__)

# Usuarios simulados (Mock Data)
USERS = {
    "admin": "1234",
    "estudiante": "pass123"
}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = data.get("username")
    password = data.get("password")
    
    if USERS.get(user) == password:
        return jsonify({"status": "success", "message": "Autenticado correctamente"}), 200
    return jsonify({"status": "error", "message": "Credenciales inválidas"}), 401

# Ruta simple para probar desde el navegador
@app.route('/', methods=['GET'])
def health_check():
    return "El Servicio de Autenticación está activo"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)