# -*- coding: utf-8 -*-
from pyjaya.clasic import JayaClasic
from pyjaya.binary import JayaBinary
import numpy as np


def function1(solution):
    return sum(np.asarray(solution)**2)


def function2(solution):
    return sum(solution)


def main():
    print("RUN: JayaClasic")
    jc = JayaClasic(5, 5, function1)
    print(jc.run(100))
    print("--------------------------------------------------------------")

    print("RUN: JayaBinary")
    jc = JayaBinary(5, 21, function2)
    print(jc.run(100))
    print("--------------------------------------------------------------")


if __name__ == '__main__':
    main()
