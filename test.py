import matplotlib.pyplot as plt
import numpy as np
import random

def randomaccesword():
    wordlist = ["banana", "strawberry", "kiwi", "Orange", "Apple"]
    wordchose = random.choice(wordlist)
    word = "_" * len(wordchose)
    #maskedword = ["_" for _ in word]
    tentatives = 6
    #lettersguessed = []
#print("Mot masqué :", "".join(maskedword))
    error = 0
    while tentatives > 0:
        print(word)    
        guess = input("Devinez une lettre : ").lower()
        if guess in wordchose:
            for i in range(len(wordchose)):
                if wordchose[i]==guess:
                    word=word[:i]+guess+word[i+1:]
        else:
            guess -= 1
            print("Letra incorrecta. Te quedan", guess, "intentos.")
        if "_" not in word:
            print("¡Felicidades! Has adivinado la palabra:", palabra_secreta)
            break
        if "_" in word:
            print("¡Désolé, vous avez perdu. Le mot était:", wordchose)
        else:
            error += 1
            print("error est egale a ", error)
randomaccesword()

plt.figure()
plt.plot([0, 1], [0, 0], 'k')
plt.plot([0.5, 0.5], [0, 1], 'k')  # Poteau vertical
plt.plot([0.5, 1], [1, 1], 'k')  # Barre horizontale
plt.plot([1, 1], [0.9, 0.8], 'k')  # Corde

# Base y poste
plt.plot([0, 1], [0, 0], 'k')  # Base
if error >= 1:
    plt.plot([0.5, 0.5], [0, 1], 'k')  # Poste vertical

    # Ajustar coordenadas según tus preferencias
cabeza_x, cabeza_y = 0.5, 0.8
cuerpo_x, cuerpo_y = 0.5, 0.6
brazo_izq_x, brazo_izq_y = 0.3, 0.6
brazo_der_x, brazo_der_y = 0.7, 0.6
pierna_izq_x, pierna_izq_y = 0.3, 0.4
pierna_der_x, pierna_der_y = 0.7, 0.4

    # Cuerpo
if error >= 2:
    plt.plot([cabeza_x, cuerpo_x], [cabeza_y, cuerpo_y], 'k')  # Cuerpo
if error >= 3:
    plt.plot([cabeza_x, brazo_izq_x], [cabeza_y, brazo_izq_y], 'k')  # Brazo izquierdo
    plt.plot([cabeza_x, brazo_der_x], [cabeza_y, brazo_der_y], 'k')  # Brazo derecho
if error >= 4:
    plt.plot([cuerpo_x, pierna_izq_x], [cuerpo_y, pierna_izq_y], 'k')  # Pierna izquierda
    plt.plot([cuerpo_x, pierna_der_x], [cuerpo_y, pierna_der_y], 'k')  # Pierna derecha

plt.axis('off')
plt.xlim(-0.2, 1.4)  # Ajuste les limites de l'axe x
plt.ylim(-0.2, 1.2)  # Ajuste les limites de l'axe y
plt.show()
