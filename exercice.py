#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    if a <= 0 :
        print("that square root is impossible")
        return -1
    i = 0
    while 1 :
        if i * i == a:
            return i
        elif (i + 1) * (i + 1) == a:
            return (i + 1)
        elif i * i < a and a < (i + 1) * (i + 1):
            return i
        i+=1
    return -1


def square(a: float) -> float:    
    a = a**2
    return a

def average(a: float, b: float, c: float) -> float:
    res = (a + b + c)/3
    return res


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    angle_degs = angle_degs * math.pi / 180
    angle_mins = angle_mins * math.pi / 10800
    angle_secs = angle_secs * math.pi / 648000
    res = angle_degs + angle_mins + angle_secs
    return res


def to_degrees(angle_rads: float) -> tuple:
    degrees = angle_rads * 180 / math.pi
    minutes = (degrees - int(degrees)) * 60)
    seconds = (minutes - int(minutes)) * 60
    return degrees, minutes, seconds


def to_celsius(temperature: float) -> float:
    return 0.0


def to_farenheit(temperature: float) -> float:
    return 0.0


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 180 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
