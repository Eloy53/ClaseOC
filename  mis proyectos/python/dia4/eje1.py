saldo = 1000

pin=1234
def  verficiar_pin (pin_usuario):
    if pin== pin_usuario: 
        return True
    elif pin != pint_usuario:
        return False
def retirar (cantidad):
    if cantidad <= saldo:
        v=(saldo-cantidad)
        print("tu saldo restante es" , v  )
    elif cantidad >= saldo:
        print("tu saldo no es suficiente")
pint_usuario=int(input("ingresar tu pin"))
if verficiar_pin(pint_usuario):
    print("acceso concedido")

    try:
        monto = int(input("ingresar monto"))  
        retirar((monto))
    except ValueError:
        print("error al ingresar el monto")
else:
    print("acceso denegado")

   

    
    

   