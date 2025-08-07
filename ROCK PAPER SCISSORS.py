import random
choices=["r","s","p"]
dict={
    "r":"🪨",
    "s":"✂️",
    "p":"📃",
}

user_choice=input("enter the choice:")
if(user_choice not in choices):
    print("invalid choice")
else:
    print("valid choice")
    
computer_choices=random.choice(choices)

print(f'you choose{dict[user_choice]}')
print(f'computer choose{dict[computer_choices]}')

if(user_choice==computer_choices):
    print("tie")
elif((computer_choices=='r') or(computer_choices=='s'and user_choice=='p') or(computer_choices=='p'and user_choice=='r')):
    print("computer wins")
elif((user_choice=="r")or (user_choice=="s" and computer_choices=="p") or (user_choice=="p"and computer_choices=="r")):
    print ("user wins ")
