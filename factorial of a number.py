# ........Using factorial function........

# import maths
# input_num=int(input(("Enter your number : ")))
# print("The factorial of ",input_num," is ",math.factorial(input_num))

#..... Factorial of a number using the for loop.........

# def fact(number_input):
#     fact=number_input
#     if(number_input<0 or number_input==0):
#         return 1
#     else:
#         for i in range(number_input-1,0,-1):
#             fact=fact*i
#         return fact

# number_input=int(input("Enter your number : "))
# print("The factorial of ",number_input," is ",fact(number_input))


# Factorial of a number By using recursive function.......

def fact(number_input):
    if(number_input<0 or number_input==0):
        return 1
    else:
        return number_input*fact(number_input-1)

number_input=int(input("Enter your number : "))
print("The factorial of ",number_input," is ",fact(number_input))