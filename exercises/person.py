class Person:
    people = []

    def __init__(self, name: str, age: int, job: str):
        assert len(name) > 0, 'Name cannot be empty.'
        assert len(job) > 0, 'Job title cannot be empty.'

        self.name = name
        self.__age = age
        self.__job = job

        Person.people.append(self)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise Exception('Age cannot be a negative number.')
        self.__age = value

    @property
    def job(self):
        return self.__job

    @job.setter
    def job(self, value):
        self.__job = value.capitalize()

    def greet(self):
        print(f"Hello! My name is {self.name} and i'm {self.age} years old!")

    @classmethod
    def people_list(cls):
        for p in cls.people:
            print(f'Name: {p.name}, Age: {p.age}, Job: {p.job}')

    def __add__(self, other):
        return self.name + other.name

    def __lt__(self, other):
        return self.age < other.age


class Student(Person):
    students_list = []

    def __init__(self, name: str, age: int, job: str, reg: int, degree: str):
        super().__init__(name, age, job)
        assert reg > 0, 'Registry has to be greater than zero.'
        assert len(degree) > 0, 'Degree title cannot be empty.'

        self.reg = reg
        self.degree = degree

        Student.students_list.append(self)

    def greet(self):
        print(f"Hello! My name is {self.name}, i'm {
              self.age} years old and i'm taking a degree in {self.degree}!")

    @classmethod
    def people_list(cls):
        for s in cls.students_list:
            print(f'Name: {s.name}, Age: {s.age}, Job: {
                  s.job}, Registry: {s.reg}, Degree: {s.degree}')


class Teacher(Person):
    teachers_list = []

    def __init__(self, name: str, age: int, job: str, group: str):
        super().__init__(name, age, job)
        assert len(group) > 0, 'Group name cannot be empty.'

        self.group = group

        Teacher.teachers_list.append(self)

    def greet(self):
        print(f"Hello! My name is {self.name}, i'm {
              self.age} years old and i'm a professor!")

    @classmethod
    def people_list(cls):
        for t in cls.teachers_list:
            print(f'Name: {t.name}, Age: {t.age}, Job: {
                  t.job}, Group Responsible: {t.group}')


class Group:
    def __init__(self, name):
        assert len(name) > 0, 'Group name cannot be empty.'

        self.name = name
        self.group = []

    def add_student(self, student):
        self.group.append(student)

    def avarage_age(self):
        age_total = 0

        for student in self.group:
            age_total += student.age

        avarage = age_total / len(self.group)

        return avarage


person1 = Person('Joana', 44, 'Nurse')
person2 = Person('Carlos', 33, 'Barist')
person3 = person1 + person2

person1.job = 'bartender'

print(f'Third person name: {person3}')
print(f'Is {person1.name} older than {person2.name}? > {person1 < person2}')

group1 = Group('Group A')
group2 = Group('Group B')

student1 = Student('Gustavo', 23, 'Student', 345200, 'Computer Science')
group1.add_student(student1)
student2 = Student('Maiara', 25, 'Student', 620340, 'Economy')
group1.add_student(student2)
student3 = Student('Jackson', 21, 'Student', 425347, 'Medical')
group2.add_student(student3)
student4 = Student('Edward', 26, 'Student', 740389, 'Law')
group2.add_student(student4)

print(f'\n{group1.name}:')
for student in group1.group:
    print(student.name)

print(f'\n{group2.name}:')
for student in group2.group:
    print(student.name)

print(f"\n{group1.name} Student's Age Avarage:")
print(group1.avarage_age())

print(f"\n{group2.name} Student's Age Avarage:")
print(group2.avarage_age())

teacher1 = Teacher('John', 47, 'Professor', group1.name)
teacher2 = Teacher('Michael', 53, 'Professor', group2.name)

print('\nPeople:')
Person.people_list()
Student.people_list()
Teacher.people_list()

print('\nGreetings:')
person1.greet()
person2.greet()

student1.greet()
student2.greet()

teacher1.greet()
teacher2.greet()
