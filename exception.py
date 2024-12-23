lines =5
for row in  range (lines):
    for col in range (lines):
        if row==col or row+col==lines-1:
            print('*',end='')
        else:
            print('',end='')
    print()
