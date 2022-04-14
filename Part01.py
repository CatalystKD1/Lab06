def numCheck(j):
  print(str(j) + " Variable has a number value!")
  
try:
  j = float(input("Write something down: "))
  if j < int(j + 1) and j > int(j):
    numCheck(j)
  else:
    numCheck(int(j))
except ValueError:
  print("An exception occurred")
  raise TypeError ("Must provide a int or float")