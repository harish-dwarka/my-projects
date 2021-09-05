import Menu
#import Fee_details
import Admission
import Student_data
import report

while True:
    # Menu.clrscreen()
    print("\t\t.............................................")
    print("\t\t*****Welcome To School Management System*****")
    print("\t\t.............................................")
    print("\n\t\t*****N.K. Bagrodia Public School*****")
    print("1: Admission")
    print("2: Student Data")
    print("3: Fee Details")
    print("4: Graphical Report")
    print("5: Exit")
    print("\t\t---------------------------------------------")
    choice = int(input("Enter your choice please:"))
    if choice == 1:
        Admission.ADM_MENU()
    elif choice == 2:
        Student_data.STU_MENU()
    elif choice == 3:
        Fee_details.FEE_MENU()
    elif choice == 4:
        report.gr_rep()
    elif choice == 5:
        break

    else:
        print("Error: Invalid choice. Try Again...")
        conti = input("Press any key to continue")
