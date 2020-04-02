from numpy import load
import numpy as np

# Pre-captured Contours

h_cnt = np.array([[1, 0],
                  [0, 1],
                  [17, 0],
                  [19, 1],
                  [19, 39],
                  [80, 39],
                  [80, 1],
                  [82, 0],
                  [96, 0],
                  [98, 1],
                  [98, 96],
                  [96, 98],
                  [82, 98],
                  [80, 96],
                  [80, 53],
                  [19, 53],
                  [19, 96],
                  [17, 98],
                  [1, 98],
                  [0, 96]])
h_cnt = h_cnt.reshape((h_cnt.shape[0], 1, h_cnt.shape[1]))

s_cnt = np.array([[34, 1],
                  [36, 0],
                  [63, 0],
                  [65, 1],
                  [71, 1],
                  [73, 3],
                  [75, 3],
                  [76, 5],
                  [78, 5],
                  [80, 7],
                  [82, 7],
                  [90, 15],
                  [90, 16],
                  [92, 18],
                  [92, 20],
                  [94, 22],
                  [94, 28],
                  [92, 30],
                  [76, 30],
                  [75, 28],
                  [75, 24],
                  [73, 22],
                  [73, 20],
                  [69, 16],
                  [67, 16],
                  [65, 15],
                  [61, 15],
                  [59, 13],
                  [38, 13],
                  [36, 15],
                  [32, 15],
                  [30, 16],
                  [28, 16],
                  [23, 22],
                  [23, 30],
                  [26, 33],
                  [28, 33],
                  [30, 35],
                  [34, 35],
                  [36, 37],
                  [42, 37],
                  [44, 39],
                  [55, 39],
                  [57, 41],
                  [63, 41],
                  [65, 43],
                  [73, 43],
                  [75, 45],
                  [78, 45],
                  [80, 47],
                  [82, 47],
                  [86, 50],
                  [88, 50],
                  [94, 56],
                  [94, 58],
                  [96, 60],
                  [96, 62],
                  [98, 64],
                  [98, 73],
                  [96, 75],
                  [96, 77],
                  [94, 79],
                  [94, 81],
                  [84, 90],
                  [82, 90],
                  [80, 92],
                  [78, 92],
                  [76, 94],
                  [75, 94],
                  [73, 96],
                  [67, 96],
                  [65, 98],
                  [36, 98],
                  [34, 96],
                  [28, 96],
                  [26, 94],
                  [23, 94],
                  [21, 92],
                  [19, 92],
                  [17, 90],
                  [15, 90],
                  [3, 79],
                  [3, 77],
                  [1, 75],
                  [1, 71],
                  [0, 69],
                  [0, 67],
                  [3, 64],
                  [15, 64],
                  [19, 67],
                  [19, 71],
                  [21, 73],
                  [21, 75],
                  [23, 77],
                  [25, 77],
                  [28, 81],
                  [32, 81],
                  [34, 83],
                  [38, 83],
                  [40, 84],
                  [61, 84],
                  [63, 83],
                  [67, 83],
                  [69, 81],
                  [73, 81],
                  [78, 75],
                  [78, 66],
                  [73, 60],
                  [71, 60],
                  [69, 58],
                  [65, 58],
                  [63, 56],
                  [55, 56],
                  [53, 54],
                  [46, 54],
                  [44, 52],
                  [36, 52],
                  [34, 50],
                  [28, 50],
                  [26, 49],
                  [23, 49],
                  [21, 47],
                  [19, 47],
                  [17, 45],
                  [15, 45],
                  [7, 37],
                  [7, 35],
                  [5, 33],
                  [5, 20],
                  [7, 18],
                  [7, 16],
                  [19, 5],
                  [21, 5],
                  [23, 3],
                  [26, 3],
                  [28, 1]])
s_cnt = s_cnt.reshape((s_cnt.shape[0], 1, s_cnt.shape[1]))

u_cnt = np.array([[0, 1],
                  [1, 0],
                  [16, 0],
                  [18, 1],
                  [18, 66],
                  [19, 68],
                  [19, 72],
                  [21, 74],
                  [21, 75],
                  [25, 80],
                  [27, 80],
                  [28, 81],
                  [30, 81],
                  [31, 83],
                  [33, 83],
                  [34, 84],
                  [39, 84],
                  [40, 86],
                  [57, 86],
                  [59, 84],
                  [65, 84],
                  [66, 83],
                  [68, 83],
                  [69, 81],
                  [71, 81],
                  [77, 75],
                  [77, 74],
                  [78, 72],
                  [78, 71],
                  [80, 69],
                  [80, 57],
                  [81, 56],
                  [81, 1],
                  [83, 0],
                  [96, 0],
                  [98, 1],
                  [98, 69],
                  [96, 71],
                  [96, 75],
                  [95, 77],
                  [95, 78],
                  [92, 81],
                  [92, 83],
                  [84, 90],
                  [83, 90],
                  [81, 92],
                  [80, 92],
                  [78, 93],
                  [77, 93],
                  [75, 95],
                  [72, 95],
                  [71, 96],
                  [66, 96],
                  [65, 98],
                  [34, 98],
                  [33, 96],
                  [27, 96],
                  [25, 95],
                  [22, 95],
                  [21, 93],
                  [19, 93],
                  [18, 92],
                  [16, 92],
                  [13, 89],
                  [12, 89],
                  [7, 84],
                  [7, 83],
                  [4, 80],
                  [4, 78],
                  [3, 77],
                  [3, 74],
                  [1, 72],
                  [1, 68],
                  [0, 66], ]
                 )
u_cnt = u_cnt.reshape((u_cnt.shape[0], 1, u_cnt.shape[1]))
# Test Data location
img_dir = '../test data'

# Open cv threshold values for making a binary from gray scaled picture
cv_lower_thr = 80
cv_upper_thr = 255

# Height and Width of scaled Contour
scaled_cnt_coef = 100

# Minimum and Maximum area for a letter Contour
area_lower_bound = 200
area_upper_bound = 2000

""" 
Matching Algorithm l3 in cvMatchModes
For more information visit:
https://docs.opencv.org/master/d3/dc0/group__imgproc__shape.html#gaf2b97a230b51856d09a2d934b78c015f
"""
match_alg = 3
# Matching Threshold
match_thr = 1.5

# Debug mode flag
verbose = True
