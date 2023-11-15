ventatotal=0
otroasistente=True
boletos=0
while otroasistente == True:
  boletos+=1
  nombre=(str(input("Ingrese el nombre del asistente: ")))
  zona=int(input("Ingrese la zona: (1, 2 o 3) "))
  dia=str(input("Inserte que día de la semana es: "))
  cupon=str(input("Inserte el tipo de cupón: (Platino, Oro o PLata) "))
  if zona== 1:
    costobase = 2000
  elif zona == 2:
    costobase= 1000
  elif zona == 3:
    costobase = 700  

  if dia.lower() in ['lunes','martes','miercoles','jueves']:
    if cupon.lower() =="platino":
      descuento=500
    elif cupon.lower() == "oro":
      descuento=300
    elif cupon.lower() =="plata":
      descuento=200
    else:
      descuento=0

  else:
    descuento=0

  costototal= costobase-descuento
  ventatotal+=costototal
  print("Nombre del asistente:",nombre)
  print("El costo de su boleto es de: $",costototal)
  otro=str(input("Hay más asistentes?: "))
  if otro.lower() =="si":
    otroasistente=True
  elif otro.lower() =="no":
    otroasistente=False

print("Se vendieron un total de",boletos,"boletos ")
print("Las ventas totales fueron de: $",ventatotal)
