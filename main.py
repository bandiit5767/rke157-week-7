import datetime
from hello import say_hello

hour = datetime.datetime.now().hour #andmed
name = input("enter your first name: ") #andmed

""" def get_greeting(daytime):

    if daytime < 12:
        return "good morning"
    elif daytime < 18:
        return "good afternoon"
    else:
        return "good evening"

def say_hello(daytime, first_name): #funktsiooni kirjeldus
    
    greeting = get_greeting(daytime)

    print(f"{greeting}, {first_name}") #-//- """

say_hello(hour, name) #funktsiooni väljakutsumine
