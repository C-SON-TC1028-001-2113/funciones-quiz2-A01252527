# Escribe tus funciones abajo de esta línea
def pies_cm(pies): 
    feet = (pies*30.48)
    return(feet)
def pulgadas_cm(pulgadas):
    inches = (pulgadas*2.54)
    return (inches)
def yardas_cm(yardas): 
    yards = (yardas*91.44)
    return(yards)
def main():
    print('1. pies a cm, 2. pulgadas a cm, 3. yardas a cm' ) 
    opciones = str(input('Introduce una opcion: '))
    cantidad = int(input('Introduce la cantidad: '))
    if cantidad > 0: 
        if opciones == '1': 
            feet = pies_cm(cantidad)
            print(feet)
        elif opciones == '2': 
            inches = pulgadas_cm(cantidad)
            print(inches)
        elif opciones == '3':
            yards = yardas_cm(cantidad)
            print(yards)
        else:
            print('Error')
    else: 
        print('Error')
        


if __name__ == '__main__':
    main()
