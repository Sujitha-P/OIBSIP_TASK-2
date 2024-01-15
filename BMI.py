def bmi_calculate(w, h):
    return w/(h**2)

def classify(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    else:
        return "Overweight"

if __name__ == "__main__":
    w = float(input("Enter your weight in kilograms: "))
    h = float(input("Enter your height in meters: "))
    bmi = bmi_calculate(w, h)
    category = classify(bmi)
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Category: {category}")
