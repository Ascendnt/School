from abc import ABC, abstractmethod


class Account(ABC):
    @abstractmethod
    def details(self):
        pass


class Email(Account):
    def __init__(self, email, name):
        self.email = email
        self.name = name

    def details(self):
        print("Your email is", self.email)
        print("Your name is", self.name)


check = Email(input("What is your email? "), input("what is your name? "))
check.details()
