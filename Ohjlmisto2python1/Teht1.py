import numpy as np

# Task 1
toDeg = [2.493, 0.911]
for rad in toDeg:
    print(np.radians(rad))

# Task 2
toRad = [137.7, 62.3]
for deg in toRad:
    print(np.degrees(deg))

# Task 3
toRadList = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
for deg in toRadList:
    print(f'deg: {deg} rad: {np.radians(deg)}')
