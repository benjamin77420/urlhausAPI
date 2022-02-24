import re


def testing():
    numbers=[1343124,141341,23543]
    lent = 0
    sum = 0

    for x in range(numbers.__len__()):
        lent = len(x)
        for x in range(len(lent)):
            sum = numbers%10
            numbers/=10


if __name__ == '__main__':
    testing()