def main_routine():
    adult_ticket = 0
    student_ticket = 0
    child_ticket = 0
    gift_ticket = 0
    total_sales = 0
    ticket_sold = 0


ticket_wanted = input("Do you want to sell a ticket? (Y/N): ").upper()
while ticket_wanted != "n":
    ticket = sell_ticket()


# Get the number of tickets wanted in the category chosen
num_ticket = int(input("How many of theses ticket do you want: "))
confirm = input(f"")
