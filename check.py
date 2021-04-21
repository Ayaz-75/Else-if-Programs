'''Q5. Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5 , print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird

Sample input
input 1: 3
output 1: weird

input 2: 24
output 2: not weird

'''
a = int(input('Enter Number: '))
if a%2!=0: # do not include the fucking range 
    print('weird')

elif a%2==0 and a>=2 and a<=5: # saheh
    print('not weird')

elif a%2==0 and a>=6 and a<=20: # saheh
    print(' cond 3: weird')

elif a%2==0 and a>20: # saheh
    print('cond 4: not Weird')
