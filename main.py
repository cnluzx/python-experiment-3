import method
import numpy as np
import matplotlib.pyplot as plt##绘制插值函数的图形
import multiprocessing

plt.rcParams["font.family"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

x = np.array([-5.0, -4.5, -4.0, -3.5, -3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
y1 = np.array([-0.1923, -0.2118, -0.2353, -0.2642, -0.3, -0.3448, -0.4000, -0.4615, -0.5000, -0.4000, 0, 0.4000, 0.5000, 0.4615, 0.4000, 0.3448, 0.3000, 0.2642, 0.2353, 0.2118, 0.1923])

data = list(zip(x, y1))###压缩成list

predict_x1=-3.75
predict_x2= 0.25

def predict_lagrange():

    predict_y1_lagrange=method.lagrange_method(data, predict_x1)
    predict_y2_lagrange=method.lagrange_method(data, predict_x2)
    print(f"Predicted_lagrange y value at x={predict_x1} is {predict_y1_lagrange}")
    print(f"Predicted_lagrange y value at x={predict_x2} is {predict_y2_lagrange}")
    return predict_y1_lagrange, predict_y2_lagrange

def predict_linear():
    predict_y1_linear=method.linear_method(data, predict_x1)
    predict_y2_linear=method.linear_method(data, predict_x2)  
    print(f"Predicted_linear y value at x={predict_x1} is {predict_y1_linear}")
    print(f"Predicted_linear y value at x={predict_x2} is {predict_y2_linear}")
    return predict_y1_linear, predict_y2_linear

def predict_spline():
    predict_y1_spline=method.spline_method(data, predict_x1)
    predict_y2_spline=method.spline_method(data, predict_x2)
    print(f"Predicted_spline y value at x={predict_x1} is {predict_y1_spline}")
    print(f"Predicted_spline y value at x={predict_x2} is {predict_y2_spline}")
    return predict_y1_spline, predict_y2_spline

def draw_graph():
    x_dense = np.linspace(min(x), max(x), 1000)
    y_lagrange = [method.lagrange_method(data, xi) for xi in x_dense]
    y_linear = [method.linear_method(data, xi) for xi in x_dense]
    y_spline = [method.spline_method(data, xi) for xi in x_dense]
    plt.figure(figsize=(12, 8))
    plt.scatter(x, y1, label='原始数据')
    plt.plot(x_dense, y_lagrange, label='拉格朗日插值')
    plt.plot(x_dense, y_linear, label='线性插值')
    plt.plot(x_dense, y_spline, label='样条插值')

    y1_lagrange, y2_lagrange = predict_lagrange()
    y1_linear, y2_linear = predict_linear()
    y1_spline, y2_spline = predict_spline()
    
    plt.scatter([predict_x1, predict_x2], [y1_lagrange, y2_lagrange], color='blue', s=100, marker='x', label=f'拉格朗日预测点')
    plt.scatter([predict_x1, predict_x2], [y1_linear, y2_linear], color='orange', s=100, marker='x', label=f'线性预测点')
    plt.scatter([predict_x1, predict_x2], [y1_spline, y2_spline], color='green', s=100, marker='x', label=f'样条预测点')
    plt.title('不同插值方法的比较', fontsize=16)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=12)
    plt.xlim(-6, 6)  # 设置x轴范围
    plt.ylim(-0.6, 0.6)  # 设置y轴范围
    # 显示图形
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    # threads = []

    # t1 = multiprocessing.Process(target=predict_lagrange)
    # threads.append(t1)

    # t2 = multiprocessing.Process(target=predict_linear)
    # threads.append(t2)

    # t3 = multiprocessing.Process(target=predict_spline)
    # threads.append(t3)

    # for t in threads:###这个可以！
    #     t.start()

    # for t in threads:
    #     t.join()    
    draw_graph()