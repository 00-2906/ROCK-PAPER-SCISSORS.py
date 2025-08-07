import random
number_to_guess=random.randint(1,100)
choice=1
while True:
    try:
        option=int(input("number of times you want to play:"))
        if(option <=0):
            print("the value entered isn't supported")
            continue
    except Error:
            print("enter a valid number value")
    while choice <=option:
        try:
            guess=int(input("enter the number to guess:"))
            if(guess < number_to_guess):
                print("too low")
            elif(guess > number_to_guess):
                print("too high")
            else:
                print("congratulations you have reached the number")
                print("fewest attempts taken :",choice)
                break
            choice+=1
        except ValueError:
            print("please enter a valid number")
    print("the correct answer is:",number_to_guess)
    play_again=input("do you want to continue (y/n) : ").lower()
    if(play_again !='y'):
        break