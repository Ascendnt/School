import sqlite3
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkMessageBox

root = Tk()


class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Store Inventory System")
        self.root.configure(background='#006400')
        width = 400
        height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.root.resizable(0, 0)


class Data:
    def Database():
        global conn, cursor
        conn = sqlite3.connect("Brg_Ims.db")
        cursor = conn.cursor()
        cursor.execute("""PRAGMA foreign_keys = ON""")
        cursor.execute("""PRAGMA auto_vacuum  = FULL""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS Accounts (
                        ACCOUNT_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        ACCOUNT_NAME TEXT UNIQUE NOT NULL,
                        Password TEXT NOT NULL
                        )""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS Inventory (
                            Item_ID INTEGER PRIMARY KEY,
                            ACC_ID INTEGER NOT NULL,
                            ITEM_NAME TEXT NOT NULL,
                            ITEM_QTY INTEGER NOT NULL,
                            ITEMS_IN_USE INTEGER NOT NULL,
                            ITEMS_NOT_IN_USE INTEGER NOT NULL
                            )""")
        cursor.execute("SELECT * FROM 'Accounts' WHERE 'ACCOUNT_NAME' = 'admin' AND 'Password' = 'admin'")
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO 'Accounts' (ACCOUNT_NAME, Password) VALUES('admin', 'admin')")
            cursor.execute(
                "INSERT INTO `Inventory` (ACC_ID, ITEM_NAME, ITEM_QTY, ITEMS_IN_USE, ITEMS_NOT_IN_USE) VALUES (?, ?, ?, ?, ?)",
                ("1", "Placeholder", "10000", "20", "9980"))
            conn.commit()
        else:
            return


##                                    ACC_NAME TEXT NOT NULL,
##        FOREIGN KEY(ACC_NAME) REFERENCES Accounts(ACCOUNT_NAME)

class Forms:
    def ShowLoginForm():
        global loginform
        global lbl_result
        loginform = Toplevel()
        loginform.grab_set()
        loginform.title("Login")
        width = 400
        height = 350
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        loginform.resizable(0, 0)
        loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
        loginform.configure(background='#006400')

        # Frames
        TopLoginForm = Frame(loginform, width=400, height=100, bd=1, relief=SOLID)
        TopLoginForm.pack(side=TOP, pady=5)
        MidLoginForm = Frame(loginform, width=300, bg='#006400')
        MidLoginForm.pack(side=TOP, pady=20)

        # Labels
        Text = Label(TopLoginForm, text="Administrator Login", font=("Arial Black", 20), width=600)
        Text.pack(fill=X)
        Username = Label(MidLoginForm, text="Username:", font=("Bahnschrift Semibold", 20), bd=18, fg='white',
                         bg='#006400')
        Username.grid(row=0)
        Password = Label(MidLoginForm, text="Password:", font=("Bahnschrift Semibold", 20)
                         , bd=18, fg='white', bg='#006400')
        Password.grid(row=1)
        lbl_result = Label(MidLoginForm, text="", font=('arial', 15), bg='#006400')
        lbl_result.grid(row=3, columnspan=2)

        # Entry Widgets
        username = Entry(MidLoginForm, textvariable=USERNAME, font=("Arial", 20), width=10)
        username.grid(row=0, column=1)
        password = Entry(MidLoginForm, textvariable=PASSWORD, font=("Arial", 20), width=10, show="*")
        password.grid(row=1, column=1)

        # Buttons
        Login = Button(MidLoginForm, text="Login", font=("Bahnschrift Semibold", 15), width=20, command=Functions.Login)
        Login.grid(row=2, columnspan=2, pady=20)
        Login.bind('<Return>', Functions.Login)

    def ShowCreateForm():
        global createform
        global lbl_result
        createform = Toplevel()
        createform.grab_set()
        createform.title("Account Creation")
        width = 400
        height = 350
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        createform.resizable(0, 0)
        createform.geometry("%dx%d+%d+%d" % (width, height, x, y))
        createform.configure(background='#006400')

        # Frames
        TopCreateForm = Frame(createform, width=400, height=100, bd=1, relief=SOLID)
        TopCreateForm.pack(side=TOP, pady=5)
        MidCreateForm = Frame(createform, width=300, bg='#006400')
        MidCreateForm.pack(side=TOP, pady=20)

        # Labels
        Text = Label(TopCreateForm, text="Account Creation", font=("Arial Black", 20), width=600)
        Text.pack(fill=X)
        Username = Label(MidCreateForm, text="Username:", font=("Bahnschrift Semibold", 20), bd=18, fg='white',
                         bg='#006400')
        Username.grid(row=0)
        Password = Label(MidCreateForm, text="Password:", font=("Bahnschrift Semibold", 20)
                         , bd=18, fg='white', bg='#006400')
        Password.grid(row=1)
        lbl_result = Label(MidCreateForm, text="", font=('arial', 15), bg='#006400')
        lbl_result.grid(row=3, columnspan=2)

        # Entry Widgets
        user_name = Entry(MidCreateForm, textvariable=USERNAME, font=("Arial", 20), width=10)
        user_name.grid(row=0, column=1)
        pass_word = Entry(MidCreateForm, textvariable=PASSWORD, font=("Arial", 20), width=10, show="*")
        pass_word.grid(row=1, column=1)

        # Buttons
        Create = Button(MidCreateForm, text="Create Account", font=("Bahnschrift Semibold", 15), width=20,
                        command=Functions.CreateAcc)
        Create.grid(row=2, columnspan=2, pady=10)
        Create.bind('<Return>', Functions.CreateAcc)

    def Home():
        global Home
        Home = Tk()
        Home.title("Store Inventory System-Home")
        Home.configure(backgroun='#006400')
        width = 400
        height = 300
        screen_width = Home.winfo_screenwidth()
        screen_height = Home.winfo_screenheight()

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
        Home.resizable(0, 0)

        # Labels
        L1 = Label(Home, fg='white', bg='#006400', font=("Arial Black", 20), text="Store Inventory System")
        L1.pack(side=TOP, padx=10, pady=10)
        L2 = Label(Home, fg='white', bg='#006400', font=("Arial", 8), text="Built and designed by F. Arguson, J.Carlos")
        L2.pack(side=TOP, padx=5, pady=5)

        # Buttons
        btn = Button(Home, font=("Bahnschrift Semibold", 10), text='Logout', height=2, width=30,
                     command=Functions.Logout)
        btn.pack(side=TOP, padx=10, pady=5)
        btn1 = Button(Home, font=("Bahnschrift Semibold", 10), text='View Inventory', height=2, width=30,
                      command=Forms.ShowView)
        btn1.pack(side=TOP)
        btn2 = Button(Home, font=("Bahnschrift Semibold", 10), text='Exit', height=2, width=30, command=Exit.Home)
        btn2.pack(side=TOP, padx=10, pady=5)

    def ShowHome():
        root.withdraw()
        Forms.Home()
        loginform.destroy()

    def ShowAddNew():
        global addnewform
        addnewform = Toplevel()
        addnewform.grab_set()
        addnewform.title("Add New Item")
        width = 600
        height = 450
        addnewform.configure(background='#006400')
        screen_width = Home.winfo_screenwidth()
        screen_height = Home.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
        addnewform.resizable(0, 0)

        # Frames
        TopAddNew = Frame(addnewform, width=600, height=100, bd=2)
        TopAddNew.pack(side=TOP, pady=15)
        MidAddNew = Frame(addnewform, width=600, bg='#006400')
        MidAddNew.pack(side=TOP, pady=40)

        # Labels
        namelabel = Label(TopAddNew, text="Add New Product", font=("Arial Black", 20), width=600)
        namelabel.pack(fill=X)
        itemnamelable = Label(MidAddNew, bg='#006400', fg='white', text='Item Name:', font=("Bahnschrift Semibold", 20),
                              bd=5)
        itemnamelable.grid(row=0, sticky=W)
        itemqtylable = Label(MidAddNew, bg='#006400', fg='white', text='Item Qty:', font=("Bahnschrift Semibold", 20),
                             bd=5)
        itemqtylable.grid(row=1, sticky=W)
        itemsinuselable = Label(MidAddNew, bg='#006400', fg='white', text='Item In Use:',
                                font=("Bahnschrift Semibold", 20), bd=5)
        itemsinuselable.grid(row=2, sticky=W)

        # Entry Widget
        itemname = Entry(MidAddNew, textvariable=ITEM_NAME, font=("Arial", 20), width=15)
        itemname.grid(row=0, column=1)
        itemqty = Entry(MidAddNew, textvariable=ITEM_QTY, font=("Arial", 20), width=15)
        itemqty.grid(row=1, column=1)
        iteminuse = Entry(MidAddNew, textvariable=ITEMS_IN_USE, font=("Arial", 20), width=15)
        iteminuse.grid(row=2, column=1)

        # Buttons
        addbutton = Button(MidAddNew, text='Save', font=("Bahnschrift Semibold", 15), width=30, bg='#009ACD',
                           command=Functions.AddNew)
        addbutton.grid(row=5, columnspan=1, pady=20)

    def ShowEdit():
        global editform
        editform = Toplevel()
        editform.grab_set()
        editform.title("Edit Product")
        width = 600
        height = 450
        editform.configure(background='#006400')
        screen_width = Home.winfo_screenwidth()
        screen_height = Home.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        editform.geometry("%dx%d+%d+%d" % (width, height, x, y))
        editform.resizable(0, 0)

        # Frames
        TopEditNew = Frame(editform, width=600, height=100, bd=2)
        TopEditNew.pack(side=TOP, pady=15)
        MidEditNew = Frame(editform, width=600, bg='#006400')
        MidEditNew.pack(side=TOP, pady=30)

        # Labels
        namelabel = Label(TopEditNew, bg='#006400', fg='white', text="Edit Product", font=("Arial Black", 20),
                          width=600)
        namelabel.pack(fill=X)
        itemnamelable = Label(MidEditNew, bg='#006400', fg='white', text='Item Name:',
                              font=("Bahnschrift Semibold", 20), bd=5)
        itemnamelable.grid(row=0, sticky=W)
        itemqtylable = Label(MidEditNew, bg='#006400', fg='white', text='Item Qty:', font=("Bahnschrift Semibold", 20),
                             bd=5)
        itemqtylable.grid(row=1, sticky=W)
        itemsinuselable = Label(MidEditNew, bg='#006400', fg='white', text='Item In Use:',
                                font=("Bahnschrift Semibold", 20), bd=5)
        itemsinuselable.grid(row=2, sticky=W)

        # Entry Widget
        itemname = Entry(MidEditNew, textvariable=ITEM_NAME, font=("Arial", 20), width=15)
        itemname.grid(row=0, column=1)
        itemqty = Entry(MidEditNew, textvariable=ITEM_QTY, font=("Arial", 20), width=15)
        itemqty.grid(row=1, column=1)
        itemsinuse = Entry(MidEditNew, textvariable=ITEMS_IN_USE, font=("Arial", 20), width=15)
        itemsinuse.grid(row=2, column=1)

        # Buttons
        savebutton = Button(MidEditNew, text='Save', font=("Bahnschrift Semibold", 15), width=30, bg='#009ACD',
                            command=Functions.Edit)
        savebutton.grid(row=5, columnspan=2, pady=20)

    def ShowView():
        global viewform
        global tree
        viewform = Toplevel()
        viewform.grab_set()
        viewform.title('Store Inventory System')
        width = 1000
        height = 600
        screen_width = Home.winfo_screenwidth()
        screen_height = Home.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
        viewform.resizable(0, 0)
        Home.withdraw()

        # Frames
        TopViewForm = Frame(viewform, bd=2, width=800, bg='white')
        LeftViewForm = Frame(viewform, bd=2, width=800, bg='#006400')
        RightViewForm = Frame(viewform, bd=2, width=800, bg='black')

        # Labels
        namelabel = Label(TopViewForm, bg='#006400', fg='white', text="Inventory", font=("Arial Black", 20), width=800)
        searchlabel = Label(LeftViewForm, bg='#006400', fg='white', text="Search", font=("Arial Black", 15))

        # Entry Widget
        search = Entry(LeftViewForm, textvariable=SEARCH, font=("Arial", 15), width=15)

        # Button
        searchbutton = Button(LeftViewForm, font=("Bahnschrift Semibold", 10), width=15, text='Search',
                              command=Functions.Search)
        resetbutton = Button(LeftViewForm, font=("Bahnschrift Semibold", 10), width=15, text='Reset Search',
                             command=Functions.Reset)
        addbutton = Button(LeftViewForm, font=("Bahnschrift Semibold", 10), width=15, text='Add Item',
                           command=Forms.ShowAddNew)
        editbutton = Button(LeftViewForm, font=("Bahnschrift Semibold", 10), width=15, text='Edit Item',
                            command=Forms.ShowEdit)
        deletebutton = Button(LeftViewForm, font=("Bahnschrift Semibold", 10), width=15, text='Delete Item',
                              command=Functions.Delete)
        exitbutton = Button(LeftViewForm, font=("Bahnschrift Semibold", 10), width=15, text='Exit', command=Exit.Form)

        # Scrollbar
        scrollbarx = Scrollbar(RightViewForm, orient=HORIZONTAL)
        scrollbary = Scrollbar(RightViewForm, orient=VERTICAL)

        # Treeview
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=("Calibri", 10))
        style.configure("mystyle.Treeview.Heading", font=("Calibri", 15))
        tree = ttk.Treeview(RightViewForm, style="mystyle.Treeview",
                            columns=("Item_ID", "ACC_ID", "ITEM_NAME", "ITEM_QTY", "ITEMS_IN_USE",
                                     "ITEMS_NOT_IN_USE"), height=100, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)

        scrollbary.config(command=tree.yview)
        scrollbarx.config(command=tree.xview)

        tree.heading('Item_ID', text="Item ID", anchor='center')
        tree.heading('ACC_ID', text="Account ID", anchor='center')
        tree.heading('ITEM_NAME', text="Item Name", anchor='center')
        tree.heading('ITEM_QTY', text="Item Quantity", anchor='center')
        tree.heading('ITEMS_IN_USE', text="Items in Use", anchor='center')
        tree.heading('ITEMS_NOT_IN_USE', text="Items not in Use", anchor='center')

        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=0)
        tree.column('#2', stretch=NO, minwidth=0, width=0)
        tree.column('#3', stretch=NO, minwidth=0, width=195)
        tree.column('#4', stretch=NO, minwidth=0, width=195)
        tree.column('#5', stretch=NO, minwidth=0, width=195)
        tree.column('#6', stretch=NO, minwidth=0, width=195)

        # Packing it up
        TopViewForm.pack(side=TOP, fill=X)
        LeftViewForm.pack(side=LEFT, fill=Y)
        RightViewForm.pack(side=RIGHT, fill=X)
        namelabel.pack(fill=X)

        ##        pictureframe.pack()
        ##        pictureframe.place(anchor = N, relx=0.5, rely=0.05)
        ##        imagelabel.pack()

        searchlabel.pack(side=TOP, anchor='center', pady=10)
        search.pack(side=TOP, padx=10, fill=X)
        searchbutton.pack(side=TOP, padx=10, pady=10, fill=X)
        resetbutton.pack(side=TOP, padx=10, pady=5, fill=X)
        addbutton.pack(side=TOP, padx=10, pady=10, fill=X)
        editbutton.pack(side=TOP, padx=10, pady=10, fill=X)
        deletebutton.pack(side=TOP, padx=10, pady=10, fill=X)
        exitbutton.pack(side=TOP, padx=10, pady=10, fill=X)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.pack()
        Functions.DisplayData()


class Exit:
    def Root():
        result = tkMessageBox.askquestion('BRG-IMS', 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            root.destroy()
            exit()

    def Home():
        result = tkMessageBox.askquestion('BRG-IMG',
                                          'Are you sure you want to exit? Completing this action will close the application',
                                          icon="warning")
        if result == 'yes':
            Home.destroy()
            exit()

    def Form():
        Home.deiconify()
        viewform.destroy()


class Functions:

    def DisplayData():
        Data.Database()
        cursor.execute("SELECT * FROM `Inventory`")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

    def Search():
        if SEARCH.get() != "":
            tree.delete(*tree.get_children())
            Data.Database()
            cursor.execute("SELECT * FROM `Inventory` WHERE `ACC_ID` = ? ITEM_NAME LIKE ?",
                           ('%' + str(SEARCH.get()) + '%',))
            fetch = cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()

    def Reset():
        tree.delete(*tree.get_children())
        Functions.DisplayData()
        SEARCH.set("")

    def AddNew():
        Data.Database()
        cursor.execute(
            "INSERT INTO `Inventory` (ACC_ID, ITEM_NAME, ITEM_QTY, ITEMS_IN_USE, ITEMS_NOT_IN_USE) VALUES (?, ?, ?, ?, ?)",
            (int(ACCOUNT_ID), str(ITEM_NAME.get()), int(ITEM_QTY.get()), int(ITEMS_IN_USE.get()),
             (int(ITEM_QTY.get()) - int(ITEMS_IN_USE.get()))))
        conn.commit()
        ITEM_NAME.set("")
        ITEM_QTY.set("")
        ITEMS_IN_USE.set("")
        cursor.close()
        conn.close()
        addnewform.withdraw()
        viewform.withdraw()
        Forms.ShowView()

    def Edit():
        if not tree.selection():
            print("ERROR")
        else:
            result = tkMessageBox.askquestion('Store Inventory System', 'Are you sure you want to edit this record?',
                                              icon="warning")
            if result == 'yes':
                curItem = tree.focus()
                contents = (tree.item(curItem))
                selecteditem = contents['values']
                tree.delete(curItem)
                Data.Database()
                cursor.execute("DELETE FROM `Inventory` WHERE `ITEM_ID` = %d" % selecteditem[0])
                cursor.execute(
                    "INSERT INTO `Inventory` (ACC_ID, ITEM_NAME, ITEM_QTY, ITEMS_IN_USE, ITEMS_NOT_IN_USE) VALUES(?, ?, ?, ?, ?)",
                    (int(ACCOUNT_ID), str(ITEM_NAME.get()), int(ITEM_QTY.get()), int(ITEMS_IN_USE.get()),
                     (int(ITEM_QTY.get()) - int(ITEMS_IN_USE.get()))))
                conn.commit()
                ITEM_NAME.set("")
                ITEM_QTY.set("")
                ITEMS_IN_USE.set("")
                cursor.close()
                conn.close()
                editform.withdraw()
                viewform.withdraw()
                Forms.ShowView()

    def Delete():
        if not tree.selection():
            print("ERROR")
        else:
            result = tkMessageBox.askquestion('BRG-IMS', 'Are you sure you want to delete this record?', icon="warning")
            if result == 'yes':
                curItem = tree.focus()
                contents = (tree.item(curItem))
                selecteditem = contents['values']
                tree.delete(curItem)
                Data.Database()
                cursor.execute("DELETE FROM `Inventory` WHERE `ITEM_ID` = %d" % selecteditem[0])
                conn.commit()
                cursor.close()
                conn.close()

    def Logout():
        result = tkMessageBox.askquestion('BRG-IMS', 'Are you sure you want to logout?', icon="warning")
        if result == 'yes':
            ACCOUNT_ID = ""
            USERNAME.set("")
            root.deiconify()
            Home.withdraw()

    def Login(event=None):
        global ACCOUNT_ID
        Data.Database()
        if USERNAME.get == "" or PASSWORD.get() == "":
            lbl_result.config(text="Please complete the required field!", fg="white")
        else:
            cursor.execute("SELECT * FROM `Accounts` WHERE `ACCOUNT_NAME` = ? AND `Password` = ?",
                           (USERNAME.get(), PASSWORD.get()))
            if cursor.fetchone() is not None:
                cursor.execute("SELECT * FROM `Accounts` WHERE `ACCOUNT_NAME` = ? AND `Password` = ?",
                               (USERNAME.get(), PASSWORD.get()))
                data = cursor.fetchone()
                ACCOUNT_ID = data[0]
                print(ACCOUNT_ID)
                USERNAME.set("")
                PASSWORD.set("")
                lbl_result.config(text="")
                Forms.ShowHome()
            else:
                lbl_result.config(text="Invalid username or password", fg="white")
                USERNAME.set("")
                PASSWORD.set("")

        cursor.close()
        conn.close()

    def CreateAcc():
        Data.Database()
        if USERNAME.get == "" or PASSWORD.get() == "":
            lbl_result.config(text="Please complete the required field!", fg="white")
        else:
            cursor.execute("INSERT INTO 'Accounts' (ACCOUNT_NAME, Password) VALUES(?, ?)",
                           (str(USERNAME.get()), str(PASSWORD.get())))
            conn.commit()
            USERNAME.set("")
            PASSWORD.set("")
            cursor.close()
            conn.close()
            createform.destroy()


# VARIABLES
USERNAME = StringVar()
PASSWORD = StringVar()
ITEM_NAME = StringVar()
ITEM_QTY = IntVar()
ITEMS_IN_USE = IntVar()
SEARCH = StringVar()

# Labeles
L1 = Label(root, fg='white', bg='#006400', font=("Arial Black", 20), text="Store Inventory System")
L1.pack(side=TOP, padx=10, pady=10)
L2 = Label(root, fg='white', bg='#006400', font=("Arial", 8), text="Built and designed by F. Arguson, J.Carlos")
L2.pack(side=TOP, padx=10, pady=5)

# Buttons
b1 = Button(root, font=("Bahnschrift Semibold", 10), text='Login', height=2, width=30, command=Forms.ShowLoginForm)
b1.pack(side=TOP, padx=10, pady=5)
b2 = Button(root, font=("Bahnschrift Semibold", 10), text='Create Account', height=2, width=30,
            command=lambda: (Data.Database(), Forms.ShowCreateForm()))
b2.pack(side=TOP, padx=10, pady=5)
b3 = Button(root, font=("Bahnschrift Semibold", 10), text='Exit', height=2, width=30, command=Exit.Root)
b3.pack(side=TOP, padx=10, pady=5)

application = Main(root)
root.mainloop()
