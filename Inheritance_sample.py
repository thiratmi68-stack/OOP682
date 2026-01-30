from models.person import Person
from models.student import Student
from models.staff import Staff
        
person = Person(1001, "John Doe", 30)        
student = Student(1234567890, "Alice", 20, "S123")
staff = Staff(2234567890, "Bob", 35, "ST456")
print(staff)
print(student)
print(person)

# polymorphic function
def get_person_info(person):
    print(isinstance(person, Person)) # True for both Student and Staff
    return f"ID: {person.pid}, Name: {person.name}, Age: {person.age}"

get_person_info(student) #returns 'ID: 1234567890, Name: Alice, Age: 20'
get_person_info(staff) #returns 'ID: 2234567890, Name: Bob, Age: 35'

# Testing with another subclass
class Employee:
    pass
manger = Employee()
# get_person_info(manger)