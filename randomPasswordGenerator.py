class RandomPasswordGenerator():   
    def __init__(self):
        self.__password = ''
    def __generateRandomPassword(self, password_length=25):
        from secrets import choice
        from string import ascii_letters, digits, punctuation
        from random import shuffle
        password_characters = ascii_letters + 2*digits + punctuation
        password_characters_list = list(password_characters)    
        shuffle(password_characters_list)
        return ''.join(choice(password_characters_list) for i in range(password_length))
    def generateRandomPassword(self, rounds=10000):
        for i in range(rounds):
            print(f'Round {i}\t{self.__password}')
            self.__password = self.__generateRandomPassword()
    def writePasswordToFile(self, file_name='password.txt'):
        with open(file_name, 'w') as f:
            f.write(f'{self.__password}')