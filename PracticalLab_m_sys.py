import csv
from datetime import date

# ==================== SIGN UP ====================
def sign_up():
    print("\n\t=== Sign Up ===")
    
    username = input("Enter a new username: ").strip()
    
    
    with open("Login Info.csv", "r") as l:
        reader = csv.reader(l)
        for row in reader:
            if len(row) >= 1 and row[0] == username:
                print("Username already exists! Please try a different one.")
                return
   
    
    password = input("Set your password: ")
    confirm_password = input("Confirm your password: ")
    
    if password != confirm_password:
        print("Passwords do not match! Sign up failed.")
        return
    
    role = input("Enter your role (Student/Teacher): ").strip().capitalize()
    
    if role not in ["Student", "Teacher"]:
        print("Invalid role! Please enter either 'Student' or 'Teacher'.")
        return
    
   
    with open("Login Info.csv", "a", newline="") as l:
        writer = csv.writer(l)
        writer.writerow([username, password, role])
    
    print("Sign Up Successful! You can now log in.\n")


# ==================== LOG IN ====================
def log_in():
    i = 0
    while i < 3:
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        admin = input("Enter your role (Student/Teacher): ").strip().capitalize()

        found = False
        user_role = None

        
        with open("Login Info.csv", "r") as l:
            reader = csv.reader(l)
            
            for row in reader:
                if len(row) >= 3 and row[0] == username and row[1] == password and row[2] == admin:
                    found = True
                    user_role = row[2]
                    break
            
            if found:
                print("Log in Successful..!")
                return user_role
            else:
                print("Incorrect Username/Password..!")
                i = i + 1
        
        
    else:
        print("Try Again after few minutes..!")
        exit()


# ==================== SELECT THE LAB ====================
def select_lab(role):
    while True:
        lab = int(input("Select the Lab:\n\t1.Unix Lab  \n\t2.ADTL Lab  \n\t3.PG Lab \n\t4.Exit\n"))
    
        match lab:
            case 1:
                unix_lab(role)
            case 2:
                adtl_lab(role)
            case 3:
                pg_lab(role)
            case 4:
                return
            case _:
                print("Invalid Choice")


# ==================== UNIX LAB ====================
def unix_lab(role):
    while True:    
        print("\t===The Unix Lab===")
        
        if role == "Teacher":
            subop = int(input("Select operation which you want to perform:\n\t1.Assign lab \n\t2.Mark Attendence \n\t3.Update Data \n\t4.Display Record \n\t5.EXIT\n"))
            
            match subop:
                case 1:
                    assign_unix()
                case 2:
                    attendence_unix()
                case 3:
                    update_unix()
                case 4:
                    display_unix()
                case 5:
                    return
                case _:
                    print("Invalid Option")
        else:
            # Student view
            subop = int(input("Select operation which you want to perform:\n\t1.Display Record \n\t2.EXIT\n"))
            
            match subop:
                case 1:
                    display_unix()
                case 2:
                    return
                case _:
                    print("Invalid Option")


# ==================== PG LAB ====================
def pg_lab(role):
    while True:
        print("\t===The PG Lab===")
        
        if role == "Teacher":
            subop = int(input("Select operation which you want to perform:\n\t1.Assign lab \n\t2.Mark Attendence \n\t3.Update Data \n\t4.Display Record \n\t5.EXIT\n"))
            
            match subop:
                case 1:
                    assign_pg()
                case 2:
                    attendence_pg()
                case 3:
                    update_pg()
                case 4:
                    display_pg()
                case 5:
                    return 
                case _:
                    print("Invalid Option")
        else:
            # Student view
            subop = int(input("Select operation which you want to perform:\n\t1.Display Record \n\t2.EXIT\n"))
            
            match subop:
                case 1:
                    display_pg()
                case 2:
                    return
                case _:
                    print("Invalid Option")


# ==================== ADTL LAB ====================
def adtl_lab(role):
    while True:
        print("\t===The ADTL Lab===")
        
        if role == "Teacher":
            subop = int(input("Select operation which you want to perform:\n\t1.Assign lab \n\t2.Mark Attendence \n\t3.Update Data \n\t4.Display Record \n\t5.EXIT\n"))
            
            match subop:
                case 1:
                    assign_adtl()
                case 2:
                    attendence_adtl()
                case 3:
                    update_adtl()
                case 4:
                    display_adtl()  
                case 5:
                    return
                case _:
                    print("Invalid Option")
        else:
            # Student view
            subop = int(input("Select operation which you want to perform:\n\t1.Display Record \n\t2.EXIT\n"))
            
            match subop:
                case 1:
                    display_adtl()
                case 2:
                    return
                case _:
                    print("Invalid Option")


# ==================== ASSIGNING THE LABS ====================
def assign_pg():
    while True:
        day = input("Enter the day :")
        slot = int(input("Enter the time slot (10:30 to 12:30 = 1 slot || 1:10 to 3:00 = 2 slot || 3:20 to 5:10 = 3 slot) : "))

        with open("PG lab timetable.csv", "r") as A:
            reader = csv.reader(A)

            for row in reader:
                if row[0] == day:
                    if row[slot] == "Free":
                        print("The PG Lab is available for the asked Time slot ...!")
                        std = input("Enter the class and batch and sub : ")
                        return 
                    else:
                        print("The lab is already acquired by the students of : ", row[slot])
                        break
            
        op = int(input("If u want to assign lab again, select as follow:\n\t1.Yes    2.Exit to Dashboard : \n"))
        if op == 2:
            break


def assign_adtl():
    while True:
        day = input("Enter the day:")
        slot = int(input("Enter the time slot (10:30 to 12:30 = 1 slot || 1:10 to 3:00 = 2 slot || 3:20 to 5:10 = 3 slot) : "))

        with open("Adtl lab timetable.csv", "r") as A:
            reader = csv.reader(A)

            for row in reader:
                if row[0] == day:
                    if row[slot] == "Free":
                        print("The Adtl Lab is available for the asked Time slot ...!")
                        std = input("Enter the class and batch and sub : ")
                        return 
                    else:
                        print("The lab is already acquired by the students of : ", row[slot])
                        break
            
        op = int(input("If u want to assign lab again, select as follow:\n\t1.Yes    2.Exit to Dashboard : \n"))
        if op == 2:
            break


def assign_unix():
    while True:
        day = input("Enter the day:")
        slot = int(input("Enter the time slot (10:30 to 12:30 = 1 slot || 1:10 to 3:00 = 2 slot || 3:20 to 5:10 = 3 slot) : "))
        
        with open("Unix lab timetable.csv", "r") as A:
            reader = csv.reader(A)

            for row in reader:
                if row[0] == day:
                    if row[slot] == "Free":
                        print("The Unix Lab is available for the asked Time slot ...!")
                        std = input("Enter the class and batch and sub : ")
                        return 
                    else:
                        print("The lab is already acquired by the students of : ", row[slot])
                        break
            
        op = int(input("If u want to assign lab again, select as follow:\n\t1.Yes    2.Exit to Dashboard : \n"))
        if op == 2:
            return


# ==================== MARKING ATTENDANCE ====================
def load_students(batch):
    students = []
    
    with open("Comp.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["batch"] == batch:
                students.append((row["rollno"], row["name"]))
    
    return students


def attendence_unix():
    while True:
        
        with open("Attendence_unix.csv", "r") as S:
            srno = sum(1 for _ in S)
        

        std = input("Class : ")
        batch = input("Batch (H-1, H-2, G-1...): ")
        slot = input("Enter slot : ")
        sub = input("Enter the Course Lab : ")

        students = load_students(batch)

        if not students:
            print(" No students found for this batch!")
            continue

        with open("Attendence_unix.csv", "a", newline="") as MA:
            writer = csv.writer(MA)

            for i, (rollno, name) in enumerate(students, start=1):
                srno += 1
                print(f"\nStudent {i}: {name} ({rollno})")

                d = date.today().strftime("%Y-%m-%d")
                attendence = input("P/A : ").upper()

                if attendence == 'P':
                    task = input("Enter the task performed : ")
                else:
                    task = "Nothing"

                writer.writerow([srno, d, rollno, name, std, sub, batch, slot, attendence, task])

        print("\n Attendance stored successfully!")

        l = int(input("\n1. Add more\n2. Exit\n"))
        if l == 2:
            break


def attendence_adtl():
    while True:
        try:
            with open("Attendence_adtl.csv", "r") as S:
                srno = sum(1 for _ in S)
        except FileNotFoundError:
            srno = 0

        std = input("Class : ")
        batch = input("Batch (H1, H2, G1...): ")
        slot = input("Enter slot : ")
        sub = input("Enter the Course Lab : ")

        students = load_students(batch)

        if not students:
            print(" No students found for this batch!")
            continue

        with open("Attendence_adtl.csv", "a", newline="") as MA:
            writer = csv.writer(MA)

            for i, (rollno, name) in enumerate(students, start=1):
                srno += 1
                print(f"\nStudent {i}: {name} ({rollno})")

                d = date.today().strftime("%Y-%m-%d")
                attendence = input("P/A : ").upper()

                if attendence == 'P':
                    task = input("Enter the task performed : ")
                else:
                    task = "Nothing"

                writer.writerow([srno, d, rollno, name, std, sub, batch, slot, attendence, task])

        print("\n Attendance stored successfully!")

        l = int(input("\n1. Add more\n2. Exit\n"))
        if l == 2:
            break


def attendence_pg():
    while True:
        try:
            with open("Attendence_pg.csv", "r") as S:
                srno = sum(1 for _ in S)
        except FileNotFoundError:
            srno = 0

        std = input("Class : ")
        batch = input("Batch (H1, H2, G1...): ")
        slot = input("Enter slot : ")
        sub = input("Enter the Course Lab : ")

        students = load_students(batch)

        if not students:
            print(" No students found for this batch!")
            continue

        # FIXED: Was writing to Attendence_unix.csv instead of Attendence_pg.csv
        with open("Attendence_pg.csv", "a", newline="") as MA:
            writer = csv.writer(MA)

            for i, (rollno, name) in enumerate(students, start=1):
                srno += 1
                print(f"\nStudent {i}: {name} ({rollno})")

                d = date.today().strftime("%Y-%m-%d")
                attendence = input("P/A : ").upper()

                if attendence == 'P':
                    task = input("Enter the task performed : ")
                else:
                    task = "Nothing"

                writer.writerow([srno, d, rollno, name, std, sub, batch, slot, attendence, task])

        print("\n Attendance stored successfully!")

        l = int(input("\n1. Add more\n2. Exit\n"))
        if l == 2:
            break


# ==================== UPDATING THE DATA ====================
def update_unix():
    rows = []

    while True:
        notfound = True

        rec_date = input("Enter the date of record (YYYY-MM-DD) : ")
        std = input("Enter the class : ")
        batch = input("Enter the batch : ")
        r = input("Enter the Roll No of student : ")

        with open("Attendence_unix.csv", "r") as A:
            reader = csv.reader(A)

            for row in reader:

                # Keep header once
                if row[0] == "Sr.No":
                    rows.append(row)
                    continue

                # Find matching record
                if (
                    row[1] == rec_date and
                    row[2] == r and
                    row[4] == std and
                    row[6] == batch
                ):

                    notfound = False

                    # Toggle attendance
                    if row[8] == "P":
                        row[8] = "A"
                        row[9] = "Nothing"

                    elif row[8] == "A":
                        row[8] = "P"
                        task = input("Enter the task performed : ")
                        row[9] = task

                # Append ONLY ONCE
                rows.append(row)

        if notfound:
            print("Record Not Found....!!\n")

        with open("Attendence_unix.csv", "w", newline="") as A:
            writer = csv.writer(A)
            writer.writerows(rows)

        print("Attendance updated successfully..!")

        i = int(input("Want to update one more attendance:\n1.Yes  2.Exit\n"))

        if i == 2:
            return
        
        rows.clear()


def update_adtl():
    rows = []

    while True:
        notfound = True

        rec_date = input("Enter the date of record (YYYY-MM-DD) : ")
        std = input("Enter the class : ")
        batch = input("Enter the batch : ")
        r = input("Enter the Roll No of student : ")

        with open("Attendence_adtl.csv", "r") as A:
            reader = csv.reader(A)

            for row in reader:

                # Keep header once
                if row[0] == "Sr.No":
                    rows.append(row)
                    continue

                # Find matching record
                if (row[1] == rec_date and row[2] == r and row[4] == std and row[6] == batch):

                    notfound = False

                    # Toggle attendance
                    if row[8] == "P":
                        row[8] = "A"
                        row[9] = "Nothing"

                    elif row[8] == "A":
                        row[8] = "P"
                        task = input("Enter the task performed : ")
                        row[9] = task

                # Append ONLY ONCE
                rows.append(row)

        if notfound:
            print("Record Not Found....!!\n")

        with open("Attendence_adtl.csv", "w", newline="") as A:
            writer = csv.writer(A)
            writer.writerows(rows)

        print("Attendance updated successfully..!")

        i = int(input("Want to update one more attendance:\n1.Yes  2.Exit\n"))

        if i == 2:
            return
        
        rows.clear()


def update_pg():
    rows = []

    while True:
        notfound = True

        rec_date = input("Enter the date of record (YYYY-MM-DD) : ")
        std = input("Enter the class : ")
        batch = input("Enter the batch : ")
        r = input("Enter the Roll No of student : ")

        with open("Attendence_pg.csv", "r") as A:
            reader = csv.reader(A)

            for row in reader:

                # Keep header once
                if row[0] == "Sr.No":
                    rows.append(row)
                    continue

                # Find matching record
                if (
                    row[1] == rec_date and
                    row[2] == r and
                    row[4] == std and
                    row[6] == batch
                ):

                    notfound = False

                    # Toggle attendance
                    if row[8] == "P":
                        row[8] = "A"
                        row[9] = "Nothing"

                    elif row[8] == "A":
                        row[8] = "P"
                        task = input("Enter the task performed : ")
                        row[9] = task

                # Append ONLY ONCE
                rows.append(row)

        if notfound:
            print("Record Not Found....!!\n")

        with open("Attendence_pg.csv", "w", newline="") as A:
            writer = csv.writer(A)
            writer.writerows(rows)

        print("Attendance updated successfully..!")

        i = int(input("Want to update one more attendance:\n1.Yes  2.Exit\n"))

        if i == 2:
            return
        
        rows.clear()

# ==================== DISPLAYING THE DATA ====================
def display_unix():
    while True:
        rec_date = input("Enter the date (YYYY-MM-DD) : ")
        std = input("Enter the class : ")
        batch = input("Enter the Batch : ")

        found = False

        with open("Attendence_unix.csv", "r") as U:
            reader = csv.reader(U)

            for row in reader:
                if rec_date == row[1] and std == row[4] and batch == row[6]:
                    print(row)
                    found = True

            if not found:
                print("Record not found..!")

        l = int(input("If want any other Data record select option : \n\t1.Yes   2.Exit\n"))
        if l == 2:
            return
        
        
def display_pg():
    while True:
        rec_date = input("Enter the date (YYYY-MM-DD) : ")
        std = input("Enter the class : ")
        batch = input("Enter the Batch : ")

        found = False

        with open("Attendence_pg.csv", "r") as U:
            reader = csv.reader(U)

            for row in reader:
                if rec_date == row[1] and std == row[4] and batch == row[6]:
                    print(row)
                    found = True

            if not found:
                print("Record not found..!")

        l = int(input("If want any other Data record select option : \n\t1.Yes   2.Exit\n"))
        if l == 2:
            return


def display_adtl():
    while True:
        rec_date = input("Enter the date (YYYY-MM-DD) : ")
        std = input("Enter the class : ")
        batch = input("Enter the Batch : ")

        found = False

        with open("Attendence_adtl.csv", "r") as U:
            reader = csv.reader(U)

            for row in reader:
                if rec_date == row[1] and std == row[4] and batch == row[6]:
                    print(row)
                    found = True

            if not found:
                print("Record not found..!")

        l = int(input("If want any other Data record select option : \n\t1.Yes   2.Exit\n"))
        if l == 2:
            return


# ==================== MAIN PROGRAM ====================
print("\t=== Welcome to Practical Lab Management ===")

while True:
    print("\n\t1. Log In")
    print("\t2. Sign Up")
    print("\t3. Exit")
    
    choice = input("\nSelect an option: ").strip()
    
    match choice:
        case "1":
            role = log_in()
            if role:
                print("\t===Practical Lab Management===")   
                select_lab(role)
        case "2":
            sign_up()
        case "3":
            print("Goodbye!")
            exit()
        case _:
            print("Invalid choice! Please select 1, 2, or 3.")