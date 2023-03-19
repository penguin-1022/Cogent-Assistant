# -*- coding: UTF-8 -*-
from Prob import Prob

class Probability:
    '''
        概率类，基于Prob枚举类型建立。
    '''
    # p为模糊概率，通过传给构造函数的数值或模糊概率词来建立
    _p = Prob.LS
    '''
        Baconian概率与Fuzzy概率结合得到的组合概率模型
        Certain(C)
        Almost Certain(AC)
        Very Likely(VL)
        More than Likely(ML)
        Likely(L)
        Barely Likely(BL)
        Lacking Support(LS)
    '''
    _combineProbability = ['LS','BL','L','ML','VL','AC','C']
    def __init__(self, p) -> None:
        '''
            p可以接收数值或者模糊概率词
        '''
        if isinstance(p, float) :
            if p < 0.0 or p > 1.0:
                raise(ValueError("数值错误：参数范围不正确！"))
            else :
                if p == 1.0 :
                    self._p = Prob.C
                elif p >= 0.95 and p <= 0.99 :
                    self._p = Prob.AC
                elif p >= 0.8 and p < 0.95 :
                    self._p = Prob.VL
                elif p >= 0.7 and p < 0.8 :
                    self._p = Prob.ML
                elif p >= 0.55 and p < 0.7 :
                    self._p = Prob.L
                elif p >= 0.5 and p < 0.55 :
                    self._p = Prob.BL
                else :
                    self._p = Prob.LS
        elif isinstance(p, int) :
            if p == 0 :
                self._p = Prob.LS
            elif p == 1 :
                self._p = Prob.C
            else :
                raise(ValueError("数值错误：输入的概率值不在范围内！"))
        elif isinstance(p, str) :
            if (p in self._combineProbability) :
                if p == 'C' :
                    self._p = Prob.C
                elif p == 'AC' :
                    self._p = Prob.AC
                elif p == 'VL' :
                    self._p = Prob.VL
                elif p == 'ML' :
                    self._p = Prob.ML
                elif p == 'L' :
                    self._p = Prob.L
                elif p == 'BL' :
                    self._p = Prob.BL
                else:
                    self._p = Prob.LS
            else :
                raise(ValueError("数值错误：传递的模糊概率词不合法！"))
        elif isinstance(p, Prob) :
            self._p = p
        else:
            raise(TypeError("类型错误：Probability构造函数接收数值、百分数或模糊概率词"))

    def getProbability(self) -> None:
        return self._p
    
    def __lt__(self, other) -> bool:
        if self._p < other._p:
            return True
        else :
            return False
    
    def __gt__(self, other) -> bool:
        if self._p > other._p:
            return True
        else :
            return False

    def __eq__(self, other) -> bool:
        if self._p == other._p:
            return True
        else :
            return False

    def __le__(self, other) -> bool:
        if self._p <= other._p:
            return True
        else :
            return False
    
    def __ge__(self, other) -> bool:
        if self._p >= other._p:
            return True
        else :
            return False
        
    def __sub__(self, other) :
        return self._p - other._p


if __name__ == '__main__':
    # p = Probability(1)
    # print(p.getProbability())
    print(Prob.LS < Prob.ML)