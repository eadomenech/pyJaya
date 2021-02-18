# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import numpy as np


class Variable(ABC):
    """Variable class
    """

    @abstractmethod
    def validate(self):
        """Client must define it self"""
        raise NotImplementedError("Client must define it self")

    @abstractmethod
    def get(self):
        """Client must define it self"""
        raise NotImplementedError("Client must define it self")

    @abstractmethod
    def convert(self):
        """Client must define it self"""
        raise NotImplementedError("Client must define it self")


class VariableInt(Variable):
    """VariableInt class

    Args:
        outside_first (int, optional):
            Lowest possible value in the range of the variable.
            Defaults to -100.
        outside_second (int, optional): Largest possible value in the
            range of the variable. Defaults to 100.
    """

    def __init__(self, outside_first=-100, outside_second=100):

        self.minor = min(outside_first, outside_second)
        self.major = max(outside_first, outside_second)
        self.validate()

    def validate(self):
        """Validate that the variables are integers

        Raises:
            NotImplementedError: "The numbers should be integer".
        """
        if not isinstance(
                self.minor, (int)) or not isinstance(self.major, (int)):
            raise NotImplementedError("The numbers should be integer")

    def get(self):
        """Returns an integer in the possible range

        Returns:
            int: Integer in the range.
        """
        np.random.seed()
        return int((self.major-self.minor) * np.random.rand() + self.minor)

    def convert(self, item):
        """Converts an item to a possible value in the range

        Args:
            item (int or float): Value to convert.

        Returns:
            int: Value in the range.
        """
        return int(np.clip(round(item), self.minor, self.major))


class VariableFloat(Variable):
    """VariableFloat class

    Args:
        outside_first (int, optional):
            Lowest possible value in the range of the variable.
            Defaults to -100.0.
        outside_second (int, optional): Largest possible value in the
            range of the variable. Defaults to 100.0.
    """

    def __init__(self, outside_first=-100.0, outside_second=100.0):

        self.minor = min(outside_first, outside_second)
        self.major = max(outside_first, outside_second)
        self.validate()

    def validate(self):
        """Validate that the variables are float

        Raises:
            NotImplementedError: "The numbers should be float".
        """
        if not isinstance(
                self.minor, (float)) or not isinstance(self.major, (float)):
            raise NotImplementedError("The numbers should be float")

    def get(self):
        """Returns an float in the possible range

        Returns:
            float: Float in the range.
        """
        np.random.seed()
        return (self.major-self.minor) * np.random.rand() + self.minor

    def convert(self, item):
        """Converts an item to a possible value in the range

        Args:
            item (int or float): Value to convert.

        Returns:
            float: Value in the range.
        """
        return float(np.clip(item, self.minor, self.major))


class VariableBinary(Variable):
    """VariableBinary class"""

    def __init__(self):

        self.minor = 0
        self.major = 1
        self.validate()

    def validate(self):
        pass

    def get(self):
        """Returns an integer in the possible range

        Returns:
            int: Integer in the range.
        """
        np.random.seed()
        return np.random.randint(2)

    def convert(self, item):
        """Converts an item to a possible value in the range

        Args:
            item (int or float): Value to convert.

        Returns:
            int: Value in the range.
        """
        return int(np.clip(round(item), self.minor, self.major))
