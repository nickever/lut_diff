#!/usr/bin/env python3

"""
Quantify the difference between two Look Up Tables (LUTs).
Generates a LUT that is the difference between the two input.
"""

__author__ = "Nick Everett"
__version__ = "0.5.0"
__license__ = "GNU GPLv3"

import sys
import operator


def _get_values(file):
    with open(file) as f:
        header = [x for x in next(f).split()]
        value_list = []
        for line in f:
            for value in line.split():
                value_list.append(float(value))
    f.close()
    return header, value_list


def _subtract(list1, list2):
    x = list(map(operator.sub, list1, list2))
    return x


def _add(list1, list2):
    x = list(map(operator.add, list1, list2))
    return x


def _output(header, body):
    with open("output_film_lut.cube", "w+") as f:
        for h in header:
            f.write("{} ".format(h))
        f.write("\n")
        count = 3
        for value in body:
            count -= 1
            f.write("%.10f " % round(value, 10))
            if count == 0:
                f.write("\n")
                count = 3
            else:
                pass
    f.close()


lut_1 = # File path here
lut_2 = # File path here
base_lut = "./blank.cube"

try:
    header1, lut_list1 = _get_values(lut_1)
    header2, lut_list2 = _get_values(lut_2)
    header_base, lut_list_base = _get_values(base_lut)
    sub_lut_list = _subtract(lut_list1, lut_list2)
    diff_lut_list = _add(sub_lut_list, lut_list_base)
    _output(header1, diff_lut_list)
except KeyboardInterrupt:
    sys.exit("Exiting...")
