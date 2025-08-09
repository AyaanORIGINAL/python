import calendar

def generate_months():
    months = (calendar.month_name[i] for i in range(1, 13))
    return months
print(list(generate_months()))