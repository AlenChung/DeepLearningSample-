from collections import deque

a = deque()

a.append(1)
a.append(2)
a.append(3)

for x in range(1, 8):
    print(x)
print("pop: " + str(a.popleft()))
print(a)