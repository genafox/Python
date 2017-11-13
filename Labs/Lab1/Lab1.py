import sys
from array import *

def robotDirections(direction):
    switcher = {
        11: 'north',
        12: 'west',
        13: 'south',
        14: 'east'
    };
    return switcher.get(direction);

def getNewDirection(currentDirection, rotation):
    newDirection = currentDirection + rotation;
    if(newDirection > 14):
        newDirection = 11;
    if(newDirection < 11):
        newDirection = 14;
    return newDirection;

def main():

    # №1 Вивести на екран букву " Z" з символів "#".
    print("########");
    print("      #");
    print("     #");
    print("    #");
    print("   #");
    print("  #");
    print(" #");
    print("#");
    print("########");

    # №2 Робот може переміщатися в чотирьох напрямах 
    # ("11" - північ, " 12" - захід, " 13" - південь, " 14" - схід) 
    # і приймати три цифрові команди: 0 - продовжувати рух, 1 - поворот наліво, - 1 - поворот направо. 
    # Дан число (11, 12, 13 або 14) - початковий напрям робота і ціле число N (0, 1 або - 1) - послана йому команда. 
    # Вивести напрям робота після виконання отриманої команди (тобто північ, захід, південь або схід).
    startDirectionCode = 11;
    rotation = 1;
    endDirection = robotDirections(getNewDirection(startDirectionCode, rotation));
    print(endDirection);

    # №3 Вивести на екран числа від 1000 до 9999 такі, що усі цифри різні. 
    for number in range(1000, 9999):
        digits = array('b', []);
        temp = number;
        while temp > 0:
            digit = temp % 10;
            if digit in digits:
                temp = -1;
                break;
            else:
                digits.append(digit);
                temp = temp // 10;
        if(temp != -1):
            print(number);


    input("press enter to exit...") 


if __name__ == "__main__":
    sys.exit(int(main() or 0))