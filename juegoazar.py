from random import randint

numero=randint(1,10)

intentos=0
while intentos < 3:
  intentos+=1
  adivinar=int(input("Intenta adivinar el número entre 1 y 10 "))
  if numero == adivinar:
    print("Has adivinado el número!, Ganaste ")
    break
  elif intentos == 3:
    print("Se te han acabado los intentos, perdiste :( ")
