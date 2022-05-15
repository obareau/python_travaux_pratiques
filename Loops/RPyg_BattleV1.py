import random

Screen_title =("| Welcome to RPyG_Battle |")

print("-" * len(Screen_title))

print(Screen_title)
print("-" * len(Screen_title))
print_lines()

Pj_Health = 50
Enemy_Health = 50
Round_Counter = 100

while True:
    
    Attack = random.randrange(0, 12)
    print("Enemy attack Pj for:",  Attack, " pts")
    Pj_Health = Pj_Health - Attack
    
    print("Health is now : ", Pj_Health)

    Round_Counter = Round_Counter - 1
    print(Round_Counter, " Round(s) left")

    if Pj_Health <= 0 :
        print("Pj is dead")
        break
        
        
    if Round_Counter == 0:
        break
        
print("Final Pj_Health", Pj_Health)