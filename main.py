my_name= input('what is your name?')
my_age= input("what is your age?")
print(f"my name is {my_name} and i am {my_age} years old")
first_number= int(input(("give me a number?")))
secound_number= int(input(("give me a secound number?")))
operayion= input(("/*-+?"))
if operayion == "+":
    print(first_number+secound_number)
elif operayion == "-":
    print(first_number-secound_number)
elif operayion == "*":
    print(first_number*secound_number)
elif operayion == "/":
    print(first_number/secound_number)
else:
    print("the operayion is not valid" ) 
bus_capacity= 30 
people_inbus= int(input("give me a numder about the people inbus"))
people_watimg = int(input("give me a number about the people people wating"))
empty_seats = bus_capacity - people_inbus
if empty_seats<people_inbus: 
        print("empty seats is avalible")

else:
       print("the bus is full")