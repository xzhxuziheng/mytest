class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def output(self):
        return '我的名字是{0}，年龄是{1}'.format(self.name, self.age)


class Teacher(Person):

    def __init__(self, name, age, j_age):
        super().__init__(name, age)
        self.j_age = j_age

    def output(self):
        new_info = super(Teacher, self).output()
        return '{0}，教龄是{1}'.format(new_info, self.j_age)


class Student(Person):

    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no

    def output(self):
        new_info = super().output()
        return '{0}，学号是{1}'.format(new_info, self.stu_no)


p = Person('aaa', 3)
t = Teacher('bbb', 30, 3)
s = Student('ccc', 12, 10001)

print(p.output())
print(t.output())
print(s.output())
