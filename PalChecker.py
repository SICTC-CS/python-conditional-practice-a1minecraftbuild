isNegative=False
ui=int(input("3 digit number please: "))

if "-" in str(ui):
  isNegative=True
  while len(str(ui))!=4:
    if len(str(ui))==3 and "-" not in str(ui):
      isNegative=False
      break
    ui=int(input("I said a 3 digit number: "))
else:
  while len(str(ui))!=3:
      ui=int(input("I said a 3 digit number: "))
      if len(str(ui))==4 and "-" in str(ui):
        isNegative=True
        break


if isNegative == True:
  ui=ui*-1

if str(ui) == str(ui)[::-1]:
  print("This is a palindrome")
else:
  print("This is not a palindrome")

