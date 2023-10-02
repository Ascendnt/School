class Account:
    def __init__(self, name):
        self.name = name

    def details(self):
        print("Your name is", self.name)


class Email(Account):
    def __init__(self, name, email):
        Account.__init__(self, name)
        self.email = email

    def display(self):
        print("Your email is", self.email)
        Account.details(self)


result = Email(input("What is your email? "), input("what is your name? "))
result.display()
