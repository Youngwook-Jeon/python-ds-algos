from collections import deque

custom_queue = deque(maxlen=3)
print(custom_queue)
custom_queue.append(1)
custom_queue.append(2)
custom_queue.append(3)
custom_queue.append(4) # deque([2, 3, 4], maxlen=3)
print(custom_queue)
print(custom_queue.popleft())