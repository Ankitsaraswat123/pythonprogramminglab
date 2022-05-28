#calculate number of uppercase letter and number of lowercase letter in a string
def lo_upp(s):
    up=0
    lo=0
    for i in s:
        if (i>='a' and i<='z'):
            lo+=1
        elif(i>='A' and i<='Z'):
            up+=1
    print('uppercase words are:',up)
    print('lowercase words are:',lo)
s=input('please enter a string')
lo_upp(s)
