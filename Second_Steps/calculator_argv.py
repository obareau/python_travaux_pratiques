# coding: utf-8

# ! Multiplication will not work on linux bacause linux use * as a joker character in string
# *todo find a better way to handle multiplication on linux
import sys

# print(sys.platform) # Just a test 

system = sys.platform



if system == "linux":
    print(" Warning ! for multiplication on linux system please use quote around operator (ex : 2 '*'3) ")
    
else:
    print ("You are using non linux system ... everything is fine with multiplication ")
    
def main():
    
    if len(sys.argv) <4:
        exit ("Usage: " + sys.argv[0] + " OPERAND OPERATOR OPERAND")
    
    a = float(sys.argv [1])
    b = float(sys.argv [3])
    op = sys.argv [2]
        
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
        exit()
        
    print(res)
    
main()
        