import sys
import random, string
import numpy as np
from array import *
from random import randint

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

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length));

def checkNumbersPresence(arr, n):
    result = True;
    for i in range(1, n):
        if(i not in arr):
            result = False;
            break;
    return result;

def binarySearchInArrayTree(arrTree, startIndex, endIndex, element):
    arrLength = endIndex - startIndex + 1;
    if(arrLength == 0):
        return -1;
    middleIdx = startIndex + arrLength // 2;
    if(arrLength % 2 == 0):
        middleIdx -= 1;
    if(arrTree[middleIdx] == element):
        return middleIdx;
    if(arrTree[middleIdx] < element):
        return binarySearchInArrayTree(arrTree, middleIdx + 1, endIndex, element);
    if(arrTree[middleIdx] > element):
        return binarySearchInArrayTree(arrTree, 0, middleIdx - 1, element);


def getDigitWords(text):
    digitWords = {};
    digitWord = '';
    sum = 0;
    for c in text:
        if c.isdigit():
            digitWord += c;
            sum += int(c);
        else:
            if(len(digitWord) > 0):
                digitWords[digitWord] = sum;
            digitWord = '';
            sum = 0;
    if(len(digitWord) > 0):
        digitWords[digitWord] = sum;
    return digitWords;


#=====================================================================

def Task1():
    print("########");
    print("      #");
    print("     #");
    print("    #");
    print("   #");
    print("  #");
    print(" #");
    print("#");
    print("########");


def Task2(startDirectionCode, rotation):
    endDirection = robotDirections(getNewDirection(startDirectionCode, rotation));
    print(endDirection);


def Task3():
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


def Task4():
    randWordLength = randint(1, 8);
    randWord = randomword(randWordLength) + '!!!!!';
    print(randWord);


def Task5():
    arrayLength = randint(5, 20);

    maxZeroCount = arrayLength // 2;
    if(arrayLength % 2 == 0):
        maxZeroCount -= 1;

    zeroOneArray = [0] * arrayLength;

    for i in range(arrayLength):
        item = randint(0, 1);

        zeroOneArray[i] = item if maxZeroCount > 0 else 1;
        if(item == 0):
            maxZeroCount -= 1;

    print(zeroOneArray);


def Task6(arr, n):
    res = checkNumbersPresence(arr, n);
    print(res);


def Task7(arrTree, element):
    elementIndex = binarySearchInArrayTree(arrTree, 0, len(arrTree) - 1, element);
    print(elementIndex);

def Task8(matrixDeclaration):
    a = np.matrix(matrixDeclaration);
    rowsMinElementsIndices = a.argmin(1);

    for i in range(a.shape[0]):
        print('Row {}: {}'.format(i, a.item((i, rowsMinElementsIndices.item(i, 0)))));


def Task9(text):
    digitWords = getDigitWords(text);
    for item in digitWords.items():
        print(item);

#=====================================================================

def main():

    # №1 Вивести на екран букву " Z" з символів "#".
    #Task1();

    # №2 Робот може переміщатися в чотирьох напрямах 
    # ("11" - північ, " 12" - захід, " 13" - південь, " 14" - схід) 
    # і приймати три цифрові команди: 0 - продовжувати рух, 1 - поворот наліво, - 1 - поворот направо. 
    # Дан число (11, 12, 13 або 14) - початковий напрям робота і ціле число N (0, 1 або - 1) - послана йому команда. 
    # Вивести напрям робота після виконання отриманої команди (тобто північ, захід, південь або схід).
    #Task2(11, 1);

    # №3 Вивести на екран числа від 1000 до 9999 такі, що усі цифри різні. 
    #Task3();

    # №4 Згенеруйте рядок символів довжини від 6 до 13, в якій рівно 5 символу !
    #Task4();

    # №5 Заповніть масив випадковим чином нулями і одиницями так, щоб кількість одиниць була більше кількості нулів. 
    #Task5();

    # №6 Перевірте, чи містить цей масив з n чисел, усі числа від 1 до n
    #Task6([1, 2, 3, 4, 5], 5);

    # №7 Здійснити пошук цього числа у впорядкованому за збільшенням масиві методом бінарного пошуку. 
    #Task7([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10);

    # №8 У матриці знайти найменший елемент в кожному рядку.
    #Task8('1 2; 3 4; 1 0');

    # №9 Даний текст. Знайти слова, що складаються з цифр, і суму чисел, які утворюють ці слова. 
    #Task9('some shit 12345. Hate this lab 1243. It sucks! 1488');

    input("press enter to exit...") 


if __name__ == "__main__":
    sys.exit(int(main() or 0))