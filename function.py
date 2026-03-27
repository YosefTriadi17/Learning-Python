def total_price(price, quantity = 292):
    total = price * quantity
    return total

def print_hello():
    print("Hello Dari Function World!")

print_hello()

print(total_price(500000, 9))

# Default Argument
print(total_price(500000))

# Keyword Argument
print(f"Total harga 3 adalah: {total_price(quantity = 9, price = 500000)}") 

def helo_user(name):

    result = f"Hello {name}, Semoga harimu menyenangkan"
    print(result)

helo_user("Budi")

def area_of_circle(radius = 50):
    pi = 3.14159
    area = pi * radius**2
    return area

area1 = area_of_circle(5)
print(f"Luas area 1 adalah: {area1}")
area2 = area_of_circle(10)
print(f"Luas area 2 adalah: {area2}")
area3 = area_of_circle()
print(f"Luas area 3 adalah: {area3}")


def print_profile(name, age, address = "Jakarta", work = "Programmer"):
    print()
    print(f"==== Profile {name} ====")
    print(f"Age: {age}")
    print(f"Address: {address}")
    print(f"Work: {work}")

print_profile("Andi", 25)
print_profile("Budi", 30, "Bandung")
print_profile("Cici", 28, work="Scientist", address = "Australia")
print_profile("Deni", 35, work = "Data Analyst")


# Global Variable
global_name = "Andi"

def show_name():
    print(f"Global Name: {global_name}")

def change_name(new_name):
    global global_name
    global_name = new_name

show_name()
change_name("Budi")
show_name()

global_name = "Cici"
show_name()


# Dinamic Parameter
def print_info(*args):
    print()
    for item in args:
        print(item)

def print_dict(**kwargs):
    print()
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info("Andi", "Budi", "Cici", "Deni", "Cindy", "Kezia")
print_dict(name = "Cindy", age = 20, address = "Jakarta", work = "Programmer")   