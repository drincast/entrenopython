def sum_number(*args):
    try:
        return sum(args)
    except Exception as ex:
        print(ex)

print(sum_number(1,2,3,4,5))
print(sum_number(1,2))
print(sum_number(1,2,3,4,5,6,7,8,9,10))

def print_info(**kwargs):
    try:
        print(type(kwargs), kwargs)
        for key, value in kwargs.items():
            print(f"{key}: {value}")
    except Exception as ex:
        print(ex)

print()
print_info(name='Carlos', age=30, city='Bogotá')
print()
print_info(name='Carlos', age=30, city='Bogotá', country='Colombia')