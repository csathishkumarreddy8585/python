var=145
copy=var
ans=0
while var!=0:
    id=var%10
    fact=1
    for num in range (1,id+1):
        fact*=num
    ans+=fact
    var//=10
if copy==ans:
    print('special number')
else:
    print('not special number')
