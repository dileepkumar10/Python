# score=int(input("Enter your score: "))
# if score >=90:
#     print("The grade is A")
# elif score >= 80:
#     print("The grade is B")
# elif score >=70:
#     print("The grade is c")
# else:
#     print("The grade is D")

#Write a program which asks the user for a number. If number is even print ‘Even’, else print ‘Odd’.
# n=int(input('Please enter a number: '))
# if  n%2==0:
#     print('Even')
# else:
#     print('odd')       


#Leap Year Checker:

year=int(input("Enter year to check leap year :"))
if year / 4 ==0 and  year /100 !=0 or year / 400 ==0:
    print(f'{year} is the leap year')
else:
    print(f"{year} is not leap year")