class Strings:
    def __init__(self, sentence):
        self.sent = sentence

    def convert(self):
        print(''.join(x for x in self.sent.title() if not x.isspace()))


print("This program will convert your sentence into camel case")
result = Strings(input("Enter a word: "))
result.convert()
