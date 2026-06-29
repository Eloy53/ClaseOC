agenda={
    "luis":11,
    "paco":5,
    "juan":67,}
nombre=input("ingresar un nombre")
if nombre=="luis":
   print("su numero es",agenda["luis"])
elif nombre=="paco":
     print("su numero es",agenda["paco"])
elif nombre=="juan":
     print("su numero es",agenda["juan"])
else:
    print("no existe este numero")