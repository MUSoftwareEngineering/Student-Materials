# wilma.py
import pytest

@pytest.fixture
def wilma():
    return "Wilma"

@pytest.fixture
def fred():
    return "Fred"

@pytest.fixture
def barney():
    return "Barney"

@pytest.fixture
def flintstones(wilma,fred):
    return [wilma,fred]

def test_flintstones(flintstones,fred):
#    assert barney not in flintstones
     assert barney in flintstones   


def test_chowder(wilma,fred,barney,flintstones):
#    assert barney not in flintstones
     #assert fred in fred
     assert barney in barney
     #assert wilma in flintstones  

def test_soup(wilma,fred,barney,flintstones):
#    assert barney not in flintstones
     assert barney in barney
     assert wilma in wilma
     assert wilma in flintstones  