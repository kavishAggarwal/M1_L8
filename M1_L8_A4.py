value_a = int(input("Enter the first number: "))
value_b = int(input("Enter the second number: "))
value_c = int(input("Enter the third number: "))
average = (value_a + value_b + value_c) / 3
print("The average of the three numbers is:", average)

if average > value_a and average > value_b and average > value_c:
    print("The average is greater than all three numbers.")
elif average > value_a and average > value_b:
    print("The average is greater than the first two numbers.")
elif average > value_a and average > value_c:
    print("The average is greater than the first and third numbers.")
elif average > value_b and average > value_c:
    print("The average is greater than the second and third numbers.")
elif average > value_a:
    print("The average is greater than the first number.")
elif average > value_b:
    print("The average is greater than the second number.")
elif average > value_c:
    print("The average is greater than the third number.")
else:
    print("The average is not greater than any of the three numbers.")