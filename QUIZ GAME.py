count=0
answer=" "
choice="y"
while(choice=="y"):
    categories=input("enter the category to choose (h,s,g) :")
    difficulty=input("enter the difficulty (e/m/a) :")
    
    if(categories=="g"):
        if(difficulty=="e"):
            print("Q.01 What is the capital of France ?")
            print("a.paris\nb.rome\nc.london")
            user_answer=input("your answer is:")
            if(user_answer=="a"):
                answer="correct"
                count+=1
            else:
                answer="wrong"

        elif(difficulty=="m"):
            print("Q:02 The president of america before donald trump ?: ")
            print("a.brak obama\nb.george bush\nc.none of these")
            user_answer=input("your answer is:")
            if(user_answer=="a"):
                answer="correct"
                count+=1
            else:
                answer="wrong"
                
        elif(difficulty=="a"):
            print("Q:03 Which lake is largest by area ?")
            print("a.Caspian sea\nb.lake surprior\nc.lake victoria")
            user_answer=input("your answer is:")
            if(user_answer=="a"):
                answer="correct"
                count+=1
            else:
                answer="wrong"
    print("answer of 1st question is:",answer)
    
    if(categories=="s"):
        if(difficulty=="e"):
            print("Q:03 What is largest planet of solar system?")
            print("a.Mars\nb.Earth\nc.Jupiter")
            user_choice1=input("your answer is:")
            if(user_choice1=="c"):
                answer="Correct!"
                count+=1
            else:
                answer="Wrong!"
        elif(difficulty=="m"):
            print("Q:04 Renewable source of energy ?")
            print("a.solar energy\nb.water\nc.coal")
            user_choice1=input("your answer is:")
            if(user_choice1=="a"):
                answer="Correct!"
                count+=1
            else:
                answer="Wrong!"
        elif(difficulty=="a"):
            print("Q:05 The charges flow from ?")
            print("a.From negative to positive\nb.From positive to negative\nc.none of these")
            user_choice1=input("your answer is:")
            if(user_choice1=="a"):
                answer="Correct!"
                count+=1
            else:
                answer="Wrong!"
        print("answer of 2nd question is:",answer)
    
    if(categories=="h"):
        if(difficulty=="e"):
            print("Q:06 When was first world war fought?")
            print("a.1914\nb.1916\nc.1978")
            user_answer2=input("your answer is:")
            if(user_answer2=="a"):
                answer="correct"
                count+=1
            else:
                answer="wrong"
        elif(difficulty=="m"):
            print("Q:07 When Pakistan was formed ?")
            print("a.14 august 1967\nb.13 august 1947\nc.14 august 1947")
            user_answer2=input("your answer is:")
            if(user_answer2=="c"):
                answer="correct"
                count+=1
            else:
                answer="wrong"
        elif(difficulty=="a"):
            print("When was 2nd world war fought ?")
            print("a.1936\nb.1935\nc.1945")
            user_answer2=input("your answer is:")
            if(user_answer2=="b"):
                answer="correct"
                count+=1
            else:
                answer="wrong"
        print("answer of 3rd question:",answer)
    choice=input("do you want to continue (y/n) ?:")
    if(choice !="y"):
        break    
print("final score is:",count)
