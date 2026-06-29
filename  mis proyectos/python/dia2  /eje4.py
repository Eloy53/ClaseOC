frase=input("ingresar una frase")
cont = 0 
for letras in frase : 
    if letras in "aeiou":
        cont = cont +1 
print (cont)        