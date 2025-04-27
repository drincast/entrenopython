def outer_function():
    try:
        x = "enclosing"

        def inner_function():
            nonlocal x
            x = "modified"
            print(f"El valor en inner es {x}")

        print(f"el valor outer {x}")
        inner_function()
        print(f"el valor outer {x}")
    except Exception as ex:
        print(ex)

outer_function()