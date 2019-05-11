#Калькулятор  v1.0 
from colorama import init 
from colorama import Fore, Back, Style


# use Colorama to make Termcolor work on Windows too
init()

print(Back.RED)

what = input( "Что делаем? (+, -, *, / ): " )

print(Back.RED)

a = float(input("Введи первое число: ") )
b = float(input("Введи второе число: ") )

print(Back.RED)

if what == "+":
    c = a + b
    print("Результат:" + str(c))

elif what == "-":
   c = a - b 
   print("Результат: " + str(c))
       elif what == "*":
       	c = a * b
       	print("Результат: " + str(c))

else:
    print("ошибка!")   
