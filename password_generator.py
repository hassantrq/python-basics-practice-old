import random

meta = {
    0: list('abcdefghijklmnopqrstuvwxyz'),
    1: list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
    2: list('1234567890'),
    3: list('~!@#$%^&*()_+=-[]|:;\\/.,<>?')
}

length=input('give pswd length: ')
pswd=""

for i in range(int(length)):
    dictindex = random.randint(0,3)
    pswd += str(random.choice(meta[dictindex]))
    
print(pswd)