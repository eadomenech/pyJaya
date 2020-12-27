# -*- coding: utf-8 -*-
"""SumSquares funtion"""

from pyJaya.variants.clasic import JayaClasic
from pyJaya.variants.selfAdadtive import JayaSelfAdadtive
from pyJaya.variants.quasiOppositional import JayaQuasiOppositional
from pyJaya.variants.samp import JayaSAMP
from pyJaya.variants.sampemultiprocess import JayaSAMPE
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
    ja = JayaSelfAdadtive(listVars, sumSquares)
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
    print(ja.run(100))
    print("--------------------------------------------------------------")

    print(
        "RUN: Self-adaptive Multi-population Elitist (SAMPE) Jaya " +
        "Algorithm MultiProcess")
    listVars = [VariableFloat(-10.0, 10.0) for i in range(30)]
    ja = JayaSAMPE(100, listVars, sumSquares)
    print(ja.run(100))
    print("--------------------------------------------------------------")


if __name__ == '__main__':
    main()
