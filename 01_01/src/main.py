"""
四則演算を行うモジュールをインポートして、計算を行う
"""

import calc
import figure.circle
import figure.rectangle

print(calc.add(1, 2))
print(calc.subtract(5, 3))
print(calc.multiply(2, 3))
print(calc.divide(6, 2))
print(figure.circle.calc_circle_area(3))
print(figure.rectangle.calc_rectangle_area(4, 5))