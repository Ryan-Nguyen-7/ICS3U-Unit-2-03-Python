#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on November 2020
# This program calculates perimeter using
#     user input and TAU constant


def main():
    # this function calculates area
    import constants
    radius = int(input("Enter radius of circle (m):"))
    print("")
    print("Perimeter is {}cm".format(radius*constants.TAU))


if __name__ == "__main__":
    main()
