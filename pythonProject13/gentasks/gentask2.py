#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_harmonic_mean(*args):
    if args:
        values = list(map(float, args))
        reciprocal_sum = sum(1/value for value in values)
        return round(len(values) / reciprocal_sum, 4)
    else:
        return None


if __name__ == "__main__":
    input_data = input("Введите числа через пробел: ").split()
    result = calculate_harmonic_mean(*input_data)
    print("Результат:", result)
