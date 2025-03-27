print("---------------------------Basic Calcualtor--------------------------")

operator = input("Enter An Operator (+ - * /): ")
num1 = float(input("Enter The First NUM"))
num2 = float(input("Enter The Second NUM"))

if operator == "+":
    result  =  num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result  =  num1 * num2
    print(result)
elif operator == "/":
    result  =  num1 / num2
    print(round(result, 3))

else:
    print(f"{operator} aint a valid operator")

print("---------------------------------------------------------------------")
print("---------------------------Basic Weight Converters Or Pounds (K or L): ")

if unit == "K":
    weight = weight * 2.205 
    unit = "Lbs"
    print(f"Your Weight is: {round(weight, 1)} {unit}")

elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your Weight is: {round(weight, 1)} {unit}")

else:
    print(f"{unit} is not valid")

print("-------------------------------------------------------------------------")
print("---------------------------Basic Temp Converter--------------------------")

unit = input("Is This Tempreature in Celcuis OR Farenhite (C/F): ")
temp = float(input("Enter The Tempreature: "))

if unit == "C":
    temp = round((9*temp)/5+32 ,1)
    print(f"The Tempreature In Faherenite is: {temp} F")

elif unit == "F":
    temp = round((temp - 32)* 5/9, 1)
    print(f"The Tempreature In Celcius is: {temp} C")

else:
    print("f{unit} is an invalid unit of measurement")

print("-------------------------------------------------------------------------")
print("---------------------------Basic Email Slicer----------------------------")

email = input("Enter Your Email")
index_num = email.index("@")

username = email[:index_num]
domain = email [index_num+1:]

print(f"Your Fucking Usernmae is {username} and domin name is{domain}")

print("-------------------------------------------------------------------------")
print("-------------------Basic Compund Intrest Calculator----------------------")


principle = 0
rate = 0
time = 0

while principle<=0:
    principle = float(input("Enter The Principle AMT"))
    if principle < 0:
        print("PRINCIPLE CAN'T BE LESS THAN OR EQ TO 0")

while rate<=0:
    rate = float(input("Enter The Principle AMT"))
    if rate < 0:
        print("PRINCIPLE CAN'T BE LESS THAN OR EQ TO 0")

while time<=0:
    time = float(input("Enter The Principle AMT"))
    if time < 0:
        print("PRINCIPLE CAN'T BE LESS THAN OR EQ TO 0")

total_balance = principle*pow((1+rate/100),time)
print(f"Balance after {time} year/s ${total_bal:.2f} ")

print("******************Another Way*********************")

principle = 0
rate = 0
time= 0

while True:
    principle = float(input("Enter The Principle AMT:"))
    if principle < 0:
        print("PRINCIPLE CAN'T BE LESS THAN OR EQ TO 0")
    else:
        break

while True:
    rate = float(input("Enter The Rate:"))
    if rate < 0:
        print("Rate CAN'T BE LESS THAN OR EQ TO 0")
    else:
        break

while True:
    time = int(input("Enter The Time AMT:"))
    if time < 0:
        print("Time CAN'T BE LESS THA OR EQ TO 0")
    else:
        break

total_bal = principle * pow((1+rate/100),time)
print(f"New Balance After {time} year/s ${total_bal:.2f}")

print("-------------------------------------------------------------------------")
print("-------------------------Countdown Timer---------------------------------")

import time


my_time = int(input("enter TIme In Sec"))

for x in range(my_time,0,-1):
    seconds = x%60
    minutes = int(x/60)%60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Wake Up")
print("-------------------------Shopping-Cart-Program----------------------------")

foods = []
prices = []
total = 0

while True:
    food = input("Enter A food to buy (q to Quit): ")
    if food.lower()=="q":
        break
    else:
        price = float(input(f"Enter The Price of {food} in $"))
        foods.append(food)
        prices.append(price)

print("------Your Cart------")


for food in foods:
    print(food, end = ", ")

for price in prices:
    total+=price
    
print()
print(f"Your Total is {total}")
print("-------------------------------------------------------------------------")
print("-------------------------Quiz-Game-Program-------------------------------")
questions = ("How MAny Elements Are There iN Periodic Table","Which Animal Lays The Largest Eggs",
"Which Is the most Abudant Gas On the PLanet's Atmopshere","How Many Bones Are There In Human Body",
"Which PLanet In The Solar System Is The Hottest: ")

options = (("A. 116","B. 117","C. 118","D. 119"),
("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
("A. Nitrogen","B. Oxygen","C. Carbon-Dioxide","D. Hydrogen"),
("A. 200","B. 207","C. 208","D. 209"),
("A. Mercury","B. Venus","C. Earth","D. Mars"))

answers = ("C","D","A","A","B")
guesses = []
score = 0
queno = 0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[queno]:
        print(option)
     

    guess = input("Enter A,B,C,D: ").upper()
    guesses.append(guess)
    if guess == answers[queno]:
        score+=1
        print('Correct!!!')
    else:
        print("Incorrect")
        print(f"{answers[queno]} is the correct answer")
    queno+=1

print('-'*40)
print("                 Result                ")
print('-'*40)

print('Answers',end="") 
for answer in answers:
    print(answer,end="  ")
print()

print('Guess',end="") 
for guess in guesses:
    print(guess,end="  ")
print()

score = int(score/len(questions)*100)
print(f"Your Score Is {score}%")
print("-------------------------------------------------------------------------")
print("---------------------Concession-Stand-Program----------------------------")
menu = {"pizza": 3.00, 
"waafers": 4.50,
"popcorn": 6.00,
"fries": 2.50,
"chips": 1.00,
"pretzel":3.50,
"soda":3.00,
"lemonade":4.25}

cart = []
total = 0
print("------------------MENU----------------")
for key,value in menu.items():
    print(f"{key}: ${value:.3f}")
print("------------------MENU----------------")

while True:
    food = input("Select AN Item Or Q To QUit: ").lower()
    if food == "q":
        break 

    elif menu.get(food) is not None:
        cart.append(food)


print("--------------Order-------------")
for food in cart:
    total += menu.get(food)
    print(food,end=" ")

print()
print(f"Total is {total:.2f}")
print("-------------------------------------------------------------------------")
print("---------------------Number-Guessing-Game----------------------------")
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)
guesses = 0 
is_running = True


print("Welcome To Py NUm GUess Game")
print(f"Select A Num BEtween {lowest_num} and {highest_num}")

while is_running:
    

    guess = input("Enter A Random Guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That NUmber is out of range")
            print(f"Select A Num BEtween {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too Low! Try Again")
        elif guess > answer:
            print("Too High Try Again")
        else:
            print(f"Correct Shit {answer} ")
            print(f"Guesses {guesses}")

    else:
        print("Invalid Guess")
        print(f"Select A Num BEtween {lowest_num} and {highest_num}")
print("-------------------------------------------------------------------------")
print("-----------------------------SET--1--------------------------------------")




        
