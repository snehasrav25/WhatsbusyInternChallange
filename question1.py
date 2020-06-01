class MoneyBox:
    def __init__(self, capacity):
        if capacity<=0:
            raise Exception('capacity should be greater than 0')
        
        self.capacity=capacity
        self.size =0
        # Your code here


    def can_add(self, v):
        if self.size+v<=self.capacity:
            return True
        else:
            return False
        # True, if you can add v coins, False otherwise
        # Your code here

    def add(self, v):
        # put v coins to moneybox
        # Your code here
        if self.can_add(v):
            self.size= self.size+v
        else:
            raise Exception('capacity is full cant add  coins')

#working scenario
Example = MoneyBox(10)
print Example.can_add(5)
print Example.add(5)

#initialize with a negitive capacity scenario
Example = MoneyBox(-1)

#cant add more coins than the capacity scenario
Example = MoneyBox(11)
print Example.can_add(5)
print Example.add(5)
print Example.add(3)