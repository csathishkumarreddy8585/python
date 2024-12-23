var=11
copy=var
res=0
while var!=0:
    ld=var%10
    res=(res*10)+ld
    var//=10
if copy==res:
    count_digit=len(str(var))
    count=0
    for num in range(1,res+1):
        if res%num==0:
            count+=0
    if count==2:
        print('polyprime number')
    else:
        print('not polyprime  number')

else:
    print('not polyprime')
