from models.student import Student
from models.classroom import ClassRoom


oop = ClassRoom("OOP")
oop.add_student(Student(1,"Alice", 20, "S54321"))
oop.add_student(Student(2,"Bob", 22, "S12345"))
print(f'{oop.name} registers {len(oop)} students')
oop.add_student(Student(3,"Charlie", 21, "S67890"))
print(len(oop))
print('Student in the classroom:')
for i in range(len(oop)):
    print(oop[i])