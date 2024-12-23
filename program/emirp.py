var=17
copy=var
res=0
while var!=0:
    ld=var%10
    res=(res*10)+ld
    var//=10
if copy!=res:
   
    fa_count1=0
    for num in range(1,copy+1):
        if copy%num==0:
            fa_count1+=1
    if fa_count1==2:
        fa_count2=0
        for fa in range(1,res+1):
            if res%fa==0:
              fa_count2+=1  
        if fa_count2==2:
            print('emirp number')
        else:
            print('not emirp  number')
    else:
            print('not emirp')

else:
    print('not EMIRP')
