# Cafe items
menu = {
    1: "Capiccino",
    2: "Latte",
    3: "Espresso",
    4: "Americano"
    }
# Cafe stock
stock = {
    "Capiccino": 189,
    "Latte": 78,
    "Espresso": 90,
    "Americano": 55
}
# Cafe item prices
price = {
    "Capiccino": 45,
    "Latte": 40,
    "Espresso": 35,
    "Americano": 40
}
# Total worth of stock in cafe
total_worth = 0
# Calculate total worth of stock
for item in stock:
    total_worth += stock[item] * price[item]
# Print total worth of stock
print("Total worth of stock in cafe: R", total_worth)
