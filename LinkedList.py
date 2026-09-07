
class Node:
    """
    DECLARE data: INTEGER
    DECLARE nextNode: INTEGER
    """
    def __init__(self,data1,nextNode1):
        self.data = data1
        self.nextNode = nextNode1

LinkedList = [Node(1,1), Node(5,4), Node(6,7), Node(7,-1), Node(2,2), Node(0,6),Node(0,8),Node(56,3),Node(0,9),Node(0,-1)]
startPointer = 0
emptyList = 5

def OutputNode(Arr,start):
    CurrentPointer = start
    while CurrentPointer != -1:
        print(Arr[CurrentPointer].data)
        CurrentPointer = Arr[CurrentPointer].nextNode

def AddNode():
    global emptyList,LinkedList
    if emptyList == -1:
        return False
    value = int(input("Data: "))
    LinkedList[emptyList] = Node(value,-1)
    CurrentPointer = startPointer
    PrevPointer = 0
    while CurrentPointer != -1:
        PrevPointer = CurrentPointer
        CurrentPointer = LinkedList[CurrentPointer].nextNode
    LinkedList[PrevPointer].nextNode = emptyList
    emptyList = LinkedList[emptyList].nextNode


    return True

OutputNode(LinkedList,startPointer)
if not AddNode():
    print("The linked list is full.")
else:
    print("Item Added")
OutputNode(LinkedList,startPointer)