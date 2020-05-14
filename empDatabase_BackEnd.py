import sqlite3
#backend

def employeeData():
    con=sqlite3.connect("employee.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY, EmpID text, Firstname text, Lastname text, DOB text, \
        Gender text, Address text, Mobile text)")
    con.commit()
    con.close()

def addEmpRec(EmpID, Firstname, Lastname, DOB, Gender, Address, Mobile):
    con=sqlite3.connect("employee.db")
    cur = con.cursor()
    cur.execute("INSERT INTO employee VALUES (NULL, ?,?,?,?,?,?,?)",(EmpID, Firstname, Lastname, DOB , Gender, Address, Mobile))
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("employee.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM employee")
    rows=cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con=sqlite3.connect("employee.db")
    cur = con.cursor()
    cur.execute("DELETE FROM employee WHERE id=?", (id,))
    con.commit()
    con.close()

def searchData(EmpID="", Firstname="", Lastname="", DOB="", Gender="", Address="", Mobile=""):
    con=sqlite3.connect("employee.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM employee WHERE EmpID=? OR Firstname=? OR Lastname=? OR DOB=? OR \
        Gender=? OR Address=? OR Mobile=? ", (EmpID, Firstname, Lastname, DOB, Gender, Address, Mobile))
    rows=cur.fetchall()
    con.close()
    return rows

def dataUpdate(id, EmpID="", Firstname="", Lastname="", DOB="", Gender="", Address="", Mobile=""):
    con=sqlite3.connect("employee.db")
    cur = con.cursor()
    cur.execute("UPDATE employee SET EmpID=?, Firstname=?, Lastname=?, DOB=?, \
        Gender=?, Address=?, Mobile=?, WHERE id=?",(EmpID, Firstname, Lastname, DOB, Gender, Address, Mobile, id))
    con.commit()
    con.close()

employeeData()

