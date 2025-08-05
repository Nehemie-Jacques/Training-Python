length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width

print("The area of the rectangle is:", area , "square units.")

item =  input("What item would you like to buy?: ")
price = float(input("What is the price of the item?: "))
quantity = int(input("How many would you like to buy?: "))
total = price * quantity

print("You have bought {quantity} {item} at ${price} each".format(quantity=quantity, item=item, price=price))
print("Your total is: ${total}")

x = 3.14
y = -4
z = 5
result = round(x) # calcule le nombre entier le plus proche
result = abs(y) # calcule la valeur absolue
result = pow(x, y) # calcule la puissance
result = max(x, y, z) # calcule la valeur maximale
result = min(x, y, z) # calcule la valeur minimale
print(result) 

import math
x = 2.9
print(math.pi) # calcule le nombre pi
print(math.e) # calcule le nombre e
print(math.ceil(x)) # calcule le nombre entier le plus proche
print(math.floor(x)) # calcule le nombre entier le plus proche
print(math.sqrt(x)) # calcule la racine carree


import math 
raduis = float(input("Enter the raduis of the circle: "))
area = math.pi * raduis ** 2
circurmference = 2 * math.pi * raduis

print("The area of the circle is:", area , "square units.")
print("The circurmference of the circle is:", circurmference , "units.") 

import math
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = math.sqrt(pow(a, 2) + pow(b, 2)) # calcule la racine carree de a^2 + b^2
print("Side C = {c}".format(c=c)) # "side" est une chaine de caractere

age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
elif age >= 3:
    print("You are a child.")
else:
    print("You are not an adult.")

response = input("Would you like food? (yes/no): ")
if response == "yes":
    print("Here is your food.")
else:
    print("No food for you.")

name = input("Enter your name: ")
if name == "":
    print("You did not enter a name.")
else:
    print("Hello, {name}!".format(name=name))

for_sale = True
if for_sale:
    print("The item is for sale.")
else:
    print("The item is not for sale.")

Python Calculator
operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print("Invalid operator.")

Python weight converter
weight = float(input("Enter your weight: "))
unit = input("Kilograms (kg) or Pounds (lb): ")
if unit == "kg":
    pounds = weight * 2.20462
    print("Your weight in pounds is: {pounds}".format(pounds=pounds))
elif unit == "lb":
    kilograms = weight / 2.20462
    print("Your weight in kilograms is: {kilograms}".format(kilograms=kilograms))
else:
    print("Invalid unit.")

unit = input("Is this temperature in Celsius (C) or Fahrenheit (F): ")
temp = float(input("Enter the temperature: "))
if unit == "C": 
   temp = round((temp * 9/5) + 32)
   print("The temperature in Fahrenheit is: {temp}°F".format(temp=temp)) 
elif unit == "F":
    temp = round((temp - 32) * 5/9)
    print("The temperature in Celsius is: {temp}°C".format(temp=temp))
else:
    print("Invalid unit.")

temp = 25
is_raining = False
if temp > 35 or temp < 0 or is_raining:
    print("It is too hot outside.")
else:
    print("It is not too hot outside.")

temp = 25
is_sunny = True
if temp >= 28 and not is_sunny:
    print("It is too hot outside.")
elif temp <= 20 and is_sunny:
    print("It is too cold outside.") 
else:
    print("It is not too hot outside.")

num = 5
a = 6
b = 7
age = 18
temperature = 25
user_role = "admin"
print("Positive" if num > 0 else "Negative")
print("Positive" if a > 0 and b > 0 else "Negative")
print("Positive" if age >= 18 else "Negative")
print("Positive" if temperature >= 20 else "Negative")
print("Positive" if user_role == "admin" else "Negative")   


name = input("Enter your full name: ")
result = len(name) # calcule la longueur de la chaine de caractere
result = name.upper() # convertit la chaine de caractere en majuscule
result = name.lower() # convertit la chaine de caractere en minuscule
result = name.title() # convertit la chaine de caractere en majuscule la premiere lettre de chaque mot
result = name.strip() # supprime les espaces au debut et a la fin de la chaine de caractere
result = name.split() # convertit la chaine de caractere en une liste de mots
result = " ".join(name) # convertit la liste de mots en une chaine de caractere
result = name.replace(" ", "_") # remplace les espaces par des underscores
result = name.count("a") # calcule le nombre de fois que la lettre "a" apparait dans la chaine de caractere
result = name.startswith("John") # verifie si la chaine de caractere commence par "John"
result = name.endswith("Doe") # verifie si la chaine de caractere se termine par "Doe"
result = name.rfind(" ") # calcule l'index de la derniere occurrence de la chaine de caractere
result = name.find("o") # calcule l'index de la premiere occurrence de la chaine de caractere
result = name.index("o") # calcule l'index de la premiere occurrence de la chaine de caractere
result = name.isdigit() # verifie si la chaine de caractere est un nombre
result = name.isalpha() # verifie si la chaine de caractere est une chaine de caractere
result = name.isalnum() # verifie si la chaine de caractere est une chaine de caractere alphanumerique
result = name.islower() # verifie si la chaine de caractere est en minuscule
result = name.isupper() # verifie si la chaine de caractere est en majuscule
result = name.istitle() # verifie si la chaine de caractere est un titre    
print(result)

credit_number = "1234-5678-9012-3456"
print(credit_number[0]) # affiche le premier caractere
print(credit_number[-1]) # affiche le dernier caractere
print(credit_number[:4]) # affiche la chaine de caractere de 0 a 3
print(credit_number[4:]) # affiche la chaine de caractere de 4 a la fin
print(credit_number[4:8]) # affiche la chaine de caractere de 4 a 7
print(credit_number[::2]) # affiche la chaine de caractere de 0 a la fin en sautant de 2 caractere a la fois

last_digits = credit_number[-4:] # affiche la chaine de caractere de 4 a la fin
print("xxxx-xxxx-xxxx-{last_digits}".format(last_digits)) 

price1 = 31.99
price2 = 10.99
price3 = 19.99
print("Price 1 is ${price1:,.2f}".format(price1=price1))
print("Price 2 is ${price2:,.2f}".format(price2=price2))
print("Price 3 is ${price3:,.2f}".format(price3=price3)) 

num = int(input("Enter a # between 1 and 10: "))
while num < 1 or num > 10:
    print("{num} is not between 1 and 10.")
    num = int(input("Enter a # between 1 and 10: "))
print("{num} is between 1 and 10.")

principale = 0
rate = 0
time 0

while principale <= 0:
    principale = float(input("Enter the principal amount: "))
while rate <= 0:
    rate = float(input("Enter the interest rate: "))
while time <= 0:
    time = float(input("Enter the number of years: "))
while time <= 0:
    time = float(input("Enter the number of years: "))

interest = principale * rate * time
print("The interest is ${interest:,.2f}".format(interest=interest))   

"For loop" permet de parcourir une chaine de caractere, une liste ou un dictionnaire
for x in range(1, 21):
    if x == 13:
        break
    else: 
        print(x)

import time 
my_time = int(input("Enter the number of seconds: "))
for x in range(my_time, 0, -1): # fait une boucle de 0 a my_time en decrementant de 1
    second = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print("{hours:02}:{minutes:02}:{second:02}".format(hours=hours, minutes=minutes, second=second)) 
    time.sleep(1) # attend 1 seconde

    print("Time's up!" )

for x in range(3): # fait une boucle de 0 a 2
    for y in range(1, 10): # fait une boucle de 1 a 9
        print(y, end="") # affiche y sans saut de ligne 
    print()

rows = int(input("Enter the # of rows: "))
colums = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(colums):
        print(symbol, end=""
    )
    print()

List = [] " Une liste est une chaine de caractere, On peut duplicer une liste, elle est mutable" et ordonnée
Set = {} " Un dictionnaire est une chaine de caractere, On ne peut pas duplicer un dictionnaire, elle non ordonnée et non mutable"
Tuple = () " Un tuple est une chaine de caractere, On peut duplicer un tuple, il est ordonné et inmutable"
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print(fruits[1:4])
print(dir(fruits)) # affiche les methodes et attributs de la chaine de caractere
print(len(fruits)) # affiche la longueur de la chaine de caractere
print(help(fruits))

for x in fruits:
    print(fruits)

fruits[0] = "orange"
print(fruits)

fruits.append("lemon")
print(fruits)

fruits.insert(1, "grape")
print(fruits)

fruits.remove("apple")
print(fruits)

fruits.pop(2)
print(fruits)

fruits.sort()
print(fruits)
print(fruits.index("kiwi"))

fruits.reverse()
print(fruits) 

fruits.clear()
print(fruits)

del fruits
print(fruits)

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("\n---- YOUR CART ----")

for i in range(len(foods)):
    print(f"{foods[i]}: ${prices[i]:.2f}")
    total += prices[i]

print()
print("Your total is: ${total}".format(total=total)) 



groceries = [{"apple", "banana", "cherry", "kiwi", "mango"},
{"carrot", "potato", "tomato"},
{"beef", "pork", "chicken"},] 

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print() 

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad: 
    for num in row:
        print(num, end=" ")
    print()

questions = (
    "How many states are in the United States?",
    "Which planet is closest to the sun?",
    "What is the capital of France?",
    "How many letters are in the alphabet?",
    "What is best for making a cup of tea?"
)

options = (
    ("A. 50", "B. 51", "C. 52", "D. 53"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
    ("A. Paris", "B. London", "C. Rome", "D. Madrid"),
    ("A. 26", "B. 27", "C. 28", "D. 29"),
    ("A. Tea", "B. Coffee", "C. Juice", "D. Water")
)

answers = ("A", "A", "A", "A", "D")  
guesses = []
score = 0

for question_num in range(len(questions)):
    print("--------------------------")
    print(questions[question_num])

    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("✅ CORRECT!")
    else:
        print("❌ INCORRECT!")
        print(f"The correct answer was: {answers[question_num]}")

print("--------------------------")
print("          RESULTS         ")
print("--------------------------")

print("Correct answers: ", end="")
for ans in answers:
    print(ans, end=" ")
print()

print("Your guesses    : ", end="")
for g in guesses:
    print(g, end=" ")
print()

percentage = int(score / len(questions) * 100)
print(f"🎯 Your score is: {percentage}%")


capitals = {"USA": "Washington, D.C.",
            "France": "Paris",
            "Germany": "Dortmund",
            "Italy": "Rome",
            "Spain": "Madrid"}

print(dir(capitals))
print(help(capitals))
print(capitals.get("Germany"))

if capitals.get("Germany"):
    print("That capital exists.")
else:
    print("That capital does not exist.")

capitals.update({"Germany": "Berlin"})
capitals.pop("Spain") # supprime le dictionnaire
capitals.popitem() # supprime le dernier dictionnaire
capitals.clear() # supprime tout le dictionnaire

keys = capitals.keys() # renvoie les clés du dictionnaire
for k in capitals.keys():
    print(k)
values = capitals.values() # renvoie les valeurs du dictionnaire
for value in capitals.values():
    print(value)

items = capitals.items()
for item in items:
    print(item)

for key, value in capitals.items():
    print(f"The capital of {key} is {value}")

menu = {"Burger": 3.99,
        "Fries": 1.99,
        "Shake": 1.99,
        "Ice Cream": 2.99,
        "Soda": 1.99,
        "Milkshake": 2.99,
        "Salad": 3.99,
        "Chips": 1.99,
        "Nuggets": 3.99
}

menu_lower = {k.lower(): k for k in menu}

cart = []
total = 0

print("------- MENU -------")
for key, value in menu.items():
    print(f"{key:12}: ${value:.2f}")
print("---------------------")


while True:
    choice = input("Select an item from the menu (q to quit): ").lower()
    if choice == "q":
        break
    elif choice in menu_lower:
        real_name = menu_lower[choice]
        cart.append(real_name)
    else:
        print("That item is not on the menu.")

print("-------- Your order -------")
for food in cart:
    total += menu[food]
    print(f"{food:12} - ${menu[food]:.2f}")
print("-------------------------")
print(f"Total is: ${total:.2f}")

import random

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# number = random.randint(low, high)
# number = random.random()
# option = random.choice(options)
random.shuffle(cards) # mélange les cartes

print(cards)


import random
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num) # génère un nombre aléatoire entre 1 et 100
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit(): # vérifie si la chaine de caractère est un nombre
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low ! Try again ! ")
        elif guess > answer:
            print("Too high ! Try again ! ")
        else:
            print(f"CORRECT ! The answer was {answer}")
            print(f"You guessed the number in {guesses} guesses")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Select a number between {lowest_num} and {highest_num}")

import random

options = ("rock", "paper", "scissors")
running = True

while running: 

    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Draw")
    elif player == "rock" and computer == "scissors":
        print("Player wins")
    elif player == "paper" and computer == "rock":
        print("Player wins")
    elif player == "scissors" and computer == "paper":
        print("Player wins")
    else:
        print("Computer wins") 

    play_again = input("Play again ? (y/n): ").lower()
    if not play_again == "y":
        running = False

print("Thanks for playing !") 


def happy_birthday(name, age):
    print(f"Happy birthday {name}!")
    print(f"You are {age} years old.")
    print("Happy birthday to you !")

happy_birthday("John Doe", 25)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Roberto", 100.01, "2023-01-01")

def add(x, y):
    z = x + y
    return z

def subrract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subrract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return f"{first} {last}"

full_name = create_name("john", "doe")
print(full_name)

def net_price(list_price, discount=0, tax=0):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(100, 0.1, 0.2))

import time

def count(start, end):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("Done!")

count(3, 10)

def hello(greeting, title, first, last):
    print(f"{greeting}, {title} {first} {last}!")

hello("Hello", "Mr.", "John", "Doe")

for x in range(1, 11):
    print(x, end=" ")


def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_number = get_phone("1", "212", "555", "1212")
print(phone_number)

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(1, 2, 3, 4))

def print_address(**address):
    for key, value in address.items():
        print(f"{key}: {value}")

print_address(street="123 Main St", 
              city="Anytown", 
              state="CA", 
              zip="12345")    

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr", "Joseph", "Smith",
               street="123 Main St", 
               city="Anytown", 
               state="CA", 
               zip="12345")

def create_dict():
    dictionary = { "a": 1, "b": 2, "c": 3 }
    return dictionary

dict = create_dict()

print(dict)
for key, value in dict.items():
    print(f"{key}: {value}")

word = "Orange"

letter = input("Guess a letter: ")

if letter in word:
    print("Correct!")
else:
    print("Incorrect!")

students = {"John", "Angel", "Bob", "Alice", "Bob", "John"}

people = input("Enter a name: ")

if people not in students: 
    print(f"{people} is not in the class")
else:
    print(f"{people} is in the class")

grades = {"John": 85, "Alice": 92, "Bob": 78}

student = input("Enter a name: ")

if student in grades: 
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} is not in the class")

doubles = [x * 2 for x in range(1, 11)]
triples = [x * 3 for x in range(1, 11)]

print(doubles)
print(triples)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

fruits = [fruit.upper() for fruit in fruits]

print(fruits)

numbers = [1, 2, -4, 9, -2, 6]
positive_nums = [num for num in numbers if num > 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 != 0]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

def day_of_week(day):
    match day:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        case _:
            return "Invalid day"

print(day_of_week(1))
print(day_of_week(2))
print(day_of_week(3))
print(day_of_week(4))
print(day_of_week(5))
print(day_of_week(6))
print(day_of_week(7))
print(day_of_week(8))

import example

result = example.pi 
result = example.square(5)
result = example.cube(5)
result = example.circumference(5)
result = example.surface_area(5)

print(result)

def show_balance(balance):
    print("************")
    print(f"Your balance is ${balance:.2f}") 
    print("************")

def deposit():
    print("************")
    amount = float(input("Enter the amount to deposit: "))
    print("************")

    if amount <= 0:
        print("Amount must be greater than 0.")
    else:
        return amount

def withdraw(balance):
    print("************")
    amount = float(input("Enter the amount to withdraw: "))
    print("************")

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must br greate than 0")
        return 0
    else :
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
    print("******************")
    print("    Banking Menu    ")
    print("******************")

        print("Banking Menu")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")

        choice = input("Enter your choice(1-4): ")

        if choice == "1":
            show_balance()
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance = -=  withdraw()
        elif choice == "4":
            is_running = False
        else:
            print("**********************************************")
            print("That is not a valid choice. Please try again.")
            print("**********************************************")

    print("**********************************************")
    print("Thank you for using the banking menu")
    print("**********************************************")

    print("Thank you for using the banking menu")

import random  # nécessaire pour random.choice()

# balance initial
balance = 100

# Fonction qui génère une ligne de 3 symboles aléatoires
def spin_row():
    symbols = ['tomato', 'banana', 'cherry', 'kiwi', 'mango']
    result = []
    for _ in range(3):
        result.append(random.choice(symbols))
    return result

# Fonction qui affiche une ligne de symboles
def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

# Fonction qui calcule le gain en fonction du symbole et de la mise
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:  # si les 3 symboles sont identiques
        if row[0] == 'tomato':
            return bet * 3
        elif row[0] == 'banana':
            return bet * 2
        else:  # tous les autres symboles gagnent juste la mise
            return bet * 1
    return 0  # sinon, aucun gain

# Boucle principale du jeu
while balance > 0:
    print(f"💰 Current balance: ${balance:.2f}")
    bet = input("🎲 Place your bet: ")

    if not bet.isdigit():
        print("❌ Invalid bet. Please enter a number.")
        continue

    bet = int(bet)

    if bet > balance:
        print("❌ Insufficient funds.")
        continue

    if bet <= 0:
        print("❌ Bet must be greater than 0.")
        continue

    balance -= bet  # on déduit la mise

    print("🎰 Spinning...\n")
    row = spin_row()
    print_row(row)

    payout = get_payout(row, bet)

    if payout > 0:
        print(f"🎉 You won ${payout:.2f}!")
    else:
        print("😢 Sorry, you lost.")

    balance += payout

    play_again = input("🔁 Play again? (Y/N): ")
    if play_again.lower() != "y":
        break

print("🎮 Game over. Thanks for playing!")

# Bloc standard pour lancer la fonction principale si besoin
# (ici non utilisé mais bon à connaître)
if __name__ == "__main__":
    pass  # rien à lancer automatiquement



# Exercice 2

# Fonction qui teste si un nombre est premier
def est_premier(n):
    if n < 2: 
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

compteur = 0
nombre = 2

# Boucle pour trouver le 512e nombre premier
while True: 
    if est_premier(nombre):
        compteur += 1
        if compteur == 512:
            print(f"Le 512e nombre premier est : {nombre}")
            break
    nombre += 1

# Exercice 3
# Trouver tous les triplets pythagoriciens (p, q, r) tels que p² + q² = r²
# Et retourner le produit maximum p × q × r

max_produit = 0
best_triplet = ()

for p in range(1, 2976): # Ceci représente le 1er coté du triangle
    for q in range(p + 1, 2976 - p): 
    # 2e coté ; p + 1 pour s’assurer que q > p et éviter les doublons 
    # 2976 - p - 1 incluse pour s’assurer que r ne devient ni négatif ni nul
        r = 2976 - p - q # Déduction du troisième coté
        if r <= q: # Vérifie que r > q pour eviter les doublons
            continue
        if p * p + q * q == r * r: 
        # Vérifie si le triplet est pythagoricien cad p² + q² = r²
        # Si oui, le triangle est rectangulaire et on calcule le produit p × q × r
            produit = p * q * r 
            if produit > max_produit:
                max_produit = produit
                best_triplet = (p, q, r)
            
print(f"Le meilleur triplet (p, q, r) est : {best_triplet}")
print(f"Le produit p × q × r est : {max_produit}")  

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"key: {key}")

plain_text = input("Enter a message to encrypt")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

import  random

words = ("apple", "banana", "cherry", "kiwi", "mango")

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" O ",
                   "   ",
                   "   "),
               2: (" O ",
                   " | ",
                   "   "),
               3: (" O ",
                   "/| ",
                   "   "),
               4: (" O ",
                   "/|\\",
                   "  "),
               5:  (" O ",
                    "/|\\",
                    "/  "),
               6: (" O ",
                   "/|\\",
                   "/ \\")}
                
for line in hangman_art[5]:
    print(line)                

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)
    

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    pass

def main():
    answer = random.choice(words)
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint
            guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try again.")
        continue

    guessed_letters.add(guess)

    if guess in answer:
        for i in range(len(answer)):
            if answer[i] == guess:
                hint[i] = guess
    else:
        wrong_guesses += 1

    if "_" not in hint:
        display_man(wrong_guesses)
        display_answer(answer)
        print(f"Congratulations! You guessed the word: {answer}")
        is_running = False
    elif wrong_guesses >= len(hangman_art) - 1:
        display_man(wrong_guesses)
        display_answer(answer)
        print(f"Game over! The word was: {answer}")
        is_running = False

if __name__ == "__main__":
    main()

from car import Car

car1 = Car("Ford", "Mustang", 2022)
car2 = Car("Tesla", "Model S", 2023)
car3 = Car("Toyota", "Camry", 2021)

car1.drive()

class student:
    class_year = 2025
    num_students = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        student.num_students += 1

student1 = student("George", 30)
student2 = student("Alice", 25)
student3 = student("Bob", 22)
student4 = student("John", 28)

print(student1.name)
print(student1.age)
print(student1.class_year)

print(student2.name)
print(student2.age)
print(student2.class_year)

print(f"Total number of students: {student.num_students}")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def make_sound(self):
        print(f"{self.name} says {self.sound}") 

class Dog(Animal):
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

class Cat(Animal):
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

dog = Dog("Fido", "woof")
cat = Cat("Garfield", "meow")

dog.eat()
dog.sleep()
dog.make_sound()

cat.eat()
cat.sleep()
cat.make_sound()


class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is a {self.color} shape that is {'filled' if self.is_filled else 'not filled'}.")        

class Circle(Shape):
    def __init__(self, color, is_filled, raduis):
        super().__init__(color, is_filled)
        self.raduis = raduis

    def describe(self):
            super().describe()
        print(f"It is a circle with an area of {3.14 * self.raduis * self.raduis:.2f}cm^2")
        
class Square(Shape):
    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled)
        self.side = side

class Triangle(Shape):
    def __init__(self, color, is_filled, base, height):
        super().__init__(color, is_filled)
        self.base = base
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {0.5 * self.base * self.height:.2f}cm^2")
        super().describe()

circle = circle(color="red", is_filled=True, raduis=5)

square = square(color="blue", is_filled=False, side=4)

triangle = triangle(color="green", is_filled=True, base=6, height=4)

print(circle.color)
print(circle.is_filled)
print(circle.raduis)

print(square.color)
print(square.is_filled)
print(square.side)

print(triangle.color)
print(triangle.is_filled)
print(triangle.base)
print(triangle.height)



from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
        
class Circle(Shape):
    def __init__(self, raduis):
        def.raduis = raduis

        def area(self):
            return 3.14 * self.raduis ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Pizza(Circle):
    def __init__(self, topping, raduis):
        super().__init__(raduis)
        self.topping = topping

shaps = [Circle(5), Triangle(10, 5), Pizza("pepperoni", 5)]

for shape in shapes:
    print(f"{shape.area()}cm²")