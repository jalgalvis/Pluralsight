"""Model for aircraft flights"""


class ClassTest:

    def instanceMethod(self):
        return "0001"


class ClassTest1:

    def __init__(self, instanceAttribute):
        self._instanceAttribute = instanceAttribute

    def instanceMethod(self):
        return self._instanceAttribute


class ClassTest2:

    def __init__(self, instanceAttribute):
        if not instanceAttribute[:2].isalpha():
            raise ValueError(f"Not 2 initial letters in '{instanceAttribute}'")
        if not instanceAttribute[:2].isupper():
            raise ValueError(f"Not 2 initial Upper letters in '{instanceAttribute}'")
        if not [instanceAttribute[2:].isdigit() and int(instanceAttribute[2:]) <= 9999]:
            raise ValueError(f"Invalid number in '{instanceAttribute}'")

        self._instanceAttribute = instanceAttribute

    def instanceMethod(self):
        return self._instanceAttribute

    def instanceMethodPartial(self):
        return self._instanceAttribute[:2]


class ClassTest3:

    def __init__(self, instanceAttribute):
        if not instanceAttribute[:2].isalpha():
            raise ValueError(f"Not 2 initial letters in '{instanceAttribute}'")
        if not instanceAttribute[:2].isupper():
            raise ValueError(f"Not 2 initial Upper letters in '{instanceAttribute}'")
        if not [instanceAttribute[2:].isdigit() and int(instanceAttribute[2:]) <= 9999]:
            raise ValueError(f"Invalid number in '{instanceAttribute}'")

        self._instanceAttribute = instanceAttribute


class ClassTest4:
    def __init__(self, instanceAttribute1,  instanceAttribute2,  instanceAttribute3):
        self._instanceAttribute1 = instanceAttribute1
        self._instanceAttribute2 = instanceAttribute2
        self._instanceAttribute3 = instanceAttribute3

    def instanceAttribute1(self):
        return self._instanceAttribute1

    def instanceAttribute4(self):
        return range(1, self._instanceAttribute2), "ABCDFGKLMNOPQRST"[:self._instanceAttribute3]

