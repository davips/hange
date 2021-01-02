import decimal as dec
import math

from hange.abs.progression import Progression
from hange.tricks import detect_precision


class AP(Progression):
    """Arithmetic Progression. A flexible inductive sequence of numbers based on Haskell interval notation.

    maxdigits: maximum amount of digits verified during precision detection
                (includes numbers to the left and to the right of the decimal separator, if any)

    Usage:
        >>> print(AP(5))
        [5]
        >>> print(AP(5, 1))
        [5 1]
        >>> print(AP(1, 3, ..., 10))
        [1 3 5 7 9]
        >>> ap = AP(0.6, 0.8, ..., 1.2)
        >>> ap
        [0.6 0.8 .+. 1.2]
        >>> print(ap)
        [0.6 0.8 1.0 1.2]
        >>> ap[1]
        0.8
        >>> print(AP(0.2, 4.1, 0.9))
        [0.2 4.1 0.9]
        >>> ap = AP(0.6, 0.8, ...)
        >>> ap
        [0.6 0.8 .+. inf]
        >>> print(ap[:5])
        [0.6 0.8 1.0 1.2 1.4]

    Usage (square brackets syntax):
        >>> from hange import h
        >>> (h[0.6, 0.8, ..., 2])
        [0.6 0.8 .+. 2.0]
    """

    def __init__(self, *args, maxdigits=28):
        super().__init__(
            "+",
            lambda a, b: a + b,
            lambda a, b: a - b,
            lambda a, b: a * b,
            lambda a, b, c: (b - a) / c,
            args,
            maxdigits
        )
