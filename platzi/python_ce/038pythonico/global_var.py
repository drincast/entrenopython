x = 5 #variable global

def modify_global_var():
    try:
        global x

        x += 3
        print(f"valor modificado: {x} ")

    except Exception as ex:
        print(ex)

modify_global_var()
print(x)