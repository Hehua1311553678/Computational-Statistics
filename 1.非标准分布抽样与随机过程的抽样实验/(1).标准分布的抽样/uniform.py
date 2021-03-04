# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 16:22
# @Author  : Hua He
# @Email   : hehua@nuaa.edu.cn
# @File    : uniform.py
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10)
for a,b in [(1, 5), (2, 8)]:
    y = [ 1/(b-a) if (i >=a and i <=b) else 0 for i in x]

    plt.plot(x, y, label="a={}, b={}".format(a, b))

plt.legend()
plt.show()
plt.savefig('./graph/uniform.png')
