#�������� �������� �������� �� ���������� ����� ������� ������������
#Variant - 1
s = input('������ ��� �����: ')
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
print('�������� �����:', max_slovo)
print('���������� �����:', min_slovo)


#Variant - 2
s = '�������� �������� �������� �� ���������� ����� ������� ������������'
a = s.split(' ')

max_len = 0
min_len = len(a)
max_slovo = ''
min_slovo = ''
for i in range(len(a)):
    if len(a[i]) > max_len:
        max_len = len(a[i])
        max_slovo = a[i]
    elif len(a[i]) < min_len:
        min_len = len(a[i])
        min_slovo = a[i]

print('�������� �����: ', max_slovo, max_len)
print('���������� �����: ', min_slovo, min_len)

#Variant - 3
s = input('������ ��� ��� �����: ').split(' ')
count = 0
for i in s:
    if len(i) > count:
        count = len(i)
        word = i
print(word)