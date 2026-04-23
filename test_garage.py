import pytest
from garage import enter_garage

def test_entergaragePass():
    garage = {
        "capacity": 10,
        "cars": {}
    }
    assert enter_garage(garage, 0, 2) == True

def test_enterFullGarage():
    garage = {
        "capacity": 0,
        "cars": {}
    }
    with pytest.raises(ValueError):
        enter_garage(garage, 0, 2)

def test_entergaragealreadyInGarage():
    garage = {
        "capacity": 4,
        "cars": {0: 2}
    }
    with pytest.raises(ValueError):
        enter_garage(garage, 0, 2)

def test_entergarageInvalidTimeType():
    garage = {
        "capacity": 4,
        "cars": {}
    }
    with pytest.raises(TypeError):
        enter_garage(garage, 0, "2")

def test_exitGarage():
    garage = {
        "capacity": 10,
        "cars": {0: 2}
    }
    assert exit_garage(garage, 0) == True