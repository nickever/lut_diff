#!/usr/bin/env python3

"""
CLI to find the difference between one LUT and another
"""

import sys
import operator


def _get_values(file):
    with open(file) as f:
        header = [x for x in next(f).split()]
        array = []
        for line in f:
            for value in line.split():
                array.append(float(value))
    f.close()
    return header, array


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


lut_1 = "./HELIUM-TO-DXL-FILM.cube"
lut_2 = "./LI_COLOR_FILM_709_VER_0_5_35.cube"
base_lut = "./Blank.cube"

try:
    header1, lut_list1 = _get_values(lut_1)
    header2, lut_list2 = _get_values(lut_2)
    header_base, lut_list_base = _get_values(base_lut)
    sub_lut_list = _subtract(lut_list1, lut_list2)
    diff_lut_list = _add(sub_lut_list, lut_list_base)
    _output(header1, diff_lut_list)
except KeyboardInterrupt:
    sys.exit("Exiting...")
