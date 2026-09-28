# unit test
def addtion(a,b):
    return a+b
# testing function 
# 1 function means 1 test
def test_addtion():
    assert addtion(10,20) == 30
    assert addtion(-10,10) == 0
    assert addtion(-10,-50) == -60

# Advance testing
# if we are using test_ befoe the func name then that func is testing func
 
def test_addition2():
    assert addtion(0,0) == 0
    assert addtion(0,100) == 100
    assert addtion(1000000,2000000) == 3000000
    assert addtion(3.4,4.3) == 7.699999999999999


    
    