
def lagrange_method(data, testdata):
    """
    parameters:
    data: list of tuples, each tuple contains [x, y] coordinates
    testdata : target x coordinate (float)
    """
    predict = 0
    data_x = [data[i][0] for i in range(len(data))]
    data_y = [data[i][1] for i in range(len(data))]

    if testdata in data_x:
        return data_y[data_x.index(testdata)]

    for i in range(len(data_x)):
        af = 1
        for j in range(len(data_x)):
            if j != i:
                af *= (testdata - data_x[j]) / (data_x[i] - data_x[j])
        predict += af * data_y[i]

    return predict

def linear_method(data, testdata):
    """
    parameters:
    data: list of tuples, each tuple contains [x, y] coordinates
    testdata : target x coordinate (float)
    """
    data_x = [data[i][0] for i in range(len(data))]
    data_y = [data[i][1] for i in range(len(data))]

    if testdata in data_x:
        return data_y[data_x.index(testdata)]

    for i in range(len(data_x) - 1):
        if data_x[i] <= testdata <= data_x[i + 1]:
            break

    slope = (data_y[i + 1] - data_y[i]) / (data_x[i + 1] - data_x[i])
    predict = slope * (testdata - data_x[i]) + data_y[i]

    return predict

def spline_method(data, testdata):
    """
    parameters:
    data: list of tuples, each tuple contains [x, y] coordinates
    testdata: target x coordinate (float)
    """
    x = [point[0] for point in data]
    y = [point[1] for point in data]
    n = len(x)
    h = [x[i + 1] - x[i] for i in range(n - 1)]

    # 构建系数矩阵A和向量b
    A = [[0] * n for _ in range(n)]
    b = [0] * n
    A[0][0] = 1
    A[n - 1][n - 1] = 1
    for i in range(1, n - 1):
        A[i][i - 1] = h[i - 1]
        A[i][i] = 2 * (h[i - 1] + h[i])
        A[i][i + 1] = h[i]
        b[i] = 6 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])

    # 解三对角线性方程组，得到二阶导数M
    M = [0] * n
    alpha = [0] * (n - 1)
    beta = [0] * (n - 1)
    alpha[0] = -A[0][1] / A[0][0]
    beta[0] = b[0] / A[0][0]
    for i in range(1, n - 1):
        alpha[i] = -A[i][i + 1] / (A[i][i] + A[i][i - 1] * alpha[i - 1])
        beta[i] = (b[i] - A[i][i - 1] * beta[i - 1]) / (A[i][i] + A[i][i - 1] * alpha[i - 1])
    M[n - 1] = (b[n - 1] - A[n - 1][n - 2] * beta[n - 2]) / (A[n - 1][n - 1] + A[n - 1][n - 2] * alpha[n - 2])
    for i in range(n - 2, -1, -1):
        M[i] = alpha[i] * M[i + 1] + beta[i]

    # 进行插值计算
    for i in range(n - 1):
        if x[i] <= testdata <= x[i + 1]:
            t = (testdata - x[i]) / h[i]
            s = (1 - t) * y[i] + t * y[i + 1] + ((1 - t) ** 3 - (1 - t)) * (h[i] ** 2) * M[i] / 6 + (t ** 3 - t) * (h[i] ** 2) * M[i + 1] / 6
            return s

    # 如果 testdata 不在插值范围内，可以选择抛出异常或返回None
    return None
