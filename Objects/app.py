class Student:    
    def __init__(self, s_id, name, age, s_class):
        self.s_id = s_id
        self.age = age
        self.name = name
        self.s_class = s_class
    #Setters
    def set_s_id(self,s_id):
        self.s_id = s_id
    def set_age(self,age):
        self.age = age
    def set_name(self,name):
        self.name = name
    def set_s_class(self,s_class):
        self.s_class = s_class
    #Getters
    def get_s_id(self):
        return self.s_id
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def get_s_class(self):
        return self.s_class
    
    #String method
    def __str__(self):
        return f'id: {self.s_id} Name: {self.name} Age: {self.age} Class: {self.s_class}'


class StudentList:
    #Add Student
    def __init__(self):
        self.ls = [] #List to manage the students        
    def add_student(self, s_id, name, age, s_class):
        new_student = Student(s_id, name, age, s_class)
        for student in self.ls:
            if(student.get_s_id()==s_id):
                print("Student with this id already exists. Can't add to the Student Management System")
                return -1 
        print("Student successfully added to Student Management System")
        self.ls.append(new_student)
        return 0
    #Update student with id to new values
    def update_student(self, s_id, name, age, s_class):
        for idx, student in enumerate(self.ls):
            if(student.get_s_id()==s_id):
                self.ls.remove(student)
                new_student = Student(s_id, name, age, s_class )
                self.ls.insert(idx, new_student)
                print("Student updated successfully!")
                return 0
        print("Student you want to update doesn't exist!")
        return -1
    #Delete student having id
    def delete_student(self, s_id):
        for student in self.ls:
            if(student.get_s_id()==s_id):
                self.ls.remove(student)
                print("Student deleted successfully!")
                return 0
        print("Student you want to delete doesn't exist!")
        return -1
    #Find student having id
    def find_student(self, s_id):
        for idx,student in enumerate(self.ls):
            if(student.get_s_id()==s_id):
                print(f"Student found at the {idx+1} position in Student Management System!")
                return 0
        print("Student you want to find doesn't exist!")
        return -1
    #Fetch students
    def displayStudent(self):
        print("Students fetched: ")
        for student in self.ls:
            print(student)
        print()
    #Sort students based on Age
    def displayStudentAgeSorted(self):
        res = sorted(self.ls, key=lambda x:x.age)
        print("Age sorted: ")
        for student in res:
            print(student)
        print()
#Testing
# student_list = StudentList()
# student_list.add_student(1, 'Rahul',17,12)
# student_list.add_student(1, 'Rohit',16,11)
# student_list.add_student(2, 'Ronit',16,11)
# student_list.add_student(3, 'Ronit',14,9)
# student_list.update_student(2, 'Rohit',16,11)
# student_list.displayStudentAgeSorted()
# student_list.update_student(3, 'Ronit',16,11)
# student_list.displayStudent()
# student_list.find_student(2)
# student_list.delete_student(2)
# student_list.displayStudentAgeSorted()
# student_list.find_student(2)
# student_list.delete_student(3)
# student_list.displayStudentAgeSorted()
def main():
    student_list = StudentList()
    choice = input("Enter c or C to continue")
    while True:
        if(choice not in ["c","C"]):
            print("Thanks for using Student Management System! Have a nice day!")
            break
        choice = input("Welcome to the Student Management System!\nEnter\n1. Add Student\n2. Update Student\n3. Delete Student\n4.Fetch Students\n5.Sort Students based on age\n6. Search student by id\n7. Quit\n")
        if(choice=='1'):
            s_id = int(input("Enter the student id:\n"))
            name = input("Enter the student name:\n")
            age = int(input("Enter the student age:\n"))
            s_class = int(input("Enter the student class:\n"))
            student_list.add_student(s_id, name,age,s_class)
            choice = 'c'
        elif(choice=='2'):
            s_id = int(input("Enter the student id to update:\n"))
            name = input("Enter the new student name:\n")
            age = int(input("Enter the new student age:\n"))
            s_class = int(input("Enter the new student class:\n"))
            student_list.update_student(s_id, name,age,s_class)
            choice = 'c'
        elif(choice=='3'):
            s_id = int(input("Enter the student id to delete:\n"))
            student_list.delete_student(s_id)
            choice = 'c'
        elif(choice=='4'):
            student_list.displayStudent()
            choice = 'c'
        elif(choice=='5'):
            student_list.displayStudentAgeSorted()
            choice = 'c'
        elif(choice=='6'):
            s_id = int(input("Enter the student id to search:\n"))
            student_list.find_student(s_id)
            choice = 'c'
        elif(choice=='7'):
            choice = 'Q'
            break
        else:
            print("You have entered an invalid choice!")
if __name__== '__main__':
    main()                

    
        