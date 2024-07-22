class str_in_and_out:
    def __init__(self):
        self.str = ""

    def inString(self):
        self.str = input()

    def outString(self):
        print(self.str.upper())

str = str_in_and_out()
str.inString()
str.outString()