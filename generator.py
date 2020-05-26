class RandomPasswordGenerator():   
    def __init__(self):
        from string import ascii_letters, digits, punctuation
        self.__password_characters = ascii_letters + digits + punctuation

    def __generateRandomPassword(self, password_length):
        from secrets import choice
        from random import shuffle
        password_characters_list = list(self.__password_characters)
        shuffle(password_characters_list)
        return ''.join(choice(password_characters_list) for i in range(password_length))

    def generateRandomPassword(self, password_length=25, output_to_file=True, file_name='password.txt'):
        password = self.__generateRandomPassword(password_length)
        if output_to_file:
            with open(file_name, 'w') as f:
                f.write(password)
        return password