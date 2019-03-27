# -*- coding: utf-8 -*-
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from pyjaya.samp import JayaSAMP
from pyjaya.utils import FloatRange, IntRange, BinaryRange
import numpy as np


def function1(solution):
    return sum(np.asarray(solution)**2)


def main():
    print("RUN: Self-adaptive Multi-population Elitist (SAMP) Jaya Algorithm")
    listVars = [FloatRange(-100.0, 100.0) for i in range(2)]
    ja = JayaSAMP(20, listVars, function1)
    print(ja.run(100))
    print("--------------------------------------------------------------")


if __name__ == '__main__':
    main()
