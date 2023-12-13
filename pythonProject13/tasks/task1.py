#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def product_between_min_max(*args):
    if not args:
        return None

    args = [float(arg) for arg in args]

    min_index = args.index(min(args))
    max_index = args.index(max(args))

    start_index, end_index = min(min_index, max_index), max(min_index, max_index)

    subset = args[start_index + 1:end_index]

    result = 1
    for num in subset:
        result *= num

    return result


if __name__ == "__main__":
    input_data = input("Введите числа через пробел: ").split()

    result = product_between_min_max(*input_data)

    print("Результат:", result)
