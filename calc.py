def convertir_fracciones(entrada):
    """ recibe un número en int o str y revisa que tipo de entrada es y lo conviertea float"""
    numero = 0
    try:
        if isinstance(entrada, str):
            print(entrada)
            if "/" in entrada:
                arr = entrada.split("/")
                numerador = arr[0]
                denominador = arr[1]
                # print(arr)
                numero = float(numerador) / float(denominador)
                # print(arr, numero)
            else:
                numero = float(entrada)
                print(type(numero))
        if isinstance(entrada, int) or isinstance(entrada, float):
            numero = entrada
    except:
        print("Error de formato de numero")
    return numero

def suma(a,b):
 """recibe dos numeros, los convierte llamando a la función anterior y los suma"""
 sumando_a = convertir_fracciones(a)
 sumando_b = convertir_fracciones(b)
 return sumando_a+sumando_b

def multiplicacion(a,b):
 """recibe dos números, los convierte con la función anterior y los multiplica"""
 mult_a = convertir_fracciones(a)
 mult_b = convertir_fracciones(b)
 return mult_a*mult_b
