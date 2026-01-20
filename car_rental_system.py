import time
import random
import os
from datetime import datetime

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def now():
    return datetime.now().strftime("%c")

# All Car Data Stored in Code
CAR_DATA = {
    1: {
        "type": "SUV",
        "cars": {
            1: ("MAHINDRA THAR", 5500),
            2: ("TATA NEXON", 4000),
            3: ("TOYOTA FORTUNER", 6000)
        }
    },
    2: {
        "type": "Sports Car",
        "cars": {
            1: ("LAMBORGHINI", 50000),
            2: ("MC LAREN", 25000),
            3: ("NISSAN GTR", 27200)
        }
    },
    3: {
        "type": "Coupe",
        "cars": {
            1: ("PORSCHE CAYENNE", 15100),
            2: ("AUDI R8", 120000),
            3: ("FERRARI ROMA", 130000)
        }
    },
    4: {
        "type": "Convertible",
        "cars": {
            1: ("JAGUAR", 15000),
            2: ("BENTLEY CONTINENTAL GT", 100000),
            3: ("MERCEDES E-CLASS", 10500)
        }
    },
    5: {
        "type": "Sedan",
        "cars": {
            1: ("HONDA CITY", 9500),
            2: ("MERCEDES", 25000),
            3: ("BMW 7-SERIES", 15000)
        }
    }
}

class Greeting:
    def welcome(self):
        print(now())
        print("\n🚗 WELCOME TO CAR RENTAL SYSTEM 🚗\n")
        time.sleep(1)
        print("Starting the program", end=" ")
        for _ in range(5):
            print(".", end=" ", flush=True)
            time.sleep(1)
        print("\n")

    def exit(self):
        clear()
        print(now())
        print("\n🙏 THANK YOU FOR USING CAR RENTAL SYSTEM 🙏")
        time.sleep(2)

def login():
    PASSWORD = "abcdefgh"
    while True:
        clear()
        print(now())
        print("\nCAR RENTAL SYSTEM LOGIN\n")
        ch = input("Enter Password (8 characters): ")
        if ch == PASSWORD:
            print("\nACCESS GRANTED")
            time.sleep(2)
            break
        else:
            print("\nACCESS DENIED!")
            input("Press Enter to try again...")

class Car:
    def __init__(self):
        self.ch1 = self.ch2 = 0
        self.t = self.d = 0
        self.cc = self.drc = 0
        self.car = ""
        self.name = ""

    def details(self):
        clear()
        print(now())
        self.name = input("\nEnter your name: ")
        self.t = int(input("For how many hours do you want the car? "))
        self.d = int(input("For how many kilometers do you want the car? "))
        driver = input("Do you want a driver? (Y/N): ")
        self.drc = 2500 if driver.lower() == "y" else 0

        print("\nLoading", end="")
        for _ in range(3):
            time.sleep(1)
            print(" .", end="")
        print()

    def cartype(self):
        clear()
        print("\nAvailable Car Types:\n")
        for key, value in CAR_DATA.items():
            print(f"{key}. {value['type']}")
        self.ch1 = int(input("\nEnter your choice: "))

    def show_cars(self):
        clear()
        selected = CAR_DATA[self.ch1]
        print(f"\n{selected['type']} Cars:\n")
        for key, (name, price) in selected["cars"].items():
            print(f"{key}. {name} - ₹{price}/hour")
        self.ch2 = int(input("\nEnter your choice: "))

    def select(self):
        self.car, self.cc = CAR_DATA[self.ch1]["cars"][self.ch2]

    def rent(self):
        clear()
        print(now())
        invoice = random.randint(1000, 9999)
        caution = self.cc * 0.25
        advance = self.cc * 0.60
        total = self.cc + self.drc + caution

        print("\n\t\tCUSTOMER INVOICE")
        print("\t\t" + "-"*55)
        print(f"\t\tInvoice No: {invoice}")
        print(f"\t\tCustomer Name: {self.name}")
        print(f"\t\tCar Model: {self.car}")
        print(f"\t\tHours: {self.t}")
        print(f"\t\tKilometers: {self.d}")
        print(f"\t\tRent Cost: ₹{self.cc}")
        print(f"\t\tDriver Cost: ₹{self.drc}")
        print(f"\t\tCaution Money: ₹{caution}")
        print(f"\t\tAdvance: ₹{advance}")
        print("\t\t" + "-"*55)
        print(f"\t\tTOTAL AMOUNT: ₹{total}")
        print("\t\t" + "-"*55)
        input("\nPress Enter to continue...")

def loading():
    clear()
    print(now())
    for msg in ["CALCULATING RENT", "PLEASE WAIT", "GENERATING INVOICE"]:
        print(f"\n{msg}", end="")
        for _ in range(3):
            time.sleep(1)
            print(" .", end="")
    print()

def main():
    g = Greeting()
    g.welcome()
    login()

    c = Car()
    c.details()

    while True:
        c.cartype()
        c.show_cars()
        c.select()

        clear()
        ask = input(f"\nConfirm {c.car}? (Y/N): ")
        if ask.lower() == "y" and random.randint(1, 10) % 2 == 0:
            print("\nCHOICE CONFIRMED")
            time.sleep(2)
            break
        else:
            print("\nSORRY! Car not available. Choose again.")
            time.sleep(2)

    loading()
    c.rent()
    g.exit()

if __name__ == "__main__":
    main()