import pytest
from firmware_simulation import MotorController

@pytest.fixture
def controller():
    return MotorController


def test_valid_speed1():
    test=controller.process_command("Set speed: 75")
    assert test["status"] == "Success"


def test_valid_speed2():
    test=controller.process_command("Set speed: 102")
    assert test["status"] == "Error"

def test_valid_type_value():
    test=controller.process_command("Set speed: text")
    assert test["status"] == "Error"