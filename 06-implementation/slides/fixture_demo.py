# fixture_demo.py

import pytest

@pytest.fixture
def example_fixture():
    return 1

@pytest.fixture
def example_fixture2():
    return 7

@pytest.fixture
def example_fixture3():
    return 9

@pytest.fixture
def toad_swift():
    return 9

@pytest.fixture
def 


def test_with_fixture(example_fixture):
    assert example_fixture == 1
def test_with_fixture2(example_fixture2):
    assert example_fixture2 == 7
def test_with_fixture3(example_fixture3):
    assert example_fixture3 == 9
def test_with_fixture4(toad_swift):
    assert toad_swift == 9


def test_fred(example_fixture):
    assert example_fixture == 1
def test_barney(example_fixture2):
    assert example_fixture2 == 7
def test_wilma(example_fixture3):
    assert example_fixture3 == 9



