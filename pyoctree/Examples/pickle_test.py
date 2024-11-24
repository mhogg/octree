import pickle

import numpy as np
from pyoctree import pyoctree

vertices = np.array(((0, 0, 0), (1, 1, 1), (2, 0, 0)), dtype=float)
polygons = np.array(((0, 1, 2),), dtype=int)

tree = pyoctree.PyOctree(vertices, polygons)

tree_data = pickle.dumps(tree)
tree_new = pickle.loads(tree_data)
