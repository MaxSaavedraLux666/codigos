"""Module providing a function printing python version."""
import random


def juego_adivinanza():
    """_summary_
    """
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de adivinanzas!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        intento = int(input("Adivina el número: "))
        intentos += 1

        if intento == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número en {
                  intentos} intentos.")
            break
        elif intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        else:
            print("Demasiado alto. Intenta de nuevo.")


if __name__ == "__main__":
    juego_adivinanza()
