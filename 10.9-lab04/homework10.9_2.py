class Queue():
    def __init__(self):
        self.items = []
    
    def size(self):   # 返回队列长度
        return len(self.items)
    
    def isempty(self): # 返回队列是否为空
        if len(self.items)==0:
            return True
        else:
            return False
    
    def push(self,element): # 加入队列
        self.items.append(element)
    
    def Qpop(self): # 出队
        return  self.items.pop(0)
    
    def peek(self): # 返回队列最前端元素，注意需要处理队列为空的情况
        return self.items[0]

    def bottom(self): #返回队尾元素
        return self.items[self.size()-1]