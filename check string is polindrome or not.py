def is_palindrome(string):
    for i in range(len(string)):
        if(string[i] == string[-(i+1)]):
            return False
    else:
        return True
    

xx = 'cbbeaeacccdceedbdecdabbaddabbadcedbdeecdcccaeaebbc'
yy = 'dabdcdbebddedcdcbbcecbbcdcdeddbebdcdbad'
# yy= 'kumar'
zz = 'ddbcbeebdbcdddeabbeccaeababaecceababaeaccebbaedddabdbeebcbdd'
# zz= 'amit'
print(is_palindrome(xx), is_palindrome(yy), is_palindrome(zz))
