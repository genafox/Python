import sys
import time
import re
from Rectangle import *

# Блок завдань 1. Ітератори і генератори
#   10. Отримати список квадратів усіх чисел списку, які більше нуля. 

def task1(numbers):
    for n in numbers:
        if n > 0:
            yield n*n;

# Блок завдань 2. Декоратори
#   2. Написати декоратор, який заміряє час роботи функції. 

def executionMeasurer(fn):
    def wrapped():
        start = time.time();
        res = fn();
        end = time.time();
        print(end - start);
        return res;
    return wrapped;

@executionMeasurer
def someFunc():
    for i in range(0, 1000, 1):
        pass;
    return "Some useless func";

# Блок завдань 3. Лямбда-функції і функції вищих порядків
#   12. Додати кожному елементу списку число, введене користувачем (за допомогою map)

def append(numbers, number):
    return list(map(lambda n: n + number, numbers));

# Блок завдань 4. ООП
#   8. Реалізувати клас з методами для обчислення площі і периметра прямокутника 


# Блок завдань 5. Регулярні вирази
#   10. Перевірити правильність введення e-mail

def checkMatch(regExp, toCheck):
    prog = re.compile(regExp);
    result = prog.match(toCheck);
    return result;

def main():

    # Task 1
    print(list(task1([1, 2, 0, -1, -5, 2])));

    # Task 2
    print(someFunc());

    # Task 3
    print(append([1, 2, 3, 4, 5], 1));

    # Task 4
    rect = Rectangle(10, 5);
    print("Width: {0}, Height: {1}".format(rect.width, rect.height));
    print("Square: {0}".format(rect.square()));
    print("Perimeter: {0}".format(rect.perimeter()));

    # Task 5
    print(checkMatch("[^@]+@[^@]+\.[^@]+", "wrong format") is not None);
    print(checkMatch("[^@]+@[^@]+\.[^@]+", "email@gmail.com") is not None);

    input("press enter to exit...") 

if __name__ == "__main__":
    sys.exit(int(main() or 0))