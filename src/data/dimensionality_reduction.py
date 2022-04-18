import numpy as np
import random as rd


def cur(A: np.ndarray, n: int, seed: int) -> np.ndarray:
    """
    CUR decomposition
    """
    # set random seed
    rd.seed(seed)

    # calculate the mean of each column
    A_sq = np.square(A)
    sum_A_sq = np.sum(A_sq)
    sum_A_sq_0 = np.sum(A_sq, axis=0)
    sum_A_sq_1 = np.sum(A_sq, axis=1)

    # get the probability of each column
    P_x_c = sum_A_sq_0 / sum_A_sq
    P_x_r = sum_A_sq_1 / sum_A_sq

    r, c = A.shape

    # generate indices
    c_index = [np.random.choice(np.arange(0, c), p=P_x_c) for i in range(n)]
    r_index = [np.random.choice(np.arange(0, r), p=P_x_r) for i in range(n)]

    C = A[:, c_index]
    R = A[r_index, :]
    W = C[r_index]

    # calcualte U
    X, sigma, Y = np.linalg.svd(W, n)
    for i in range(len(sigma)):
        if sigma[i] == 0:
            continue
        else:
            sigma[i] = 1 / sigma[i]
    sigma = np.diag(sigma)
    U = np.dot(np.dot(Y, sigma), X.T)

    return C, U, R
