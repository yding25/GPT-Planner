import numpy as np

for repeat in range(100):
    p_file = np.array([0.8, 0.2])
    index = np.random.choice(list(range(0, 2)), p=p_file)
    print(index)