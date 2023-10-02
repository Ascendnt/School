import sqlite3
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkMessageBox

root = Tk()

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Store Inventory System")
        self.root.configure(background = '#006400')
        width = 400
        height = 250
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.root.resizable(0, 0)

class Data:
    def Database():
        global conn, cursor
        conn = sqlite3.connect("myshopdata.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO 'admin' (username, password) VALUES ('admin', 'admin')")
            conn.commit()

class Forms:
    def ShowLoginForm():
        global loginform
        global lbl_result
        loginform = Toplevel()
        loginform.title("Login")
        loginform.configure(background = '#006400')       
        width = 400
        height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        loginform.resizable(0, 0)
        loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))

        
    #Frames
        TopLoginForm = Frame(loginform, width=400, height=100, bd=1, relief=SOLID)
        TopLoginForm.pack(side=TOP, pady=5)
        MidLoginForm = Frame(loginform, width=300, bg = '#006400')
        MidLoginForm.pack(side=TOP, pady=20)
        
    #Labels
        Text = Label(TopLoginForm, text="Administrator Login", font=("Arial Black", 20), width=600)
        Text.pack(fill=X)
        Username = Label(MidLoginForm, text="Username:", font=("Bahnschrift Semibold", 20), bd=18, fg = 'white', bg = '#006400')
        Username.grid(row=0)
        Password = Label(MidLoginForm, text="Password:", font=("Bahnschrift Semibold", 20)
                         , bd=18, fg = 'white', bg = '#006400')
        Password.grid(row=1)
        lbl_result = Label(MidLoginForm, text="", font=('arial', 18))
        lbl_result.grid(row=3, columnspan=2)
        
    #Entry Widgets
        username = Entry(MidLoginForm, textvariable=USERNAME, font=("Arial", 20), width=10)
        username.grid(row=0, column=1)
        password = Entry(MidLoginForm, textvariable=PASSWORD, font=("Arial", 20), width=10, show="*")
        password.grid(row=1, column=1)
        
    #Buttons
        Login = Button(MidLoginForm, text="Login", font=("Bahnschrift Semibold", 15), width=20, command=Functions.Login)
        Login.grid(row=2, columnspan=2, pady=20)
        Login.bind('<Return>', Functions.Login)

    def Home():
        global Home
        Home = Tk()
        Home.title("Store Inventory System-Home")
        Home.configure(background = '#006400')
        width = 400
        height = 300
        screen_width = Home.winfo_screenwidth()
        screen_height = Home.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
        Home.resizable(0, 0)
        
    #Labels
        L1 = Label(Home, fg = 'white', bg = '#006400', font = ("Arial Black", 20), text = "Store Inventory System")
        L1.pack(side=TOP, padx=10, pady=10)
        L2 = Label(Home, fg = 'white', bg = '#006400', font = ("Arial", 8), text = "Built and designed by F. Arguson, J.Castillo")
        L2.pack(side=TOP, padx=5, pady=5)
        
    #Buttons
        btn = Button(Home, font=("Bahnschrift Semibold", 10), text = 'Logout', height=2, width=30, command=Functions.Logout)
        btn.pack(side=TOP, padx=10, pady=5)
        btn1 = Button(Home, font=("Bahnschrift Semibold", 10), text = 'View Inventory', height=2, width=30, command=Forms.ShowView)
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
        addnewform.title("Add New Item")
        width = 600
        height = 450
        addnewform.configure(background = '#006400')
        screen_width = Home.winfo_screenwidth()
        screen_height = Home.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
        addnewform.resizable(0, 0)
        
    #Frames
        TopAddNew = Frame(addnewform, width=600, height=100, bd=2)
        TopAddNew.pack(side=TOP, pady=15)
        MidAddNew = Frame(addnewform, width=600, bg='#006400')
        MidAddNew.pack(side=TOP, pady=40)
        
    #Labels
        namelabel = Label(TopAddNew,text="Add New Product", font=("Arial Black", 20), width=600)
        namelabel.pack(fill=X)
        prodnamelable = Label(MidAddNew, bg = '#006400', fg = 'white' , text='Product Name:', font=("Bahnschrift Semibold", 20), bd = 5)
        prodnamelable.grid(row=0, sticky=W)
        prodqtylable = Label(MidAddNew, bg = '#006400', fg = 'white' , text='Product Qty:', font=("Bahnschrift Semibold", 20), bd = 5)
        prodqtylable.grid(row=1, sticky=W)
        prodpricelable = Label(MidAddNew, bg = '#006400', fg = 'white' , text='Product Price:', font=("Bahnschrift Semibold", 20), bd = 5)
        prodpricelable.grid(row=2, sticky=W)
        wholesaleqtylable = Label(MidAddNew, bg = '#006400', fg = 'white' , text='Wholesale Qty:', font=("Bahnschrift Semibold", 20), bd = 5)
        wholesaleqtylable.grid(row=3, sticky=W)
        wholesalepricelable = Label(MidAddNew, bg = '#006400', fg = 'white' , text='Wholesale Price:', font=("Bahnschrift Semibold", 20), bd = 5)
        wholesalepricelable.grid(row=4, sticky=W)
        
    #Entry Widget
        prodname = Entry(MidAddNew, textvariable=PRODUCT_NAME, font=("Arial", 20), width=15)
        prodname.grid(row=0, column=1)
        prodqty  = Entry(MidAddNew, textvariable=PRODUCT_QTY, font=("Arial", 20), width=15)
        prodqty.grid(row=1, column=1)
        prodprice = Entry(MidAddNew, textvariable=PRODUCT_PRICE, font=("Arial", 20), width=15)
        prodprice.grid(row=2, column=1)
        wholesaleqty = Entry(MidAddNew, textvariable=WHOLESALE_QTY, font=("Arial", 20), width=15)
        wholesaleqty.grid(row=3, column=1)
        wholesaleprice = Entry(MidAddNew, textvariable=WHOLESALE_PRICE, font=("Arial", 20), width=15)
        wholesaleprice.grid(row=4, column=1)
        
    #Buttons
        addbutton = Button(MidAddNew, text='Save', font=("Bahnschrift Semibold", 15), width=30, bg='#009ACD', command=Functions.AddNew)
        addbutton.grid(row=5, columnspan=2, pady=20)

    def ShowEdit():
        global editform
        if not tree.selection():
            print("ERROR")
        else:
            editform = Toplevel()
            editform.title("Edit Product")
            width = 600
            height = 450
            editform.configure(background = '#006400')
            screen_width = Home.winfo_screenwidth()
            screen_height = Home.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            editform.geometry("%dx%d+%d+%d" % (width, height, x, y))
            editform.resizable(0, 0)
            
        #Frames
            TopEditNew = Frame(editform, width=600, height=100, bd=2)
            TopEditNew.pack(side=TOP, pady=15)
            MidEditNew = Frame(editform, width=600, bg='#006400')
            MidEditNew.pack(side=TOP, pady=30)
            
        #Labels
            namelabel = Label(TopEditNew, text="Edit Product", font=("Arial Black", 20),width=600)
            namelabel.pack(fill=X)
            prodnamelable = Label(MidEditNew, bg = '#006400', fg = 'white' , text='Product Name:', font=("Bahnschrift Semibold", 20), bd = 5)
            prodnamelable.grid(row=0, sticky=W)
            prodqtylable = Label(MidEditNew, bg = '#006400', fg = 'white' , text='Product Qty:', font=("Bahnschrift Semibold", 20), bd = 5)
            prodqtylable.grid(row=1, sticky=W)
            prodpricelable = Label(MidEditNew, bg = '#006400', fg = 'white' , text='Product Price:', font=("Bahnschrift Semibold", 20), bd = 5)
            prodpricelable.grid(row=2, sticky=W)
            wholesaleqtylable = Label(MidEditNew, bg = '#006400', fg = 'white' , text='Wholesale Qty:', font=("Bahnschrift Semibold", 20), bd = 5)
            wholesaleqtylable.grid(row=3, sticky=W)
            wholesalepricelable = Label(MidEditNew, bg = '#006400', fg = 'white' , text='Wholesale Price:', font=("Bahnschrift Semibold", 20), bd = 5)
            wholesalepricelable.grid(row=4, sticky=W)
            
        #Entry Widgets
            prodname = Entry(MidEditNew, textvariable=PRODUCT_NAME, font=("Arial", 20), width=15)
            prodname.grid(row=0, column=1)
            prodqty  = Entry(MidEditNew, textvariable=PRODUCT_QTY, font=("Arial", 20), width=15)
            prodqty.grid(row=1, column=1)
            prodprice = Entry(MidEditNew, textvariable=PRODUCT_PRICE, font=("Arial", 20), width=15)
            prodprice.grid(row=2, column=1)
            wholesaleqty = Entry(MidEditNew, textvariable=WHOLESALE_QTY, font=("Arial", 20), width=15)
            wholesaleqty.grid(row=3, column=1)
            wholesaleprice = Entry(MidEditNew, textvariable=WHOLESALE_PRICE, font=("Arial", 20), width=15)
            wholesaleprice.grid(row=4, column=1)
            
        #Buttons
            savebutton = Button(MidEditNew, text='Save', font=("Bahnschrift Semibold", 15), width=30, bg='#009ACD', command=Functions.Edit)
            savebutton.grid(row=5, columnspan=2, pady=20)

    def ShowView():
        global viewform
        global tree
        viewform = Toplevel()
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
        
    #Frames
        TopViewForm = Frame(viewform, bd = 2, width = 800)
        TopViewForm.pack(side = TOP, fill = X)
        LeftViewForm = Frame(viewform, bd=2, width = 800, bg='#006400')
        LeftViewForm.pack(side = LEFT, fill = Y)
        RightViewForm = Frame(viewform, bd=2, width = 800)
        RightViewForm.pack(side = RIGHT)
        
    #Labels
        namelabel = Label(TopViewForm, bg = '#006400', fg = 'white', text = "Inventory", font = ("Arial Black", 20), width = 800)
        namelabel.pack(fill = X)
        searchlabel = Label(LeftViewForm, bg = '#006400', fg = 'white', text = "Search", font = ("Arial Black", 15))
        searchlabel.pack(side = TOP, anchor = 'center', pady=10)
        
    #Entry Widget
        search = Entry(LeftViewForm, textvariable=SEARCH, font = ("Arial", 15), width = 10)
        search.pack(side = TOP, padx=10, fill = X)
        
    #Button
        searchbutton = Button(LeftViewForm, font=("Bahnschrift Semibold", 10), text = 'Search', command=Functions.Search)
        searchbutton.pack(side = TOP, padx=10, pady=10, fill=X)
        resetbutton = Button(LeftViewForm, font=("Bahnschrift Semibold", 10), text = 'Reset Search', command=Functions.Reset)
        resetbutton.pack(side = TOP, padx=10, pady=5, fill=X)
        addbutton = Button(LeftViewForm, font=("Bahnschrift Semibold", 10), text = 'Add Item', command=Forms.ShowAddNew)
        addbutton.pack(side = TOP, padx=10, pady=10, fill=X )
        editbutton = Button(LeftViewForm, font=("Bahnschrift Semibold", 10), text = 'Edit Item', command=Forms.ShowEdit)
        editbutton.pack(side = TOP, padx=10, pady=10, fill=X)
        deletebutton = Button(LeftViewForm, font=("Bahnschrift Semibold", 10), text = 'Delete Item', command=Functions.Delete)
        deletebutton.pack(side = TOP, padx=10, pady=10, fill=X)
        exitbutton = Button(LeftViewForm, font=("Bahnschrift Semibold", 10), text = 'Exit', command=Exit.Form)
        
        exitbutton.pack(side = TOP, padx=10, pady=10, fill=X)
    #Scrollbar
        scrollbarx = Scrollbar(RightViewForm, orient=HORIZONTAL)
        scrollbary = Scrollbar(RightViewForm, orient=VERTICAL)

    #Treeview 
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=("Calibri", 10))
        style.configure("mystyle.Treeview.Heading", font=("Calibri", 15))
        tree = ttk.Treeview(RightViewForm, style="mystyle.Treeview",
                            columns=("Product ID", "Product Name", "Product Qty", "Product Price",
                            "Wholesale Qty", "Wholesale Price"), height=100, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)

        tree.heading('Product ID', text="Product ID", anchor='center')
        tree.heading('Product Name', text="Product Name", anchor='center')
        tree.heading('Product Qty', text="Product Qty", anchor='center')
        tree.heading('Product Price', text="Product Price", anchor='center')
        tree.heading('Wholesale Qty', text="Wholesale Qty", anchor='center')
        tree.heading('Wholesale Price', text="Wholesale Price", anchor='center')

        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=0)
        tree.column('#2', stretch=NO, minwidth=0, width=200)
        tree.column('#3', stretch=NO, minwidth=0, width=150)
        tree.column('#4', stretch=NO, minwidth=0, width=150)
        tree.column('#5', stretch=NO, minwidth=0, width=150)
        tree.pack()
        Functions.DisplayData()

class Exit:
    def Root():
        result = tkMessageBox.askquestion('Store Inventory System', 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            root.destroy()
            exit()
    def Home():
        result = tkMessageBox.askquestion('Store Inventory System','Are you sure you want to exit? Completing this action will close the application', icon="warning")
        if result == 'yes':
            Home.destroy()
            exit()
    def Form():
        Home.deiconify()
        viewform.withdraw()

class Functions:
        
    def DisplayData():
        Data.Database()
        cursor.execute("SELECT * FROM `product`")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()


    def Search():
        if SEARCH.get() != "":
            tree.delete(*tree.get_children())
            Data.Database()
            cursor.execute("SELECT * FROM `product` WHERE `product_name` LIKE ?", ('%' + str(SEARCH.get()) + '%',))
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
        cursor.execute("INSERT INTO `product` (product_name, product_qty, product_price, wholesale_qty, wholesale_price) VALUES(?, ?, ?, ?, ?)",
                       (str(PRODUCT_NAME.get()), int(PRODUCT_QTY.get()), int(PRODUCT_PRICE.get()), int(WHOLESALE_QTY.get()), int(WHOLESALE_PRICE.get())))
        conn.commit()
        PRODUCT_NAME.set("")
        PRODUCT_PRICE.set("")
        PRODUCT_QTY.set("")
        WHOLESALE_QTY.set("")
        WHOLESALE_PRICE.set("")
        cursor.close()
        conn.close()
        addnewform.withdraw()
        viewform.withdraw()
        Forms.ShowView()

    def Edit():
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']
        tree.delete(curItem)
        Data.Database()
        cursor.execute("DELETE FROM `product` WHERE `product_id` = %d" % selecteditem[0])
        cursor.execute("INSERT INTO `product` (product_name, product_qty, product_price, wholesale_qty, wholesale_price) VALUES(?, ?, ?, ?, ?)",
               (str(PRODUCT_NAME.get()), int(PRODUCT_QTY.get()), int(PRODUCT_PRICE.get()), int(WHOLESALE_QTY.get()), int(WHOLESALE_PRICE.get())))
        conn.commit()
        PRODUCT_NAME.set("")
        PRODUCT_PRICE.set("")
        PRODUCT_QTY.set("")
        WHOLESALE_QTY.set("")
        WHOLESALE_PRICE.set("")
        cursor.close()
        conn.close()
        editform.withdraw()
        viewform.withdraw()
        Forms.ShowView()

    def Delete():
        if not tree.selection():
            print("ERROR")
        else:
            result = tkMessageBox.askquestion('Store Inventory System', 'Are you sure you want to delete this record?', icon="warning")
            if result == 'yes':
                curItem = tree.focus()
                contents = (tree.item(curItem))
                selecteditem = contents['values']
                tree.delete(curItem)
                Data.Database()
                cursor.execute("DELETE FROM `product` WHERE `product_id` = %d" % selecteditem[0])
                conn.commit()
                cursor.close()
                conn.close()
    
    def Logout():
        result = tkMessageBox.askquestion('Simple Inventory System', 'Are you sure you want to logout?', icon="warning")
        if result == 'yes': 
            admin_id = ""
            root.deiconify()
            Home.withdraw()


    def Login(event=None):
        global admin_id
        Data.Database()
        if USERNAME.get == "" or PASSWORD.get() == "":
            lbl_result.config(text="Please complete the required field!", fg="red")
        else:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
            if cursor.fetchone() is not None:
                cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
                data = cursor.fetchone()
                admin_id = data[0]
                USERNAME.set("")
                PASSWORD.set("")
                lbl_result.config(text="")
                Forms.ShowHome()
            else:
                lbl_result.config(text="Invalid username or password", fg="red")
                USERNAME.set("")
                PASSWORD.set("")
        cursor.close()
        conn.close()
        
#VARIABLES
USERNAME = StringVar()
PASSWORD = StringVar()
PRODUCT_NAME = StringVar()
PRODUCT_PRICE = IntVar()
PRODUCT_QTY = IntVar()
WHOLESALE_QTY = IntVar()
WHOLESALE_PRICE = IntVar()
SEARCH = StringVar()

#Labeles
L1 = Label(root, fg = 'white', bg = '#006400', font = ("Arial Black", 20), text = "Store Inventory System")
L1.pack(side = TOP, padx=10, pady=10)
L2 = Label(root, fg = 'white', bg = '#006400', font = ("Arial", 8), text = "Built and designed by F. Arguson, J.Castillo")
L2.pack(side=TOP, padx=10, pady=5)

#Buttons
b1 = Button(root, font=("Bahnschrift Semibold", 10), text = 'Login', height = 2, width = 30,command = Forms.ShowLoginForm)
b1.pack(side=TOP, padx=10, pady=5)
b2 = Button(root, font=("Bahnschrift Semibold", 10), text = 'Exit', height = 2, width = 30, command = Exit.Root)
b2.pack(side=TOP, padx=10, pady=5)



application = Main(root)
root.mainloop()
