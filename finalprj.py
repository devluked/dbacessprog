import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="finalassignment")
mycursor = mydb.cursor()
print(mydb)

if (mydb):
    print("\nDB Connection Successful!\n")
else:
    print("\nDB Connection Unsuccessful!\n")


def show_dbs():
    mycursor.execute("Show databases")
    print("\nHere's the databases being accessed through the Xampp MySQL server onto Phpmyadmin:")
    for db in mycursor:
        print(db)


def show_tables():
    mycursor.execute("Show tables")
    print("Here's the tables in the database for the gallery:")
    myresult = mycursor.fetchall()
    for tb in myresult:
        print(tb)


def show_columns(table):
    print(f"Here's the columns in the table {table}:")
    mycursor.execute(f"DESCRIBE {table}")
    myresult = mycursor.fetchall()
    for column in myresult:
        print(column[0])


def show_entries(table, column):
    print(f"Here's the records in the table {table} and the column {column}.")
    mycursor.execute(f"SELECT {column} FROM {table}")
    myresult = mycursor.fetchall()
    for rec in myresult:
        print(rec)


def grab_record(table, att, value):
    print(f"Here are the results for the {att} {value}:")
    mycursor.execute(f"SELECT * FROM {table} WHERE {att} LIKE {value}")
    myresult = mycursor.fetchall()
    for val in myresult:
        print(val)


def sort(table, att, dir):
    print(f"Sorting the {table} table by the {att} column in {dir} order:")
    mycursor.execute(f"SELECT * FROM {table} ORDER BY {att} {dir}")
    myresult = mycursor.fetchall()
    print()
    for val in myresult:
        print(val)


def grab_all_records(table):
    print(f"Here are the records from the {table} table:")
    mycursor.execute(f"SELECT * FROM {table}")
    myresult = mycursor.fetchall()
    for row in myresult:
        print(row)
    print()
    print("Would you like to sort these values?")
    print()
    ch = input("Y/N: ")
    print()
    if ch == "Y":
        print("Which value do you want to sort by?")
        show_columns(table)
        print()
        att = input()
        print()
        print("Would you like to sort ascending or descending?")
        dir = input("asc/desc: ")
        if dir == "asc":
            print()
            sort(table, att, dir)
        elif dir == "desc":
            print()
            sort(table, att, dir)
        else:
            print("I don't know that sort method")
            return
    elif ch == "N":
        return


print("""\nWelcome to my database application!
If you would like to quit, simply enter 5.
Below this there is a list of commands for the application.
Next to them you will find a corresponding number.
Entering that number will run that function.\n""")

x = True
while x:
    print("""1. Show ALL table names
2. Show ALL column names in specified table
3. Look up a record and return its data
4. Show ALL records in a table
5. Quit\n""")
    choice = input()
    if choice == "1":
        print()
        show_tables()
        print("\n")
    elif choice == "2":
        print("\nWhich table's columns would you like to see?: ")
        show_tables()
        print()
        clchoice = input()
        print()
        show_columns(clchoice)
        print("\n")
    elif choice == "3":
        rchoice = []
        print("\nWhich table is the record in?")
        show_tables()
        print()
        x = input()
        rchoice.append(x)
        print(f"\nWhich column is the record in table {rchoice[0]}?")
        show_columns(rchoice[0])
        x = input("\n")
        rchoice.append(x)
        print()  # This empty print is specifically for formatting purposes.
        show_entries(rchoice[0], rchoice[1])
        x = input(f"\nInput the specific value of the record (You must start and end the value with '.):")
        rchoice.append(x)
        print()
        grab_record(rchoice[0], rchoice[1], rchoice[2])
        print("\n")
    elif choice == "4":
        print("\nWhich table would you like to grab ALL records from:")
        show_tables()
        x = input("\n")
        print()
        grab_all_records(x)
        print("\n")
    elif choice == "5":
        x = False
