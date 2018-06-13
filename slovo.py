#Програма виводить найдовше та найкоротше слово введене корисутвачем
#Variant - 1
s = input('Введіть тут текст: ')
count = 0
max_count = 0
min_count = len(s)
slovo = ''
max_slovo = ''
min_slovo = ''
for i in range(len(s)):
    if s[i]!=' ':
        #print(s[i], end='')
        slovo+=s[i]
        count+=1
    else:
        #print()
        if count>max_count:
            max_count = count
            max_slovo = slovo
        elif count<min_count:
            min_count=count
            min_slovo=slovo
        slovo=''
        count=0
print('Найдовше слово:', max_slovo)
print('Найкоротше слово:', min_slovo)

