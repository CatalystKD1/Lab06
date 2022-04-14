def hypotenus(a, b):
  a = a**2
  b = b**2
  c = a + b
  c = round(c, 2)
  print("The hypotenus is " + str(c) + ".")
a = float(input("Input first side: "))
try:
  if a < int(a + 1) and a > int(a):
    b = float(input("Input second side: "))
    try:
      if b < int(b + 1) and b > int(b) and a > 0:
        hypotenus(a, b)
      else:
        hypotenus(int(a), int(b))
    except ValueError:
      print("An exception occurred")
      if a > 0:
        raise TypeError ("numeric must be creater then 0")
      else:
        raise TypeError ("Must provide a int or float")
  else:
    b = float(input("Input second side: "))
    try:
      if b < int(b + 1) and b > int(b) and b > 0:
        hypotenus(a, b)
      else:
        hypotenus(int(a), int(b))
    except ValueError:
      if a > 0:
        raise TypeError ("numeric must be creater then 0")
      else:
        raise TypeError ("Must provide a int or float")
except ValueError:
  print("An exception occurred")
  raise TypeError ("Must provide a int or float")