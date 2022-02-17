
# Input number to be tested and then result will be printed


a_number = int(input("Please enter a number: "))
if a_number < 5:
    print("Number is less than 5")
elif a_number > 10:
    print("Number is greater than 10")
else:
    print("Number is greater than 5 and it is less than 10")

choice = "Okay" if a_number < 5 else "Not Okay"
print(choice)