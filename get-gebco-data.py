import enum
import sys
import numpy
from stl import mesh
from stl.base import Y

VERTICIES_COUNT = 0

numpy.set_printoptions(threshold=sys.maxsize)
grid = numpy.loadtxt("./GEBCO Data/gebco_2020_n51.1962890373543_s50.804077114909894_w1.1266480162739754_e1.8099975921213627.asc", skiprows=6)

num_rows = 94
num_cols = 164

shifted_grid = []

for i in range(num_rows):
    for j in range(num_cols):
        grid[i][j] += 80
        VERTICIES_COUNT += 1

channel_mesh = numpy.meshgrid(VERTICIES_COUNT, dtype=mesh.Mesh.dtype)
channel_mesh = mesh.Mesh(channel_mesh, remove_empty_areas=False)

# The mesh normals (calculated automatically)
channel_mesh.normals
# The mesh vectors
channel_mesh.v0, channel_mesh.v1, channel_mesh.v2
# Accessing individual points (concatenation of v0, v1 and v2 in triplets)
assert (channel_mesh.points[0][0:3] == channel_mesh.v0[0]).all()
assert (channel_mesh.points[0][3:6] == channel_mesh.v1[0]).all()
assert (channel_mesh.points[0][6:9] == channel_mesh.v2[0]).all()
assert (channel_mesh.points[1][0:3] == channel_mesh.v0[1]).all()

channel_mesh.save("channel-mesh.stl")