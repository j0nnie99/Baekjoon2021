class Calculator:
    def __init__(self):
        self.x = 0

    def add(self, val):
        self.x += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.x += val
        if self.x > 100:
            self.x = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.x)