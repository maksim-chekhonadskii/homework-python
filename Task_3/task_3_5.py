import sys

result = 0
while True:
    line = input("Enter number or q for exit: ")
    tokens = line.split(" ")
    for token in tokens:
        try:
            number = float(token)
            result += number
            print(result)
        except:
            if token == 'q':
                print(f"Your sum is {result}. Program is terminated")
                exit(0)
            else:
                print(f"Your sum is {result}. Input error", file=sys.stderr)
                exit(1)
#print(result)
#exit()