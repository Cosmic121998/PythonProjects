height = float(input("enter your height m: "))
weight = float(input("enter your weight in kg: "))
bmi: float = round(weight / height ** 2)
if bmi < 18.5:
    print(f"your bmi is {bmi}, are underweight")
elif bmi < 25:
    print(f"your bmi is {bmi}, you are normal")
elif bmi < 30:
    print(f"your bmi is {bmi}, you are obese")
else:
    print(f"your bmi is {bmi}, you are clinically obese")
