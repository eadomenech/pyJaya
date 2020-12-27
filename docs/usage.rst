=====
Usage
=====

To use pyJaya::

    from pyJaya.variants.clasic import JayaClasic
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
    
    print("RUN: JayaClasic")
    # Two variables in the range [-6.0, 6.0]
    listVars = [VariableFloat(-6.0, 6.0) for i in range(2)]
    # JayaClasic with initial population of 100 solutions and two constrains.
    ja = JayaClasic(
        100, listVars, himmelblau,
        listConstraints=[himmelblauConstraintOne, himmelblauConstraintTwo])
    # Execution of 100 iterations and obtaining better and worse solution
    print(ja.run(100).getBestAndWorst())
