'''
Реализуйте алгоритм, удаляющий узел из середины односвязного списка (то
есть узла, не являющегося ни начальным, ни конечным - не обязательно находящегося
точно в середине). Доступ предоставляется только к этому узлу.
'''
class LinkedList:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next
    def __str__(self):
        return str(self.cargo)

def remove_element(element, x):
    start = element
    for i in range(x):
        buffer = element
        element = element.next
    buffer.next = element.next



element1 = LinkedList(24)
element2 = LinkedList(2)
element3 = LinkedList(17)
element4 = LinkedList(21)
element1.next = element2
element2.next = element3
element3.next = element4

remove_element(element1, 1)
