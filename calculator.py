import logging
result = None
firstnumber = float(input("Podaj liczbę: "))
matematical_operation =int(input("Podaj operację matematyczną: 1 dla (+), 2 dla (-), 3 dla (*), 4 dla (/) "))
if matematical_operation == 1: 
    secondnumber = int(input("Podaj 2 liczbę: "))
    result = firstnumber + secondnumber
elif matematical_operation == 2:
    secondnumber = int(input("Podaj 2 liczbę: "))
    result = firstnumber - secondnumber
elif matematical_operation == 3:
    secondnumber = int(input("Podaj 2 liczbę: "))
    result = firstnumber * secondnumber
elif matematical_operation == 4:
    secondnumber = int(input("Podaj 2 liczbę: "))
    result = firstnumber / secondnumber
else:
    print("Wybrano niepoprawną operację matematyczną")
    exit(1)
print(result)