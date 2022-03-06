class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

# 다중상속을 할 경우에는 하나하나 시행해야한다, super x
class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)


# 드랍쉽
dropship = FlyableUnit()

