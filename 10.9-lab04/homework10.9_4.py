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

class BinaryTree:
    def __init__(self,data=None,left=None,right=None): # 如果创建节点对象时left或right参数为空，则默认该节点没有左或右子树
        self.data=data
        self.left=left
        self.right=right
    # def preorder(self): # 前序遍历
    #     print(self.data,end=' ')
    #     if self.left != None:
    #         self.left.preorder()
    #     if self.right != None:
    #         self.right.preorder()
    # def midorder(self): # 中序遍历
    #     if self.left != None:
    #         self.left.midorder()
    #     print(self.data,end=' ')
    #     if self.right != None:
    #         self.right.midorder()
    # def postorder(self): # 后序遍历
    #     if self.left != None:
    #         self.left.preorder()
    #     if self.right != None:
    #         self.right.preorder()
    #     print(self.data,end=' ')
    def FloorOrder(root):  #层序遍历
        if not root:
            return
        q = Queue()   #建立队列
        q.push(root)  #根节点入队
        while q.size() > 0:
            node = q.Qpop()   #创建节点
            print(node.data,end=' ')
            if node.left:  #左孩子入队
                q.push(node.left)
            if node.right:  #右孩子入队
                q.push(node.right)
    def leaf(self):
        if self.left != None:    #递归找到叶节点
            self.left.leaf()
        if self.right != None:
            self.right.leaf()
        if self.left == None and self.right == None:  #判断是叶节点后输出
            print(self.data,end = ' ')
        
    def height(self):
        if self.data is None: # 空的树高度为0, 只有root节点的树高度为1
            return 0
        elif self.left is None and self.right is None:
            return 1
        elif self.left is None and self.right is not None:
            return 1 + self.right.height()
        elif self.left is not None and self.right is None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())

layer3_2 = BinaryTree(2,BinaryTree(7),BinaryTree(4))   #建立树
layer2_5 = BinaryTree(5,BinaryTree(6),layer3_2)
layer2_1 = BinaryTree(1,BinaryTree(0),BinaryTree(8))
layer1_3 = BinaryTree(3,layer2_5,layer2_1)

layer1_3.FloorOrder()
layer1_3.leaf()