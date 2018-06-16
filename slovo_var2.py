#програма приймає текст від користувача та виводить найдовше та найкоротше слово
s = input('Введіть тут текст: ')
a = s.split(' ') #розбиваємо текст на окремі слова

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

print('Найдовше слово: ', max_slovo, max_len)
print('Найкоротше слово: ', min_slovo, min_len)
