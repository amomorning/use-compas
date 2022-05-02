coords = [
      -50, 0, 0,
      50, 0, 0,
      50, 0, 100,
      200, 0, 100,
      200, 0, 300,
      -50, 0, 300,
      -50, 100, 0,
      50, 100, 0,
      50, 100, 100,
      200, 100, 100,
      200, 100, 300,
      -50, 100, 300
    ]

index = [
      0, 1, 2, 3, 4, 5,
      11, 10, 9, 8, 7, 6,
      6, 7, 1, 0,
      2, 1, 7, 8,
      8, 9, 3, 2,
      9, 10, 4, 3,
      5, 4, 10, 11,
      0, 5, 11, 6
    ]

size= [6, 4]
count= [2, 6]

from compas.datastructures import Mesh

mesh = Mesh()
pts = []
for i in range(0, len(coords), 3):
    x, y, z = coords[i], coords[i+1], coords[i+2]
    pts.append(mesh.add_vertex(x=x, y=y, z=z))

cur = 0
for k in range(len(size)):
    sz = size[k]
    cnt = count[k]
    for i in range(cnt):
        tmp = []
        for j in range(sz):
            idx = index[cur + i*sz + j]
            tmp.append(pts[idx]) 
        mesh.add_face(tmp)
    cur += cnt * sz


vts = list(mesh.vertices())

print(vts)


neighbor = mesh.vertex_neighbors(vts[0])

print(vts[0], 'neighbor:', list(neighbor))
    
