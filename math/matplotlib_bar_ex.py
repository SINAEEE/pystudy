

import numpy as np
import matplotlib.pyplot as plt


def ex1():
    x_name = ('1','2','3','4','5','6','7','8','9','10','11','12')
    y1_value = (21.6,23.6,45.8,77.0,102.2,133.3,327.9, 348.0, 137.6, 49.3, 53.0, 24.9)
    n_groups = len(x_name)
    index = np.arange(n_groups)

    plt.bar(index,y1_value,tick_label=x_name, align='center')

    plt.show()

if __name__ == '__main__':
    ex1()

