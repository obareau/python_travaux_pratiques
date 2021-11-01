# coding: utf-8

# ! when reading from the command line using input(), the resulting value is a string, 
# ! Even if you only typed digits. therfore the addition operator + conncatenate the string


def wrong_way():
    a = input("first number:")
    b = input("second number:")
    print (a + b) # !result will be wrong
    print("Wrong result \n")

wrong_way()


def good_way():
    a = input("first number again:")
    b = input("second number again:")
    print(int(a) + int(b))
    print("Good result \n")
    
good_way()