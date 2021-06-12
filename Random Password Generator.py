import random
def pass_gen(length=8):
    scl=["@","#","!","$","%","&"]
    upper=chr(random.randint(65,90))
    lower=chr(random.randint(97,122))
    special_ch=random.choice(scl)
    digits=random.randint(0, 99999)
    digits=str(digits)
    password=upper+lower+special_ch+digits
    l=random.sample(password, length)
    password=("").join(l)
    return password

minm_char=int(input("Atleast how many characters your password should have ? "))
result=pass_gen(minm_char)
print(result)

    
