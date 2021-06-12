#1 Write a Python prgram to find those number which are divisible by 7,5 , between 1500 and 2700(both included).

# for i in range(1500,2701):
#     if(i%7==0 and i%5==0):
#         print(i)

#2 Write a Python program to count the number of even and odd numbers from a series of numbers .

# even=0
# odd=0
# for i in range(1,100):
#     if(i%2==0):
#         even+=1
#     else:
#         odd+=1
# print("The numbers of even number between 1-99 is : ",even)
# print("The numbers of odd number between 1-99 is : ",odd)

#3 Write a Python program which iterates the integers from 1 to 50 . For multiples of 3 print "Fizz" instead of the numbers  and for the multiples of 5 print "Buzz" . For numbers which are multiples of both 3 and 5 print "FizzBuzz".

# for i in range(1,50):
#     if(i%3==0 and i%5!=0):
#         print("Fizz")
#     elif(i%5==0 and i%3!=0):
#         print("Buzz")
#     elif(i%3==0 and i%5==0):
#         print("FizzBuzz")
#     else:
#         print(i)


#4 Write a Python program to calculate the sum and average of n integer numbers .

# input_num=int(input("Enter the number of integers that you have to calculate the sum and average : "))
# sum=0
# for i in range(input_num):
#     n=int(input("Enter the numbers : "))
#     sum=sum+n
# print("Sum of ",input_num," numbers is ",sum)
# print("The average is ",sum/input_num)

#5 Write a program to calculate the factorial of a number .

n=int(input("Enter your number : "))
fact=1
for i in range(n,0,-1):
    fact=fact*i  
print(n,"! = ",fact)
