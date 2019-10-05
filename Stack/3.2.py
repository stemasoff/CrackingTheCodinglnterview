'''
Как реализовать стек, в котором кроме стандартных функций push и рор будет
поддерживаться функция min, возвращающая минимальный элемент? Все
операции - push, рор и min - должны выполняться за время 0( 1 ).
'''
class Stack:
    minimum = None
    def __init__(self):
        self.items = []
    def push(self, x):
        self.items.append(x)
        if self.minimum == None:
            self.minimum = x
        elif x < self.minimum:
            self.minimum = x
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return (self.items == [])
    def min(self):
        return self.minimum
s = Stack()
s.push(54)
s.push(45)
s.push(1)
print(s.min())