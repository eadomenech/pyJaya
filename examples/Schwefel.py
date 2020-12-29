# -*- coding: utf-8 -*-
"""Schwefel funtion
http://benchmarkfcns.xyz/benchmarkfcns/schwefelfcn.html"""

import numpy as np

from pyJaya.variants.clasic import JayaClasic
from pyJaya.variants.selfAdaptive import JayaSelfAdaptive
from pyJaya.variants.quasiOppositional import JayaQuasiOppositional
from pyJaya.variants.samp import JayaSAMP
from pyJaya.variants.sampe import JayaSAMPE
from pyJaya.variables import VariableFloat


def schwefel(solution):
    s = 0
    for e in solution:
        s += e * np.sin(np.sqrt(abs(e)))
    return -1 / len(solution) * s


def main():
    print("RUN: JayaClasic")
    listVars = [VariableFloat(-500.0, 500.0) for i in range(30)]
    ja = JayaClasic(100, listVars, schwefel)
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print("RUN: Self-adaptive Jaya Algorithm")
    listVars = [VariableFloat(-500.0, 500.0) for i in range(30)]
    ja = JayaSelfAdaptive(listVars, schwefel)
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print("RUN: Quasi-oppositional Based Jaya (QO-Jaya) Algorithm")
    listVars = [VariableFloat(-500.0, 500.0) for i in range(30)]
    ja = JayaQuasiOppositional(100, listVars, schwefel)
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print("RUN: Self-adaptive Multi-population (SAMP) Jaya Algorithm")
    listVars = [VariableFloat(-500.0, 500.0) for i in range(30)]
    ja = JayaSAMP(100, listVars, schwefel)
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print(
        "RUN: Self-adaptive Multi-population Elitist (SAMPE) Jaya " +
        "Algorithm MultiProcess")
    listVars = [VariableFloat(-500.0, 500.0) for i in range(30)]
    ja = JayaSAMPE(100, listVars, schwefel)
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")


if __name__ == '__main__':
    main()
