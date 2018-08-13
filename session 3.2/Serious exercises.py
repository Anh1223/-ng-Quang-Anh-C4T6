m=(float(input("How tall are you? ")))/100
kg=(float(input("How heavy are you? ")))
BMI=kg//(m*m)
print("Your BMI is:",BMI)
if BMI<16:
    print("Severely underweight")
elif BMI<18.5:
    print("Underweight")
elif BMI<25:
    print("Normal")
elif BMI<30:
    print("Overweigh")
else:
    print("Obese")