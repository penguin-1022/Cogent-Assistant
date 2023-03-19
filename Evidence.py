# -*- coding: UTF-8 -*-
from Probability import Probability

class Evidence:
    '''
        证据类
    '''
    _content = ""                      # 证据文本内容
    _credibility = Probability(0)      # 可信度
    _relevance = Probability(0)        # 相关性
    _inferentialForce = Probability(min(_credibility.getProbability(), _relevance.getProbability())) # 推断力

    # def __init__(self, credibility, relevance, inferentialForce) -> None:
    #     self._credibility = Probability(credibility)
    #     self._relevance = Probability(relevance)
    #     self._inferentialForce = Probability(inferentialForce)
    
    def __init__(self, content, *args) -> None:
        '''
            content接收一个str类型，表示证据的文本内容。
            args为可变参数，如果只传入一个，那么将设置可信度（credibility）。
            如果传入两个，那么将先后分别设置可信度（credibility）和相关度（relevance）。
        '''
        if not isinstance(content, str) :
            raise(TypeError("类型错误：证据内容需要为字符串！"))
        else :
            self._content = content
        if len(args) == 1 :
            self._credibility = Probability(args[0])
        elif len(args) == 2 :
            self._credibility = Probability(args[0])
            self._relevance = Probability(args[1])
            self._inferentialForce = Probability(min(self._credibility.getProbability(), self._relevance.getProbability()))

    def getCredibility(self) -> Probability:
        '''
            返回可信度，返回类型为模糊概率值
        '''
        return self._credibility.getProbability()
    
    def getRelevance(self) -> Probability:
        '''
            返回相关度，返回类型为模糊概率值
        '''
        return self._relevance.getProbability()
    
    def getInferentialForce(self) -> Probability:
        '''
            返回推断力，返回类型为模糊概率值
        '''
        return self._inferentialForce.getProbability()
    
    def setCredibility(self, credibility) -> None:
        self._credibility = Probability(credibility)

    def setRelevance(self, relevance) -> None:
        self._relevance = Probability(relevance)
    
    def setInferentialForce(self) -> None:
        '''
            根据已有的可信度和相关度来计算推断力
        '''
        self._inferentialForce = Probability(min(self._credibility.getProbability(), self._relevance.getProbability()))
    
    def __eq__(self, other) -> bool:
        if self._inferentialForce == other._inferentialForce :
            return True
        else :
            return False
    
    def __le__(self, other) -> bool:
        if self._inferentialForce <= other._inferentialForce :
            return True
        else :
            return False
    
    def __ge__(self, other) -> bool:
        if self._inferentialForce >= other._inferentialForce :
            return True
        else :
            return False
    
    def __lt__(self, other) -> bool:
        if self._inferentialForce < other._inferentialForce :
            return True
        else :
            return False
    
    def __gt__(self, other) -> bool:
        if self._inferentialForce > other._inferentialForce :
            return True
        else :
            return False
        
    def __sub__(self, other) -> bool:
        return self._inferentialForce - other._inferentialForce
    
if __name__ == '__main__' :
    obj = Evidence("The news reported that...",1)
    # obj.setRelevance('BL')
    # print(obj.getCredibility())
    # print(obj.getRelevance())
    # obj.setInferentialForce()
    # print(obj.getInferentialForce())