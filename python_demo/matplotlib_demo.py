import matplotlib.pyplot as plt

# Sample 1: Basic Plot
month1 = [1,3,4,7,8]
month2 = [1,2,6,7,9]
revenue1 = [10000,15000,12000,30000,50000]
revenue2 = [5000,18000,10000,25000,41000]
plt.plot(month1, revenue1, label="WeiYen")
plt.plot(month2, revenue2, label="Tom")
plt.xlabel("month")
plt.ylabel("revenue")
plt.legend()
plt.title("sample")
plt.show()

# Sample 2: Set Axis
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "ro")
# plt.axis([0, 5, 0, 20])
# plt.show()

# Sample 3: plot with numpy
# t = list(range(1, 100, 2))
# plt.plot(t, t, "r--")
import numpy as np

t = np.arange(0, 5, 0.2)
plt.plot(t, t, "r--", t, t**2, "bs", t, t**3, "g^")
plt.show()
