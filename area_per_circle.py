#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 03/07/2025
# It calculates the are and perimeter of a circle.

import math


def main():

    radius = float(input("Enter the radius of a circle (cm):"))
    # Gets the input

    circumference = math.pi * 2 * radius
    # Calculates the circumference
    area = math.pi * radius ** 2
    # Calculates the area
    print("The area of a circle is {: .2f} cm".format(area))
    # Displays the area
    print("The circumference of a circle is {: .2f} cm".format(circumference))


# Displays the circumference

if __name__ == "__main__":
    main()
