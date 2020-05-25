from randomPasswordGenerator import RandomPasswordGenerator

generator = RandomPasswordGenerator() # argument: password length. default is 25 
generator.generateRandomPassword(10000) # argument: number of rounds before generating the final password. default is 10k
generator.writePasswordToFile() # argument: output file name