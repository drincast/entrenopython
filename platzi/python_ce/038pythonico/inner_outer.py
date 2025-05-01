x = 'global' # variable global

def outer_function():
    try:
        x = 'enclosing'

        #funcion interna
        def inner_function():
            x = 'local' #variable local
            print(f"variable local {x}")

        inner_function()
        print(x)

    except Exception as ex:
        print(ex)

outer_function()
print(x)
