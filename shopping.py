product1 = input("Please enter product name: ")
product2 = input("Please enter product name: ")
product3 = input("Please enter product name: ")
product1_price = float(input("What is the price of " + product1 + " "))
product2_price = float(input("What is the price of " + product2 + " "))
product3_price = float(input("What is the price of " + product3 + " "))
total = {product1_price, product2_price, product3_price}
res = sum(total)
print(res)
# found how to do the above on https://www.geeksforgeeks.org/python-program-to-find-sum-of-elements-in-list/
num = {product1_price, product2_price, product3_price}
avg = sum(num) /len (num)
print(avg)
# Found how to do the average on https://www.geeksforgeeks.org/find-average-list-python/
print("The Total of {}, {}, {} is R{} and the average price of the items is R{}.".format(product1, product2, product3, res, avg))