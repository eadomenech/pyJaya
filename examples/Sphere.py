# -*- coding: utf-8 -*-
"""Sphere funtion"""

import numpy as np

from pyJaya.variants.clasic import JayaClasic
from pyJaya.variants.selfAdadtive import JayaSelfAdadtive
from pyJaya.variants.quasiOppositional import JayaQuasiOppositional
from pyJaya.variants.samp import JayaSAMP
from pyJaya.variants.sampemultiprocess import JayaSAMPE
from pyJaya.variables import VariableFloat


def sphere(solution):
    return sum(np.asarray(solution)**2)


def main():
    print("RUN: JayaClasic")
    listVars = [VariableFloat(-100.0, 100.0) for i in range(30)]
    ja = JayaClasic(100, listVars, sphere)
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print("RUN: Self-adaptive Jaya Algorithm")
    listVars = [VariableFloat(-100.0, 100.0) for i in range(30)]
    ja = JayaSelfAdadtive(listVars, sphere)
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print("RUN: Quasi-oppositional Based Jaya (QO-Jaya) Algorithm")
    listVars = [VariableFloat(-100.0, 100.0) for i in range(30)]
    ja = JayaQuasiOppositional(100, listVars, sphere)
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print("RUN: Self-adaptive Multi-population (SAMP) Jaya Algorithm")
    listVars = [VariableFloat(-100.0, 100.0) for i in range(30)]
    ja = JayaSAMP(100, listVars, sphere)
    print(ja.run(100))
    print("--------------------------------------------------------------")

    print(
        "RUN: Self-adaptive Multi-population Elitist (SAMPE) Jaya " +
        "Algorithm MultiProcess")
    listVars = [VariableFloat(-100.0, 100.0) for i in range(30)]
    ja = JayaSAMPE(100, listVars, sphere)
    print(ja.run(100))
    print("--------------------------------------------------------------")


if __name__ == '__main__':
    main()
