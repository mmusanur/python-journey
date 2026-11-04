cgpa = float(input("enter your cgpa"))
marks = int(input("enter your marks"))

eligibile = cgpa>=3.80 or marks>=90
print("Scholorship Eligible" , eligibile)