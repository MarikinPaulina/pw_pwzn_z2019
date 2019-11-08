"""
Na (1 pkt.):
- Zaimplementuj klasy: Rectangle, Square, Circle dziedziczące z klasy Figure
oraz definiujące jej metody:
    - Rectangle powinien mieć dwa atrybuty odpowiadające bokom (a i b)
    - Klasa Square powinna dziedziczyć z Rectangle.
    - Circle ma posiadać tylko atrybut r (radius).
- Przekształć metody we własności (properties).
---------
Na (2 pkt.):
- Zwiąż ze sobą boki a i b klasy Square (tzn. modyfikacja boku a lub boku b
powinna ustawiać tę samą wartość dla drugiego atrybutu).
- Zaimplementuj metody statyczne pozwalające na obliczenie pola i obwodu
figury na podstawie podanych parametrów.
- Zaimplementuj classmethod "name" zwracającą nazwę klasy.
---------
Na (3 pkt.):
- Zaimplementuj klasę Diamond (romb) dziedziczącą z Figure,
po której będzie dziedziczyć Square,
tzn. Square dziediczy i z Diamond i Rectangle.
- Klasa wprowadza atrybuty przekątnych (e i f) oraz metody:
-- are_diagonals_equal: sprawdź równość przekątnych,
-- to_square: po sprawdzeniu równości przekątnych zwróci instancję
klasy Square o takich przekątnych.
- Zwiąż ze sobą atrybuty e i f (w klasie Diamond) oraz a, b, e i f
(w klasie Square)
"""
from math import pi


class Figure:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    @classmethod
    def name(cls):
        return cls.__name__

    def __str__(self):
        return (
            f'{self.name()}: area={self.area:.3f}, '
            f'perimeter={self.perimeter:.3f}'
        )


class Circle(Figure):
    __r = None

    def __init__(self, r):
        self.__r = r

    @classmethod
    def area(cls, r):
        return pi*r**2

    @property
    def area(self):
        return pi*self.__r**2

    @classmethod
    def perimeter(cls, r):
        return 2*pi*r

    @property
    def perimeter(self):
        return 2*pi*self.__r


class Rectangle(Figure):
    __a = None
    __b = None

    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    @classmethod
    def area(cls, a, b):
        return a*b

    @property
    def area(self):
        return self.__a * self.__b

    @classmethod
    def perimeter(cls, a, b):
        return 2*(a+b)

    @property
    def perimeter(self):
        return 2*(self.__a + self.__b)


class Diamond(Figure):
    __e = None
    __f = None

    @property
    def area(self):
        return self.__e*self.__f*0.5

    @property
    def perimeter(self):
        return 2*(self.__e**2 + self.__f**2)**0.5


class Square(Rectangle, Diamond):

    def __init__(self, a):
        super().__init__(a, a)

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value
        self.__b = value

    @classmethod
    def area(cls, a):
        return a**2

    @classmethod
    def perimeter(cls, a):
        return 4*a



if __name__ == '__main__':

    kolo1 = Circle(1)
    assert str(kolo1) == 'Circle: area=3.142, perimeter=6.283'

    rec_1 = Rectangle(2, 4)
    assert str(rec_1) == 'Rectangle: area=8.000, perimeter=12.000'

    # print("Square")
    sqr_1 = Square(4)
    assert str(sqr_1) == 'Square: area=16.000, perimeter=16.000'  # Tu był błąd (area=8.000)

    diam_1 = Diamond(6, 8)
    assert str(diam_1) == 'Diamond: area=24.000, perimeter=20.000'

    diam_2 = Diamond(1, 1)
    assert str(diam_2) == 'Diamond: area=0.500, perimeter=2.828'

    sqr_3 = diam_2.to_square()
    assert str(diam_2) == 'Square: area=0.500, perimeter=2.828'