import Menu
import Student_data
import mysql.connector as co


def STU_MENU():
    while True:
        # Student_data.clrScreen ()
        print("\t\t.......................................")
        print("\t\t*****Welcome to School Management System*****")
        print("\t\t.............................................")
        print("\n\t\t*****Student Data Menu*****")
        print("1: Add Student Record")
        print("2: Show Student Details")
        print("3: Search Student Records")
        print("4: Delete Student Records")
        print("5: Exit")
        print("\t\t---------------------------------------------")

        choice = int(input("Enter your choice here: "))

        if choice == 1:
            Student_data.Add_Records()
        elif choice == 2:
            Student_data.Show_Stu_Details()
        elif choice == 3:
            Student_data.Search_Stu_Details()
        elif choice == 4:
            Student_data.Delete_Stu_Details()
        elif choice == 5:
            return
        else:
            print("Error. Please try again from 1 to 5")
            conti = "Press any key to continue"


def Add_Records():
    try:
        mycon = co.connect(host="localhost", user="root", passwd="Flatno432", database="NKBPS")
        cursor = mycon.cursor()
        session = input('Enter Academic Session(e.g 2020-21): ')
        stname = input('Enter Student Name: ')
        stclass = input('Enter Class: ')
        stsec = input('Enter Section: ')
        stroll = input('Enter Roll No.: ')
        sub1 = input('Enter Subject 1: ')
        sub2 = input('Enter Subject 2: ')
        sub3 = input('Enter Subject 3: ')

        query = "insert into student (session, stname, stclass, stsec, stroll, sub1, sub2, sub3) values('{}','{}'," \
                "'{}','{}', '{}','{}','{}','{}')".format(session, stname, stclass, stsec, stroll, sub1, sub2, sub3)
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print("Record has been saved in Student Table")
    except:
        print("Error Entering Record")


def Show_Stu_Details():
    mycon = co.connect(host="localhost", user="root", passwd="Flatno432", database="NKBPS")
    cursor = mycon.cursor()
    cursor.execute("select * from student")
    data = cursor.fetchall()
    for row in data:
        print(row)


def Search_Stu_Details():
    mycon = co.connect(host="localhost", user="root", passwd="Flatno432", database="NKBPS")
    cursor = mycon.cursor()
    ac = input("Enter Roll No.: ")
    st = "select * from student where stroll='%s'" % (ac)
    cursor.execute(st)
    data = cursor.fetchall()
    print(data)


def Delete_Stu_Details():
    mycon = co.connect(host="localhost", user="root", passwd="Flatno432", database="NKBPS")
    cursor = mycon.cursor()
    ac = input("Enter Roll No.: ")
    st = "delete from student where stroll='%s'" % (ac)
    cursor.execute(st)
    mycon.commit()
    print("Data deleted successfully")


