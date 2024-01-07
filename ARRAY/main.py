'''array tutorial starting from 7/1/2024 welcome to DSA with python''' 
class ArrayProblem:
    def __init__(self):
        self.arr = []
        self.size = 0
    def insert(self, value):
        self.arr.append(value)
        self.size += 1

    def display(self):
        print(self.arr)

    def delete(self, index):
        del self.arr[index]
        self.size -= 1

    def update(self, index, value):
        self.arr[index] = value

arr = ArrayProblem()
arr.insert(10)
arr.insert(20)
arr.insert(30)
arr.display()
arr.delete(1)
arr.display()
arr.update(0, 100)
arr.display()