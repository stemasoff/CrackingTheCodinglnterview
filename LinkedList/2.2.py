'''
Реализуйте алгоритм для нахождения в односвязном списке k-го элемента
с конца.
'''
class LinkedList:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next
    def __str__(self):
        return str(self.cargo)

def search(element, k):
    cnt = 0
    start = element
    while element.next != None:
        element = element.next
        cnt += 1
    element = start
    for i in range(cnt - k):
        element = element.next
    return element

element1 = LinkedList(24)
element2 = LinkedList(2)
element3 = LinkedList(17)
element4 = LinkedList(21)
element1.next = element2
element2.next = element3
element3.next = element4
print(search(element1, 3))