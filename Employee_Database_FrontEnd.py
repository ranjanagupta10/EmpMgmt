#Frontend

from tkinter import *
import tkinter.messagebox
import empDatabase_BackEnd

class Employee:

    # TO CREATE MAIN FRAME
    def __init__(self,root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="gold")
        self.root.resizable(False,False)

        # VARIABLES DECLARED
        EmpID = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()
        DOB = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

        #=============================================Funtions============================================

        # TO EXIT WHOLE WINDOW
        def iExit():
            iExit = tkinter.messagebox.askyesno("Employee Management System","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        # TO CLEAR DATA FROM TEXT ENTRY FIELDS
        def clearData():
            self.txtEmpID.delete(0,END)
            self.txtfna.delete(0,END)
            self.txtLna.delete(0,END)
            self.txtDOB.delete(0,END)
            self.txtGender.delete(0,END)
            self.txtAdr.delete(0,END)
            self.txtMobile.delete(0,END)

        # EVENT CREATED FOR LISTBOX, SO WHEN AN ITEM IS SELECTD IN LISTBOX IT GETS FETCHED BACK INTO THE TEXT FIELDS
        def EmployeeRec(event):
            global sd
            searchEmp = employeeList.curselection()[0]
            sd = employeeList.get(searchEmp)

            # IT DELETES THE EXISTING VALUES IN TEXT FILEDS AND FETCHES THE ITEMS FROM LIST BOX TO RESPECTIVE FIELDS
            self.txtEmpID.delete(0,END)
            self.txtEmpID.insert(END,sd[1])
            self.txtfna.delete(0,END)
            self.txtfna.insert(END,sd[2])
            self.txtLna.delete(0,END)
            self.txtLna.insert(END,sd[3])
            self.txtDOB.delete(0,END)
            self.txtDOB.insert(END,sd[4])
            self.txtGender.delete(0,END)
            self.txtGender.insert(END,sd[5])
            self.txtAdr.delete(0,END)
            self.txtAdr.insert(END,sd[6])
            self.txtMobile.delete(0,END)
            self.txtMobile.insert(END,sd[7])

        # IT ADDS DATA INTO DATABASE AFTER CALLING IT FROM BACKEND
        def addData():
            if(len(EmpID.get())!=0):
                empDatabase_BackEnd.addEmpRec(EmpID.get(), Firstname.get(), Lastname.get(), DOB.get(), Gender.get(), Address.get(), Mobile.get())
                employeeList.delete(0,END)
                employeeList.insert(END,(EmpID.get(), Firstname.get(), Lastname.get(), DOB.get(), Gender.get(), Address.get(), Mobile.get()))

        # IT DISPLAYS ALL DATA AFTER FETCHING IN FOR LOOP FROM BACKEND
        def DisplayData():
            employeeList.delete(0,END)
            for row in empDatabase_BackEnd.viewData():
                employeeList.insert(END,row,str(""))

        # IT DELETES EMPLOYEE DATA FROM IT'S EMPLOYEE ID
        def DeleteData():
            if(len(EmpID.get())!=0):
                empDatabase_BackEnd.deleteRec(sd[0])
                clearData()
                DisplayData()

        # IT SEARCHES DATABASE FOR THE FIELDS AND REFLECTS THE RESULTS IN LISTBOX
        def searchDatabase():
            employeeList.delete(0,END)
            for row in empDatabase_BackEnd.searchData(EmpID.get(), Firstname.get(), Lastname.get(), DOB.get(), Gender.get(), Address.get(), Mobile.get()):
                employeeList.insert(END,row,str(""))

        # IT UPDATES DATABASE BY DELETING THE SELECTED DATA AND ADDING ANOTHER IN IT'S PLACE BASICALLY OVERWRITE
        def update():
            if(len(EmpID.get())!=0):
                empDatabase_BackEnd.deleteRec(sd[0])
            if(len(EmpID.get())!=0):
                empDatabase_BackEnd.addEmpRec(EmpID.get(), Firstname.get(), Lastname.get(), DOB.get(), Gender.get(), Address.get(), Mobile.get())
                employeeList.delete(0,END)
                employeeList.insert(END,(EmpID.get(), Firstname.get(), Lastname.get(), DOB.get(), Gender.get(), Address.get(), Mobile.get()))

        # FUNCTION WHICH RESTRICTS DATA ENTERED TO BE ONLY A DIGITS
        def correct(inp):
            if inp.isdigit():
                return True
            elif inp == "":
                return True
            else:
                return False

        reg = self.root.register(correct)

        # FUNCTION WHICH RESTRICTS DATA ENTERED TO BE ONLY A ALPHABETS
        def correct1(inp):
            if inp.isalpha():
                return True
            elif inp == "":
                return True
            else:
                return False

        reg1 = self.root.register(correct1)

        #=============================================Frames==============================================
        MainFrame = Frame(self.root, bg="gold")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="light goldenrod", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial', 47, 'bold'), text="Employee Management System", bg="light goldenrod")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="light goldenrod", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, bg="light goldenrod", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, bg="light goldenrod", relief=RIDGE,
                                font=('arial',20,'bold'), text="Employee Info\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, bg="light goldenrod", relief=RIDGE,
                                font=('arial',20,'bold'), text="Employee Details\n")
        DataFrameRIGHT.pack(side=RIGHT)

        #======================================Labels and Entry Widget====================================
        self.lblEmpID = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Employee ID: ",padx=2, pady=2, bg="light goldenrod")
        self.lblEmpID.grid(row=0, column=0, sticky=W)
        self.txtEmpID = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=EmpID, width=29, \
         validate ="key", validatecommand=(reg, '%P'))
        self.txtEmpID.grid(row=0, column=1)

        self.lblfna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="First Name: ",padx=2, pady=2, bg="light goldenrod")
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Firstname, width=29, \
         validate ="key", validatecommand=(reg1, '%P'))
        self.txtfna.grid(row=1, column=1)

        self.lblLna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Last Name: ",padx=2, pady=2, bg="light goldenrod")
        self.lblLna.grid(row=2, column=0, sticky=W)
        self.txtLna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Lastname, width=29, \
         validate ="key", validatecommand=(reg1, '%P'))
        self.txtLna.grid(row=2, column=1)

        self.lblDOB = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Date of Birth: ",padx=2, pady=2, bg="light goldenrod")
        self.lblDOB.grid(row=3, column=0, sticky=W)
        self.txtDOB = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=DOB, width=29)
        self.txtDOB.grid(row=3, column=1)

        self.lblGender = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Gender: ",padx=2, pady=2, bg="light goldenrod")
        self.lblGender.grid(row=4, column=0, sticky=W)
        self.txtGender = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Gender, width=29, \
         validate ="key", validatecommand=(reg1, '%P'))
        self.txtGender.grid(row=4, column=1)

        self.lblAdr = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Address: ",padx=2, pady=2, bg="light goldenrod")
        self.lblAdr.grid(row=5, column=0, sticky=W)
        self.txtAdr = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Address, width=29)
        self.txtAdr.grid(row=5, column=1)

        self.lblMobile = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Mobile No: ",padx=2, pady=2, bg="light goldenrod")
        self.lblMobile.grid(row=6, column=0, sticky=W)
        self.txtMobile = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Mobile, width=29, \
         validate ="key", validatecommand=(reg, '%P'))
        self.txtMobile.grid(row=6, column=1)

        #====================================Listbar and Scrollbar Widget===================================

        # SCROLLBAR DEFINED AND ADDED NEXT TO LISTBOX WHILE USING SET ATTRIBUTE OF IT TO ATTACH IT TO LISTBOX
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # IT RECALLS THE EMPLOYEEREC EVENT WHICH HELPS IN DISPLAYING SELECTED DATA IN LISTBOX BACK TO TEXT FIELDS
        employeeList = Listbox(DataFrameRIGHT, width=61, height=16, font=('arial',12,'bold'), yscrollcommand=scrollbar.set)
        employeeList.bind('<<ListboxSelect>>', EmployeeRec)
        employeeList.grid(row=0, column=0, padx=8)
        scrollbar.config(command = employeeList.yview)

        #=============================================Button Widget=========================================

        self.btnAddDate = Button(ButtonFrame, text="Add New", font=('arial', 20, 'bold'),height=1, width=10, bd=4, command=addData)
        self.btnAddDate.grid(row=0, column=0)

        self.btnDisplayDate = Button(ButtonFrame, text="Display", font=('arial', 20, 'bold'),height=1, width=10, bd=4, command=DisplayData)
        self.btnDisplayDate.grid(row=0, column=1)

        self.btnClearDate = Button(ButtonFrame, text="Clear", font=('arial', 20, 'bold'),height=1, width=10, bd=4, command=clearData)
        self.btnClearDate.grid(row=0, column=2)

        self.btnDeleteDate = Button(ButtonFrame, text="Delete", font=('arial', 20, 'bold'),height=1, width=10, bd=4, command=DeleteData)
        self.btnDeleteDate.grid(row=0, column=3)

        self.btnSearchDate = Button(ButtonFrame, text="Search", font=('arial', 20, 'bold'),height=1, width=10, bd=4, command=searchDatabase)
        self.btnSearchDate.grid(row=0, column=4)

        self.btnUpdateDate = Button(ButtonFrame, text="Update", font=('arial', 20, 'bold'),height=1, width=10, bd=4, command=update)
        self.btnUpdateDate.grid(row=0, column=5)

        self.btnExitDate = Button(ButtonFrame, text="Exit", font=('arial', 20, 'bold'),height=1, width=10, bd=4, command=iExit)
        self.btnExitDate.grid(row=0, column=6)






if __name__=='__main__':
    root = Tk()
    application = Employee(root)
    root.mainloop()

