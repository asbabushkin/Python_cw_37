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
        return self.students.pop(index)

    def __str__(self):
        a = ''
        for i in self.students:
            a += str(i) + '\n'
        return a


def changeGroup(group1, group2, index):
    group2.addStudent(group1.removeStudent(index))


student1 = Student('Ivanov', [2, 3, 4, 5, 5, 5])
student2 = Student('Petrova', [5, 5, 3, 4, 4])
student3 = Student('Sidorova', [4, 4, 3, 3, 5, 5])
student4 = Student('Marks', [4, 4, 3, 3, 5, 5])
student5 = Student('Engels', [4, 4, 3, 3, 5, 5])
student6 = Student('Lenin', [4, 4, 3, 3, 5, 5])
students = [student1, student2, student3]
myGroup = Group(students)

group2 = [student4, student5, student6]
myGroup2 = Group(group2)
changeGroup(myGroup, myGroup2, 1)

print('Group1')
print(myGroup)
print('Group2')
print(myGroup2)

# print(student1.__str__())
# student1.addMark(3)
# print(student1.__str__())
# student1.editMark(1, 4)
# print(student1.__str__())
# student1.deleteMark(6)
# print(student1.__str__())
# print(student1.averageMark())

# print(myGroup.__str__())
# myGroup.addStudent(student3)
# print(myGroup.__str__())
# # myGroup.removeStudent(0)
# print(myGroup.__str__())
