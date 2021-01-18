# -*- coding: utf-8 -*-
"""Sphere funtion"""

# Temp
import sys
sys.path.append("")

import numpy as np

from pyJaya.variants.clasic import JayaClasic
from pyJaya.variants.selfAdaptive import JayaSelfAdaptive
from pyJaya.variants.quasiOppositional import JayaQuasiOppositional
from pyJaya.variants.samp import JayaSAMP
from pyJaya.variants.sampe import JayaSAMPE, MultiprocessJayaSAMPE
from pyJaya.variables import VariableFloat


def sphere(solution):
    return sum(np.asarray(solution)**2)


def main():

    # Vars
    listVars = [VariableFloat(-100.0, 100.0) for i in range(30)]

    print("RUN: JayaClasic")
    ja = JayaClasic(100, listVars, sphere)
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print("RUN: Self-adaptive Jaya Algorithm")
    ja = JayaSelfAdaptive(listVars, sphere)
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print("RUN: Quasi-oppositional Based Jaya (QO-Jaya) Algorithm")
    ja = JayaQuasiOppositional(100, listVars, sphere)
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print("RUN: Self-adaptive Multi-population (SAMP) Jaya Algorithm")
    ja = JayaSAMP(100, listVars, sphere)
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print(
        "RUN: Self-adaptive Multi-population Elitist (SAMPE) Jaya " +
        "Algorithm MultiProcess")
    ja = MultiprocessJayaSAMPE(100, listVars, sphere)
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")


if __name__ == '__main__':
    main()
