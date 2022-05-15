import random

Pj_Health = 50
Enemy_Health = 50
Round_Counter = 100

# Title screen

def print_lines(text):
    print("-" * len(text))
    
def print_highlighted_text(text):
    print_lines(text)
    print(text)
    print_lines(text)    

print_highlighted_text("| Welcome to RPyG_Battle |")

# Gameloop

while True:
    
    Attack = random.randrange(0, 12)
    print("Enemy attack Pj for:",  Attack, " pts")
    Pj_Health = Pj_Health - Attack
    
    print("Health is now : ", Pj_Health)

    Round_Counter = Round_Counter - 1
    print(Round_Counter, " Round(s) left")

    if Pj_Health <= 0 :
        print_highlighted_text("| Pj is dead |")
        break
        
        
    if Round_Counter == 0:
        break
        
print("Final Pj_Health", Pj_Health)