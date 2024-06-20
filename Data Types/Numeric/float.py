# num1=float(input("Enter the first number: "))
# num2=float(input("Enter the second number: "))

# #Basic Arithmetic 
# result1=num1 + num2 
# print("Addition:", result1)

# result2=num1 - num2 
# print("Subtraction:", result2)

# result3 = num1 * num2      
# print("Multiplication:", result3)

# result4 = num1 / num2      
# print("Division:", result4)

# #Rounding 
# result5=round(3.13345555, 2)
# print("Rounded: ", result5)    


#example 2

op1=int(input("Enter a number 1-Arithmetic 2-Rounding : "))
if op1==1:
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))

    #Basic Arithmetic 
    result1=num1 + num2 
    print("Addition:", result1)

    result2=num1 - num2 
    print("Subtraction:", result2)

    result3 = num1 * num2      
    print("Multiplication:", result3)

    result4 = num1 / num2      
    print("Division:", result4)
elif  op1==2:
#Rounding 
    n=int(input("How many decimal places do you want? ")) 
    d=float(input("What is the number to be rounded? "))    
    r=round(d,n)
    print("Rounded: ", r)    