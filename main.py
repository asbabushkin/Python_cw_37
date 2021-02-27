import json

class Student:
    def __init__(self, name, marks=[]):
        self.name = name
        self.marks = marks

    def addMark(self, mark):
        self.marks.append(mark)

    def deleteMark(self, index):
        self.marks.pop(index)

    def editMark(self, index, editedMark):
        self.marks[index] = editedMark

    def averageMark(self):
        return sum(self.marks) / len(self.marks)

    def __str__(self):
        a = ''
        for i in self.marks:
            a += str(i) + ',' + ' '
        a = a[0:len(a) - 2]
        return self.name + ': ' + a



class Group:
    def __init__(self, students=[]):
        self.students = students

    def addStudent(self, student):
        self.students.append(student)

    def removeStudent(self, index):
        # self.students.pop(index)
        return self.students.pop(index)


    def __str__(self):
        a = ''
        for i in self.students:
            a += str(i) + '\n'
        return a

    def dump_class_journal(self, file):
        f = open(file, mode = 'w')
        studList = []
        for i in self.students:
            studList.append([i.name, i.marks])
        tmp = {'Students': [studList]}
        json.dump(tmp, f)
        f.close()



def changeGroup(group1, group2, index):
    group2.addStudent(group1.removeStudent(index))

def dump_student_to_json(stud, fileName):
    data = {'name': stud.name, 'marks': stud.marks}
    f = open(fileName, mode='w')
    json.dump(data, f)
    f.close()

def loadFromFile(fileName):
    f = open(fileName, mode='r')
    temp = json.load(f)
    f.close()
    return temp['name'], temp['marks']





student1 = Student('Ivanov', [2, 3, 4, 5, 5, 5])
student2 = Student('Petrova', [5, 5, 3, 4, 4])
student3 = Student('Sidorova', [4, 4, 3, 3, 5, 5])
student4 = Student('Marks', [4, 4, 3, 3, 5, 5])
student5 = Student('Engels', [4, 4, 3, 3, 5, 5])
student6 = Student('Lenin', [4, 4, 3, 3, 5, 5])
group1 = [student1, student2, student3]
myGroup = Group(group1)
group2 = [student4, student5, student6]
myGroup2 = Group(group2)

# выводим информацию о студенте
print('Выводим информацию о студенте')
print(student1)

# добавляем оценку
print('Добавляем оценку')
student1.addMark(3)
print(student1)

# исправляем оценку
print('Исправляем оценку')
student1.editMark(1, 4)
print(student1)

# удаляем оценку
print('Удаляем оценку')
student1.deleteMark(6)
print(student1)

# рассчитываем средний балл студента
print('Рассчитываем средний балл студента')
print(student1.averageMark())
print()

# добавляем студента в группу
print('Добавление студента в группу: ')
print(myGroup)
myGroup.addStudent(student6)
print(myGroup)

# удаляем студента из группы
print('Удаляем студента из группы ')
print(myGroup)
myGroup.removeStudent(3)
print(myGroup)

# переводим студента из группы 1 в группу 2
print('Переводим студента из группы 1 в группу 2')
print(myGroup)
print(myGroup2)
changeGroup(myGroup, myGroup2, 0)
print('Group1')
print(myGroup)
print('Group2')
print(myGroup2)

# загружаем данные о студенте в json-файл, затем выгружаем данные из файла в консоль
print('Загружаем данные о студенте в json-файл, затем выгружаем данные из файла в консоль')
dump_student_to_json(student5, 'Student.json')
print(loadFromFile('Student.json'))

# загружаем журнал с оценками группы в json-файл
print('Загружаем журнал с оценками группы в json-файл, затем выгружаем в консоль')
myGroup2.dump_class_journal('Group.json')
# выгрузку в консоль доделать