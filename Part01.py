def is_numeric(j):
  print(str(j) + " Variable has a number value!")
  
try:
  #I added the try before doing thr isinstance. I wanted to test a method of finding a int I found effective. This is a algorithm yo print a int without the .0 at the end. It also sorts the ints froms floats
  j = float(input("Write something down: "))
  print("Is " + str(j) + " a float? " + str(isinstance(j, float)))
  print("Is " + str(j) + " a int? " + str(isinstance(j, int)))
  if j < int(j + 1) and j > int(j):
    is_numeric(j)
  else:
    is_numeric(int(j))
except ValueError:
  print("An exception occurred")
  raise TypeError ("Must provide a int or float")