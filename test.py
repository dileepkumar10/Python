
# for num in range(1,6):
#     print(f'The square of given number is {num*num}')

# for num in range(1, 6):
#     square = num * num
#     print(square)

# name=input("Enter the name to check charector  count : ")

# print(len(name))

# name=list(name.lower())
# print(name)

# num=int(input('Enter a number: '))
# for i in range(1,11, 2):
#     prod=i*num
#     print(f'{num}  x {i} = {prod}')


def mul(num):
    if num ==0:
        print('please  enter non zero value')
    else:    
        
            for i in range(1,11,1):
                prod=i*num
                print(f'{num} x {i} = {prod}')
            
            return f'{num} x {i} = {num*i}'
                
        
#print(mul(5))
    
# m=int(input("Enter the number: "))
# mul(m)