import random
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Necesario para usar sesiones

questions = [
    {"question": "define scrum:", "answer": "es un marco de trabajo agil para gestionar proyectos complejos, especialmente en el desarrollo de software"},
    {"question": "¿en qué se basa scrum?", "answer": "en la interaccion y entrega incremental, lo que permite adaptarse a los cambios y obtener retroalimentacion constante"},
    {"question": "¿cuál es el objetivo de scrum?", "answer": "maximizar el valor del producto y la satisfaccion del cliente"}
]
random.shuffle(questions)

@app.route("/", methods=["GET", "POST"])
def main():
    if "question_idx" not in session:
        session["question_idx"] = 0
        session["attempts"] = 3

    question_idx = session["question_idx"]
    response = ""

    if request.method == "POST":
        user_answer = request.form["answer"].strip().lower()
        correct_answer = questions[question_idx]["answer"].lower()

        if user_answer == correct_answer:
            response = "¡Correcto!"
            session["question_idx"] += 1
            session["attempts"] = 3  # Resetear intentos para la siguiente pregunta
        else:
            session["attempts"] -= 1
            if session["attempts"] == 0:
                response = f"Incorrecto. La respuesta correcta es: {questions[question_idx]['answer']}"
                session["question_idx"] += 1
                session["attempts"] = 3
            else:
                response = f"Incorrecto. Te quedan {session['attempts']} intentos."

    if session["question_idx"] >= len(questions):
        return render_template("rol.html", response="Has completado la sección de preguntas sobre Scrum.")  # Asegurar que el template existe
    
    return render_template("quiz.html", question=questions[session["question_idx"]], response=response)

roles = [
    {"question": "product_owner", "answer": "representa los intereses del cliente y define el product backlog o lista de tareas"},
    {"question": "scrum_master", "answer": "facilita el proceso scrum, elimina obstaculos y asegura que el equipo siga los principios de scrum"},
    {"question": "team_dev", "answer": "son los encargados de crear el producto, trabajando en sprints y colaborando entre si"}
]
random.shuffle(roles)

@app.route("/rol", methods=["GET", "POST"])
def rol():
    if "role_idx" not in session:
        session["role_idx"] = 0
        session["attempts"] = 3

    role_idx = session["role_idx"]
    response = ""

    if request.method == "POST":
        user_answer = request.form["answer"].strip().lower()
        correct_answer = roles[role_idx]["answer"].lower()

        if user_answer == correct_answer:
            response = "¡Correcto!"
            session["role_idx"] += 1
            session["attempts"] = 3
        else:
            session["attempts"] -= 1
            if session["attempts"] == 0:
                response = f"Incorrecto. La respuesta correcta es: {roles[role_idx]['answer']}"
                session["role_idx"] += 1
                session["attempts"] = 3
            else:
                response = f"Incorrecto. Te quedan {session['attempts']} intentos."

    if session["role_idx"] >= len(roles):
        return render_template("completion.html", response="¡Has completado el quiz de roles de Scrum!")  # Nuevo template para finalizar
    
    return render_template("role_quiz.html", role=roles[session["role_idx"]], response=response)

@app.route("/restart")
def restart():
    session.clear()  # Borra los datos de la sesión para empezar de nuevo
    return render_template("restart.html")  # Nueva plantilla para confirmar el reinicio


if __name__ == "__main__":
    app.run(debug=True)
