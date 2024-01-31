#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
if __name__ == "__main__":
    def multiply_until_zero():
        product = 1
        while True:
            number = float(input("Введите число (введите 0 для завершения): "))
            if number == 0:
                break
            product *= number
        return product

    # Вызываем функцию и выводим результат
    result = multiply_until_zero()
    print(f"Результат перемножения: {result}")
