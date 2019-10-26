class Person:
    # initializing the variables
    # name = ""
    # age = 0

    # defining constructor
    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

        # defining class methods

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)


# definition of subclass starts here
class Student(Person):
    # studentId = ""

    #def __init__(self, student_name, student_age=60, student_id=3):
        # super().__init__(student_name, student_age)
        # self.studentId = student_id
   def __init__(self,  student_name, student_age=60, student_id=3):
          super().__init__(student_name, student_age)
          self.studentId = student_id


   def get_id(self):
        return self.studentId  