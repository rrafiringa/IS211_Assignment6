#!/usr/bin/env python
# -*- Coding: utf-8 -*-

"""
Conversion functions
"""


def fahr_to_celsius(fahr):
    """
    Fahrenheit to Celsius converter
    :param fahr: (Decimal) - Units in Fahrenheit
    :return: (Decimal): Units in celsius
    """
    a = float(fahr) - 32.0
    b = 5.0 / 9
    return a * b


def fahr_to_kelvin(fahr):
    """
    Conversion from Fahrenheit to Kelvin
    :param fahr: (Decimal) - Units in Fahrenheit
    :return: (Decimal) - Units in Kelvin
    """
    a = float(fahr)
    b = 459.67
    c = 5.0 / 9
    return (a + b) * c


def celsius_to_fahr(celsius):
    """
    Conversion from Celsius to Fahrenheit
    :param celsius: (Decimal) - Units in Celsius
    :return: (Decimal) Units in Fahrenheit
    """
    a = float(celsius)
    b = 9.0 / 5
    c = 32.0
    return (a * b) + c


def celsius_to_kelvin(celsius):
    """
    Conversion from Celsius to Kelvin
    :param celsius: (Decimal) Units in Celsius
    :return: (Decimal) - Units in Kelvin
    """
    a = float(celsius)
    b = 273.15
    return a + b


def kelvin_to_fahr(kelvin):
    """
    Conversion from Kelvin to Fahrenheit
    :param kelvin: (Decimal) - Units in Kelvin
    :return: (Decimal) - Units in Fahrenheit
    """
    a = float(kelvin)
    b = 9.0 / 5
    c = 459.67
    return a * b - c


def kelvin_to_celsius(kelvin):
    """
    Conversion from Kelvin to Celsius
    :param kelvin: (Decimal) - Units in Kelvin
    :return: (Decimal) - Units in Celsius
    """
    a = float(kelvin)
    b = 273.15
    return a - b


if __name__ == '__main__':
    val = 0
    print 'F to C: ', fahr_to_celsius(val)
    print 'F to K: ', fahr_to_kelvin(val)
    print 'C to F: ', celsius_to_fahr(val)
    print 'C to K: ', celsius_to_kelvin(val)
    print 'K to C: ', kelvin_to_celsius(val)
    print 'K to F: ', kelvin_to_fahr(val)
