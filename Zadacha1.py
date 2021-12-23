import matplotlib.pyplot as plt
from numpy import *


def main():
    plt.figure(figsize=(3, 3))
    x = arange(-10, 10.01, 0.11)

    plt.subplot(231)
    plt.plot(x, sin(x) / x, 'b')
    plt.title(r'$\frac{\sin{\left(x \right)}}{x}$')

    plt.subplot(232)
    plt.plot(x, ((x ** 3) - (6 * x ** 2) + (3 * x)) / abs(x), 'g')
    plt.axis('equal')
    plt.title(r'$f {\left(x \right)} = \frac{\left(x^{3} - 6 x^{2} + 3 x \right)}{\left|{x}\right|}$')

    plt.subplot(233)
    plt.plot(x, x ** 2 - 2 * x - 4 - abs(x ** 2 + x - 2), 'r-')
    plt.title(r'$f {\left(x \right)} = x^{2} - 2x - 4 - |x^{2} + x - 2|$')

    plt.subplot(234)
    a = 2 ** sin(x)
    b = 2 ** x
    plt.plot(x, a, x, b)
    plt.title(r'$2^{\sin{\left(x \right)}} 2^{x}$')

    plt.subplot(235)
    plt.plot(x, (1 / (x - 2)) + 1, 'g')  
    plt.title(r'$f{\left(x \right)} = \frac{1}{x - 2} + 1$')

    plt.subplot(236)
    plt.plot(x, sqrt(x) * sqrt(1 - x), 'g')  
    plt.title(r'${y} = \sqrt{x} \sqrt{1 - x}$')

    plt.show()


if __name__ == '__main__':
    main()

