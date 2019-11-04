from griff4.py101.a.mya import AClass


class BClass:
    def __init__(self):
        print("BClass called", self)

def b_method():
    print("b_method called:", AClass().a_method())
    
