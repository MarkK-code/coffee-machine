class Coffee:

    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cup = cups
        self.money = money

    def take(self):
        print("\nI gave you $"+str(self.money))
        self.money = self.money - self.money

    def remaining(self):
        print("\nThe coffee machine has:\n" + str(self.water) + " of water\n"
                + str(self.milk) + " of milk\n"+str(self.coffee_beans) + " of coffee beans\n"
                + str(self.cup) + " of disposable cups\n$" + str(self.money) + " of money")

    def fill(self):
        water_fill = int(input("\nWrite how many ml of water do you want to add:\n"))
        milk_fill = int(input("Write how many ml of milk do you want to add:\n"))
        coffee_beans_fill = int(input("Write how many grams of coffee beans do you want to add:\n"))
        cup_fill = int(input("Write how many disposable cups of coffee do you want to add:\n"))
        self.water = self.water + water_fill
        self.milk = self.milk + milk_fill
        self.coffee_beans = self.coffee_beans + coffee_beans_fill
        self.cup = self.cup + cup_fill

    def buy(self):
        no_water = "Sorry, not enough water!"
        no_beans = "Sorry, not enough coffee beans!"
        no_cups = "Sorry, not enough cups!"
        no_milk = "Sorry, not enough milk!"
        choice = input("\nWhat do you want to buy? 1 - espresso,2 - latte, 3 - cappuccino:\n")
        if choice == "back":
            self.run()
        if choice == "1":
            if self.water < 250:
                print(no_water)
                self.run()
            elif self.coffee_beans < 16:
                print(no_beans)
                self.run()
            elif self.cup < 1:
                print(no_cups)
                self.run()
            else:
                print("I have enough resources, making you a coffee!")
                self.water = self.water - 250
                self.coffee_beans = self.coffee_beans - 16
                self.cup = self.cup - 1
                self.money = self.money + 4
        elif choice == "2":
            if self.water < 350:
                print(no_water)
                self.run()
            elif self.milk < 75:
                print(no_milk)
                self.run()
            elif self.coffee_beans < 20:
                print(no_beans)
                self.run()
            elif self.cup < 1:
                print(no_cups)
                self.run()
            else:
                print("I have enough resources, making you a coffee!")
                self.water = self.water - 350
                self.milk = self.milk - 75
                self.coffee_beans = self.coffee_beans - 20
                self.cup = self.cup - 1
                self.money = self.money + 7
        elif choice == "3":
            if self.water < 200:
                print(no_water)
                self.run()
            elif self.milk < 100:
                print(no_milk)
                self.run()
            elif self.coffee_beans < 12:
                print(no_beans)
                self.run()
            elif self.cup < 1:
                print(no_cups)
                self.run()
            else:
                print("I have enough resources, making you a coffee!")
                self.water = self.water - 200
                self.milk = self.milk - 100
                self.coffee_beans = self.coffee_beans - 12
                self.cup = self.cup-1
                self.money = self.money + 6

    def run(self):
        action = input("\nWrite action (buy, fill, take, remaining, exit):\n")
        while action != "exit":
            if action == "take":
                self.take()
            if action == "remaining":
                self.remaining()
            if action == "fill":
                self.fill()
            if action == "buy":
                self.buy()
            self.run()
        exit()


coffee = Coffee(400, 540, 120, 9, 550)
coffee.run()
