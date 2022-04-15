def is_leapYear(year):
  if year % 4 == 0:
    if year % 400 == 0:
      print(str(year) + " is a leap year.")
    elif year % 100 == 0:
      print(str(year) + " is not a leap year.")
    else:
      print(str(year) + " is a leap year.")
  else:
    print(str(year) + " is not a leap year.")
year = "1000"
if not isinstance(year, int):
  raise ValueError("Must be a integer")
is_leapYear(year)