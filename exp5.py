num = int(input("Enter a number up to which the odd and even numbers should be listed: "))

for i in range(num + 1):  
    if i % 2 == 0:
        print(str(i) + " is even")
    else:
        print(str(i) + " is odd")


num = int(input("Enter a number up to which the odd and even numbers should be listed: "))

while num >= 0:  
    if num % 2 == 0:
        print(str(num) + " is even")
    else:
        print(str(num) + " is odd")
    num -= 1
