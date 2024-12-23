S = '{({[]})()}'
count = 0
while S != '':
    if '()' in S:
        S = S.replace('()','',1)
        count += 1
    if '[]' in S:
        S = S.replace('[]','',1)
        count += 1
    if '{}' in S:
        S = S.replace('{}','',1)
        count += 1
    else:
        break
print(count)
