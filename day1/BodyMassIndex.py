height = float(input("Enter your height in m : "))
weight = float(input("Enter your weight in kg : "))
BMI = weight/height ** 2
print(int(BMI))
print(f"your BMI = {round(BMI, 2)}")