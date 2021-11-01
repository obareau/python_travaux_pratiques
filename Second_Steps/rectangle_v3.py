# coding: utf-8

# let's improve our rectangle by using parameters

import sys

def main():
    if len(sys.argv) != 3:
        exit("Needs 2 arguments: width length") # ! 2 arguments separated with a space  
    
    # Asking parameters    
    width = int(sys.argv[1] ) 
    length = int(sys.argv[2] )
    
    # Check parameters
    if length <= 0:
        exit("length is not positive")
        
    if width <= 0:
        exit("width is not positive")
    
    # Return values    
    area = length * width
    print("The area is: ", area)
    
main()