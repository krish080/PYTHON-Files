import os

#init variable for while loop
do=True

#main loop
while do:
    #clearing command prompt
    os.system('cls')

    #getting the initail inputs
    noOfSubjects=int(input("Enter the no of subject: "))
    totalMark=int(input("Enter the max mark per subject:"))

    #init variables for calculations
    mark=[]
    subject=[]
    grade=[]
    avg=0
    percent=0
    total=0

    #getting the name and mark of each subject
    for i in range(noOfSubjects):
        b=input("Enter name of subject "+str(i+1)+": ")
        a=int(input("Enter mark in subject "+str(i+1)+": "))
        mark.append(a)
        subject.append(b)
        total+=a

    #calculating the grade
    for n in mark:
        i=int((n/totalMark)*100)
        if i>=90 and i <= 100 :
            grade.append("A+")
        elif i>=80:
            grade.append("A")
        elif i>=70:
            grade.append("B+")
        elif i>=60:
            grade.append("B")
        elif i>=50:
            grade.append("C+")
        elif i>=40:
            grade.append("C")
        else:
            grade.append("F")

            
    #calculating avg and percent
    avg=total/noOfSubjects
    percent=(avg/float(totalMark))*100
    os.system('cls')

    #printing the marks grade and avg
    print("S.no   subject       mark     grade")
    for n,i in enumerate(mark):
        print(f"{str(i): <6}",f"{str(subject[n]): <13}",f"{str(mark[n]): <8}",f"{str(grade[n]): <10}")
    print(" ")    
    print("Average mark is:",avg)
    print("Percentage  is:",percent)
    print("Total is",total)
    print(" ")

    #repeat the program
    d=input("do you want to continue (y/n):")

    #cloasing the program
    if d=="n":
        do=False
