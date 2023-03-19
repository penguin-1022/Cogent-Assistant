# -*- coding: UTF-8 -*-

from enum import Enum

class Prob(Enum):
    '''
        定义成枚举类，方便进行比较
    '''
    LS = 0
    BL = 1
    L = 2
    ML = 3
    VL = 4
    AC = 5
    C = 6

    # 自定义比较方法
    def __lt__(self, other) -> bool:
        if self.value < other.value:
            return True
        else :
            return False
    
    def __gt__(self, other) -> bool:
        if self.value > other.value :
            return True
        else :
            return False

    def __eq__(self, other) -> bool:
        if self.value == other.value :
            return True
        else :
            return False

    def __le__(self, other) -> bool:
        if self.value <= other.value :
            return True
        else :
            return False
    
    def __ge__(self, other) -> bool:
        if self.value >= other.value :
            return True
        else :
            return False
        
    def __add__(self, other) :
        pass

    def __sub__(self, other) :
        '''
            两个Prob相减。该函数用于balance函数的实现，不用于其它方法
        '''
        if self.value - other.value == 1 :
            return Prob.BL
        elif self.value - other.value == 2 :
            return Prob.L
        elif self.value - other.value == 3 :
            return Prob.ML
        elif self.value - other.value == 4 :
            return Prob.VL
        elif self.value - other.value == 5 :
            return Prob.AC
        elif self.value - other.value == 0 :
            return Prob.LS
        elif self.value - other.value == 6 :
            return Prob.C
        
if __name__ == '__main__' :
    # print(max(Prob.C, Prob.BL))
    print(Prob.C-Prob.AC)