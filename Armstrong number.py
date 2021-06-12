n=int(input(("Enter a number : ")))
str_n=str(n)
arm_no=0
for i in range(len(str_n)):
    arm_no=arm_no+(int(str_n[i])**3)

if(arm_no==n):
    print(n," is an Armstrong number .")
else:
    print(n," is not an Armstrong number .")

# 1,2,3,4,5,6,7,8,9,153,370,371,407,1634,8208,9474,54748........are Armstrong number 