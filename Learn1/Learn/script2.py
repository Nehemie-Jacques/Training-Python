from script1  import favorite_food

def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")
    
def main():
    print("This is script2.py")
    favorite_food("sushi")
    favorite_drink("Water")
    print("Goodbye from script2.py")

if __name__ == "__main__":
    main()