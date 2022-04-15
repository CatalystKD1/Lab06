def getYear():
  try:
    # Could not find a way that assert can check if a input is of a certain value type
    year = int(input("What year would you like to know if a leap year? For B.C. enter a negative number: "))
    is_leapYear(year)
  except:
    print("An exception occurred")
    getYear()

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

getYear()

"""
Another way to make this program is to have a assert to check if n is a int. However a try works better here do to assert not being able to check if a input is the correct variable type when it is being called. So if the user inputs a invalid 
"""