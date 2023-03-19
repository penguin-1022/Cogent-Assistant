# -*- coding: UTF-8 -*-
from Prob import Prob
from Evidence import Evidence
from Probability import Probability

class Hypothesis:
    '''
        假设类
    '''
    _content = ""                  # 假设的文本内容
    _likehood = Prob.LS            # 假设成立的最终概率
    _isSimpleHypothesis = True     # 是否为简单假设

    # _favoringEvidences = []        # 支持的证据
    # _disfavoringEvidences = []     # 不支持的证据
    _favoring = Prob.LS            # 所有支持假设的概率
    _disfavoring = Prob.LS         # 所有不支持假设的概率

    # _subFavoringHypothesis = []    # 全部有利子假设
    # _subDisfavoringHypothesis = [] # 全部不利子假设
    _logic = 'AND'                 # 逻辑参数
    _logicRelevance = Prob.C      # 逻辑参数相关性

    def __init__(self, content, isSimple = True, logic = 'AND', logicRelevance = Prob.C) -> None:
        '''
            默认生成简单假设。
            content为假设的文本内容
            若为复杂假设，则isSimple需要赋值False
            logic为逻辑参数（复杂假设用到）
            logicRelevance为逻辑参数相关性（复杂假设用到）
        '''
        self._content = content
        self._isSimpleHypothesis = isSimple
        self._logic = logic
        self._logicRelevance = logicRelevance
        self._favoringEvidences = []        # 支持的证据
        self._disfavoringEvidences = []     # 不支持的证据
        self._subFavoringHypothesis = []    # 全部有利子假设
        self._subDisfavoringHypothesis = [] # 全部不利子假设
    
    def reason(self) :
        '''
            根据所有的支持假设和不支持假设来推导该假设的可能性
        '''

        if self._isSimpleHypothesis == True : # 简单假设的情况
            # 如果既有有利假设，也有不利假设
            if len(self._favoringEvidences) >= 1 and len(self._disfavoringEvidences) >= 1 :
                self._favoring = max(self._favoringEvidences) # 返回的其实是一个Evidence类，比较是根据实例的推断力比较
                self._disfavoring = max(self._disfavoringEvidences) # 返回的其实是一个Evidence类，比较是根据实例的推断力比较
                if self._disfavoring >= self._favoring : # 
                    self._likehood = Prob.LS
                else : # 支持假设的概率严格大于不支持假设的概率
                    # print(self._favoring.getInferentialForce())
                    # print(self._disfavoring.getInferentialForce())
                    self._likehood = self._favoring - self._disfavoring
                return self._likehood
            elif len(self._favoringEvidences) >= 1 : # 只有有利假设
                self._likehood = max(self._favoringEvidences).getInferentialForce()
                return self._likehood
            else : # 只有不利假设
                self._likehood = max(self._disfavoringEvidences).getInferentialForce()
                return self._likehood
        
        else : # 复杂假设时
            if self._logic == 'AND' : 
                if len(self._subFavoringHypothesis) >= 1 and len(self._subDisfavoringHypothesis) >= 1:
                    favoringProbability = max(self._subFavoringHypothesis)
                    disfavoringProbability = max(self._subDisfavoringHypothesis)
                    if disfavoringProbability >= favoringProbability :
                        combineProbability = Prob.LS
                    else :
                        combineProbability = favoringProbability - disfavoringProbability
                    # 取min(逻辑参数相关性，balance函数结果)
                    self._likehood = min(self._logicRelevance, combineProbability)
                elif len(self._subFavoringHypothesis) >= 1 : # 只有有利假设
                    favoringProbability = min(self._subFavoringHypothesis)._likehood
                    # 取min(逻辑参数相关性，所有概率最小值)
                    self._likehood = min(favoringProbability, self._logicRelevance)
                else : # 只有不利假设
                    disfavoringProbability = min(self._subDisfavoringHypothesis)._likehood
                    # 取min(逻辑参数相关性，所有概率最小值)
                    self._likehood = min(disfavoringProbability, self._logicRelevance)
                return self._likehood
                
            elif self._logic == 'OR' :
                # 存在有利子假设，也有不利子假设
                if len(self._subFavoringHypothesis) >= 1 and len(self._subDisfavoringHypothesis) >= 1:
                    favoringProbability = max(self._subFavoringHypothesis)
                    disfavoringProbability = max(self._subDisfavoringHypothesis)
                    if disfavoringProbability >= favoringProbability :
                        combineProbability = Prob.LS
                    else :
                        combineProbability = favoringProbability - disfavoringProbability
                    # 取min(逻辑参数相关性，balance函数结果)
                    self._likehood = min(self._logicRelevance, combineProbability)
                elif len(self._subFavoringHypothesis) >= 1 : # 只有有利假设
                    favoringProbability = max(self._subFavoringHypothesis)
                    # 取min(逻辑参数相关性，所有概率最大值)
                    self._likehood = min(favoringProbability, self._logicRelevance)
                else : # 只有不利假设
                    disfavoringProbability = max(self._subDisfavoringHypothesis)
                    # 取min(逻辑参数相关性，所有概率最大值)
                    self._likehood = min(disfavoringProbability, self._logicRelevance)
                return self._likehood
            else :
                raise(TypeError("类型错误：逻辑参数的类型不对！"))
            
    
    def addFavoringEvidence(self, e) -> None:
        if isinstance(e, Evidence) :
            self._favoringEvidences.append(e)
            # print(self._favoringEvidences)
        else :
            raise(TypeError("类型错误：不是Evidence类！"))
    
    def addDisfavoringEvidence(self, e) -> None:
        if isinstance(e, Evidence) :
            self._disfavoringEvidences.append(e)
        else :
            raise(TypeError("类型错误：不是Evidence类！"))
        
    def addSubFavoringHypothesis(self, h) -> None:
        if isinstance(h, Hypothesis) :
            self._subFavoringHypothesis.append(h)
        else:
            raise(TypeError("类型错误：不是Hypothesis类！"))

    def addSubDisfavoringHypothesis(self, h) -> None:
        if isinstance(h, Hypothesis) :
            self._subDisfavoringHypothesis.append(h)
        else:
            raise(TypeError("类型错误：不是Hypothesis类！"))
        
    def __eq__(self, other) -> bool:
        if self._likehood == other._likehood :
            return True
        else :
            return False

    def __le__(self, other) -> bool:
        if self._likehood <= other._likehood :
            return True
        else :
            return False

    def __ge__(self, other) -> bool:
        if self._likehood >= other._likehood :
            return True
        else :
            return False

    def __lt__(self, other) -> bool:
        if self._likehood < other._likehood :
            return True
        else :
            return False

    def __gt__(self, other) -> bool:
        if self._likehood > other._likehood :
            return True
        else :
            return False

    # def test(self) :
    #     print(id(self._favoringEvidences))
    
# if __name__ == '__main__' :
#     h4 = Hypothesis("Demolisher SAM的射程范围为850km。")
#     h5 = Hypothesis("6月24日测试的SAM射程时680km。")
#     e1 = Evidence("Demolisher SAM的最大射程为850km，可以摧毁在1300米到10000米之间高空飞行的目标。M国对SAM规格的可靠性有90%的信心",'VL','C')
#     e2 = Evidence("2017年6月24日，与M国接壤的J国的导弹跟踪雷达站检测到从Tantrum发射的SAM，该地空导弹飞行了大约680公里，并摧毁了飞行在1000米处的目标飞机。",'AC','C')
#     print("证据1的推断力为：",end=' ')
#     print(e1.getInferentialForce())
#     print("证据2的推断力为：",end=' ')
#     print(e2.getInferentialForce())
#     h4.addFavoringEvidence(e1)
#     h5.addFavoringEvidence(e2)
#     # h4.test()
#     # h5.test()
#     print("假设4成立的概率为：",end='')
#     print(h4.reason())
#     print("假设5成立的概率为：",end='')
#     print(h5.reason())

#     h2 = Hypothesis("2017年6月24日测试的SAM射程在Demolisher SAM的射程范围内",False,'AND',Prob.C)
#     h2.addSubFavoringHypothesis(h4)
#     h2.addSubFavoringHypothesis(h5)
#     print("假设2成立的概率为：", end="")
#     print(h2.reason())

#     h6 = Hypothesis("2017年6月24检测到的SAM的射程高度为1000米")
#     h7 = Hypothesis("DemolisherSAM的射程高度在1300米和10000米之间")
#     h6.addFavoringEvidence(e1)
#     h7.addFavoringEvidence(e2)
#     print("假设6成立的概率为：",end='')
#     print(h6.reason()) # 这个地方一开始没推理，导致h3出错了。应该还是涉及到self._likehood的修改
#     print("假设7成立的概率为：",end='')
#     print(h7.reason())
#     h3 = Hypothesis("J国的导弹跟踪雷达站检测到从Tantrum发射的SAM的射程高度与DemolisherSAM的射程高度不一致",False,'AND',Prob.C)
#     h3.addSubFavoringHypothesis(h6)
#     h3.addSubFavoringHypothesis(h7)
#     print("假设3成立的概率为：",end="")
#     print(h3.reason())
#     h1 = Hypothesis("M国向Z国出售Demolisher SAM",False,'AND',Prob.C)
#     h1.addSubFavoringHypothesis(h2)
#     h1.addSubDisfavoringHypothesis(h3)
#     print("假设1成立的概率为：",end="")
#     print(h1.reason())