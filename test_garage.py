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

def test_exitGarageCarNotInGarage():
    garage = {
        "capacity": 10,
        "cars": {0: 2}
    }
    with pytest.raises(KeyError):
        exit_garage(garage, 2)

 
def test_get_available_spots():
    garage = {
        "capacity": 2,
        "cars": {0: 2}
    }
    assert get_available_spots(garage) == 1

def test_get_available_spots_WhenFull():
    garage = {
        "capacity": 1,
        "cars": {0: 2}
    }
    assert get_available_spots(garage) == 0

def test_get_available_spots_WhenOverFull():
    garage = {
        "capacity": 1,
        "cars": {0: 2, 1: 2}
    }
    assert get_available_spots(garage) == 0
 
def test_calculate_fee():
    assert calculate_fee(10, 3) == 30
 
@pytest.mark.parametrize("hours, rate", [
    (-10, 2),
    (10, -2),
    (-10, -2)
])