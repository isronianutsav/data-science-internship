square = lambda x : x*x
print(square(5))

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