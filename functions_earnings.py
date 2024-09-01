def compute_earnings(hourly_wage, hours_worked):
    if hours_worked > 40:
        return 40*hourly_wage + (hours_worked-40)*hourly_wage*1.5
    else:
        return hours_worked*hourly_wage
def main():
    hourly_wage = float(input("Enter wage: "))
    hours_worked = float(input("Enter hours: "))
    earning = compute_earnings(hourly_wage,hours_worked)
    print(f"The earnings are {earning:.2f}")
main()