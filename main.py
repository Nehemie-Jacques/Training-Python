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