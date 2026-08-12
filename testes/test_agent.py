from src.tools.math_tools import multiply, divide


def test_multiply():
    result = multiply.invoke({
        "a": 15,
        "b": 8
    })

    assert result == 120


def test_divide():
    result = divide.invoke({
        "a": 120,
        "b": 3
    })

    assert result == 40