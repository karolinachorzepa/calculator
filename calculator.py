import sys
import logging
logging.basicConfig(level=logging.DEBUG)

result = None
firstnumber = float(input("Podaj liczbę: "))
matematical_operation =int(input("Podaj operację matematyczną: 1 dla (+), 2 dla (-), 3 dla (*), 4 dla (/) "))
if matematical_operation == 1: 
    secondnumber = float(input("Podaj 2 liczbę: "))
    logging.info(f"Dodaję {firstnumber} i {secondnumber}")
    result = firstnumber + secondnumber
elif matematical_operation == 2: 
    secondnumber = float(input("Podaj 2 liczbę: "))
    logging.info(f"Odejmuję {firstnumber} i {secondnumber}")
    result = firstnumber - secondnumber
elif matematical_operation == 3: 
    secondnumber = float(input("Podaj 2 liczbę: "))
    logging.info(f"Mnożę {firstnumber} i {secondnumber}")
    result = firstnumber * secondnumber
elif matematical_operation == 4: 
    secondnumber = float(input("Podaj 2 liczbę: "))
    logging.info(f"Dzielę {firstnumber} i {secondnumber}")
    result = firstnumber / secondnumber
else:
    logging.error("Wybrano niepoprawną operację matematyczną")
    exit(1)
print(f"Wynik działania to {result}")