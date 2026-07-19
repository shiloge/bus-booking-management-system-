import mysql.connector as m
import sys
from datetime import datetime
dt=datetime.now()
mydb=m.connect(host="localhost",user="root", passwd="password",database="vyathra")
mycursor=mydb.cursor()
mycursor.execute("TRUNCATE TABLE curr ")
mydb.commit()
# This function displays the welcome screen of the application.
# It allows the user to choose between login, new user registration,
# admin panel access, or exiting the program.
def welc():
    print("============================================================")
    print("                                 #WELCOME TO  VYATHRA#                                                   \n \n")
    print("                 PLEASE OPEN IN FULL SCREEN FOR BETTER VIEWING                                                   \n \n")
    c='y'
    while c=='y':
        print("Existing Customer?,      PRESS 1 TO LOGIN")
        print("New to Golden,              PRESS 2 TO CREATE ACCOUNT")
        print("Adminstration?              PRESS 3 TO ADMIN PANEL")
        print("Wanna Quit?                 PRESS 9 to Exit")
        ch=int(input("Enter your Choice:"))
        if ch==1:
            login()
        elif ch==2:
            newuser()
        elif ch==3:
            admin1()
        elif ch==9:
            print("Exiting, Come Back Again!")
            sys.exit()
        else:
            print("Try again")
        
# This function is used to register a new user.
            
def newuser():
    print("Create new user")
    nm=input("Enter your Name:")
    gen=input("Enter Gender(M/F):")
    mob=input("Enter mobile number:")
    print("Make sure Username doesn't exceed 10 characters and Alphanumeric")
    usn=input("Enter your USERNAME:")
    mail=input("Enter your email:")
    passwd=input("Enter your Password:")
    p1=input("Re-enter your Password:")
    if passwd==p1:
        print("Password Matched!")
        sql = "INSERT INTO cred VALUES (%s, %s, %s, %s, %s)"
        val = (usn, nm, mail, passwd, dt)
        mycursor.execute(sql, (val))
        mydb.commit()
        sqp = "INSERT INTO userdata VALUES (%s, %s, %s, %s, %s)"
        vap = (usn, nm, mail, mob,gen)
        mycursor.execute(sqp,( vap))
        mydb.commit()
        print("New user created Successfully! \n Start Travelling with Golden today")
        return
    else:
        print("Password is not matching")
        x=input("Do you want to start over (Y/N)")
        if x=='y':
            newuser()
        if x=='n':
            print("returning home")
            welc()
        
        
        # This function authenticates an existing user and if successful redirects to user menu
def login():
    user=input("Enter your Username:")
    passwd=input("Enter your Password:")
    query="select * from cred where UID=%s AND password=%s"
    mycursor.execute(query,(user,passwd))
    mydat=mycursor.fetchone()
    if mydat!=None:
        print("Login Successful!")
        print("Welcome",mydat[1])
        sql="INSERT INTO curr values(%s,%s,%s)"
        mycursor.execute(sql,(user,passwd,dt))
        mydb.commit()
        home()
    else:
        print("Incorrect Username or Password")
        h=input("Do you want to try again (Y/N)")
        if h=='y':
            login()
        elif h=='n':
            print("returning home")
            welc()
    
# This function displays the main user menu after successful login.
def home():
    mycursor.execute("select * from curr ")
    myrecords=mycursor.fetchall()
    user=myrecords[0][0]
    password='myrecords[0][1]'
    c='y'
    while c=='y':
        print("1. Book Now")
        print("2. Booking Status")
        print("3. Booking History")
        print("4. Manage Account")
        print("5. Log out")
        ch=int(input("Enter your choice:"))
        if ch==1:
            book()
        elif ch==2:
            bookstat()
        elif ch==3:
            bookhist()
        elif ch==4:
            manageacc()
        elif ch==5:
            print("Logging Out")
            mycursor.execute("TRUNCATE TABLE curr ")
            mydb.commit()
            welc()
        else:
            print("Invalid input")
            home()
# This function handles admin authentication.
def admin1():
    mycursor.execute("select * from admin")
    myrecords=mycursor.fetchall()
    user=input("Enter your Username:")
    passwd=input("Enter your password:")
    for x in myrecords:
        if user==x[0]:
            if passwd==x[1]:
                print("Access Granted")
                print("Welcome SIR")
                admin()
                return
    
    print("You are unauthorized to Admin access, Redirecting to Home")
    welc()
# This function displays the admin control panel.
def admin():
    print("****************************")
    print("Welcome to Admin panel")
    print("1. ADD BUS ROUTE")
    print("2. DELETE BUS ROUTE")
    print("3. VIEW BUS ROUTES")
    print("4. VIEW BUS BOOKINGS")
    print("5. MANAGE USERS")
    print("6. Home")
    ch=int(input("Enter your Choice:"))
    if ch==1:
        addbus()
    elif ch==2:
        delbus()
    elif ch==3:
        busview()
    elif ch==4:
        viewbook()
    elif ch==5:
        manageuser()
    elif ch==6:
        welc()
    else :
        print("Invalid option")
        admin()
# This function allows the admin to add a new bus route.
def addbus():
    print("ADD BUS")
    busno=int(input("ENTER BUS NO.:"))
    print("Enter route in format start-end")
    route=input("Enter the route:")
    print("Enter the time in hh:mm:ss format")
    stime=input("Enter the start time:")
    etime=input("Enter the end time:")
    print("THREE STOPS CAN BE ADDED")
    stop1=input("Enter the first stop:")
    stop2=input("Enter the second stop:")
    stop3=input("Enter the third stop:")
    type1=input("Enter the bus type:")
    fare=int(input("Enter the bus fare:"))
    seat=int(input("Enter the no of bus seats:"))
    sql="INSERT INTO bussid values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,(busno,route,stime,etime,stop1,stop2,stop3,type1,fare,seat,))
    mydb.commit()
    print("BUS ROUTE ADDED SUCCESSFULLY")
    x=input("Do you want to add more routes?(Y/N):")
    if x=='y':
        addbus()
    elif x=='n':
        print("Returning to admin panel")
        admin()
    else:
        print("Invalid input, returning to panel")
        admin()
# This function allows the admin to delete an existing bus route.
def delbus():
    x=input("Do you want to view the bus routes (Y/N)")
    if x=='y':
        mycursor.execute("SELECT * from bussid")
        myrecords=mycursor.fetchall()
        print("BusNo\tRoute\tStart\tEnd\tStop 1\tStop 2\tStop 3\tBus Type \tFare\tSeats")
        for row in myrecords:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}\t{row[7]}\t{row[8]}\t{row[9]}\t")
        
    elif x=='n':
        print("OK Then")

    mycursor.execute("select busno from bussid")
    myrecords=mycursor.fetchall()
    sz=len(myrecords)
    sh=int(input("Enter the Bus no. of the route you want to delete:"))
    found=False
    for i in range(sz):
        if sh==myrecords[i][0]:
            found=True
            sql="DELETE from bussid where busno= %s"
            mycursor.execute(sql, (sh,))
            mydb.commit()
            print("Route of Bus Number",sh," deleted successfully")
            x=input("Do you want to delete more routes?(Y/N):")
            if x=='y':
                delbus()
            elif x=='n':
                print("Returning to admin panel")
                admin()
            else:
                print("Invalid input, returning to panel")
                admin()
    if not found:
        print("Bus Route not found")
        delbus()

# This function displays all the available bus routes.
def busview():
    mycursor.execute("SELECT * from bussid")
    myrecords=mycursor.fetchall()
    print("Present Bus records are::")
    columns=[desc[0] for desc in mycursor.description]
    print("Bus no |                   Route                 |   Start    |   End     |    Stop 1     |      Stop 2     |   Stop 3   |       Bus Type        |   Fare   |    Seat    |")
    for row in myrecords:
        print(row[0],':          ',row[1],':  ',row[2],':',row[3],':',row[4],':',row[5],':',row[6],':',row[7],':  ',row[8],  ':    ',row[9])
    
    x=input("PRESS ANY BUTTON to go back to Admin panel")
    if x==9:
        admin()
    else:
        admin()
# This function allows the admin to manage registered users
def manageuser():
    mycursor.execute("SELECT UID, name FROM cred")
    myrecords = mycursor.fetchall()
    print("\nUID\t\tNAME")
    print("-"*30)
    for r in myrecords:
        print(f"{r[0]}\t\t{r[1]}")
    c='y'
    
    while c=='y':
        print("\n\n1. Add User")
        print("2. Delete User")
        print("3. User Specific data")
        print("4. Full user data")
        print("5. Back")
        ch=int(input("Enter your choice:"))
        if ch==1:
            newuser()
        elif ch==2:
            dropuser()
        elif ch==3:
            userdata()
        elif ch==4:
            fulldata()
        elif ch==5:
            admin()

        else:
            print("Invalid input")
            manageuser()
    
# This function allows a logged-in user to book bus tickets.
def book():
    mycursor.execute("select * from bussid")
    buses=mycursor.fetchall()
    print("Available routes are:")
    print("Bus no |                   Route                 |   Start    |   End     |    Stop 1     |      Stop 2     |   Stop 3   |       Bus Type        |   Fare   |    Seat    |\n")
    for row in buses:
         print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}\t{row[7]}\t{row[8]}\t{row[9]}\n")
    busno=input("Enter the bus no of the route:")
    rs="SELECT route from bussid where busno={}".format(busno)
    mycursor.execute(rs)
    route=mycursor.fetchone()
    if not route:
        print("Invalid Bus no")
        home()
        return
    try:
        seats=int(input("Enter the number of seats:"))
        if seats<=0:
            print('Invalid no. of seats')
            return
    except ValueError:
        print("Invalid input")
        return
    mycursor.execute("select * from curr")
    current=mycursor.fetchone()
    username=current[0]
    sh=input("Are you sure to confirm the booking?(Y/N)")
    if sh in 'yY':
         sql="INSERT into bookings(route,uid,busno,seats)values(%s,%s,%s,%s)"
         val=(route[0],username,busno,seats)
         try:
             mycursor.execute(sql,val)
             mydb.commit()
             booking_id = mycursor.lastrowid
             print("Booking is successfull\n",seats,"seat(s) in bus no ",busno)
             custom_id = "VSN" + str(booking_id).zfill(6)
             sqp="update bookings SET book_id=%s where bookno=%s"
             mycursor.execute(sqp,(custom_id,booking_id))
             mydb.commit()
             
             print("Booking ID is",custom_id)
             x=input("press any key to return home")
             home()
         except Exception as e:
             mydb.rollback()
             print("Booking failed",e)
             x=input("press any key to return home")
             home()
    else:
        print("Booking was unsuccessful")
        x=input("Press any key to return home:")
        home()
#This function displays the latest booking status of the logged-in user
def bookstat():
    mycursor.execute("select * from curr")
    current=mycursor.fetchone()
    user=current[0]
    sql="SELECT * FROM bookings WHERE UID=%s ORDER BY bookno DESC limit 1"
    mycursor.execute(sql,(user,))
    record=mycursor.fetchall()
    if record:
        print(" Booking ID |                   Route                 |   Booking time    |   Bus no   |    Seat    |\n")
        for row in record:
            print(f"{row[0]}\t{row[1]}\t{row[3]}\t{row[4]}\t{row[5]}\t\n")
        x=input("Press any key to return home:")
        if x!=None:
            home()
    else:
        print("No Booking found")
        x=input("Press any key to return home:")
        if x!=None:
            home()
# This function displays the complete booking history
def bookhist():
    mycursor.execute("select * from curr")
    current=mycursor.fetchone()
    user=current[0]
    sql="SELECT * FROM bookings WHERE UID=%s "
    mycursor.execute(sql,(user,))
    myrecords=mycursor.fetchall()
    if myrecords:
        print("                                 BOOKING HISTORY                                                   \n \n")
        print(" Booking ID |                   Route                 |   Booking time    |   Bus no   |    Seat    |\n")
        for row in myrecords:
            print(f"{row[0]}\t{row[1]}\t{row[3]}\t{row[4]}\t{row[5]}\t\n")
        x=input("Press any key to return home:")
        if x!=None:
            home()
    else:
        print("Booking history is empty")
        x=input("Press any key to return home:")
        if x!=None:
            home()
# This function allows the admin to view all bookings made by all users.
def viewbook():
    mycursor.execute("SELECT * FROM bookings")
    record=mycursor.fetchall()
    print("BOOKINGS HISTORY")
    if record:
        print(" Booking ID |                   Route                 |    UID    |   Booking time    |   Bus no   |    Seat    |\n")
        for row in record:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t\n")
        x=input("Press any key to return home:")
        admin()
    else:
        print(" Booking History is empty ")
        x=input("Press any key to return home:")
        admin()
# This function allows the admin to delete a user account.
def dropuser():
    ud=input("Enter the User ID:")
    s="SELECT name from cred where UID=%s"
    mycursor.execute(s,(ud,))
    n=mycursor.fetchone()
    if n:
        sql="Delete from cred where UID=%s"
        sqt="Delete from userdata where UID=%s"
        mycursor.execute(sql,(ud,))
        mydb.commit()
        mycursor.execute(sqt,(ud,))
        mydb.commit()
        print("User deleted successfully")
    else:
        print("User ID invalid")
        manageuser()
# This function displays complete information of a specific user.
def userdata():
    us=input("Enter the User ID:")
    sql="SELECT  A.UID,A.name,A.email,A.password,A.date,B.mobile,B.gender FROM cred  A, userdata B WHERE A.UID=B.UID and A.UID=%s "
    mycursor.execute(sql,(us,))
    myrecords=mycursor.fetchall()
    if not myrecords:
        print("User ID invalid")
        return
    print("\nUSER DETAILS")
    print("-" * 60)
    print("UID\tNAME\tEMAIL\tMOBILE\tGENDER\tDATE")
    print("-" * 60)
    for r in myrecords:
        print(
            f"{r[0]}\t{r[1]}\t{r[2]}\t{r[5]}\t{r[6]}\t{r[4].strftime('%d-%m-%Y')}"
        )

        
            
        
# This function displays complete information of all users.
def fulldata():
    
    query = """
    SELECT A.uid, A.name, A.email, A.password, A.date,
           B.mobile, B.gender
    FROM cred A
    JOIN userdata B
    ON A.uid = B.uid
    """
    
    mycursor.execute(query)
    records = mycursor.fetchall()
    
    print("\nALL USER DETAILS")
    print("-" * 80)
    print("UID\tNAME\tEMAIL\tMOBILE\tGENDER\tDATE")
    print("-" * 80)

    for r in records:
        print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[5]}\t{r[6]}\t{r[4].strftime('%d-%m-%Y')}")
    
def manageacc():
    mycursor.execute("select * from curr")
    current=mycursor.fetchone()
    uid=current[0]

    while True:
        print("\n--- MANAGE ACCOUNT ---")
        print("1. Change Name")
        print("2. Change Email")
        print("3. Change Password")
        print("4. Change Mobile")
        print("5. Change Gender")
        print("6. Exit")

        ch = input("Enter choice: ")

        try:
            if ch == "1":
                name = input("Enter new name: ")
                mycursor.execute("UPDATE cred SET name=%s WHERE UID=%s", (name, uid))
                mycursor.execute("UPDATE userdata SET name=%s WHERE UID=%s", (name, uid))

            elif ch == "2":
                email = input("Enter new email: ")
                mycursor.execute("UPDATE cred SET email=%s WHERE UID=%s", (email, uid))
                mycursor.execute("UPDATE userdata SET email=%s WHERE UID=%s", (email, uid))

            elif ch == "3":
                pwd = input("Enter new password: ")
                mycursor.execute("UPDATE cred SET password=%s WHERE UID=%s", (pwd, uid))
 

            elif ch == "4":
                mob = input("Enter new mobile: ")
                mycursor.execute("UPDATE userdata SET mobile=%s WHERE UID=%s", (mob, uid))

            elif ch == "5":
                gen = input("Enter gender (M/F): ")
                mycursor.execute("UPDATE userdata SET gender=%s WHERE UID=%s", (gen, uid))

            elif ch == "6":
                print("Returning to home")
                break

            else:
                print("Invalid option")
                continue

            mydb.commit()
            print("Updated successfully")

        except Exception as e:
            mydb.rollback()
            print("Update failed:", e)    
    

welc()
