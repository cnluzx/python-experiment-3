from matplotlib import pyplot as plt    

def lagrange(data,testdata):
    predict=0
    data_x=[data[i][0] for i in range(len(data))]
    data_y=[data[i][1] for i in range(len(data))]
    if testdata[0] in data_x:
        return data_y[data_x.index(testdata[0])]
    for i in range(len(data_x)):
        af=1
        for j in range(len(data_x)):
            if j!=i:
                af*=(testdata[0]-data_x[j])/(data_x[i]-data_x[j])
            predict+=af*data_y[i]
    return predict  