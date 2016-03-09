#!/usr/bin/env python
# -*- Coding: utf-8 -*_

"""
Conversion functions
"""

import decimal as dec

# Set decimal precision
# dec.getcontext().prec = 30


def fahr_to_celsius(fahr):
    """
    Fahrenheit to Celsius converter
    :param fahr: (Decimal) - Units in Fahrenheit
    :return: (Decimal): Units in celsius
    """
    return dec.Decimal((fahr - 32) * dec.Decimal(5/9))


def fahr_to_kelvin(fahr):
    """
    Conversion from Fahrenheit to Kelvin
    :param fahr: (Decimal) - Units in Fahrenheit
    :return: (Decimal) - Units in Kelvin
    """
    return dec.Decimal((fahr + 459.67) * 5/9)


def celsius_to_fahr(celsius):
    """
    Conversion from Celsius to Fahrenheit
    :param celsius: (Decimal) - Units in Celsius
    :return: (Decimal) Units in Fahrenheit
    """
    return (dec.Decimal(celsius) * 9/5) \
           + dec.Decimal(32)


def celsius_to_kelvin(celsius):
    """
    Conversion from Celsius to Kelvin
    :param celsius: (Decimal) Units in Celsius
    :return: (Decimal) - Units in Kelvin
    """
    return dec.Decimal(celsius + 273.15)


def kelvin_to_fahr(kelvin):
    """
    Conversion from Kelvin to Fahrenheit
    :param kelvin: (Decimal) - Units in Kelvin
    :return: (Decimal) - Units in Fahrenheit
    """
    return dec.Decimal((kelvin * 9/5)) \
           - dec.Decimal(459.67)


def kelvin_to_celsius(kelvin):
    """
    Conversion from Kelvin to Celsius
    :param kelvin: (Decimal) - Units in Kelvin
    :return: (Decimal) - Units in Celsius
    """
    return dec.Decimal(kelvin - 273.15)


if __name__ == '__main__':
    print 'F to C: ', fahr_to_celsius(100)
    print 'F to K: ', fahr_to_kelvin(100)
    print 'C to F: ', celsius_to_fahr(100)
    print 'C to K: ', celsius_to_kelvin(100)
    print 'K to C: ', kelvin_to_celsius(100)
    print 'K to F: ', kelvin_to_fahr(100)