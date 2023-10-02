class favorite:
    def __init__(self, hobby):
        self.hobby = hobby

    def love(self):
        return self.hobby


what_favorite = favorite(input("Type your favorite: "))
print("My favorite is", what_favorite.love())


class color:
    def __init__(self, crayola):
        self.c = crayola

    def crayon(self):
        return self.c


share = color(input("Tell us a color: "))
print("The color is", share.crayon())


class email:
    def __init__(self, gmail):
        self.g = gmail

    def account(self):
        return self.g


enter = email(input("Enter your email: "))
print("Your email is: ", enter.account())


