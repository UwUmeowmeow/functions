def check_bmi(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "Obese"

# Main routine
get_bmi = float(input("Enter BMI: "))
print(f"With a BMI of {get_bmi} you status is {check_bmi(get_bmi)}")
