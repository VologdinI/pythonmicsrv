from typing import Final


class Student:
    def __init__(self, fnf, age, group, mid_grade):
        self.fnf = fnf
        self.age = age
        self.group = group
        self.mid_grade = mid_grade
        if mid_grade >= 4:
            self.scholarship = 4000
        elif mid_grade == 5:
            self.scholarship = 6000
        else:
            self.scholarship = 0



    def make_money(self):
        print(f"Stipend of : {self.fnf}=  {self.scholarship}")

    def __str__(self):
        print(f"Name: {self.fnf}, Age: {self.age}")

    def compare_scholarship(self, another_guy_which_have_scolarship):
        return self.scholarship>another_guy_which_have_scolarship.scholarship


class Aspirant(Student):
    def __init__(self, fnf, age, group, mid_grade, science_work):
        super().__init__(fnf, age, group, mid_grade)
        self.science_work = science_work
        if mid_grade >= 4:
            self.scholarship = 6000
        elif mid_grade == 5:
            self.scholarship = 8000


    def __str__(self):
        print(f"Name: {self.fnf}, Age: {self.age}")
    pass

s = Student("Вологдин Илья Владимирович", 18, "5142704/30801", 3.5)
a = Aspirant("Владислав", 26, "10142704/30801", 4.2, "Исследование метрик производительности программного кода")

print(s.__str__())
print(a.__str__())
s.make_money()
a.make_money()
print(a.compare_scholarship(s))
