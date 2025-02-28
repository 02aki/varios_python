import random

def main():
    questions = [
        {
            "question": "¿Cuáles son los pasos para cambiar el nombre de hostname en un servidor Ubuntu?",
            "answer": "ser root, editar el archivo /etc/hosts y dar el comando hostnamectl set-hostname nuevonombre"
        },
        {
            "question": "¿Cuál es el comando para saber qué IP se tiene en una máquina de Ubuntu?",
            "answer": "ip a"
        },
        {
            "question": "¿Cuál es el comando para saber qué puertos TCP y UDP que están escuchando en el sistema?",
            "answer": "netstat"
        },
        {
            "question": "¿Cuál es el comando para saber qué puertos están siendo escuchados por dif procesos en ejecución?",
            "answer": "lsof"
        },
        {
            "question": "¿Cuál es el comando que permite descubrir redes y host como auditor?",
            "answer": "nmap"
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

if __name__ == "__main__":
    main()
