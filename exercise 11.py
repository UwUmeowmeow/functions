#calculate overdue fines for books at a library
def calc_fines(day_overdue):
    base_charge = .5
    daily_charge = .8
    max_charge = 30
    gross_charge = base_charge + (day_overdue * daily_charge)
    if gross_charge > max_charge:
        fine = max_charge
    else:
        fine = gross_charge
    return fine


# Main routine

day_overdue_ = int(input("Enter days overdue! "))
print(f"for{day_overdue_} the fine is ${calc_fines(day_overdue_):.2f}")
