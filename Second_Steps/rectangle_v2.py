# coding: utf-8

# ! let's pimp our formal rectangle.py code (cf First Steps section)

def main():
    # length = 10
    # width = 3
    
    # Value testing
    length = int(input("Length: "))
    width = int(input("Width: "))
    
    if length <= 0 :
        print("Length is not positive! ")
        return
    
    if width <= 0 :
        print("Width is not positive! ")
        return
    
    # Algo
    area = length * width
    print("The area is: " , area) # print a str + value of area even if area is a int
    
    # Todo : build a more robust value test and implement it
    # Todo : loop while value are not strictly superior to 0

main()