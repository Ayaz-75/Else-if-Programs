age=int(input("Enter the Age: "))

if age==5:
    print('1 class')

elif age>=6 and age<=10:
    print('5 class')

elif age>10 and age<=15:
    print('10 class')

elif age>15 and age<=22:
    print('12 class')

elif age>22 and age<=30:
    print('under Graduation')

elif age>30 and age<100:
    print('Graduation is possible , Masters is possible, PHD is possible')

else:
    print('invalid age')

