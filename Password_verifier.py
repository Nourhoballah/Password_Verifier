import string
class PasswordVerifier:
    def __init__(self, password):
        self.password = password

    def password_verifier(self):
        list_of_errors=[] # a list to know  all the mistakes a person wrote
        characters= "!@#$%^&*?"

        #criteria verification
        if len(self.password) < 8:
                list_of_errors.append(" Password must be at least 8 characters long")
        if not any(char.isdigit() for char in self.password): # we verify each character in the password if there is a digit
                # any function in python verify if at least one character is True
                list_of_errors.append("\n There's no number is the password.")
        if not any(char in string.ascii_lowercase  for char in self.password):
                list_of_errors.append("\n There's not lower case letter.")
        if not any(char in string.ascii_uppercase  for char in self.password):
                list_of_errors.append("\n There's not upper case letter.")
        if not any(char in characters for char in self.password):
                list_of_errors.append("\n There's not special character.")
        if " " in self.password:
                list_of_errors.append("\n Theres a space in your password.")
        if list_of_errors:
            return f"These are the errors in the password:\n" + "".join(list_of_errors)
        else:
            return "Password is acceptable!"



#try the code
user_password = input("Enter your password to verify: ")
verifier = PasswordVerifier(user_password)
print(verifier.password_verifier())









