class Student:
    students_list = []
    def __init__(self,id,name,age,course):
        self.id = id
        self.name = name
        self.age = age
        self.course = course
        Student.students_list.append(self)
    
    def __eq__(self,other): # overloading == 
        if isinstance(other,Student):
            return self.id == other.id # TODO modify it to age
    
    def __lt__(self,other): # overloading <
        if self.id < other.id: #TODO modify to compare using age then using id
            return True
        else:
            return False
    
    @classmethod
    def sortstudents(cls):
        cls.students_list.sort()
    
    @classmethod
    def searchstudent(cls,id):
        for student in cls.students_list:
            if student.id == id:
                return student
        return None
    
    def __repr__(self):
        return f"ID:{self.id},Name:{self.name}"
 
if __name__ == '__main__':
    s1 = Student(12,'bob',21,'bsc')
    s2 = Student(6,'tom',21,'bcom')
    s3 = Student(8,'joe',21,'bsc')
 
    #for student in Student.students_list:
    # print(student)

    #print(Student.searchstudent(6))
    Student.sortstudents()
    #Student.students_list.sort()
    for student in Student.students_list:
        print(student)