
import random
i=0
my_pass="Amit"
result="Abcd"
while(my_pass!=result):
    def pass_gen(length=4):
        
        upper=chr(random.randint(65,90))
        lower=chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122))
        password=upper+lower
        l=random.sample(password, length)
        password=("").join(l)
        return password

    result=pass_gen()
    print(result)
    print(i)
    i=i+1
else:
    print("The password is found at : ",i)
