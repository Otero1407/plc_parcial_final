voz=str(input("Para activar, di Alexa: "))
voz.count("Alexa")
if voz.count("Alexa")==1:
  print("¿Dime, cómo puedo ayudarte?")

elif voz.count("Alexa")>1:
  print("Tranquilo, solo di mi nombre una vez")
