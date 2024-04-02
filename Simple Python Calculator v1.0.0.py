'''Simple Python Calculator v1.0.0.
Includes Python Packaging SDK and libTools for debugging.'''
import easygui
import os

def main():


    #Basic Code
    print("\n\nSimple Python Calculator v1.0.0.\nIncludes Python Packaging SDK and libTools for debugging.")
    
    a=int(input("Enter 1st Number: "))
    b=int(input("Enter 2nd Number: "))
    c=input("Choose An Operator(+, -, *, /): ")

    if c=="+":
        print("\nThe Sum Is: ", a+b)
    elif c=="-":
        print("\nThe Differnece Is: ", a-b)
    elif c=="*":
        print("\nThe Product Is: ", a*b)
    elif c=="/":
        print("\nThe Quotient Is: ", a/b)
    else:
        print("\nInvalid Operator")

    
    #Code For Making The Program Repeat
    Repeat = "True"
    if Repeat == "True":
        main()
    else:
        print("Bye")
        
main()
