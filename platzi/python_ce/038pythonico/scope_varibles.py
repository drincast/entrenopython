xg = 100    #variable de ambito global

def local_function():
    x = 10 #variable local
    print(f"valor de la variable es {x}")

def show_global():
    try:
        print(f"valor de la variable xg es {xg}")
    except Exception as ex:
        print(ex)

local_function()
#print(x) genera error no existe variable
print(xg)
show_global()