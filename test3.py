#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import math
if __name__ == "__main__":
    def circle(radius):
        return math.pi * radius ** 2

    def cylinder():
        radius = float(input("Введите радиус цилиндра: "))
        height = float(input("Введите высоту цилиндра: "))
        
        choice = input("Введите 'боковая' для площади боковой поверхности или 'полная' для полной площади: ")
        
        if choice == 'боковая':
            lateral_surface_area = 2 * math.pi * radius * height
            print(f"Площадь боковой поверхности цилиндра: {lateral_surface_area}")
        elif choice == 'полная':
            lateral_surface_area = 2 * math.pi * radius * height
            total_surface_area = lateral_surface_area + 2 * circle(radius)
            print(f"Полная площадь цилиндра: {total_surface_area}")
        else:
            print("Неверный ввод. Пожалуйста, введите 'боковая' или 'полная'.")

    # Вызываем функцию cylinder()
    cylinder()
