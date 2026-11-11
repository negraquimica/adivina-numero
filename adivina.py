import random

MAX_INTENTOS = 7

# La computadora elige un número secreto entre 1 y 100
secreto = random.randint(1, 100)
intentos = 0

print(f"¡Adivina el número! Estoy pensando en uno entre 1 y 100. Tienes {MAX_INTENTOS} intentos.")

# Repetimos mientras queden intentos
while intentos < MAX_INTENTOS:
    texto = input("Tu número: ")

    # Si no escribieron un número, avisamos y volvemos a preguntar
    # (esto no gasta un intento)
    if not texto.isdigit():
        print("Eso no es un número. Intenta de nuevo.")
        continue

    numero = int(texto)
    intentos += 1

    if numero == secreto:
        print(f"¡Correcto! Lo lograste en {intentos} intentos.")
        break

    restantes = MAX_INTENTOS - intentos
    pista = "Más alto ⬆" if numero < secreto else "Más bajo ⬇"

    # Elegimos el mensaje según cuántos intentos quedan
    if restantes > 1:
        print(f"{pista} (te quedan {restantes} intentos)")
    elif restantes == 1:
        print(f"{pista} (queda 1 intento)")
    # Si quedan 0 no mostramos pista: el mensaje final lo dice todo
else:
    # Este bloque solo corre si el while terminó sin pasar por break
    print(f"Se acabaron los intentos. El número era {secreto}.")
