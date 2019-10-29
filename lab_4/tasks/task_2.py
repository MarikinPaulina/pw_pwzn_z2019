"""
Częśćć 1 (1 pkt): Uzupełnij klasę Vector tak by reprezentowała wielowymiarowy wektor.
Klasa posiada przeładowane operatory równości, dodawania, odejmowania,
mnożenia (przez liczbę i skalarnego), długości
oraz nieedytowalny (własność) wymiar.
Wszystkie operacje sprawdzają wymiar.
Część 2 (1 pkt): Klasa ma statyczną metodę wylicznia wektora z dwóch punktów
oraz metodę fabryki korzystającą z metody statycznej tworzącej nowy wektor
z dwóch punktów.
Wszystkie metody sprawdzają wymiar.
"""


class Vector:
    dim = None  # Wymiar vectora

    @property
    def len(self):
        raise NotImplemented

    def __init__(self, *args):
        self.vec = args
        # raise NotImplemented

    @staticmethod
    def calculate_vector(beg, end):
        """
        Calculate vector from given points

        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: Calculated vector
        :rtype: tuple
        """
        return Vector.from_points(beg, end).vec

    @classmethod
    def from_points(cls, beg, end):
        """"""
        """
        Generate vector from given points.

        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: New vector
        :rtype: tuple
        """
        if len(end) == len(beg):
            result = cls(*end) - cls(*beg)
            return result
        else:
            raise ValueError

    @property
    def dim(self):
        return len(self.vec)

    def __eq__(self, other):
        if self.dim == other.dim:
            for a, b in zip(self.vec, other.vec):
                if a != b:
                    return False
            return True

    def __add__(self, other):
        if self.dim == other.dim:
            args = list(a+b for a, b in zip(self.vec, other.vec))
            out = Vector(*args)
            return out
        else:
            raise ValueError

    def __sub__(self, other):
        if self.dim == other.dim:
            args = list(a-b for a, b in zip(self.vec, other.vec))
            out = Vector(*args)
            return out
        else:
            raise ValueError

    def __mul__(self, other):
        if isinstance(other, Vector):
            if self.dim == other.dim:
                args = list(a*b for a, b in zip(self.vec, other.vec))
                out = sum(args)
                return out
            else:
                raise ValueError
        else:
            args = list(a*other for a in self.vec)
            out = Vector(*args)
            return out

    def len(self):
        args = list(a ** 2 for a in self.vec)
        out = sum(args) ** 0.5
        return int(out)

    def __len__(self):
        return self.dim


if __name__ == '__main__':
    v1 = Vector(1, 2, 3)
    v2 = Vector(1, 2, 3)
    assert v1 + v2 == Vector(2, 4, 6)
    assert v1 - v2 == Vector(0, 0, 0)
    assert v1 * 2 == Vector(2, 4, 6)
    assert v1 * v2 == 14
    assert len(Vector(3,4)) == 2
    assert Vector(3,4).dim == 2
    assert Vector(3,4).len == 5.
    assert Vector.calculate_vector([0, 0, 0], [1,2,3]) == (1,2,3)
    assert Vector.from_points([0, 0, 0], [1,2,3]) == Vector(1,2,3)
