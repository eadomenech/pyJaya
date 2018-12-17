# -*- coding: utf-8 -*-
from jaya.clasic import JayaClasic
from jaya.binary import JayaBinary
import numpy as np


def function1(solution):
    return sum(np.asarray(solution)**2)


def function2(solution):
    return sum(solution)


def main():
    print "RUN: JayaClasic"
    jc = JayaClasic(5, 5, function1)
    print jc.run(2000)
    print "--------------------------------------------------------------"

    print "RUN: JayaBinary"
    jc = JayaBinary(5, 21, function2)
    print jc.run(10)
    print "--------------------------------------------------------------"


if __name__ == '__main__':
    main()
