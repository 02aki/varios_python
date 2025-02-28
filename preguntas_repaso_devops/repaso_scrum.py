import random

def main():
    questions = [
        {
            "question": "define scrum:",
            "answer": "es un marco de trabajo agil para gestionar proyectos complejos, especialmente en el desarrollo de software"
        },
        {
            "question": "¿en qué se basa?",
            "answer": "en la interaccion y entrega incremental, lo que permite adaptarse a los cambios y obtener retroalimentacion constante"
        },
        {
            "question": "¿cuál es su objetivo?",
            "answer": "maximizar el valor del producto y la satisfaccion del cliente"
        }
    ]

    attempts = 3

    # Shuffle questions
    random.shuffle(questions)

    for q in questions:
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
    roles = ["product_owner", "scrum_master", "team_dev"]
    # Definiciones de los roles
    role_definitions = {
        "product_owner": "Es el responsable de maximizar el valor del producto y gestionar el backlog del producto.",
        "scrum_master": "Es el facilitador del equipo Scrum. Ayuda a eliminar obstáculos y asegura que el equipo siga los principios de Scrum.",
        "team_dev": "Es el equipo de desarrollo. Son los encargados de crear el producto, trabajando en sprints y colaborando entre sí."
    }
    
    while True:
        for i, opcion in enumerate(roles):
            print(f"{i+1}. {opcion}")
        
        seleccion = input("Selecciona una opción: ")
        
        try:
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(roles):
                opcion_elegida = roles[seleccion - 1]
                print(f"Has seleccionado la opción: {opcion_elegida}")
                # Mostrar la definición del rol seleccionado
                print(f"Definición: {role_definitions[opcion_elegida]}")
                break
            else:
                print("Opción no válida. Por favor, selecciona un número de la lista.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")

if __name__ == "__main__":
    main()
    rol()