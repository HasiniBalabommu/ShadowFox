h=float(input("enter height in meters"))
w=int(input("enter weight in kgs"))
BMI=w/h**2
if(BMI>=30):
    print("obesity")
elif(BMI>=25 and BMI<=29):
    print("Overweight")
elif(BMI>=18.5 and BMI<=25):
    print("Normal")
else:
    print("Underweight")
