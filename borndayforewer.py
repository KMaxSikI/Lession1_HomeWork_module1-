#Модуль 5

question_ear = int(input('В каком году родился А.С. Пушкин: ')) # Задаем вопрос про год рождения


while question_ear != 1799: # Пишем условие, что пока ответ не будет равен 1799, задавать вопрос снова
    question_ear = int(input('В каком году родился А.С. Пушкин: '))
    continue # Если ответ верный продолжаем

question_day = input('А в какой день он родился А.С. Пушкин: ') # Задаем вопрос про день рождения

while question_day != '6' and question_day.lower() != 'шесть': # Пишем условие, что пока ответ не будет равен 6 (шести), задавать вопрос снова
    question_day = input('А в какой день он родился А.С. Пушкин: ')

print('Верно')