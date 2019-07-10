valores=range (50,101,2)
print valores
n=0
n2=0
for i in valores:
    if i%2==0:
     n=n+i
    else:
         n2=n2+i
print "suma pares "+"="+str(n)
print "suma impares "+"="+str(n2)

#nuevo_valor= input ("ingrese nuevo valor: ")
#valores += [nuevo_valor]
#valores.append (input("ingrese nuevo_valor: "))
#print valores
#valores.pop(0)
#print valores
