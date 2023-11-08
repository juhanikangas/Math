import numpy as np

# Task 1
leg1 = 1.6
leg2 = 2.3
hypotenuse = np.sqrt(leg1**2 + leg2**2)
print(hypotenuse)

# Task 2
D = 6.4
ratio = (3, 2)
x = D / np.sqrt(ratio[0]**2 + ratio[1]**2)
W = ratio[0] * x
L = ratio[1] * x

print(f"Width: {W}")
print(f"Length: {L}")
