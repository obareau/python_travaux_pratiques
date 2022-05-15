import random

Pj_Health = 50
Enemy_Health = 50
Round_Counter = 10
Pj_Rank = ("Lord") 


# Title screen

def print_lines(text):
    print("-" * len(text))
    
def print_highlighted_text(text):
    print_lines(text)
    print(text)
    print_lines(text)    

print_highlighted_text("| Welcome to RPyG_Battle |")
Pj_Name = input("Please enter your name : ")
End_Message = (Pj_Rank + Pj_Name," is dead !")
# Gameloop

while True:
    
    Attack = random.randrange(0, 12)
    print("Enemy attack Pj for:",  Attack, " pts")

    if Attack <= 6:
        Pj_Health = Pj_Health +3
        print("It was à lame hit")
        print("Health is now : ", Pj_Health)
        print("-")
        
    
    elif Attack >= 10:
        Pj_Health = Pj_Health - 4    
        print("It was a Critical hit !!!" )
        print("Health is now : ", Pj_Health) 
        print("*")
        
    
    if Attack > 6 and Attack < 10: 
        print("Enemy could do better next time..")
        print("Health is now : ", Pj_Health)    
        print(".")
        
    Pj_Health = Pj_Health - Attack
    
    

    Round_Counter = Round_Counter - 1
    print(Round_Counter, " Round(s) left")

    if Pj_Health <= 0 :
        print(f"{Pj_Rank} {Pj_Name.title()} is dead")
        break
        
        
    if Round_Counter == 0:
        print(f"{Pj_Rank} {Pj_Name.title()} Ecaped")
        break
        
print("Final Pj_Health", Pj_Health)