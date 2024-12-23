def c_disarum(num,dup,cdigit,sol=0):
    while dup!=0:
        id=dup%10
        sol+=id*cdigit
        cdigit-=1
        dup//=10
    return sol==num
num=135
print('disarum' if c_disarum(num,num,len(str(num))) else 'not disarum')
