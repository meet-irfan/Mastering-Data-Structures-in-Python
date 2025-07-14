#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import deque

queue = deque()
queue.append(10)  # Enqueue
queue.append(20)
queue.append(30)

print(queue.popleft())  # Dequeue -> 10
print(queue[0])         # Front -> 20
print(queue[-1])        # Rear -> 30


# In[ ]:




