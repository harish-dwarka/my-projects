import Menu
import report
import mysql.connector as co
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from tabulate import tabulate


def gr_rep():
    while True:
        print("\t\t........................................")
        print("\t\t*****Welcome to School Management System*****")
        print("\t\t.............................................")
        print("\n\t\t*****Graphical Report*****")
        print("1: Class wise student details")
        print("2: Session wise student details")
        print("3: Tabulate Admission detail report")
        print("4: Return")
        print("\t\t--------------------------------------------")
        choice=int(input("Enter your choice: "))

        if choice == 1:
            report.cwsr()
        elif choice == 2:
            report.swsr()
        elif choice == 3:
            report.tabar()
        elif choice == 4:
            return
        else:
            print("Error: Invalid Choice Choice try again.....")
            conti = "Press any key to return to Main menu"


def cwsr():
    mycon=co.connect(host="localhost", user="root", passwd="Flatno432", database="NKBPS")
    cursor=mycon.cursor()
    cursor.execute("select distinct(stclass) from student")
    data = cursor.fetchall()
    clas = []
    for row in data:
        clas.append(row[0])
    print('Distinct Classes', clas)
    cursor.execute("select count(stclass) from student group by stclass")
    data = cursor.fetchall()
    no_o_s = []
    for row in data:
        no_o_s.append(row[0])
    print('Students present:', no_o_s)
    import matplotlib.pyplot as pl
    print(pl.pie(no_o_s, labels=clas, autopct="%1.1f%%"))
    pl.show()


def tabar():
    mycon = co.connect(host="localhost", user="root", passwd="Flatno432", database="NKBPS")
    cursor = mycon.cursor()
    try:
        cursor.execute("select * from admission")
        print(tabulate(cursor, headers=['Admission No', 'Roll No', 'Name', 'Class'], tablefmt='psql'))
        '''data = cursor.fetchall()
        for rec in data:
        print(rec)'''
    except:
        print('Something Went Wrong Sorry')
