print(__name__)
class Woman:
    def __init__(self,weight,height,iq):
        self.weight =  weight
        self.height = height
        self.iq = iq
    def eat(self):
        self.weight = self.weight + 10
    def study(self):
        self.iq = self.iq + 10
    def sleep(self):
        self.height = self.height + 10
    def show(self):
        print("키, 몸무게, iq는 ",self.height,' ',self.weight,' ',self.iq,"입니다.")
# 5월20일 수정