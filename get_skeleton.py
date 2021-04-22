
from compas_skeleton.datastructure import Skeleton
lines = [
([0.0, 0.0, 0.0], [0.0, 10.0, 0.0]),
([0.0, 0.0, 0.0], [-8.6, -5.0, 0.0]),
([0.0, 0.0, 0.0], [8.6, -5.0, 0.0])
]

skeleton = Skeleton.from_skeleton_lines(lines)
print(skeleton)
