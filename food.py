def order(name):
    print("Welcome to Gaster's food products " + name + "!")
    desire = input("[A]place order, [B]leave")
    desire = desire.lower()
    prices = {
    "pizza" : 50,
    "hamburger" : 45,
    "dumplings" : 52,
    "nayo's pudding" : 24,
    "grilled cheese" : 37
    }
    food_list = ["pizza", "hamburger", "dumplings", "nayo's pudding", "grilled cheese"]
    if desire == "a":
        for i in range(0, len(food_list)):
            j = i + 1
            print(j, ":", food_list[i], ":", prices[food_list[i]])
        order = input("Would you like to place an order? (y/n) ")
        order = order.lower()
        if order == "y":
            item = input("What would you like to order? ")
            item = item.lower()
            if item in food_list:
                print("Then, the price will be", prices[item])
                print("Thank you for visiting us!")
            else:
                print("Your order is invalid.")
        elif order == "n":
            print("Ah, well, thank you for coming by.")
        else:
            print("Well, I will just assume you want to leave.")
    elif desire == "b":
        print("Thank you for joining us!")
    else:
        print("Okay, byeee")

n = input("Enter your name please: ")
order(n)
