class Computer:
    def __init__(self, max_price):
        self.__max_price = max_price

    def sell(self):
        print(f"Selling Price: {self.__max_price}")

    def set_max_price(self, price):
        s# Operator Overloading Example

class Comparable:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

# Creating objects
ob1 = Comparable(3)
ob2 = Comparable(4)

# Comparing values
print(ob1 < ob2)  # Output: True
print(ob1 == ob2) # Output: False

# Additional objects for testing
ob3 = Comparable(3)
ob4 =lf.__max_price = price

# Create an object for the class Computer
computer = Computer(1000)

# Display the initial selling price
computer.sell()

# Change the value of max price
computer.set_max_price(1200)

# Display the updated selling price
computer.sell()
