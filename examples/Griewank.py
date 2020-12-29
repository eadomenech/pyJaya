# -*- coding: utf-8 -*-
"""Griewank funtion
http://benchmarkfcns.xyz/benchmarkfcns/griewankfcn.html"""

import numpy as np

from pyJaya.variants.clasic import JayaClasic
from pyJaya.variants.selfAdaptive import JayaSelfAdaptive
from pyJaya.variants.quasiOppositional import JayaQuasiOppositional
from pyJaya.variants.samp import JayaSAMP
from pyJaya.variants.sampe import JayaSAMPE
from pyJaya.variables import VariableFloat


def griewank(solution):
    s = sum(np.asarray(solution) ** 2)
    p = 1
    for item, e in enumerate(solution):
        p *= np.cos(e / np.sqrt(item+1))
    return 1 + s/4000 - p


def main():
    print("RUN: JayaClasic")
    listVars = [VariableFloat(-600.0, 600.0) for i in range(30)]
    ja = JayaClasic(100, listVars, griewank)
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print("RUN: Self-adaptive Jaya Algorithm")
    listVars = [VariableFloat(-600.0, 600.0) for i in range(30)]
    ja = JayaSelfAdaptive(listVars, griewank)
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print("RUN: Quasi-oppositional Based Jaya (QO-Jaya) Algorithm")
    listVars = [VariableFloat(-600.0, 600.0) for i in range(30)]
    ja = JayaQuasiOppositional(100, listVars, griewank)
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print("RUN: Self-adaptive Multi-population (SAMP) Jaya Algorithm")
    listVars = [VariableFloat(-600.0, 600.0) for i in range(30)]
    ja = JayaSAMP(100, listVars, griewank)
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print(
        "RUN: Self-adaptive Multi-population Elitist (SAMPE) Jaya " +
        "Algorithm MultiProcess")
    listVars = [VariableFloat(-600.0, 600.0) for i in range(30)]
    ja = JayaSAMPE(100, listVars, griewank)
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")


if __name__ == '__main__':
    main()
