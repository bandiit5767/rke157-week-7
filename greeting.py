def get_greeting(daytime):

    if daytime < 12:
        return "good morning"
    elif daytime < 18:
        return "good afternoon"
    else:
        return "good evening"

""" def say_hello(daytime, first_name): #funktsiooni kirjeldus
    
    greeting = get_greeting(daytime)

    print(f"{greeting}, {first_name}") #-//- """