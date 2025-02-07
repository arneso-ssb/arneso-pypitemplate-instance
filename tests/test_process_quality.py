import sys

from arneso_pypitemplate_instance.process_data import add
from arneso_pypitemplate_instance.process_data import multiply
from arneso_pypitemplate_instance.process_data import subtract


def test_add() -> None:
    facit = 7
    result = add(4, 3)
    assert result == facit


def test_subtract() -> None:
    facit = 1
    if sys.platform.startswith("win"):
        result = subtract(4, 3)
        assert result == facit


def test_unit_id() -> None:
    facit = 12
    if sys.platform.startswith("linux"):
        result = multiply(4, 3)
        assert result == facit
