#lowest: 0.3678794311519011
# squared = 0.6922006275553465


print("Finds the number that to the power of its self results in the lowest number possible\n")


while True: #Main Loop

  while True: # Takes in starting value
    d = input("Starting Value (ex:0.5): ")
    if d.replace('.','',1).isdigit() == True:
      break
    else:
      print("number")
  a = float(d)
  

  b = d
  while True:  #takes in precision
    c = input("Precision (ex:0.0001): ")
    if c.replace('.','',1).isdigit() == True:
      c = float(c)
      if c > 0 and c < float(d):
        break
      else:
        print("0-" + str(d))
    else:
      print("float")
  c = float(c)


  while True:  # Loops through starting value at the rate of the precision value only breaking once the numbers start increasing
    b = a
    a = a - c
    if a ** a > b ** b:
      break


  #prints output
  print("\n\nNumber is around " + str(b) + "\n")
  print("It to the power of itself is: " + str((b ** b)) + "\n")
  print("The Number is in between " + str(b) + " and " + str(a) + ".\n")