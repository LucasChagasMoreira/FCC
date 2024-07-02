import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    array_1d = np.array(list)
    matrix3x3 = array_1d.reshape(3,3)    

    calculations= {
        "mean": [
            np.mean(matrix3x3, axis=0).tolist(),
            np.mean(matrix3x3, axis=1).tolist(),
            np.mean(matrix3x3.flatten().tolist())
        ],
        "variance": [
            np.var(matrix3x3, axis=0).tolist(),
            np.var(matrix3x3, axis=1).tolist(),
            np.var(matrix3x3.flatten().tolist())
        ],
        "standard deviation": [
            np.std(matrix3x3, axis=0).tolist(),
            np.std(matrix3x3, axis=1).tolist(),
            np.std(matrix3x3.flatten().tolist())
        ],
        "max": [
            np.max(matrix3x3, axis=0).tolist(),
            np.max(matrix3x3, axis=1).tolist(),
            np.max(matrix3x3.flatten().tolist())
        ],
        "min": [
            np.min(matrix3x3, axis=0).tolist(),
            np.min(matrix3x3, axis=1).tolist(),
            np.min(matrix3x3.flatten().tolist())
        ],
        "sum": [
            np.sum(matrix3x3, axis=0).tolist(),
            np.sum(matrix3x3, axis=1).tolist(),
            np.sum(matrix3x3.flatten().tolist())
        ]

    }

    return calculations

print(calculate([0,1,2,3,4,5,6,7,8,]))