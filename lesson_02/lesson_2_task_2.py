def is_year_leap(year):
    return year % 4 == 0


result_2024 = is_year_leap(2024)
result_2023 = is_year_leap(2023)

print(f"год 2024: {result_2024}")
print(f"год 2023: {result_2023}")
