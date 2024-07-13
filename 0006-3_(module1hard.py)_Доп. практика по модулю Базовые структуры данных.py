students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} #Исх. множество
                                #неупоряд. объектов
a = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
                         # 1 вариант:
#print(list(a)) #Используя команду list(a) получаем список, неупорядоченный по алфавиту
#print(sorted(a)) #Используя команду sorted(a) получаем список по алфавиту
                         # 2 вариант (который я использовал):
print(sorted(a)) #Сразу используя команду sorted(a) к исх. множеству, получаем список по алфавиту
      # без промежуточной команды list(a), т.к. упорядоченное множество по сути это уже список

# Вычисляем ср. знач. оценок по каждому ученику в алфавитном порядке
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
b = [5, 3, 3, 5, 4]
b = sum(b) / len(b)
print(b)
c = [2, 2, 2, 3]
c = (sum(c) / len(c))
print(c)
d = [4, 5, 5, 2]
d = sum(d) / len(d)
print(d)
e = [4, 4, 3]
e = sum(e) / len(e)
print(e)
f = [5, 5, 5, 4, 5]
f = sum(f) / len(f)
print(f)
print(b, c, d, e, f) # Среднее знач. оценок по каждому ученику в алфавитном порядке
# составляем словарь, где ключ - имя ученика, а значение - его средний балл.
students = print(sorted(a))
grades = print(b, c, d, e, f)

#Список учеников и список средней оценки взял из вывода в программе
students = ['Aaron', 'Bilbo', 'Johnny', 'Khendrik', 'Steve']
grades = 4.0, 2.25, 4.0, 3.6666666666666665, 4.8
Average_grades_of_students = dict(zip(students, grades))
print(Average_grades_of_students) # Получил требуемый в задаче словарь
