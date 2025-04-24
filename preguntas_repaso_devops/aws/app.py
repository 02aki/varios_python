import random
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "supersecretkey"

databases = [
    {"db": "rds", "description": "facilita la operacion, config y escalado de una bd relacional"},
    {"db": "aurora", "description": "relacional, nativa de aws, mas elasticidad, compatible de postgressql y mysql"},
    {"db": "dynamodb", "description": "no relacional, llave valor, nativa de aws, se distribuye en muchos nodos, tiene un hashid y en base a esto ve en que nodo o particion  se va a guardar"},
    {"db": "documentdb", "description": "almacenar documentos y consultar los atributos"},
    {"db": "elasticcache", "description": "en memoria, estructura de datos que no son petsistentes por mucho tiempo, informacion que cambia rapido y que los usuarios acceden rapido"},
    {"db": "neptune", "description": "relaciones entre cosas como las redes sociales. Gestionada por aws"},
    {"db": "timestream", "description": "series de tiempo. Recoger, almacenar y procesar secuencias de tiempo"},
    {"db": "quantum", "description": "inmutable, transacciones online"},
    {"db": "cassandra", "description": "keyspaces, escrituras lentas pero rápidas de leer"},
    {"db": "datawarehouse - redshift", "description": "analisis de gran cantidad de datos, escalable, se integra con s3"},
    {"db": "datalake", "description": "repositorio centralizado donde se ponen todos los datos de cualquier tipo"}
]
random.shuffle(databases)

ec2s = [
    {"ec2": "de proposito general", "description": "t, a, m mac"},
    {"ec2": "es la generacion", "description": "el numero agregado"},
    {"ec2": "es el tipo de procesador", "description": "la letra agregada"},
]
random.shuffle(ec2s)

elastics= [
    {"elasticidad": "autoscalling", "description": "quitar o agregar servidores de acuerdo a la demanda"},
    {"elasticidad": "el valor deseado", "description": "nunca por debajo del minimo ni arriba del maximo"}
]
random.shuffle(elastics)

@app.route("/")
def start():
    session.clear()
    session["step"] = "databases"
    session["db_idx"] = 0
    session["ec2_idx"] = 0
    session["elasticidad_idx"] = 0
    return redirect(url_for("db_quiz"))

@app.route("/databases", methods=["GET", "POST"])
def question_quiz():
    if "db_idx" not in session:
        return redirect(url_for("start"))
    
    if request.method == "POST":
        user_answer = request.form["answer"].strip().lower()
        correct_answer = databases[session["db_idx"]]["answer"].lower()
        
        if user_answer == correct_answer:
            session["db_idx"] += 1
        
    if session["db_idx"] >= len(databases):
        session["step"] = "ec2s"
        return redirect(url_for("ec2_quiz"))
    
    return render_template("quiz.html", db=databases[session["db_idx"]])

@app.route("/ec2s", methods=["GET", "POST"])
def ec2_quiz():
    if "ec2_idx" not in session:
        return redirect(url_for("start"))
    
    if request.method == "POST":
        user_answer = request.form["answer"].strip().lower()
        correct_answer = ec2s[session["ec2_idx"]]["answer"].lower()
        
        if user_answer == correct_answer:
            session["ec2_idx"] += 1
        
    if session["ec2_idx"] >= len(ec2s):
        session["step"] = "elastics"
        return redirect(url_for("elastic_quiz"))
    
    return render_template("ec2_quiz.html", ec2=ec2s[session["ec2_idx"]])

@app.route("/events", methods=["GET", "POST"])
def event_quiz():
    if "event_idx" not in session or session["step"] != "events":
        return redirect(url_for("start"))
    
    if request.method == "POST":
        user_answer = request.form["answer"].strip().lower()
        correct_answer = events[session["event_idx"]]["event"].lower()

        if user_answer == correct_answer:
            session["event_idx"] += 1

    if session["event_idx"] >= len(events):
        session["step"] = "artefacts"
        return redirect(url_for("artefact_quiz"))

    return render_template("event_quiz.html", event=events[session["event_idx"]])

@app.route("/artefacts", methods=["GET", "POST"])
def artefact_quiz():
    if "artefact_idx" not in session or session["step"] != "artefacts":
        return redirect(url_for("start"))
    
    if request.method == "POST":
        user_answer = request.form["answer"].strip().lower()
        correct_answer = artefacts[session["artefact_idx"]]["artefact"].lower()

        if user_answer == correct_answer:
            session["artefact_idx"] += 1

    if session["artefact_idx"] >= len(artefacts):
        session["step"] = "principios"
        return redirect(url_for("principio_quiz"))

    return render_template("artefact_quiz.html", artefact=artefacts[session["artefact_idx"]])

@app.route("/principios", methods=["GET", "POST"])
def principio_quiz():
    if "principio_idx" not in session or session["step"] != "principios":
        return redirect(url_for("start"))
    
    if request.method == "POST":
        user_answer = request.form["answer"].strip().lower()
        correct_answer = principios[session["principio_idx"]]["principio"].lower()

        if user_answer == correct_answer:
            session["principio_idx"] += 1

    if session["principio_idx"] >= len(principios):
        return render_template("completion.html", response="¡Has completado el quiz de Scrum!")

    return render_template("principio_quiz.html", principio=principios[session["principio_idx"]])

@app.route("/restart")
def restart():
    return redirect(url_for("start"))

if __name__ == "__main__":
    app.run(debug=True)
