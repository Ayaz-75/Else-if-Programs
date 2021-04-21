marks=int(input("Enter a number"))
if marks<100 and marks>=85:
    print("grade is A+")

elif marks<85 and marks>=75:
    print("Grade is A")

elif marks<75 and marks>=65:
    print("Grade is B")

elif marks<65 and marks>=50:
    print("Grade is C")

elif marks<50 and marks>=1:
    print("Fail")

else:
    print("Invalid marks")
