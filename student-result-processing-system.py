passed = 0
fail = 0
for i in range(1,6):
    name = input("Enter your name :")
    mark = int(input("Enter your mark :"))
    if mark<0 or mark>100:
        print("Invalied Number")
        continue
    if mark>=80:
        grade = "A+"
        passed = passed +1
    elif mark>=70:
        grade = "A"
        passed = passed + 1 
    elif mark>=60:
        grade = "A-"
        passed= passed + 1
    elif mark>=50:
        grade = "B+"
        passed = passed + 1
    elif mark>=40:
        grade = "B"
        passed = passed + 1 
    elif mark>=33:
        grade = "C"
        passed = passed + 1
    else:
        grade = "F"
        fail = fail + 1 
    print (name,mark,grade)
print("Total passed:", passed)
print("Totall fail:", fail)           
