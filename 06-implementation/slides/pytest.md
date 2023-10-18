PS> python -m venv venv
PS> .\venv\Scripts\activate
(venv) PS> python -m pip install pytest


# test_with_unittest.py

from unittest import TestCase

class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_always_fails(self):
        self.assertTrue(False)


python -m unittest discover


# test_with_pytest.py

def test_always_passes():
    assert True

def test_always_fails():
    assert False


venv) $ pytest
============================= test session starts =============================
platform win32 -- Python 3.10.5, pytest-7.1.2, pluggy-1.0.0
rootdir: ...\effective-python-testing-with-pytest
collected 4 items

test_with_pytest.py .F                                                   [ 50%]
test_with_unittest.py F.                                                 [100%]

================================== FAILURES ===================================
______________________________ test_always_fails ______________________________

    def test_always_fails():
>       assert False
E       assert False

test_with_pytest.py:7: AssertionError
________________________ TryTesting.test_always_fails _________________________

self = <test_with_unittest.TryTesting testMethod=test_always_fails>

    def test_always_fails(self):
>       self.assertTrue(False)
E       AssertionError: False is not true

test_with_unittest.py:10: AssertionError
=========================== short test summary info ===========================
FAILED test_with_pytest.py::test_always_fails - assert False
FAILED test_with_unittest.py::TryTesting::test_always_fails - AssertionError:...

========================= 2 failed, 2 passed in 0.20s =========================


The output then indicates the status of each test using a syntax similar to unittest:

    A dot (.) means that the test passed.
    An F means that the test has failed.
    An E means that the test raised an unexpected exception.



# test_assert_examples.py

def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_some_primes():
    assert 37 in {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }


# fixture_demo.py

import pytest

@pytest.fixture
def example_fixture():
    return 1

def test_with_fixture(example_fixture):
    assert example_fixture == 1




# test_format_data.py

import pytest

@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]
