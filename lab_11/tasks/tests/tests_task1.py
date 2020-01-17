import pytest

from lab_11.tasks.tools.calculator import (
    Calculator,
    CalculatorError,
    EmptyMemory,
    NotNumberArgument,
    WrongOperation,
)


@pytest.fixture()
def calculator(scope='module'):
    return Calculator()


@pytest.mark.parametrize(
    ('operator', 'arg1', 'arg2', 'expected'),
    [
        pytest.param('+', '1', '2',   3,      id='add1'),
        pytest.param('+', '5', '9',  14,      id='add2'),
        pytest.param('-', '5', '1',   4,      id='sub1'),
        pytest.param('-', '1', '4',  -3,      id='sub2'),
        pytest.param('*', '1', '5',   5,      id='mul1'),
        pytest.param('*', '7', '0.5', 3.5,    id='mul2'),
        pytest.param('/', '8', '2',   4,      id='div1'),
        pytest.param('/', '2', '8',   0.25,   id='div2')
    ],
)
def test_operations(calculator, operator, arg1, arg2, expected):
    assert calculator.run(operator, arg1, arg2) == expected


@pytest.mark.parametrize(
    ('operator', 'arg1', 'arg2', 'expected'),
    [
        pytest.param('*', 3, None, EmptyMemory, id='EmptyMemory1'),
        pytest.param('^', 2, 5, WrongOperation, id='WrongOperation1'),
        pytest.param(4, 2, 5, WrongOperation, id='WrongOperation2'),
        pytest.param(2, '*', 5, WrongOperation, id='WrongOperation3'),
        pytest.param('/', 5, 'a', NotNumberArgument, id='NotNumberArgument1')
    ]
)
def test_exceptions(calculator, operator, arg1, arg2, expected):
    try:
        calculator.run(operator, arg1, arg2)
    except CalculatorError as exc:
        assert type(exc) == expected
    else:
        raise AssertionError


def test_emptyMemory2(calculator):
    try:
        calculator.in_memory()
    except CalculatorError as exc:
        assert type(exc) == EmptyMemory
    else:
        raise AssertionError


def test_emptyMemory3(calculator):
    try:
        calculator.run('+', 1, 2)
        calculator.memorize()
        assert calculator.run('-', 3) == 0
        calculator.clean_memory()
        calculator.run('+', 2)
    except CalculatorError as exc:
        assert type(exc) == EmptyMemory
    else:
        raise AssertionError


def test_zeroDivisionError(calculator):
    try:
        calculator.run('/', 5, 0)
    except CalculatorError as exc:
        assert type(exc.__cause__) == ZeroDivisionError
    else:
        raise AssertionError
