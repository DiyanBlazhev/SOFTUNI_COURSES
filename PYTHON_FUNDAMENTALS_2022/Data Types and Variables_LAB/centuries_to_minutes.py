centuries = int(input())
year = int(centuries * 100)
day = int(365.2422 * year)
hour = day * 24
minutes = 60 * hour
print(f"{centuries} centuries = {year} years = {day} days = {hour} hours = {minutes} minutes")