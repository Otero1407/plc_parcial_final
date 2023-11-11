error=0
contador=0
veces=int(input("indique cuantas lecutras de temperatura hay: "))
while contador<veces:
  contador+=1
  temp=int(input("indique la temperatura que detectó: "))
  if temp>=40 or temp<=10:
    error+=1

porcent=(error/veces)*100
print("EL sensor se equivocó",error,"veces")
print("El porcentaje de error del sensor es de",porcent,"%")
