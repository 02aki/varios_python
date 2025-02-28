import random

def scrum():
    scrum_definitions = [
        {
            "question": "define scrum:",
            "answer": "es un marco de trabajo agil para gestionar proyectos complejos, especialmente en el desarrollo de software"
        },
        {
            "question": "¿en qué se basa scrum?",
            "answer": "en la interaccion y entrega incremental, lo que permite adaptarse a los cambios y obtener retroalimentacion constante"
        },
        {
            "question": "¿cuál es el objetivo de scrum?",
            "answer": "maximizar el valor del producto y la satisfaccion del cliente"
        }
    ]

    attempts = 3

    # Shuffle questions
    random.shuffle(scrum_definitions)

    for q in scrum_definitions:
        print(q["question"])
        for attempt in range(attempts):
            user_answer = input(f"Intento {attempt + 1}: ")
            if user_answer.strip() == q["answer"]:
                print("¡Correcto!")
                break
            else:
                print("Incorrecto. Intenta de nuevo.")
        else:
            print(f"La respuesta correcta es: {q['answer']}")
        print()  # Print a newline for better readability

def rol():
    roles = [
        {
            "question": "product_owner",
            "answer" : "representa los intereses del cliente y define el product backlog o lista de tareas"
        },
        {
            "question":"scrum_master",
            "answer": "facilita el proceso scrum, elimina obstaculos y asegura que el equipo siga los principios de scrum"
        },
        {
            "question": "team_dev",
            "answer": "son los encargados de crear el producto, trabajando en sprints y colaborando entre sí"
        }
    ]
    attempts = 3

    # Shuffle questions
    random.shuffle(roles)

    for q in roles:
        print(q["question"])
        for attempt in range(attempts):
            user_answer = input(f"Intento {attempt + 1}: ")
            if user_answer.strip() == q["answer"]:
                print("¡Correcto!")
                break
            else:
                print("Incorrecto. Intenta de nuevo.")
        else:
            print(f"La respuesta correcta es: {q['answer']}")
        print()  # Print a newline for better readability

if __name__ == "__main__":
    scrum()
    rol()