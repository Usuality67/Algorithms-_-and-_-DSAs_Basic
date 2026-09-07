class Node:
    """
    PRIVATE Data: INTEGER
    PRIVATE LeftPointer,RightPointer: INTEGER
    """
    def __init__(self,Data1):
        self.__Data = Data1
        self.__LeftPointer,self.__RightPointer = -1,-1
    def GetLeft(self):
        return self.__LeftPointer
    def GetRight(self):
        return self.__RightPointer
    def GetData(self):
        return self.__Data
    def SetLeft(self,Left):
        self.__LeftPointer = Left
    def SetRight(self,Right):
        self.__RightPointer = Right
    def SetData(self,Value):
        self.__Data = Value
class Tree:
    """
    PRIVATE Tree: ARRAY[0:19] OF Node
    PRIVATE FirstNode,NumberNodes: INTEGER
    """
    def __init__(self):
        self.__FirstNode,self.__NumberNodes = -1,0
        self.__Tree = [Node(-1) for x in range(20)]
    def InsertNode(self,NewNode):
        if self.__FirstNode == -1:
            self.__Tree[self.__NumberNodes] = NewNode
            self.__FirstNode = 0
        else:
            self.__Tree[self.__NumberNodes] = NewNode

            Current = self.__FirstNode


            if self.__Tree[Current].GetData() > NewNode.GetData():

                Prev = Current
                Current = self.__Tree[Current].GetLeft()
                if Current == -1:
                    self.__Tree[Prev].SetLeft(self.__NumberNodes)
                else:
                    Flag = False
                    while Current != -1:
                        Flag = False
                        Prev = Current
                        if self.__Tree[Current].GetData() > NewNode.GetData():
                            Current = self.__Tree[Current].GetLeft()
                            Flag = True
                        else:
                            Current = self.__Tree[Current].GetRight()
                    if Flag:
                        self.__Tree[Prev].SetLeft(self.__NumberNodes)
                    else:
                        self.__Tree[Prev].SetRight(self.__NumberNodes)
            else:
                Prev = Current
                Current = self.__Tree[Current].GetRight()
                if Current == -1:
                    self.__Tree[Prev].SetRight(self.__NumberNodes)
                else:
                    Flag = False
                    while Current != -1:
                        Flag = False
                        Prev = Current
                        if self.__Tree[Current].GetData() > NewNode.GetData():
                            Current = self.__Tree[Current].GetLeft()
                            Flag = True
                        else:
                            Current = self.__Tree[Current].GetRight()
                    if Flag:
                        self.__Tree[Prev].SetLeft(self.__NumberNodes)
                    else:
                        self.__Tree[Prev].SetRight(self.__NumberNodes)
        self.__NumberNodes += 1
    def OutputTree(self):
        if self.__FirstNode == -1:
            print("No Nodes.")
        else:
            for x in range(self.__NumberNodes):
                print(f"{self.__Tree[x].GetLeft()},{self.__Tree[x].GetData()},{self.__Tree[x].GetRight()}")


TheTree = Tree()
TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(11))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(1))
TheTree.InsertNode(Node(20))
TheTree.InsertNode(Node(7))
TheTree.InsertNode(Node(15))
TheTree.OutputTree()