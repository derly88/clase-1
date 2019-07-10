from random import randint

lista=[]
for i in range(3):
    lista.append(randint(0,100))
#n=randint(10,100)

adivinado = False
print lista
for i in range(5):
    a=input("ingrese su valor ")
    if a in lista:
        print "ganaste"
        adivinado=True
        break
    else:
        print "sigue intentando"
if not adivinado:
    #print "los numeros eran "+ str (lista)
    cad=""
    for i in lista:
        cad+=str(i)+", "
    print "es: "+cad[:-2]        
