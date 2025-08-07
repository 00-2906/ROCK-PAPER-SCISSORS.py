def exchange_currency():
    convert=0
    dict={
        
    }
    
    my_dict={
        "cad":209.77,
        "usd":283.70,
        "eur":333.84,
        "sa":76.03,
    }
    user_choice=float(input("enter amount (RS):"))
    convert=my_dict["cad"]*user_choice
    print("converted rate from RS to specified currency is:" ,convert)
    convert=my_dict["usd"]*user_choice
    print("converted rate from RS to specified currency is:" ,convert)
    convert=my_dict["eur"]*user_choice
    print("converted rate from RS to specified currency is:" ,convert)
    convert=my_dict["sa"]*user_choice
    print("converted rate from RS to specified currency is:" ,convert)
        
exchange_currency()
    