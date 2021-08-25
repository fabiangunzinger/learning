#!/usr/bin/env python

def check(name):
    return input('{}, is this really you? '.format(name))

def secret(name):
    return input('Okay {}, do you want me to tell you a secret? '.format(name))
    
def main():
    name = input("Hello, I'm Python. What is your name? ")
    if name == 'Molly':
        answer = check('Molly')
        if answer in ['Yes', 'yes']:
            answer = secret('Molly')    
            if answer in ['Yes', 'yes']:
                print('Fabian loves you so, so much!')
    else:
        greet(name)
    
if __name__ == '__main__':
    main()
