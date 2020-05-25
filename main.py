from randomPasswordGenerator import RandomPasswordGenerator

generator = RandomPasswordGenerator()
generator.generateRandomPassword(10000)
generator.writePasswordToFile()