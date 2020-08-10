import inspect
import re
import os
import pytest
import random
import session4
from decimal import Decimal
import math

qualean_inputs = {-1, 0, 1}


def test_readme_exists():
    """
    Check if the README file exists
    :return: None
    """
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    """
    Test the length of the README file
    :return: None
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_file_for_formatting():
    """
    Tests the formatting for the README file
    :return: None
    """
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_function_name_had_cap_letter():
    """
    Checking PEP-8 guidelines for function names. Pass if all alphabets(a-z) are in small case.
    :return: None
    """
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_invalid_input_type():
    """
    Valid input types to Qualean() class are float, int and Decimal
    :return: None
    """
    with pytest.raises(ValueError):
        session4.Qualean('1')
    with pytest.raises(ValueError):
        session4.Qualean([-1])


def test_invalid_input_value():
    """
    Check input values to Qualean() class. Expected values are {-1, 0, +1}
    :return: None
    """
    with pytest.raises(ValueError):
        session4.Qualean(-10)
    with pytest.raises(ValueError):
        session4.Qualean(Decimal(1.5))
    with pytest.raises(ValueError):
        session4.Qualean(0.1)


def test_invalid_input_for__and__():
    """
    Ensuring correctness of object type, for __and__()
    :return: None
    """
    with pytest.raises(ValueError):
        q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
        q1 & 10


def test_and_case1():
    """
    Test the bitwise and operator on two qualeans
    :return: None
    """
    for _ in range(500):
        q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
        q2 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
        q3 = q1 & q2
        assert isinstance(q3, session4.Qualean), 'Invalid bitwise `&` operation'


def test_and_case2():
    """
    Test the boolean and operator, in a short-circuit scenario
    :return: None
    """
    q1 = session4.Qualean(0)
    result = q1 and q2
    assert not result, 'Expected to result in False when q1 is false and q2 undefined'


def test_invalid_input_for__or__():
    """
    Ensuring correctness of object type, for __or__()
    :return: None
    """
    with pytest.raises(ValueError):
        q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
        q1 | 10


def test_or_case1():
    """
    Test the bitwise `or` operator
    :return: None
    """
    for _ in range(500):
        q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
        q2 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
        q3 = q1 | q2
        assert isinstance(q3, session4.Qualean), 'Invalid bitwise `|` operation'


def test_or_case2():
    """
    Test the boolean or operator, in a short-circuit scenario
    :return: None
    """
    q1 = session4.Qualean(1)
    result = q1 or q2
    assert result, 'Expected to result in True when q1 is true and q2 undefined'


def test_rectangle_repr():
    """
    Ensuring that __repr__ yields string in expected format
    :return: None
    """
    r = session4.Qualean(random.sample(qualean_inputs, 1)[0])
    assert r.__repr__() == 'Qualean instance with value : {}'.format(r.number)


def test_rectangle_str():
    """
    Ensuring that __str__ yields string in expected format
    :return: None
    """
    r = session4.Qualean(random.sample(qualean_inputs, 1)[0])
    assert r.__str__() == 'Qualean : {}'.format(r.number)


def test_invalid_input_for__add__():
    """
    Ensuring correctness of object type, for __add__()
    :return: None
    """
    with pytest.raises(ValueError):
        q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
        q1 + 10


def test_add_case1():
    """
    Test the add operation by adding q1 100 times and check the result
    :return: None
    """
    q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
    q_sum = round(q1.number * 100, 10)
    q_temp = q1
    for _ in range(99):
        q_temp = q_temp + q1

    assert q_sum == q_temp.number, 'Sum implementation is buggy'


def test_add_case2():
    """
    Test the add operation by adding 3 random qualeans
    :return: None
    """
    q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
    q2 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
    q3 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
    q_temp = q1 + q2 + q3

    q_sum = round(q1.number + q2.number + q3.number, 10)
    assert q_sum == q_temp.number, 'Sum implementation is buggy'


def test_add_case3():
    """
    Test the sum of 1 million different q's
    :return: None
    """
    q_sum = session4.Qualean(0)
    for _ in range(1000000):
        q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
        # q1 = session4.Qualean(1)
        q_sum += q1
    assert math.isclose(round(q_sum.number, 10), 0, rel_tol=1e-09, abs_tol=1e3)


def test_invalid_input_for__eq__():
    """
    Ensuring correctness of object type, for __eq__()
    :return: None
    """
    with pytest.raises(ValueError):
        q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
        _ = q1 == 10


def test_eq():
    """
    Test the '==' operator
    :return: None
    """
    for _ in range(500):
        q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
        q2 = session4.Qualean(random.sample(qualean_inputs, 1)[0])

        result = q1 == q2
        assert result == (Decimal(q1.number) == Decimal(q2.number)), ' == Comparison is buggy'


def test_invalid_input_for__ge__():
    """
    Ensuring correctness of object type, for __ge__()
    :return: None
    """
    with pytest.raises(ValueError):
        q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
        _ = q1 >= 10


def test_ge():
    """
    Test the '>=' operator
    :return: None
    """

    for _ in range(500):
        q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
        q2 = session4.Qualean(random.sample(qualean_inputs, 1)[0])

        result = q1 >= q2
        assert result == (Decimal(q1.number) >= Decimal(q2.number)), ' >= Comparison is buggy'


def test_invalid_input_for__gt__():
    """
    Ensuring correctness of object type, for __gt__()
    :return: None
    """
    with pytest.raises(ValueError):
        q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
        _ = q1 > 10


def test_gt():
    """
    Test the '>' operator
    :return: None
    """
    for _ in range(500):
        q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
        q2 = session4.Qualean(random.sample(qualean_inputs, 1)[0])

        result = q1 > q2
        assert result == (Decimal(q1.number) > Decimal(q2.number)), ' > Comparison is buggy'


def test_invalid_input_for__le__():
    """
    Ensuring correctness of object type, for __le__()
    :return: None
    """
    with pytest.raises(ValueError):
        q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
        _ = q1 <= 10


def test_le():
    """
    Test the '<=' operator
    :return: None
    """
    for _ in range(500):
        q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
        q2 = session4.Qualean(random.sample(qualean_inputs, 1)[0])

        result = q1 <= q2
        assert result == (Decimal(q1.number) <= Decimal(q2.number)), ' <= Comparison is buggy'


def test_invalid_input_for__lt__():
    """
    Ensuring correctness of object type, for __lt__()
    :return: None
    """
    with pytest.raises(ValueError):
        q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
        _ = q1 < 10


def test_lt():
    """
    Test the '<' operator
    :return: None
    """
    for _ in range(500):
        q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
        q2 = session4.Qualean(random.sample(qualean_inputs, 1)[0])

        result = q1 < q2
        assert result == (Decimal(q1.number) < Decimal(q2.number)), ' < Comparison is buggy'


def test_invalid_input_for__mul__():
    """
    Ensuring correctness of object type, for __mul__()
    :return: None
    """
    with pytest.raises(ValueError):
        q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
        _ = q1 * 'test'


def test_mul():
    """
    Test the '*' operator
    :return: None
    """
    for _ in range(500):
        q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
        q2 = session4.Qualean(random.sample(qualean_inputs, 1)[0])

        result = q1 * q2
        assert result.number == round(Decimal(q1.number) * Decimal(q2.number), 10), ' * Multiplication is buggy'


def test_sqrt():
    """
    Test the sqrt() method
    :return: None
    """
    for _ in range(500):
        q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])

        if q1.number < 0:
            with pytest.raises(ArithmeticError):
                q1.__sqrt__()
        else:
            result = q1.__sqrt__()
            assert result.number == round(Decimal(q1.number).sqrt(), 10), ' sqrt is buggy'


def test_bool():
    """
    Test the bool operator
    :return:
    """
    for _ in range(500):
        q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])

        result = bool(q1)
        assert result == bool(Decimal(q1.number)), ' bool is buggy'


def test_float():
    for _ in range(500):
        q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
        result = float(q1)
        assert isinstance(result, float), 'Expected float number, got {}'.format(str(type(result)))


def test_invertsign():
    for _ in range(500):
        q1 = session4.Qualean(random.sample(qualean_inputs, 1)[0])
        inverted_q1 = q1.__invertsign__()
        q2 = q1 * -1
        assert inverted_q1 == q2, 'Invertsign is buggy'

