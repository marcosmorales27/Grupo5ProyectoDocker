import os
import time
import psycopg2
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                host=os.getenv('DB_HOST', 'servicio-2'),
                database=os.getenv('DB_NAME', 'mibasedatos'),
                user=os.getenv('DB_USER', 'usuario'),
                password=os.getenv('DB_PASS', 'secreto')
            )
            return conn
        except psycopg2.OperationalError:
            retries -= 1
            print(f"Esperando a la BD... intentos restantes: {retries}")
            time.sleep(2)
    return None

def init_db():
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS visitas (id SERIAL PRIMARY KEY, mensaje VARCHAR(100));')
        conn.commit()
        cur.close()
        conn.close()
        print("Tabla inicializada correctamente.")

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "UP", "service": "Backend Python + PostgreSQL"})

@app.route('/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "No hay conexión con la BD"}), 500
    
    cur = conn.cursor()
    cur.execute("INSERT INTO visitas (mensaje) VALUES ('Acceso desde Servicio 3 (Web)')")
    conn.commit()
    
    cur.execute('SELECT * FROM visitas ORDER BY id DESC LIMIT 5;')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    resultados = [{"id": r[0], "mensaje": r[1]} for r in rows]
    return jsonify(resultados)

if __name__ == '__main__':
    time.sleep(3)
    init_db()
    app.run(host='0.0.0.0', port=3000)