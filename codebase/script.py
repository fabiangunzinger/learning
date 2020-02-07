#!/usr/bin/env python

def greet(name):
    print("Hey {}! I'm Python.".format(name))
    
def check(name):
    input('{}, is this really you? '.format(name))

def secret(name):
    input('Okay {}, do you want me to tell you a secret? '.format(name))
    
def main():
    name = input("What is your name? ")
    if name == 'Molly':
        answer = check('Molly')
        if answer == 'Yes':
            answer = secret('Molly')    
            if answer == 'Yes':
                print('Fabian loves you so, so much!')
    else:
        greet(name)
    
if __name__ == '__main__':
    main()