from tkinter import *
from tkinter import messagebox

# from db import Database (not yet used)

# db = Database("storage.db")


def main_menu():
    window.title("Untitled")  # name of the app not yet determined
    window.geometry("1280x720")
    window.config(bg="black")  # background of the program not yet determined
    title1 = Label(window, text="Title", font=('Helvetica', 45, 'bold'), bg='black', fg='white')
    title1.place(relx=0.5, rely=0.5, anchor=CENTER)  # Title of the product/company
    button1 = Button(window, text="Order Now!", font=('Helvetica', 20, 'bold'), bg='black', fg='white',
                          command=commands)
    button1.place(relx=0.5, rely=0.65, anchor=CENTER)
    button2 = Button(window, text="Check recent order", font=('Helvetica', 20, 'bold'), bg='black',
                          fg='white')
    button2.place(relx=0.5, rely=0.75, anchor=CENTER)
    button3 = Button(window, text="Exit", font=('Helvetica', 20, 'bold'), bg='black', fg='white',
                          command=window.destroy)
    button3.place(relx=0.5, rely=0.85, anchor=CENTER)


def commands():
    window = Tk()
    window.geometry("480x800")
    window.config(bg="black")
    order_list1 = Button(window, text="Coca-Cola           P 25.00", font=('Helvetica', 15, 'bold'),
                              bg='black', fg='white', command=confirmation)
    order_list1.place(relx=0.0, rely=0.0)
    order_list2 = Button(window, text="Sprite              P 25.00", font=('Helvetica', 15, 'bold'),
                              bg='black', fg='white', command=confirmation)
    order_list2.place(relx=0.0, rely=0.06)
    order_list3 = Button(window, text="Siomai Rice", font=('Helvetica', 15, 'bold'),
                              bg='black', fg='white', command=confirmation)
    order_list3.place(relx=0.0, rely=0.12)
    order_list4 = Button(window, text="Lumpia", font=('Helvetica', 15, 'bold'),
                              bg='black', fg='white', command=confirmation)
    order_list4.place(relx=0.0, rely=0.18)
    order_list5 = Button(window, text="Hotsilog", font=('Helvetica', 15, 'bold'),
                              bg='black', fg='white', command=confirmation)
    order_list5.place(relx=0.0, rely=0.24)
    order_list6 = Button(window, text="Longsilog", font=('Helvetica', 15, 'bold'),
                              bg='black', fg='white', command=confirmation)
    order_list6.place(relx=0.0, rely=0.30)
    order_list7 = Button(window, text="Longadog", font=('Helvetica', 15, 'bold'),
                              bg='black', fg='white', command=confirmation)
    order_list7.place(relx=0.0, rely=0.36)
    order_list8 = Button(window, text=" dito niyo lagay order list", font=('Helvetica', 15, 'bold'),
                              bg='black', fg='white', command=confirmation)
    order_list8.place(relx=0.0, rely=0.42)
    order_list9 = Button(window, text="dito niyo lagay order list ", font=('Helvetica', 15, 'bold'),
                              bg='black', fg='white', command=confirmation)
    order_list9.place(relx=0.0, rely=0.48)
    order_list10 = Button(window, text="dito niyo lagay order list ", font=('Helvetica', 15, 'bold'),
                               bg='black', fg='white', command=confirmation)
    order_list10.place(relx=0.0, rely=0.54)
    order_list11 = Button(window, text="dito niyo lagay order list", font=('Helvetica', 15, 'bold'),
                               bg='black', fg='white', command=confirmation)
    order_list11.place(relx=0.0, rely=0.6)
    order_list12 = Button(window, text="dito niyo lagay order list ", font=('Helvetica', 15, 'bold'),
                               bg='black', fg='white', command=confirmation)
    order_list12.place(relx=0.0, rely=0.66)

    back_button = Button(window, text="Back", font=('Helvetica', 15, 'bold'),
                              bg='black', fg='white', command=window.destroy)
    back_button.place(relx=0.0, rely=0.95)





def confirmation():
    answer = messagebox.askquestion("CONFIRM", "Confirm your order?")
    if answer == "Yes":
        Label(window, text="not finished")
    elif answer == "No":
        breakpoint()




window = Tk()
main_menu()
window.mainloop()
