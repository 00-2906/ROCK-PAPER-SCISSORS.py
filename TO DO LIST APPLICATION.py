print("------------------TO DO TASK--------------------")
print("1.add task\n2.remove task\n3.view task\n4.exit")
list=[ ]
option="y"
while(True):
    choice=int(input("enter the option user wants to select:"))
    if(choice >=1 and choice <=4):
        print("valid choice")
    else:
        print("not valid choice")
    if(choice==1):
        filter=input("select the filter (w/d) : ")
        while(option=="y"):
            if(filter=="w" or filter=="d"):
                user_add=input("enter the task user wants to add in the list:")
                list.append(user_add)
            else:
                print("not valid filter")    
            option=input("do you want to continue ?: ")
            if(option !="y"):
                break
    if(choice==2):
        user_mark=int(input("enter the task user wants to mark from list:"))
        try:
            if(list[user_mark]):
                print(list[user_mark],"->","completed")
                print(list)
        except:
            print("not in list")
    elif(choice==3):
        print(list)
    elif(choice==4):
        print("exit")
    
 