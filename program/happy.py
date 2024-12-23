num=10
while num>9:
    sum=0
    while num!=0:
        ld=num%10
        sum+=(ld)**2
        num//=10
    num=sum
if num ==1 or num==7:
    print('H')
else:
    print('n')

def sqr(num,sum=0):
    while num!=0:
        ld=num%10
        sum+=(ld)**2
        num//=10
    return sum
def check(num):
    while num>9:
        num=sqr(num)
    return num==1 or num==7
num=10
print('H' if check(num) else 'n')
n=145
copy,ans=n,0
while n!=0:
    ld=n%10
    sum=1
    for val in range(1,ld+1):
        sum*=val
    ans+=sum
    n//=10
if ans==copy :
    print('s')
else:
    print('n')
    

