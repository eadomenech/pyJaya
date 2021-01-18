# -*- coding: utf-8 -*-
"""Himmelblau funtion with constraints
http://benchmarkfcns.xyz/benchmarkfcns/himmelblaufcn.html
"""

# Temp
import sys
sys.path.append("")

from pyJaya.variants.clasic import JayaClasic
from pyJaya.variants.selfAdaptive import JayaSelfAdaptive
from pyJaya.variants.quasiOppositional import JayaQuasiOppositional
from pyJaya.variants.samp import JayaSAMP
from pyJaya.variants.sampe import JayaSAMPE
from pyJaya.variables import VariableFloat


def himmelblau(solution):
    """Himmelblau function

    Args:
        solution (Solution): Candidate solution

    Returns:
        float: Himmelblau function value
    """
    return (
        solution[0] ** 2 + solution[1] - 11) ** 2 +\
        (solution[0] + solution[1] ** 2 - 7) ** 2


def himmelblauConstraintOne(solution):
    """First restriction

    Args:
        solution (Solution): Candidate solution

    Returns:
        bool: True if it meets the constraint, False otherwise
    """
    return (26 - (solution[0] - 5) ** 2 - solution[1] ** 2) >= 0


def himmelblauConstraintTwo(solution):
    """Second restriction

    Args:
        solution (Solution): Candidate solution

    Returns:
        bool: True if it meets the constraint, False otherwise
    """
    return (20 - 4 * solution[0] - solution[1]) >= 0


def main():

    # Vars
    listVars = [VariableFloat(-6.0, 6.0) for i in range(2)]

    print("RUN: JayaClasic")
    ja = JayaClasic(
        100, listVars, himmelblau,
        listConstraints=[himmelblauConstraintOne, himmelblauConstraintTwo])
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print("RUN: Self-adaptive Jaya Algorithm")
    ja = JayaSelfAdaptive(
        listVars, himmelblau,
        listConstraints=[himmelblauConstraintOne, himmelblauConstraintTwo])
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print("RUN: Quasi-oppositional Based Jaya (QO-Jaya) Algorithm")
    ja = JayaQuasiOppositional(
        100, listVars, himmelblau,
        listConstraints=[himmelblauConstraintOne, himmelblauConstraintTwo])
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print("RUN: Self-adaptive Multi-population (SAMP) Jaya Algorithm")
    ja = JayaSAMP(
        100, listVars, himmelblau,
        listConstraints=[himmelblauConstraintOne, himmelblauConstraintTwo])
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")

    print(
        "RUN: Self-adaptive Multi-population Elitist (SAMPE) Jaya " +
        "Algorithm MultiProcess")
    ja = JayaSAMPE(
        100, listVars, himmelblau,
        listConstraints=[himmelblauConstraintOne, himmelblauConstraintTwo])
    print(ja.run(100).getBestAndWorst())
    print("--------------------------------------------------------------")


if __name__ == '__main__':
    main()
