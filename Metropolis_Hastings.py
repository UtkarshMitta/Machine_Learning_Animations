import numpy
import matplotlib.pyplot as plt
from math import e, pi
from manim import *
from scipy.stats import expon


def norm(x, mu, sigma):
    return (
        1
        / ((2 * pi * sigma**2) ** 0.5)
        * e ** ((-((x - mu) ** 2)) / (2 * sigma**2))
    )


n = int(input())
expo = numpy.vectorize(expon.pdf)
l = numpy.zeros(n)
l[0] = 1
selection = numpy.zeros(n)
selection[0] = 1
for i in range(1, n, 1):
    num0 = numpy.random.normal(l[i - 1], 2, size=None)
    selection[i] = num0
    a = (
        expon.pdf(num0)
        * norm(l[i - 1], num0, 2)
        / (expon.pdf(l[i - 1]) * norm(num0, l[i - 1], 2))
    )
    if a >= 1:

        l[i] = num0
    else:
        prob = numpy.random.uniform(low=0, high=1, size=None)
        if prob <= a:
            l[i] = num0
        else:
            l[i] = l[i - 1]
x = numpy.linspace(-10, 10, n)
y = expo(x)
plt.plot(x, y)
plt.style.use("seaborn-whitegrid")
plt.plot(l, numpy.zeros(n))
plt.show()
print(l, len(l))


class MetropolisHastings(Scene):
    def construct(self):
        grid = Axes(
            x_range=[-10, 10, 1],
            y_range=[0, 1, 0.1],
        ).add_coordinates()
        graph = grid.plot(lambda x: expon.pdf(x), color=BLUE).make_jagged()
        self.add(grid, graph)
        self.play(Create(graph))
        dot = Dot(color=WHITE).move_to(grid.c2p(l[0], 0, 0))
        self.add(dot)
        self.play(FadeIn(dot))
        graph_temp = grid.plot(lambda x: norm(x, l[0], 2))
        self.add(graph_temp)
        self.play(Create(graph_temp))
        for i in range(1, n, 1):
            dot = Dot(color=WHITE).move_to(grid.c2p(selection[i], 0, 0))
            self.add(dot)
            self.play(FadeIn(dot))
            graph_temp_0 = grid.plot(lambda x: norm(x, selection[i], 2))
            self.add(graph_temp_0)
            self.play(Create(graph_temp_0))
            if selection[i] == l[i]:
                dot.set_color(GREEN)
                self.play(FadeOut(graph_temp))
                graph_temp = graph_temp_0
            else:
                cross = Cross(scale_factor=0.1).move_to(dot)
                self.add(cross)
                self.play(FadeIn(cross))
                self.play(FadeOut(graph_temp_0))
            self.wait(0.5)
