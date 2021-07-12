import sys
import numpy

VERTICIES_COUNT = 0

numpy.set_printoptions(threshold=sys.maxsize)
grid = numpy.loadtxt("./GEBCO Data/gebco_2020_n51.1962890373543_s50.804077114909894_w1.1266480162739754_e1.8099975921213627.asc", skiprows=6)

num_rows = 94
num_cols = 164

xyz_grid = []

for i in range(num_rows):
    for j in range(num_cols):
        xyz = []
        xyz.append(i)
        xyz.append(j)
        xyz.append((grid[i][j] + 80)/6)
        xyz_grid.append(xyz)
        VERTICIES_COUNT += 1

numpy.savetxt("pointcloud.asc", xyz_grid, delimiter=", ")