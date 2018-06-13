#Variant - 3
s = input('¬вед≥ть тут ваш текст: ').split(' ')
count = 0
for i in s:
    if len(i) > count:
        count = len(i)
        word = i
print(word)