class Automobile:
    type = "Automobile industry"
    def __init__(self, name, ceo, founded):
        self.name = name
        self.ceo = ceo
        self.founded = founded
        self.store = []
        self.net_worth = 0
        
    def information(self):
        print (f"""
            This is {self.name} industry owned by {self.ceo}. Founded in the year {self.founded}.
            Mr {self.name} is one of the greatest developer
            """)
    
    def add_a_car(self):
        name = input("Name of car: ")
        color = input("Name of color: ")
        make = input("Make of car: ")
        year = int(input("year when car was created: "))
        price = float(input("Price of car: "))

        print()
        add_to_dictionary = { "name": name, "color": color, "make": make, "year": year, "price": price}
        self.store.append(add_to_dictionary)
        print(f"\ncar added to store.")

    def view_cars(self):
        choice = input("1. show all cars\n2. show a car\n(choose 1/2): ")
        if choice == "1":    
            index = 0
            for car in self.store:
                index += 1
                print(f"{" "*6}({index})")
                print(f"{"Name":10}:{car["name"]}\n{"Color":10}:{car["color"]}\n{"Make":10}:{car["make"]}\n{"Year":10}:{car["year"]}\n{"Price":10}:{car["price"]}\n")
            if not self.store:
                print("\nNo car available in Store\n")
        
        elif choice =="2":
            choose_car= input("Which car would like to view?: ")
            found = False
            for car in self.store:
                if choose_car == car["name"]:
                    print("##"*20)
                    print(f"{"Name":10} { car["name"]}\n{"Color":10} { car["color"]}\n{"Make":10} { car["make"]}\n{"Year":10} { car["year"]}\n{"Price":10} { car["price"]}\n")
                    found = True
                    print("##"*12)

            if not found:
                print(f"\n{choose_car} does not exist in store\n")


    def calculate_networth(self):
        for car in self.store:
            self.net_worth += car["price"]
        else:
            if self.net_worth == 0:
                print(f"{"=="*24}\nYou have ${self.net_worth} in your company.\nGo and get your car assets\n{"=="*24}")
            else:
                print(f"You have ${self.net_worth} in your company.")    

    def deleting_car(self):
        choice = self.store.pop(int(input("Which car do you choose to remove from system?: "))-1)
        print(f"\n{choice["name"]} has been removed from system.\n")             

    def run_industry(self):
      print(f"{"=="*24}\nWelcome to {self.name}. what do you want to do today?\n{"=="*24}")
      while True:    
        options = input("\n1. Add a car.\n2. View cars\n3. View networth\n4. About the industry\n5. Delete a car\n6. Exit\nchoose(1/2/3/4): ")

        if options == "1":
            self.add_a_car() #calling the add_to_car method
        elif options == "2":
            self.view_cars()
        elif options == "3":
            self.calculate_networth()
        elif options == "4":
            self.information()
        elif options == "5":
            self.deleting_car()
        elif options == "6":
            break





if __name__=="__main__":
    jola = Automobile("Kal Motors","Kalada", 2024)
    jola.run_industry()

