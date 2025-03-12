#Lambda function 
addition = lambda num1, num2: num1 + num2

subtraction = lambda num1, num2: num1 - num2

multiply = lambda num1, num2: num1 * num2

divide = lambda num1, num2: num1 / num2

squared = lambda num1: num1**2


#variables
list_options_operation = ["0", "1", "2", "3", "4", "5", "6"]
list_options_app_text = ["1. Suma", "2. Resta", "3. Multiplicación", "4. División", "5. Cuadrado", "6. números pares", "7. Salir"]

numbers = range(11)


#funtions
def go_print(val):
    print(val)

def menu_option():
    print("\nSeleccione una operación")
    for opc in list_options_app_text:
        print(opc)

def calculator():
    men = 0
    option = "0"

    while option in list_options_operation:
        menu_option()

        option = input("Opción: ")

        if option == "7":
            print("\nSe finaliza la ejecución de calculator")
            print("----------------------------------------------------\n")

        if option in list_options_operation:
            #para la memoria o resultado que lleva
            mesagge = "Digite el primer número: " if men == 0 else f"Digite el primer número (men = {men}): "
            val = input(mesagge)
            if val == '':
                num1 = men
            else:
                num1 = float(val)
                        
            if option != "5":
                num2 = float(input("Digite el segundo número: "))
        
        if option == "1":
            men = addition(num1, num2)
            print("\nLa suma es: ", men)
        elif option == "2":
            men = subtraction(num1, num2)
            print("\nLa resta es: ", men)
        elif option == "3":
            men = multiply(num1, num2)
            print("\nLa multiplicación es: ", men)
        elif option == "4":
            men = divide(num1, num2)
            print("\nLa división es: ", men)
        elif option == "5":
            men = squared(num1)
            print("\nEl cuadrado es: ", men)
        elif option == "6":
            print("\nBuscar números pares en la lista", list(numbers))
            even_numbers = list(filter(lambda x : x%2 == 0, numbers))
            print("los pares son: ", even_numbers)

        input("\nteclea para continua")

calculator()