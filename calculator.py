import sys
import logging
logging.basicConfig(level=logging.DEBUG)

result = None
firstnumber = float(input("Podaj liczbę: "))
matematical_operation =int(input("Podaj operację matematyczną: 1 dla (+), 2 dla (-), 3 dla (*), 4 dla (/) "))
secondnumber = float(input("Podaj 2 liczbę: "))
if matematical_operation == 1: 
    logging.info(f"Dodaję {firstnumber} i {secondnumber}")
    result = firstnumber + secondnumber
elif matematical_operation == 2: 
    logging.info(f"Odejmuję {firstnumber} i {secondnumber}")
    result = firstnumber - secondnumber
elif matematical_operation == 3: 
    logging.info(f"Mnożę {firstnumber} i {secondnumber}")
    result = firstnumber * secondnumber
elif matematical_operation == 4: 
    logging.info(f"Dzielę {firstnumber} i {secondnumber}")
    result = firstnumber / secondnumber
else:
    logging.error("Wybrano niepoprawną operację matematyczną")
    exit(0)
print(f"Wynik działania to {result}")