#raise a custom error
import pytest

class NotInRange(Exception):
    def __init__(self, message="value not in range"):
        self.message = message
        super().__init__(self.message)


def test_generic():
    a= 5
    with pytest.raises(NotInRange):
        if a not in range(10, 20):
            raise NotInRange

#It should be noted that if you want to apply a test to a specific fuction,
#always make sure to add the the first key words to the function

def test_something():
    a = 2
    b = 2
    assert True #Comparison to ensure if True/false



    