import Menu
import Admission
import mysql.connector as co


def ADM_MENU():
    while True:
        #Admission_clrScreen()
        print("\t\t.............................................")
        print("\t\t*****Welcome To School Management System*****")
        print("\t\t.............................................")
        print("\n\t\t*****Admission*****")
        print("1: Admission Details")
        print("2: Search")
        print("3: Show Admission Details")
        print("4: Delete records")
        print("5: Update Admission Details")
        print("6: Return")
        print("\t\t---------------------------------------------")

        choice = int(input("Enter your choice here:"))
        if choice == 1:
            Admission.admin_details()
        elif choice == 2:
            Admission.search_admin_details()
        elif choice == 3:
            Admission.show_admin_details()
        elif choice == 4:
            Admission.delete_admin_details()
        elif choice == 5:
            Admission.edit_admin_details()
        elif choice == 6:
            return

        else:
            print("Error: Invalid choice. Try Again...")
            conti = "Press any key to return to Main Menu"


def admin_details():
    try:
        mycon = co.connect(host="localhost", user="root", passwd="Flatno432", database="NKBPS")
        cursor = mycon.cursor()
        adno = input('Enter Admission No.: ')
        rno = input('Enter Roll No.: ')
        sname = input('Enter Student Name: ')
        clas = input('Enter Class: ')

        query = "insert into admission(adno, rno, sname, clas) values('{}','{}','{}','{}')".format(adno, rno, sname, clas)
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print('Record has been saved in admission table')

    except:
        print('Error')


def search_admin_details():
    mycon = co.connect(host="localhost", user="root", passwd="Flatno432", database="NKBPS")
    cursor = mycon.cursor()
    ac = input("Enter Admission No.: ")
    st = "select * from Admission where adno='%s'"%(ac)
    cursor.execute(st)
    data = cursor.fetchall()
    print(data)


def show_admin_details():
    mycon = co.connect(host="localhost", user="root", passwd="Flatno432", database="NKBPS")
    cursor = mycon.cursor()
    cursor.execute("select * from admission")
    data = cursor.fetchall()
    for row in data:
        print(row)


def delete_admin_details():
    mycon=co.connect(host="localhost", user="root", passwd="Flatno432", database="NKBPS")
    cursor = mycon.cursor()
    ac = input("Enter Admission No.:")
    st = "delete from Admission where adno='%s'"%(ac)
    cursor.execute(st)
    mycon.commit()
    print('Data DELETED successfully')


def edit_admin_details():
    mycon = co.connect(host="localhost", user="root", passwd="Flatno432", database="NKBPS")
    cursor = mycon.cursor()

    print("1: Edit Name: ")
    print("2: Edit Class: ")
    print("3: Edit Roll no.: ")
    print("4: Return: ")
    print("\t\t-------------------------")
    choice = int(input("Enter your choice here: "))
    if choice == 1:
        Admission.edit_name()
    elif choice == 2:
        Admission.edit_class()
    elif choice == 3:
        Admission.edit_roll_no()
    elif choice == 4:
        return
    else:
        print("Error: Invalid Choice")
        print("Press any key to return to")


def edit_name():
    mycon = co.connect(host="localhost", user="root", passwd="Flatno432", database="NKBPS")
    cursor = mycon.cursor()
    ac = input("Enter Admission No.: ")
    nm = input("Enter Correct Name: ")
    st = "update admssion set sname='%s' where adno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print("Data UPDATED successfully")


def edit_class():
    mycon = co.connect(host="localhost", user="root", passwd="Flatno432", database="NKBPS")
    cursor = mycon.cursor()
    ac = input("Enter Admission No.: ")
    nm = input("Enter correct class: ")
    st = "update admission set clas='%s' where adno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print("Data updated successfully")


def edit_roll_no():
    mycon = co.connect(host="localhost", user="root", passwd="Flatno432", database="NKBPS")
    cursor = mycon.cursor()
    ac = input("Enter Admission No.: ")
    nm = input("Enter Correct Roll No.: ")
    st = "update admission set rno='%s' where adno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print("Data updated successfully")






