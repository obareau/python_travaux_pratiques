# coding: utf-8

def main():
    a = float(input("Number x = "))
    b = float(input("Number y = "))
    op = input("Operator (+ - * /): ")
    
    if op == "+":
        res = a+b
    elif op == "-":
        res = a-b
    elif op == "*":
        res = a*b
    elif op == "/":
        res = a/b
    else:
        print("Invalid operator: '{}'".format(op))
        return
    print(res)
    

main()