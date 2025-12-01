start = 0
#Ask user for a number and keep adding it to start until the user enters -1
user_number = int(input("Enter a number, to stop enter -1: "))
#Add while to loop until user enters -1
while user_number != -1:
    start += user_number
    user_number = int(input("Enter a number, to stop enter -1: "))
#Endthe loop when the user enters -1 and print the sum
print("The sum of the numbers is:", start)
