import sqlite3
'''
tablename: student id,name,age,class
'''

def add_student():
    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    s_id = int(input("Enter the student id:\n"))
    name = input("Enter the student name:\n")
    age = int(input("Enter the student age:\n"))
    s_class = int(input("Enter the student class:\n"))
    try:
        cur.execute("""insert into student (id, name, age, class) values (?,?,?,?)""",(s_id,name,age,s_class))
    except Exception as e:
        print(f'Student could not be added since the student with that id exists')
    conn.commit()
    cur.execute("select * from student")
    print(cur.fetchall())
    conn.close()
    
def update_student():
    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    
    cur.execute("select * from student")
    beforeexec = cur.fetchall()
    s_id = int(input("Enter the student id to update:\n"))
    name = input("Enter the student name:\n")
    age = int(input("Enter the student age:\n"))
    s_class = int(input("Enter the student class:\n"))
    cur.execute("""update student set name = ? , age = ? , class = ? where id = ? """,(name, age, s_class, s_id))
    conn.commit()
    cur.execute("select * from student")
    afterexec = cur.fetchall()
    if(beforeexec!=afterexec):
        print("Update was successfully completed")
        print(afterexec)
    else:
        print("Update had no impact because it was not possible or the updated values were the same")
        print(afterexec)
        
    conn.close()
    
def delete_student():
    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    cur.execute("select * from student")
    beforeexec = cur.fetchall()
    s_id = int(input("Enter the student id to delete:\n"))
    cur.execute("""delete from student where id = ? """,(s_id,))
    conn.commit()
    cur.execute("select * from student")
    afterexec = cur.fetchall()
    if(beforeexec!=afterexec):
        print("Delete was successfully completed")
        print(afterexec)
    else:
        print("Delete was not possible as the id doesn't exist")
        print(afterexec)
        
    conn.close()
    
def displayStudent():
    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    cur.execute("select * from student")
    res = cur.fetchall()
    print(f"ID \tName \t     Age Class")
    for row in res:
        print(row)
    conn.close()
    
def displayStudentAgeSorted():
    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    cur.execute("select * from student order by age asc")
    res = cur.fetchall()
    print(f"ID \tName \t     Age Class")
    for row in res:
        print(row)
    conn.close()
    
def find_student():
    conn = sqlite3.connect('student.db')
    cur = conn.cursor()
    s_id = int(input("Enter the student id to find:\n"))
    cur.execute("select * from student where id = ?",(s_id,))
    res = cur.fetchall()
    if (res==[]):
        print("The student id you are looking for was not found")
    else:
        print("The student id you are looking for was found")
        print(f"ID \tName \t     Age Class")
        for row in res:
            print(row)
    conn.close()
    
def main():
    choice = input("Enter c or C to continue")
    while True:
        if(choice not in ["c","C"]):
            print("Thanks for using Student Management System! Have a nice day!")
            break
        choice = input("Welcome to the Student Management System!\nEnter\n1. Add Student\n2. Update Student\n3. Delete Student\n4.Fetch Students\n5.Sort Students based on age\n6. Search student by id\n7. Quit\n")
        if(choice=='1'):
            add_student()
            choice = 'c'
        elif(choice=='2'):
            update_student()
            choice = 'c'
        elif(choice=='3'):
            delete_student()
            choice = 'c'
        elif(choice=='4'):
            displayStudent()
            choice = 'c'
        elif(choice=='5'):
            displayStudentAgeSorted()
            choice = 'c'
        elif(choice=='6'):
            find_student()
            choice = 'c'
        elif(choice=='7'):
            choice = 'Q'
            break
        else:
            print("You have entered an invalid choice!")
if __name__== '__main__':
    main()        

#Testing
# add_student()
# update_student()
# delete_student()
# fetch_student()
# fetch_student_age_sorted()
# search_student()



# Create a connection to the student database
# conn = sqlite3.connect('student.db')
# cur = conn.cursor()
# cur.execute("drop table student")
# cur.execute("create table student (id int primary key, name varchar, age int, class int)")
# conn.commit()
# cur.execute(f"insert into student values (?,?,?,?)",(1,'Rahul Noronha', 17, 12))
# cur.close()
# conn.close()