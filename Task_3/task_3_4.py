def my_func (*args):
    x = abs(float(input("Input x ")))
    y = int(input("Input y "))
    return x ** y

print(f'Result is {my_func()}')