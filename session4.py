import random
from decimal import Decimal


class Qualean(object):
    def __init__(self, state):
        """
        Initialize the Qualean object
        :param state:
        """
        if isinstance(state, int) or isinstance(state, float) or isinstance(state, Decimal):
            if state == -1 or state == 0 or state == 1:
                self.number = round(Decimal(state * random.uniform(-1, 1)), 10)
            else:
                raise ValueError('Invalid value for state. Expected {-1, 0, +1}')
        else:
            raise ValueError('Invalid type for state. Expected int / float / decimal.')

    def __and__(self, other):
        """
        Bitwise `&` operator between two Qualeans
        :param other: Qualean
        :return: Qualean
        """
        if not isinstance(other, Qualean):
            raise ValueError("unsupported operand type(s) for &: 'Qualean' and {}.".format(str(type(other))))

        q1 = format(self.number, '.10f').split('.')
        q2 = format(other.number, '.10f').split('.')
        integer_part = int(q1[0]) & int(q2[0])
        decimal_part = int(q1[1]) & int(q2[1])

        result = Qualean(0)
        result.number = round(Decimal('{}.{}'.format(integer_part, decimal_part)), 10)
        return result

    def __or__(self, other):
        """
        Bitwise `|` operator between two Qualeans
        :param other: Qualean
        :return: Qualean
        """
        if not isinstance(other, Qualean):
            raise ValueError("unsupported operand type(s) for &: 'Qualean' and {}.".format(str(type(other))))
        q1 = format(self.number, '.10f').split('.')
        q2 = format(other.number, '.10f').split('.')
        integer_part = int(q1[0]) | int(q2[0])
        decimal_part = int(q1[1]) | int(q2[1])

        result = Qualean(0)
        result.number = round(Decimal('{}.{}'.format(integer_part, decimal_part)), 10)
        return result

    def __repr__(self):
        """
        String representation of the object of the Qualean class
        :return: string
        """
        return 'Qualean instance with value : {}'.format(self.number)

    def __str__(self):
        """
        Readable string representation of the qualean
        :return: string
        """
        return 'Qualean : {}'.format(self.number)

    def __add__(self, other):
        """
            Add two Qualeans, by overloading the binary `+` operator
            :param other: Qualean
            :return: Qualean
        """
        if not isinstance(other, Qualean):
            raise ValueError("unsupported operand type(s) for +: 'Qualean' and {}.".format(str(type(other))))
        result = Qualean(0)
        result.number = round(self.number + other.number, 10)
        return result

    def __eq__(self, other):
        """
            Checking the equality of two Qualeans
            :param other: Qualean
            :return: Qualean
        """
        if not isinstance(other, Qualean):
            raise ValueError("unsupported operand type(s) for ==: 'Qualean' and {}.".format(str(type(other))))
        return self.number == other.number

    def __float__(self):
        """
            Return a floating point representation of the Qualean
            :return: float
        """
        return float(self.number)

    def __ge__(self, other):
        """
            Compare two Qualeans, by overloading the binary `>=` operator
            :param other: Qualean
            :return: bool
        """
        if not isinstance(other, Qualean):
            raise ValueError("unsupported operand type(s) for >: 'Qualean' and {}.".format(str(type(other))))
        return self.number >= other.number

    def __gt__(self, other):
        """
            Compare two Qualeans, by overloading the binary `>` operator
            :param other: Qualean
            :return: bool
        """
        if not isinstance(other, Qualean):
            raise ValueError("unsupported operand type(s) for >: 'Qualean' and {}.".format(str(type(other))))
        return self.number > other.number

    def __invertsign__(self):
        result = Qualean(0)
        result.number = round(self.number * -1, 10)
        return result

    def __le__(self, other):
        """
            Compare two Qualeans, by overloading the binary `<=` operator
            :param other: Qualean
            :return: bool
        """
        if not isinstance(other, Qualean):
            raise ValueError("unsupported operand type(s) for <=: 'Qualean' and {}.".format(str(type(other))))
        return self.number <= other.number

    def __lt__(self, other):
        """
            Compare two Qualeans, by overloading the binary `<` operator
            :param other: Qualean
            :return: bool
        """
        if not isinstance(other, Qualean):
            raise ValueError("unsupported operand type(s) for <: 'Qualean' and {}.".format(str(type(other))))
        return self.number < other.number

    def __mul__(self, other):
        """
            Multiply two Qualeans, by overloading the binary `*` operator.
            :param other: Qualean, float, int, Decimal
            :return: Qualean
        """
        if isinstance(other, Qualean):
            result = Qualean(0)
            result.number = round(self.number * other.number, 10)
            return result
        elif isinstance(other, int) or isinstance(other, float) or isinstance(other, Decimal):
            result = Qualean(0)
            result.number = round(self.number * Decimal(other), 10)
            return result
        else:
            raise ValueError("unsupported operand type(s) for *: 'Qualean' and {}.".format(str(type(other))))

    def __sqrt__(self):
        """
            Method for performing square root operation for qualeans
            :return: qualean
        """
        if self.number >= 0:
            result = Qualean(0)
            result.number = round(self.number.sqrt(), 10)
            return result
        else:
            raise ArithmeticError('Cannot compute sqrt of negative numbers. Complex numbers are not supported.')

    def __bool__(self):
        """
            Convert qualean to python bool. Return False when qualean is 0, and True otherwise
            :return: bool
        """
        if self.number == Decimal(0):
            return False
        else:
            return True
