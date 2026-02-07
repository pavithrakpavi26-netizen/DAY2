name = input("Enter your name: ")
age = input("Enter your current age: ")
age = int(age)
new_age = age + 4
print(f"Hey {name}, you will be {new_age} years old in 2030.")

total_bill = float(input("Enter the total bill amount: "))
people = int(input("Enter the number of people: "))
share = total_bill / people
print(f"Total Bill: {total_bill}")
print(f"Each person pays: {share}")

print(type(total_bill))
print(type(people))
print(type(share))


item_name = "Laptop"
quantity = 2
price = 499.99
in_stock = True
total_cost = quantity * price
print("Item:", item_name)
print("Quantity:", quantity)
print("Price:", price)
print("Available:", in_stock)
print("Total Cost:", total_cost)

