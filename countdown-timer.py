
import time
hours = int(input("Enter your hours :"))
minutes = int(input("Enter your minutes :"))
seconds = int(input("Enter your seconds"))
total = hours * 3600 + minutes * 60 +seconds
for i in range(total,-1,-1):
    hours = i//3600
    minutes = (i % 3600)//60
    seconds = (i % 60)
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    time.sleep(1)
print("Time is up")    