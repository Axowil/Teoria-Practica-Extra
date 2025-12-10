
""" 
Escriba un programa Python que pida el nombre de usuario y luego el dominio,
luego el programa deberá imprimir el correo electrónico juntando el nombre de usuario y
el dominio y usando el caracter @ en medio. Como restricción no podrá usar el operador punto(.)
para concatenar strings. Si el usuario ingresa como nombre "alumno" y como dominio "pweb1", deberá imprimir: "alumno@pweb1".
"""
#definir una funcion para devolver correo
def devolver_coreeo(usuario,dominio):
    return usuario +"@" +dominio
    
#Inicializar datos 
introducir_usuario = str(input('Introducir el nombre de usuario :'))
introducir_dominio = str(input('Introducir su dominio de correo '))

resultado = devolver_coreeo(introducir_usuario,introducir_dominio)

print(f'Su nombre es "{introducir_usuario}" y su dominio es "{introducir_dominio}" y su correo electronico es {resultado}') 