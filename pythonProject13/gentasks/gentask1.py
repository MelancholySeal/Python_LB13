#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def geometric_mean(*args):
    if args:
        values = list(map(float, args))
        product = 1.0
        for value in values:
            product *= value
        return round(pow(product, 1/len(values)), 4)
    else:
        return None


if __name__ == "__main__":
    input_data = input("Введите числа через пробел: ").split()
    result = geometric_mean(*input_data)
    print("Результат:", result)
