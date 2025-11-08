class Student:
    def __init__(self, name, age, school, knowledge=0):
        self.name = name
        self.age = age
        self.school = school
        self.knowledge = knowledge

    def study(self):
        self.knowledge += 10
        print(f"{self.name} навчається. Рівень знань: {self.knowledge}")

    def work(self):
        print(f"{self.name} працює, застосовуючи свої знання.")

    def rest(self):
        print(f"{self.name} відпочиває після навчання.")

student1 = Student("Роман", 17, "Ліцей №16")
student1.study()
student1.work()
student1.rest()