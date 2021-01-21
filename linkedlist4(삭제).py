# 링크드 리스트의 복잡한 기능 2 (특정데이터 삭제)

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next = next

class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data)

    def add(self,data):
        if self.head == "":
            self.head =Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self,data):
        if self.head =="":
            print("해당 값을 가진 노드가 없습니다.")
            return
        
        if self.head == data: # head를 삭제하는 경우
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data==data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                else:
                    node = node.next

#test
linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

linkedlist1.delete(0)

linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

for data in range(1,10):
    linkedlist1.add(data)
linkedlist1.desc()

linkedlist1.delete(4)

linkedlist1.desc()
