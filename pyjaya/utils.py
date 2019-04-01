# -*- coding: utf-8 -*-
import numpy as np


class NumberRange():

    def __init__(self, outside_first=0, outside_second=1):

        self.minor = min(outside_first, outside_second)
        self.major = max(outside_first, outside_second)
        self.validate()

    def validate(self):
        """Client must define it self"""
        raise NotImplementedError("Client must define it self")

    def get(self):
        """Client must define it self"""
        raise NotImplementedError("Client must define it self")

    def convert(self):
        """Client must define it self"""
        raise NotImplementedError("Client must define it self")


class IntRange(NumberRange):

    def validate(self):
        if not isinstance(self.minor, (int)) or not isinstance(self.major, (int)):
            raise NotImplementedError("The numbers should be integer")

    def get(self):
        np.random.seed()
        return int((self.major-self.minor) * np.random.rand() + self.minor)

    def convert(self, value):
        value = round(value)
        if value > self.major:
            return self.major
        elif value < self.minor:
            return self.minor
        else:
            return value


class FloatRange(NumberRange):

    def validate(self):
        if not isinstance(
                self.minor, (float)) or not isinstance(self.major, (float)):
            raise NotImplementedError("The numbers should be float")

    def get(self):
        np.random.seed()
        return (self.major-self.minor) * np.random.rand() + self.minor

    def convert(self, value):
        if value > self.major:
            return self.major
        elif value < self.minor:
            return self.minor
        else:
            return value


class BinaryRange(NumberRange):

    def validate(self):
        pass

    def get(self):
        np.random.seed()
        return np.random.randint(2)

    def convert(self, value):
        value = round(value)
        if value > 1:
            return 1.0
        elif value < 0.0:
            return 0.0
        else:
            return value
