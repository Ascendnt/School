from tkinter import *
from database import Database

db = Database("store.db")


def populate_list():
    for row in db.fetch():
        test_list.insert(END, row)


def add_item():
    print("add")


def remove_item():
    print("remove")


def update_item():
    print("update")


def clear_text():
    print("clear")


app = Tk()

text = StringVar()
test_label = Label(app, text="Part Name", font=("bold", 14), pady=20)
test_label.grid(row=0, column=0, sticky=W)
test_entry = Entry(app, textvariable=text)
test_entry.grid(row=0, column=1)

text = StringVar()
test_label = Label(app, text="Part Name2", font=("bold", 14),)
test_label.grid(row=0, column=2, sticky=W)
test_entry = Entry(app, textvariable=text)
test_entry.grid(row=0, column=3)

text = StringVar()
test_label = Label(app, text="Part Name3", font=("bold", 14),)
test_label.grid(row=1, column=0, sticky=W)
test_entry = Entry(app, textvariable=text)
test_entry.grid(row=1, column=1)

text = StringVar()
test_label = Label(app, text="Part Name4", font=("bold", 14),)
test_label.grid(row=1, column=2, sticky=W)
test_entry = Entry(app, textvariable=text)
test_entry.grid(row=1, column=3)


test_list = Listbox(app, height=8, width=50, border=0)
test_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

test_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=test_list.yview)

add_btn = Button(app, text="add something", width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text="remove something", width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text="update something", width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text="clear something", width=12, command=clear_text)
clear_btn.grid(row=2, column=3 )



app.title("Testing")
app.geometry("700x350")

populate_list()

app.mainloop()
