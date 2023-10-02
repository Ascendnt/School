import sqlite3
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkMessageBox
import customtkinter

root = Tk()


class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("BRG-IMS")
        self.root.iconbitmap("E:/backups/Users/BALANTUCAS/Downloads/3.ico")  # icon
        width = 400
        height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.root.resizable(0, 0)
        Data.Database()


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
        if cursor.fetchone() is None:
            conn.commit()
        else:
            return


class Forms:
    def ShowLoginForm():
        global loginform
        global lbl_result
        loginform = Toplevel()
        loginform.grab_set()
        loginform.title("Login")
        loginform.iconbitmap("E:/backups/Users/BALANTUCAS/Downloads/3.ico")  # icon
        width = 400
        height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        loginform.resizable(0, 0)
        loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
        loginform.configure(background='gray35')

        # Frames
        TopLoginForm = customtkinter.CTkFrame(loginform, width=400, height=100, bd=1, relief=SOLID)
        TopLoginForm.pack(side=TOP, pady=5)
        MidLoginForm = customtkinter.CTkFrame(loginform, width=100, height=100)
        MidLoginForm.pack(side=TOP, pady=25)

        # Labels
        Text = customtkinter.CTkLabel(TopLoginForm, text="Login", width=600)
        Text.pack(padx=0, pady=1)
        Username = customtkinter.CTkLabel(MidLoginForm, text="Username:", text_font=("Bahnschrift Semibold", 15))
        Username.grid(row=0)
        Password = customtkinter.CTkLabel(MidLoginForm, text="Password:", text_font=("Bahnschrift Semibold", 15))
        Password.grid(row=1)
        lbl_result = customtkinter.CTkLabel(MidLoginForm, text="")
        lbl_result.grid(row=3, columnspan=2)

        # Entry Widgets
        username = customtkinter.CTkEntry(MidLoginForm, textvariable=USERNAME, width=100)
        username.grid(row=0, column=1)
        password = customtkinter.CTkEntry(MidLoginForm, textvariable=PASSWORD, width=100, show="*")
        password.grid(row=1, column=1)

        # Buttons
        Login = customtkinter.CTkButton(MidLoginForm, text="Login", command=Functions.Login)
        Login.grid(row=2, columnspan=2, pady=20)

    def ShowCreateForm():
        global createform
        global lbl_result
        createform = Toplevel()
        createform.grab_set()
        createform.title("Account Creation")
        width = 400
        height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        createform.iconbitmap("E:/backups/Users/BALANTUCAS/Downloads/3.ico")  # icon
        createform.resizable(0, 0)
        createform.geometry("%dx%d+%d+%d" % (width, height, x, y))
        createform.configure(background='gray35')

        # Frames
        TopCreateForm = customtkinter.CTkFrame(createform, width=400, height=100, bd=1, relief=SOLID)
        TopCreateForm.pack(side=TOP, pady=5)
        MidCreateForm = customtkinter.CTkFrame(createform, width=300, bg='#006400')
        MidCreateForm.pack(side=TOP, pady=20)

        # Labels
        Text = customtkinter.CTkLabel(TopCreateForm, text="Account Creation", width=600)
        Text.pack(fill=X)
        Username = customtkinter.CTkLabel(MidCreateForm, text="Username:", text_font=("Bahnschrift Semibold", 15))
        Username.grid(row=0)
        Password = customtkinter.CTkLabel(MidCreateForm, text="Password:", text_font=("Bahnschrift Semibold", 15))
        Password.grid(row=1)
        lbl_result = customtkinter.CTkLabel(MidCreateForm, text="", bg='#006400')
        lbl_result.grid(row=3, columnspan=2)

        # Entry Widgets
        user_name = customtkinter.CTkEntry(MidCreateForm, textvariable=USERNAME, width=100)
        user_name.grid(row=0, column=1)
        pass_word = customtkinter.CTkEntry(MidCreateForm, textvariable=PASSWORD, width=100, show="*")
        pass_word.grid(row=1, column=1)

        # Buttons
        Create = customtkinter.CTkButton(MidCreateForm, text="Create Account", command=Functions.CreateAcc)
        Create.grid(row=2, columnspan=2, pady=10)

    def Home():
        global Home
        Home = Tk()
        Home.title("Barangay Inventory Management System-Home")
        Home.configure(background='gray35')
        Home.iconbitmap("E:/backups/Users/BALANTUCAS/Downloads/3.ico")  # icon
        width = 400
        height = 300
        screen_width = Home.winfo_screenwidth()
        screen_height = Home.winfo_screenheight()

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
        Home.resizable(0, 0)

        # Labels
        L1 = customtkinter.CTkLabel(Home, fg='blue', bg='black',
                                    text="Barangay Inventory Management System",
                                    text_color="white", text_font=("Bahnschrift Semibold", 12))
        L1.pack(side=TOP, padx=10, pady=10)
        L2 = customtkinter.CTkLabel(Home, fg='blue', bg='black',
                                    text="Built and designed by Group 5",
                                    text_color="white", text_font=("Bahnschrift Semibold", 12))
        L2.pack(side=TOP, padx=5, pady=5)

        # Buttons
        btn = customtkinter.CTkButton(Home, text='Logout',
                                      command=Functions.Logout)
        btn.pack(side=TOP, padx=10, pady=5)
        btn1 = customtkinter.CTkButton(Home, text='View Inventory',
                                       command=Forms.ShowView)
        btn1.pack(side=TOP)
        btn2 = customtkinter.CTkButton(Home, text='Exit', command=Exit.Home)
        btn2.pack(side=TOP, padx=10, pady=5)

    def ShowHome():
        root.withdraw()
        Forms.Home()
        loginform.destroy()

    def ShowAddNew():
        global addnewform
        addnewform = customtkinter.CTkToplevel()
        addnewform.grab_set()
        addnewform.title("Add New Item")
        width = 600
        height = 450
        addnewform.configure(background='light blue')
        screen_width = Home.winfo_screenwidth()
        screen_height = Home.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
        addnewform.resizable(0, 0)
        if switch.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

        # Frames
        TopAddNew = customtkinter.CTkFrame(addnewform)
        TopAddNew.pack(side=TOP, pady=15)
        MidAddNew = customtkinter.CTkFrame(addnewform, border_color='light blue', fg_color='light blue')
        MidAddNew.pack(side=TOP, pady=40)

        # Labels
        namelabel = customtkinter.CTkLabel(TopAddNew, text="Add New Product", width=600)
        namelabel.pack(fill=X)
        itemnamelable = customtkinter.CTkLabel(MidAddNew, bg='#006400', fg='white', text='Item Name:')
        itemnamelable.grid(row=0, sticky=W)
        itemqtylable = customtkinter.CTkLabel(MidAddNew, bg='#006400', fg='white', text='Item Qty:')
        itemqtylable.grid(row=1, sticky=W)
        itemsinuselable = customtkinter.CTkLabel(MidAddNew, bg='#006400', fg='white', text='Item In Use:')
        itemsinuselable.grid(row=2, sticky=W)

        # Entry Widget
        itemname = customtkinter.CTkEntry(MidAddNew, textvariable=ITEM_NAME, width=100)
        itemname.grid(row=0, column=1)
        itemqty = customtkinter.CTkEntry(MidAddNew, textvariable=ITEM_QTY, width=100)
        itemqty.grid(row=1, column=1)
        iteminuse = customtkinter.CTkEntry(MidAddNew, textvariable=ITEMS_IN_USE, width=100)
        iteminuse.grid(row=2, column=1)

        # Buttons
        addbutton = customtkinter.CTkButton(MidAddNew, text='Save', command=Functions.AddNew)
        addbutton.grid(row=5, columnspan=2, pady=20)

    def ShowEdit():
        global editform
        editform = customtkinter.CTkToplevel()
        editform.grab_set()
        editform.title("Edit Product")
        width = 600
        height = 450
        editform.configure(background='light blue')
        screen_width = Home.winfo_screenwidth()
        screen_height = Home.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        editform.geometry("%dx%d+%d+%d" % (width, height, x, y))
        editform.resizable(0, 0)

        # Frames
        TopEditNew = customtkinter.CTkFrame(editform, width=600, height=100)
        TopEditNew.pack(side=TOP, pady=15)
        MidEditNew = customtkinter.CTkFrame(editform, border_color='light blue', fg_color='light blue')
        MidEditNew.pack(side=TOP, pady=30)

        # Labels
        namelabel = customtkinter.CTkLabel(TopEditNew, bg='#006400', fg='white', text="Edit Product",
                          width=600)
        namelabel.pack(fill=X)
        itemnamelable = customtkinter.CTkLabel(MidEditNew, bg='#006400', fg='white', text='Item Name:')
        itemnamelable.grid(row=0, sticky=W)
        itemqtylable = customtkinter.CTkLabel(MidEditNew, bg='#006400', fg='white', text='Item Qty:')
        itemqtylable.grid(row=1, sticky=W)
        itemsinuselable = customtkinter.CTkLabel(MidEditNew, bg='#006400', fg='white', text='Item In Use:')
        itemsinuselable.grid(row=2, sticky=W)

        # Entry Widget
        itemname = customtkinter.CTkEntry(MidEditNew, textvariable=ITEM_NAME, width=100)
        itemname.grid(row=0, column=1)
        itemqty = customtkinter.CTkEntry(MidEditNew, textvariable=ITEM_QTY, width=100)
        itemqty.grid(row=1, column=1)
        itemsinuse = customtkinter.CTkEntry(MidEditNew, textvariable=ITEMS_IN_USE, width=100)
        itemsinuse.grid(row=2, column=1)

        # Buttons
        savebutton = customtkinter.CTkButton(MidEditNew, text='Save', command=Functions.Edit)
        savebutton.grid(row=5, columnspan=2, pady=20)

    def ShowView():
        global viewform
        global tree
        global switch
        viewform = customtkinter.CTkToplevel()
        viewform.grab_set()
        viewform.title('Barangay Inventory Management System')
        width = 1000
        height = 600
        screen_width = Home.winfo_screenwidth()
        screen_height = Home.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
        viewform.iconbitmap("E:/backups/Users/BALANTUCAS/Downloads/3.ico")  # icon
        customtkinter.set_appearance_mode("System")
        viewform.resizable(0, 0)
        Home.withdraw()

        # Frames
        TopViewForm = customtkinter.CTkFrame(viewform, bd=2, width=800, bg='white')
        LeftViewForm = customtkinter.CTkFrame(viewform, bd=2, width=800, bg='#006400')
        RightViewForm = customtkinter.CTkFrame(viewform, bd=2, width=800, bg='black')

        # Labels
        namelabel = customtkinter.CTkLabel(TopViewForm, bg='#006400', fg='white', text="Inventory", width=800)
        searchlabel = customtkinter.CTkLabel(LeftViewForm, bg='#006400', fg='white', text="Search")

        # Entry Widget
        search = customtkinter.CTkEntry(LeftViewForm, textvariable=SEARCH, width=100)

        # Button
        searchbutton = customtkinter.CTkButton(LeftViewForm, width=15, text='Search',
                                               command=Functions.Search)
        resetbutton = customtkinter.CTkButton(LeftViewForm, width=15, text='Reset Search',
                                              command=Functions.Reset)
        addbutton = customtkinter.CTkButton(LeftViewForm, width=15, text='Add Item',
                                            command=Forms.ShowAddNew)
        editbutton = customtkinter.CTkButton(LeftViewForm, width=15, text='Edit Item',
                                             command=Forms.ShowEdit)
        deletebutton = customtkinter.CTkButton(LeftViewForm, width=15, text='Delete Item',
                                               command=Functions.Delete)
        exitbutton = customtkinter.CTkButton(LeftViewForm, width=15, text='Exit', command=Exit.Form)

        switch = customtkinter.CTkSwitch(LeftViewForm, text="Dark Mode", command=Functions.change_mode)

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
        switch.pack(side=TOP, padx=10, pady=10, fill=X)
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
                                          'Are you sure you want to exit? '
                                          'Completing this action will close the application',
                                          icon="warning")
        if result == 'yes':
            Home.destroy()
            exit()

    def Form():
        Home.deiconify()
        viewform.destroy()


class Functions:

    def Login(event=None):
        global ACCOUNT_ID
        Data.Database()
        if USERNAME.get == "" or PASSWORD.get() == "":
            lbl_result.config(text="Please complete the required field!", fg="black")
        else:
            cursor.execute("SELECT * FROM `Accounts` WHERE `ACCOUNT_NAME` = ? AND `Password` = ?",
                           (USERNAME.get(), PASSWORD.get()))
            if cursor.fetchone() is not None:
                cursor.execute("SELECT * FROM `Accounts` WHERE `ACCOUNT_NAME` = ? AND `Password` = ?",
                               (USERNAME.get(), PASSWORD.get()))
                data = cursor.fetchone()
                ACCOUNT_ID = data[0]
                USERNAME.set("")
                PASSWORD.set("")
                lbl_result.config(text="")
                Forms.ShowHome()
            else:
                lbl_result.config(text="Invalid username or password", fg="black", font=15)
                USERNAME.set("")
                PASSWORD.set("")
        cursor.close()
        conn.close()

    def DisplayData():
        Data.Database()
        cursor.execute("SELECT * FROM `Inventory`")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=data)
        cursor.close()
        conn.close()

    def Search():
        if SEARCH.get() != "":
            tree.delete(*tree.get_children())
            Data.Database()
            cursor.execute("SELECT * FROM `Inventory` WHERE `ITEM_NAME` LIKE ?", ('%' + str(SEARCH.get()) + '%',))
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
            "INSERT INTO `Inventory` (ACC_ID, ITEM_NAME, ITEM_QTY, ITEMS_IN_USE, ITEMS_NOT_IN_USE) "
            "VALUES (?, ?, ?, ?, ?)",
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
            result = tkMessageBox.askquestion('Barangay Inventory Management System',
                                              'Are you sure you want to edit this record?',
                                              icon="warning")
            if result == 'yes':
                curItem = tree.focus()
                contents = (tree.item(curItem))
                selecteditem = contents['values']
                tree.delete(curItem)
                Data.Database()
                cursor.execute("DELETE FROM `Inventory` WHERE `ITEM_ID` = %d" % selecteditem[0])
                cursor.execute(
                    "INSERT INTO `Inventory` (ACC_ID, ITEM_NAME, ITEM_QTY, ITEMS_IN_USE, ITEMS_NOT_IN_USE) "
                    "VALUES(?, ?, ?, ?, ?)",
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
            USERNAME.set("")
            root.deiconify()
            Home.withdraw()

    def CreateAcc():
        Data.Database()
        if USERNAME.get == "" or PASSWORD.get() == "":
            lbl_result.config(text="Please complete the required field!", fg="black")
        else:
            cursor.execute("INSERT INTO 'Accounts' (ACCOUNT_NAME, Password) VALUES(?, ?)",
                           (str(USERNAME.get()), str(PASSWORD.get())))
            tkMessageBox.showinfo("Success!", "Account has been created.")
            conn.commit()
            USERNAME.set("")
            PASSWORD.set("")
            cursor.close()
            conn.close()
            createform.destroy()

    def change_mode():
        if switch.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")


# VARIABLES
USERNAME = StringVar()
PASSWORD = StringVar()
ITEM_NAME = StringVar()
ITEM_QTY = IntVar()
ITEMS_IN_USE = IntVar()
SEARCH = StringVar()

# Labeles
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
L1 = customtkinter.CTkLabel(root, text="Barangay Inventory Management System",
                            text_color='white', text_font=("Bahnschrift Semibold", 12))
L1.pack(side=TOP, padx=10, pady=10)
L2 = customtkinter.CTkLabel(root, text="Built and designed by Group 5",
                            text_color='white', text_font=("Bahnschrift Semibold", 12))
L2.pack(side=TOP, padx=10, pady=5)
root.configure(bg='gray35')
# Buttons
b1 = customtkinter.CTkButton(root, text='Login', command=Forms.ShowLoginForm)
b1.pack(side=TOP, padx=10, pady=7)
b2 = customtkinter.CTkButton(root, text='Create Account',
                             command=lambda: (Data.Database(), Forms.ShowCreateForm()))
b2.pack(side=TOP, padx=10, pady=7)
b3 = customtkinter.CTkButton(root, text='Exit', command=Exit.Root)
b3.pack(side=TOP, padx=10, pady=7)

application = Main(root)
root.mainloop()
