def canIcallfizzbuzz():
    fizzbuzz(1)
def checkfizzbuzz(value,expected):
    actual=fizzbuzz(value)
    assert actual==expected
def test_return1with1():
    checkfizzbuzz(1,"1")
def test_return2with2():
    checkfizzbuzz(2,"2")
def test_returnfizz():
    checkfizzbuzz(3,"fizz")
def test_returnbuzz():
    