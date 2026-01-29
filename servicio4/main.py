from flask import Flask, request, jsonify

app = Flask(__name__)

# Usuarios simulados (Mock Data)
USERS = {
    "admin": "1234",
    "estudiante": "pass123",
    "docente": "admin123"
}

@app.route('/login', methods=['POST'])
def login():
    # Obtener datos del JSON enviado
    data = request.get_json()
    
    # Validar que lleguen los datos
    if not data:
        return jsonify({"status": "error", "message": "Faltan datos (JSON)"}), 400

    user = data.get("username")
    password = data.get("password")
    
    # Verificación de credenciales
    if USERS.get(user) == password:
        return jsonify({
            "status": "success", 
            "message": "Autenticado correctamente",
            "token": "token-simulado-12345" 
        }), 200
    
    return jsonify({"status": "error", "message": "Credenciales inválidas"}), 401

# Ruta de Health Check (para probar en navegador)
@app.route('/', methods=['GET'])
def health_check():
    return jsonify({
        "service": "Servicio de Autenticación",
        "status": "activo",
        "port": 5000
    })

if __name__ == '__main__':
    # host='0.0.0.0' es vital para que Docker exponga el servicio
    app.run(host='0.0.0.0', port=5000)