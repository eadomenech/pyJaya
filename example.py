# -*- coding: utf-8 -*-
from pyjaya.clasic import JayaClasic
from pyjaya.binary import JayaBinary
from pyjaya.utils import FloatRange, IntRange, BinaryRange
import numpy as np


def function1(solution):
    return sum(np.asarray(solution)**2)


def function2(solution):
    return sum(solution)


def main():
    print("RUN: JayaClasic")
    listVars1 = [FloatRange(-100.0, 100.0) for i in range(2)]
    listVars2 = [IntRange(0, 50) for i in range(2)]
    jc = JayaClasic(5, listVars1+listVars2, function1)
    print(jc.run(100))
    print("--------------------------------------------------------------")

    print("RUN: JayaBinary")
    listVars = [BinaryRange() for i in range(10)]
    jc = JayaBinary(5, listVars, function2)
    jc.toMaximize()
    print(jc.run(100))
    print("--------------------------------------------------------------")


if __name__ == '__main__':
    main()
