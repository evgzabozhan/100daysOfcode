age = input("What's your current are?\n")
age_as_int = int(age)
years_remaining = 100 - age_as_int
days_remaining = years_remaining * 365
month_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
hours_remaining = days_remaining * 24

print(f"You have {years_remaining} years "
      f", {month_remaining} month "
      f", {weeks_remaining} weeks "
      f", {days_remaining} days "
      f"and {hours_remaining} hours ")