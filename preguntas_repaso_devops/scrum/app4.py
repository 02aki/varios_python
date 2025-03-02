import random
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "supersecretkey"

questions = [
    {"question": "define scrum:", "answer": "es un marco de trabajo agil para gestionar proyectos complejos, especialmente en el desarrollo de software"},
    {"question": "¿en qué se basa scrum?", "answer": "en la interaccion y entrega incremental, lo que permite adaptarse a los cambios y obtener retroalimentacion constante"},
    {"question": "¿cuál es el objetivo de scrum?", "answer": "maximizar el valor del producto y la satisfaccion del cliente"}
]
random.shuffle(questions)

roles = [
    {"question": "product_owner", "answer": "representa los intereses del cliente y define el product backlog o lista de tareas"},
    {"question": "scrum_master", "answer": "facilita el proceso scrum, elimina obstaculos y asegura que el equipo siga los principios de scrum"},
    {"question": "team_dev", "answer": "son los encargados de crear el producto, trabajando en sprints y colaborando entre si"}
]
random.shuffle(roles)

events = [
    {"event": "sprint", "description": "interacciones cortas y fijas (generalmente de 2 a 4 semanas) en las que se trabaja para entregar un incremento del producto."},
    {"event": "sprint planning", "description": "el equipo planifica el trabajo del sprint y selecciona las tareas del product backlog."},
    {"event": "daily", "description": "reunión diaria de 15 min. para sincronizar el trabajo y detectar obstáculos."},
    {"event": "sprint review", "description": "se presenta el incremento del producto al product owner y a los interesados para obtener retro."},
    {"event": "sprint retrospective", "description": "el equipo reflexiona sobre el sprint y busca mejoras para el próximo."}
]
random.shuffle(events)

artefacts = [
    {"artefacts": "product backlog", "description": "lista priorizada de todas las funcionalidades y mejoras del producto"},
    {"artefacts": "sprint backlog", "description": "lista de tareas seleccionadas del product backlog para el sprint actual"},
    {"artefacts": "incremento", "description": "la suma de todos los elementos del product backlog completada durante un sprint y los incrementos de todos los sprint anteriores"},
   ]
random.shuffle(events)

@app.route("/")
def start():
    session.clear()
    session["step"] = "questions"
    session["question_idx"] = 0
    session["role_idx"] = 0
    session["event_idx"] = 0
    session["artefacts_idx"] = 0
    session["attempts"] = 3
    return redirect(url_for("question_quiz"))

@app.route("/questions", methods=["GET", "POST"])
def question_quiz():
    if "question_idx" not in session:
        return redirect(url_for("start"))
    
    if request.method == "POST":
        user_answer = request.form["answer"].strip().lower()
        correct_answer = questions[session["question_idx"]]["answer"].lower()
        
        if user_answer == correct_answer:
            session["question_idx"] += 1
        
    if session["question_idx"] >= len(questions):
        session["step"] = "roles"
        return redirect(url_for("role_quiz"))
    
    return render_template("quiz.html", question=questions[session["question_idx"]])

@app.route("/roles", methods=["GET", "POST"])
def role_quiz():
    if "role_idx" not in session:
        return redirect(url_for("start"))
    
    if request.method == "POST":
        user_answer = request.form["answer"].strip().lower()
        correct_answer = roles[session["role_idx"]]["answer"].lower()
        
        if user_answer == correct_answer:
            session["role_idx"] += 1
        
    if session["role_idx"] >= len(roles):
        session["step"] = "events"
        return redirect(url_for("event_quiz"))
    
    return render_template("role_quiz.html", role=roles[session["role_idx"]])

@app.route("/events", methods=["GET", "POST"])
def event_quiz():
    if "event_idx" not in session:
        return redirect(url_for("start"))
    
    if request.method == "POST":
        user_answer = request.form["answer"].strip().lower()
        correct_answer = events[session["event_idx"]]["event"].lower()
        
        if user_answer == correct_answer:
            session["event_idx"] += 1
        
    if session["event_idx"] >= len(events):
    #    return render_template("completion.html", response="¡Has completado el quiz de eventos de Scrum!")
    
        return render_template("event_quiz.html", event=events[session["event_idx"]])

@app.route("/artefacts", methods=["GET", "POST"])
def artefacts_quiz():
    if "artefacts_idx" not in session:
        return redirect(url_for("start"))
    
    if request.method == "POST":
        user_answer = request.form["answer"].strip().lower()
        correct_answer = events[session["artefacts_idx"]]["artefacts"].lower()
        
        if user_answer == correct_answer:
            session["artefacts_idx"] += 1
        
    if session["artefacts_idx"] >= len(events):
        return render_template("completion.html", response="¡Has completado el quiz de artefactos de Scrum!")
    
    return render_template("artefacts_quiz.html", artefact=artefacts[session["artefacts_idx"]])

@app.route("/restart")
def restart():
    session.clear()
    return redirect(url_for("start"))

if __name__ == "__main__":
    app.run(debug=True)
