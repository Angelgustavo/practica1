from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def obtener_conexion():
    conn = sqlite3.connect("tarjeta.db")# conecta la base de datos y si no existe la crea 
    conn.row_factory = sqlite3.Row #los resultados se convierten en un direcionario key, value 
    return conn # devuelve la conexión para usarla 

@app.route('/') # ruta principal 
def home():
    return jsonify({"Mensaje":"Bienvenidos al centro de consulta de saldos tarjeta ciudad"})

@app.route('/usuarios', methods=['GET'])# consultar usuarios 
def obtener_usuarios():
    try:
        #cambio
        conn = obtener_conexion()
        usuarios = conn.execute("SELECT * FROM usuarios").fetchall()
        conn.close()
        return jsonify([dict(u) for u in usuarios])
    except sqlite3.OperationalError:
        return jsonify({"error": "La tabla 'usuarios' no existe. Ejecuta la inicialización."}), 500

@app.route('/usuarios', methods=['POST'])
def agregar_usuario():
    data = request.json
    cedula = data["cedula"]
    saldo = data["saldo"]

    conn = obtener_conexion()
    conn.execute("INSERT INTO usuarios (cedula, saldo) VALUES (?, ?)", (cedula, saldo))
    conn.commit()
    conn.close()

    return jsonify({"mensaje":"Usuario agregado correctamente"})

if __name__ == '__main__':
    app.run(debug=True, port=8080)