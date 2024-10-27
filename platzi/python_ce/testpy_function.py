def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def menu_option():
    print("\nSeleccione una operación")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def calculator():
    men = 0
    option = "0"

    while option != "5":
        menu_option()

        option = input("Opción: ")

        if option == "5":
            print("\nSe finaliza la ejecución de calculator")
            print("----------------------------------------------------\n")

        if option in ["1", "2", "3", "4"]:
            #para la memoria o resultado que lleva
            mesagge = "Digite el primer número: " if men == 0 else f"Digite el primer número (men = {men}): "
            val = input(mesagge)
            if val == '':
                num1 = men
            else:
                num1 = float(val)
                        
            num2 = float(input("Digite el segundo número: "))
        
        if option == "1":
            men = addition(num1, num2)
            print("La suma es: ", men)
        elif option == "2":
            men = subtraction(num1, num2)
            print("La resta es: ", men)
        elif option == "3":
            men = multiply(num1, num2)
            print("La multiplicación es: ", men)
        elif option == "4":
            men = divide(num1, num2)
            print("La división es: ", men)
            

calculator()