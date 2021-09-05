import Menu             # Display the Main Menu #
import Admission        # Display the Options in the Admission Menu #
import Student_data     # Display the Menu for the Student data #
import fee_details      # Display the Fees Details #
import report           # Display graphical Reports #

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
        fee_details.FEE_MENU()
    elif choice == 4:
        report.gr_rep()
    elif choice == 5:
        break
    else:
        print("Error: Invalid choice. Try Again...")
        conti = input("Press any key to continue")
