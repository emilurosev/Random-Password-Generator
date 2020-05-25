class RandomPasswordGenerator():   
    def __init__(self, password_length=25):
        self.__password = ''
        self.__password_length = password_length
    def __generateRandomPassword(self):
        from secrets import choice
        from string import ascii_letters, digits, punctuation
        from random import shuffle
        password_characters = ascii_letters + digits + punctuation
        password_characters_list = list(password_characters)    
        shuffle(password_characters_list)
        return ''.join(choice(password_characters_list) for i in range(self.__password_length))
    def generateRandomPassword(self, rounds=10000):
        for i in range(rounds):
            self.__password = self.__generateRandomPassword()
            print(f'Round {i}\t{self.__password}')
    def writePasswordToFile(self, file_name='password.txt'):
        with open(file_name, 'w') as f:
            f.write(f'{self.__password}')