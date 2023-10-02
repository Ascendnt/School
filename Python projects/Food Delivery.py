from tkinter import *



# from db import Database (not yet used)

# db = Database("storage.db")


class Application:
    def __init__(self, window):
        self.window = window
        self.window.title("Untitled")  # name of the app not yet determined
        self.window.geometry("1280x720")
        self.window.config(bg="black")  # background of the program not yet determined
        self.main_menu()

    def main_menu(self):

        self.title1 = Label(self.window, text="Title", font=('Helvetica', 45, 'bold'), bg='black', fg='white')
        self.title1.place(relx=0.5, rely=0.5, anchor=CENTER)  # Title of the product/company
        self.button1 = Button(self.window, text="Order Now!", font=('Helvetica', 20, 'bold'), bg='black', fg='white',
                              command=self.commands)
        self.button1.place(relx=0.5, rely=0.65, anchor=CENTER)
        self.button2 = Button(self.window, text="Check recent order", font=('Helvetica', 20, 'bold'), bg='black',
                              fg='white')
        self.button2.place(relx=0.5, rely=0.75, anchor=CENTER)
        self.button3 = Button(self.window, text="Exit", font=('Helvetica', 20, 'bold'), bg='black', fg='white',
                              command=self.window.destroy)
        self.button3.place(relx=0.5, rely=0.85, anchor=CENTER)

    def commands(self):
        self.order_list1 = Button(self.window, text="Coca-Cola           P 25.00", font=('Helvetica', 15, 'bold'),
                                  bg='black', fg='white', command=self.confirmation)
        self.order_list1.place(relx=0.0, rely=0.0)
        self.order_list2 = Button(self.window, text="Sprite              P 25.00", font=('Helvetica', 15, 'bold'),
                                  bg='black', fg='white', command=self.confirmation)
        self.order_list2.place(relx=0.0, rely=0.06)
        self.order_list3 = Button(self.window, text="dito niyo lagay order list", font=('Helvetica', 15, 'bold'),
                                  bg='black', fg='white', command=self.confirmation)
        self.order_list3.place(relx=0.0, rely=0.12)
        self.order_list4 = Button(self.window, text="dito niyo lagay order list ", font=('Helvetica', 15, 'bold'),
                                  bg='black', fg='white', command=self.confirmation)
        self.order_list4.place(relx=0.0, rely=0.18)
        self.order_list5 = Button(self.window, text=" dito niyo lagay order list", font=('Helvetica', 15, 'bold'),
                                  bg='black', fg='white', command=self.confirmation)
        self.order_list5.place(relx=0.0, rely=0.24)
        self.order_list6 = Button(self.window, text="dito niyo lagay order list ", font=('Helvetica', 15, 'bold'),
                                  bg='black', fg='white', command=self.confirmation)
        self.order_list6.place(relx=0.0, rely=0.30)
        self.order_list7 = Button(self.window, text=" dito niyo lagay order list", font=('Helvetica', 15, 'bold'),
                                  bg='black', fg='white', command=self.confirmation)
        self.order_list7.place(relx=0.0, rely=0.36)
        self.order_list8 = Button(self.window, text=" dito niyo lagay order list", font=('Helvetica', 15, 'bold'),
                                  bg='black', fg='white', command=self.confirmation)
        self.order_list8.place(relx=0.0, rely=0.42)
        self.order_list9 = Button(self.window, text="dito niyo lagay order list ", font=('Helvetica', 15, 'bold'),
                                  bg='black', fg='white', command=self.confirmation)
        self.order_list9.place(relx=0.0, rely=0.48)
        self.order_list10 = Button(self.window, text="dito niyo lagay order list ", font=('Helvetica', 15, 'bold'),
                                  bg='black', fg='white', command=self.confirmation)
        self.order_list10.place(relx=0.0, rely=0.54)
        self.order_list11 = Button(self.window, text="dito niyo lagay order list", font=('Helvetica', 15, 'bold'),
                                  bg='black', fg='white', command=self.confirmation)
        self.order_list11.place(relx=0.0, rely=0.6)
        self.order_list12 = Button(self.window, text="dito niyo lagay order list ", font=('Helvetica', 15, 'bold'),
                                  bg='black', fg='white', command=self.confirmation)
        self.order_list12.place(relx=0.0, rely=0.66)
        self.title1.destroy()
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.back_button = Button(self.window, text="Back", font=('Helvetica', 15, 'bold'),
                                  bg='black', fg='white', command=self.back)
        self.back_button.place(relx=0.0, rely=0.95)

        self.confirm.destroy()
        self.yes.destroy()
        self.no.destroy()

    def back(self):
        self.order_list1.destroy()
        self.order_list2.destroy()
        self.order_list3.destroy()
        self.order_list4.destroy()
        self.order_list5.destroy()
        self.order_list6.destroy()
        self.order_list7.destroy()
        self.order_list8.destroy()
        self.order_list9.destroy()
        self.order_list10.destroy()
        self.order_list11.destroy()
        self.order_list12.destroy()
        self.back_button.destroy()
        self.main_menu()

    def confirmation(self):
        self.confirm = Label(self.window, text="Confirm your order?", font=('Helvetica', 15, 'bold'),
                                  bg='black', fg='white')
        self.confirm.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.yes = Button(self.window, text="Yes", font=('Helvetica', 15, 'bold'),
                                  bg='black', fg='white')
        self.yes.place(relx=0.45, rely=0.55, anchor=CENTER)
        self.no = Button(self.window, text="No", font=('Helvetica', 15, 'bold'),
                                  bg='black', fg='white', command=self.commands)
        self.no.place(relx=0.55, rely=0.55, anchor=CENTER)
        self.order_list1.destroy()
        self.order_list2.destroy()
        self.order_list3.destroy()
        self.order_list4.destroy()
        self.order_list5.destroy()
        self.order_list6.destroy()
        self.order_list7.destroy()
        self.order_list8.destroy()
        self.order_list9.destroy()
        self.order_list10.destroy()
        self.order_list11.destroy()
        self.order_list12.destroy()
        self.back_button.destroy()








root = Tk()
project = Application(root)
root.mainloop()
