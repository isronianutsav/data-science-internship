"""marks= int(input("enter your marks:- "))
if(marks>=91):
    print("A GRADE")
elif(marks>=80):
    print("B GRADE")
elif(marks>=60):
    print("C GRADE")
elif(marks>=40):
    print("D GRADE")
else:
    print("FAIL") """

"""
#through functions
def gradingSystems(marks):
    
    if(marks>=91):
        print("A GRADE")
    elif(marks>=80):
        print("B GRADE")
    elif(marks>=60):
        print("C GRADE")
    elif(marks>=40):
        print("D GRADE")
    else:
        print("FAIL")

marks= int(input("enter your marks : "))
gradingSystems(marks)

"""

#through lambda -  elif is not allowed
#Gradingmarks = lambda x : print("A GRADE") if (x>=91) else (print("B GRADE") if (x>=80) else (print("C GRADE") if (x>=60) else (print("D GRADE") if (x>=40) else print("FAIL"))) )
Gradingmarks = lambda x: (
    print("A GRADE") if x >= 91 else
    print("B GRADE") if x >= 80 else
    print("C GRADE") if x >= 60 else
    print("D GRADE") if x >= 40 else
    print("FAIL")
)
marks= int(input("enter your marks : "))
Gradingmarks(marks)
