def is_numeric(j):
  print(str(j) + " Variable has a number value!")
  
try:
  #technically TRY returns a TRUE because otherwise it would not work. If this loop hole is not the proper way please let me know
  j = float(input("Write something down: "))
  if j < int(j + 1) and j > int(j):
    is_numeric(j)
  else:
    is_numeric(int(j))
except ValueError:
  print("An exception occurred")
  raise TypeError ("Must provide a int or float")