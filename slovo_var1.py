#програма приймає текст від користувача та виводить найдовше та найкоротше слово
s = input('Введіть тут текст: ')
count = 0 #лічильник кількості літер в слові
max_count = 0 # в цю змінну буде записуватись кількість символів в слові максимальна
min_count = len(s) # в цю змінну буде записуватись кількість символів в слові мінімальна
slovo = ''     #пустий стрінг
max_slovo = '' #пустий стрінг
min_slovo = '' #пустий стрінг

#перебираємо по одному по порядку всі символи в строці s
for i in range(len(s)):
    if s[i]!=' ':    #якщо символ не пробіл то додаємо його в змінну slovo(таким чином вибираємо окремі слова з строки)
        slovo+=s[i]
        count+=1
 #якщо натрапили на пробіл в тексті то порівнюємо довжину щойно відібраного слова з максимальним і мінамальним
    else:
        if count>max_count:
            max_count = count
            max_slovo = slovo
        elif count<min_count:
            min_count=count
            min_slovo=slovo
            #Обнуляємо змінні для наступного проходження циклу
        slovo=''
        count=0
 
#виводимо результат
print('Максимальне слово:', max_slovo)
print('Мінімальне слово:', min_slovo)
