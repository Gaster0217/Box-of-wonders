import numpy as np
import time
import random as rnd

Food_items = {
    "meaty pizza": 2000,
    "king burger": 1500,
    "greasy american fries": 1100,
    "schmeckle": 9999,
    "egirl bathwater": 99999,
    "cola": 500
}
Food_supplies = {
    "meaty pizza": 4,
    "king burger": 3,
    "greasy american fries": 3,
    "schmeckle": 2,
    "egirl bathwater": 5,
    "cola": 1
}

gender = ["She", "He"]
reference = ["her", "his"]

Foods = ["meaty pizza", "king burger", "greasy american fries", "schmeckle", "egirl bathwater", "cola"]
prices = np.array([[Food_items["meaty pizza"], Food_items["king burger"], Food_items["greasy american fries"]],
                  [Food_items["schmeckle"], Food_items["egirl bathwater"], Food_items["cola"]]])

drinks = prices[1:, :]
main_course = prices[0:1, :]


class Cafeteria:
    def __init__(self):
        self.cash = 0
        self.supply = 10

    def serve(self, x=""):
        self.supply -= Food_supplies[x]
        self.cash += Food_items[x]

    def surplus(self, x=""):
        self.supply += Food_supplies[x]
        self.cash -= Food_items[x]


class Buyer:
    def __init__(self):
        self.hunger = 15
        self.cash = 5000

    def order(self, x=""):
        self.cash -= Food_items[x]
        self.hunger -= Food_supplies[x]

    def a_turn(self):
        self.hunger += 1

    def work(self, hours):
        self.cash += hours * 40
        self.hunger += np.exp(hours) / 1.5**hours


buyer = Buyer()
lunch = Cafeteria()


def work():
    if buyer.cash < 0:
        print(f"You are currently in debt and you owe {-buyer.cash}")
    buyer.a_turn()
    b = int(input("How many hours?"))
    buyer.work(b)
    print(f"You just worked. You now have {buyer.cash}")


def in_laborer(food):
    if buyer.cash <= 0 or buyer.cash < Food_items[food]:
        print("Sorry! You don't have enough money")
        a = input("Would you like to work? (y/n)").lower()
        if a == "y":
            work()
        else:
            print(f"Lets hope you don't die of starvation! You have {buyer.hunger}, if it crosses 30, its game over!")
    else:
        buyer.order(food)
        print(f"You just ordered {food} worth {Food_items[food]} and you now have {buyer.cash} left")


def rules(customers):
    print(f"You are now playing as the cafeterian. You have {customers} number of customers.")
    print(f"You have {lunch.supply} amount of supplies. The following foods take the following amount of supplies")
    print(Food_supplies)


def in_lunch(customers):
    n = 0
    for i in range(0, customers):
        randomness = rnd.randint(0, 1)
        f = Foods[rnd.randint(0, len(Foods)-1)]
        time.sleep(2)
        print(f"Customer no. {i+1} has placed {reference[randomness]} order. {gender[randomness]} has ordered {f}")
        if lunch.supply <= 0 or lunch.supply < Food_supplies[f]:
            time.sleep(1.5)
            print("You don't have enough supplies")
            time.sleep(0.5)
            o = input("Would you like to surplus? (y/n)")
            if o == "y":
                p = input("What would you like to add?")
                if p in Food_items:
                    lunch.surplus(p)
                else:
                    print("Invalid response, you just lost a customer.")
            else:
                time.sleep(1.5)
                print("Well, its your business that's gonna go downfall not mine.")
        else:
            lunch.serve(f)
            time.sleep(1.75)
            print(f"You managed to serve {f}")
            n += 1
    print(f"You successfully served {n} number of customers")


choice1 = input("What would you like to do [A]Be the customer, [B]Be the lunchlady? ").lower()
if choice1 == "a":
    print(f"Hellooo o//. Welcome to my small cafe!!")
    time.sleep(2)
    print(f"Here, you have to buy food in order to survive but that won't really be easy because cash is hard to comeby!")
    time.sleep(2)
    print(f"You have {buyer.cash} amount of money to start and {buyer.hunger} hunger points (gameover if it crosses 30)")
    time.sleep(2)
    print("Money:", "\n", Food_items)
    time.sleep(2)
    print("Hunger reduction points:", "\n", Food_supplies)
    while True:
        try:
            opt = input("Would you like to [A]work or [B]place order").lower()
            if opt == "a":
                work()
            elif opt == "b":
                food = input("What would you like to order?")
                if food in Food_items:
                    in_laborer(food)
                else:
                    print("Invalid response!")
            else:
                print("Invalid response!")
        except:
            print("Something went wrong!")

elif choice1 == "b":
    customers = rnd.randint(5, 10)
    rules(customers)
    in_lunch(customers)
