# -*- coding: utf-8 -*-
"""SumSquares funtion"""

# Temp
import sys
sys.path.append("")

from pyJaya.variants.clasic import JayaClasic
from pyJaya.variants.selfAdaptive import JayaSelfAdaptive
from pyJaya.variants.quasiOppositional import JayaQuasiOppositional
from pyJaya.variants.samp import JayaSAMP
from pyJaya.variants.sampe import JayaSAMPE
from pyJaya.variables import VariableFloat


def sumSquares(solution):
    r = 0.0
    for item, s in enumerate(solution):
        r += (item + 1) * s ** 2
    return r


def main():
    print("RUN: JayaClasic")
    listVars = [VariableFloat(-10.0, 10.0) for i in range(30)]
    ja = JayaClasic(100, listVars, sumSquares)
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print("RUN: Self-adaptive Jaya Algorithm")
    listVars = [VariableFloat(-10.0, 10.0) for i in range(30)]
    ja = JayaSelfAdaptive(listVars, sumSquares)
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print("RUN: Quasi-oppositional Based Jaya (QO-Jaya) Algorithm")
    listVars = [VariableFloat(-10.0, 10.0) for i in range(30)]
    ja = JayaQuasiOppositional(100, listVars, sumSquares)
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print("RUN: Self-adaptive Multi-population (SAMP) Jaya Algorithm")
    listVars = [VariableFloat(-10.0, 10.0) for i in range(30)]
    ja = JayaSAMP(100, listVars, sumSquares)
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print(
        "RUN: Self-adaptive Multi-population Elitist (SAMPE) Jaya " +
        "Algorithm MultiProcess")
    listVars = [VariableFloat(-10.0, 10.0) for i in range(30)]
    ja = JayaSAMPE(100, listVars, sumSquares)
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")


if __name__ == '__main__':
    main()
