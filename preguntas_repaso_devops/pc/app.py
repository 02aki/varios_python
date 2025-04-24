from flask import Flask, render_template, request, jsonify
import subprocess, os

app = Flask(__name__)

# Definir una carpeta segura para la simulación de archivos
BASE_DIRECTORY = os.path.abspath("./home")

# Ruta principal
@app.route("/")
def home():
    return render_template("index.html")

# Ejecutar comandos en la terminal (comandos restringidos)
@app.route("/run-command", methods=["POST"])
def run_command():
    allowed_commands = ["ls", "pwd", "whoami", "echo"]
    command = request.json.get("command")

    # Verificar si el comando es seguro
    if command.split()[0] not in allowed_commands:
        return jsonify({"output": "Error: Comando no permitido"})

    try:
        result = subprocess.check_output(command, shell=True, text=True)
    except Exception as e:
        result = f"Error: {e}"
    
    return jsonify({"output": result})

# Obtener archivos en una carpeta (restringido a BASE_DIRECTORY)
@app.route("/list-files", methods=["POST"])
def list_files():
    folder = request.json.get("folder", BASE_DIRECTORY)

    # Verificar que la carpeta esté dentro del directorio permitido
    folder_path = os.path.abspath(folder)
    if not folder_path.startswith(BASE_DIRECTORY):
        return jsonify({"error": "Acceso denegado"})

    try:
        files = os.listdir(folder_path)
        return jsonify({"files": files})
    except Exception as e:
        return jsonify({"error": str(e)})

# Cambiar fondo de pantalla (solo simulado)
@app.route("/change-wallpaper", methods=["POST"])
def change_wallpaper():
    wallpaper = request.json.get("wallpaper")
    return jsonify({"message": "Fondo cambiado", "wallpaper": wallpaper})

if __name__ == "__main__":
    app.run(debug=True)
