def main():
    roles = ["product_owner", "scrum_master", "team_dev"]
    while True:
        for i, opcion in enumerate(roles):
            print(f"{i+1}. {opcion}")
        
        seleccion = input("Selecciona una opción: ")
        
        try:
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(roles):
                opcion_elegida = roles[seleccion - 1]
                print(f"Has seleccionado la opción: {opcion_elegida}")
                break
            else:
                print("Opción no válida. Por favor, selecciona un número de la lista.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")

if __name__ == "__main__":
    main()