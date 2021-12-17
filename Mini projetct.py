#BMI Calculator 

weight = input("your weight:")
height = input("your height:")

weight = float(weight)
height=  float(height)

bmi = weight / ((height/100)**2)

print(f"your BMI if{bmi}.")

