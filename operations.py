class Operation():
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(self.a,self.b)
    def add(self):
        return str(self.a+self.b)
    def sub(self):
        return str(self.a-self.b)
    def div(self):
        return str(self.a%self.b)
    def mul(self):
        return str(self.a*self.b)
