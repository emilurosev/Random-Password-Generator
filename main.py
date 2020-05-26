from generator import RandomPasswordGenerator

if __name__ == '__main__':
    generator = RandomPasswordGenerator()
    pwd = generator.generateRandomPassword()
    print(pwd) 