import numpy as np
n = int(input())
x0, y0 = map(int, input().split())
xh, yh = map(int, input().split())
V = np.array([[xh - x0],
              [yh - y0]])
theta = np.pi * (n - 2) / (n * 2)
R = np.array([[np.cos(theta), np.sin(theta)],
              [-1 * np.sin(theta), np.cos(theta)]])
P0 = np.array([[x0],
               [y0]])
P1 = P0 + (R @ V) * np.cos(theta)
print(P1[0, 0], P1[1, 0])


