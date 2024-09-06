my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
my_dict.update({'1':2})
#print(my_dict)
import queue
MyQueue = queue.Queue()
MyQueue.put(1)
MyQueue.put(2)
MyQueue.put(3)
print(MyQueue.get())
print(MyQueue.qsize())