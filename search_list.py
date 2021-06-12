'''
All The codes are here that how you are finding your key_element by just calling the function .

'''
def search(l,key):
    for item in l:
        if(key==item):
            return True
    else:
        return False

if __name__=="__main__":
    l=[1,2,3,4,5,6,7,8,9,10]
    key=5
    print(search(l,key))
