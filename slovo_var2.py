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