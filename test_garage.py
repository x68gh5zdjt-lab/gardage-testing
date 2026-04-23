import pytest
from garage import enter_garage

def test_entergaragePass():
    garage = {
        "capacity": 10,
        "cars": {}
    }
    assert enter_garage(garage, 0, 2) == True