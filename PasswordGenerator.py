import string
import random

class PasswordGenerator:
    def __init__(self, length, complexity):
        self.length = length
        self.complexity = complexity
    
    charset_basic = list(string.ascii_letters)

    charset_complex = list(string.ascii_letters + string.digits)

    chartset_all = list(string.ascii_letters + string.digits + string.punctuation)

    def GeneratePassword(self):
        password = ''
        if(self.complexity == 1):
            for i in range(self.length):
                password += random.choice(self.charset_basic)
        if(self.complexity == 2):
            for i in range(self.length):
                password += random.choice(self.charset_complex)
        if(self.complexity == 3):
            for i in range(self.length):
                password += random.choice(self.chartset_all)
        
        return password

if __name__ == "__main__":
    while True:
        print("Welcome to the password generator.")
        length = int(input("Desired password length (Integers only): "))
        print("Password Complexity: Only Letters = 1 | Letters & Numbers = 2 | All Characters = 3")
        complexity = int(input("Complexity: "))
        
        Generator = PasswordGenerator(length, complexity)
        print(Generator.GeneratePassword())
        
        print("Redo? Y/N")
        finished = input("Answer: ")
        if (finished == 'N' or 'n'):
            break
