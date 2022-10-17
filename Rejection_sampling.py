from manim import *
import numpy
import matplotlib.pyplot as plt
from math import pi
from math import e


def norm(x, mu, sigma):
    return 1 / ((2 * pi) ** 0.5 * sigma) * e ** ((-((x - mu) ** 2)) / (2 * sigma**2))


def pdf(x):
    return 0.5 * norm(x, -3, 0.5) + 0.5 * norm(x, 3, 0.5)


n = int(input())
x = numpy.random.normal(0, 2, n)
y = numpy.zeros(n)
for i in range(n):
    y[i] = numpy.random.uniform(low=0, high=6.5 * norm(x[i], 0, 2), size=None)
filter = y <= pdf(x)
plt.style.use("seaborn-whitegrid")
plt.plot(x[filter], y[filter], "o", color="green")
plt.plot(x[~filter], y[~filter], "o", color="red")
plt.show()


class RejectionSampling(Scene):
    def construct(self):
        grid = Axes(
            x_range=[-5, 5, 1],
            y_range=[0, int(6.5 / (8 * pi) ** 0.5) + 1, 0.2],
        ).add_coordinates()
        graph = grid.plot(lambda x: pdf(x), color=GREEN)
        graph2 = grid.plot(lambda x: 6.5 * norm(x, 0, 2), color=YELLOW)
        self.add(grid, graph, graph2)
        text0=MathTex(r"f(x)=0.5\mathcal{N}(3,0.25)+0.5\mathcal{N}(-3,0.25)").shift(3*UP+3*RIGHT).scale(0.5)
        self.add(text0)
        self.play(Write(text0))
        text1=MathTex(r"g(x)=\mathcal{N}(0,4)").next_to(text0,DOWN).scale(0.5)
        self.add(text1)
        self.play(Write(text1))
        text2=MathTex(r"C=6.5").next_to(text1,DOWN).scale(0.5)
        self.add(text2)
        self.play(FadeIn(text2))
        for i in range(n):
            dot = Dot(color=WHITE).move_to(grid.c2p(x[i], 0, 0))
            self.add(dot)
            self.play(FadeIn(dot))
            START = grid.c2p(x[i], 0, 0)
            END = grid.c2p(x[i], 2, 0)
            line = DashedLine(START, END, color=BLUE)
            self.add(line)
            self.play(Create(line))
            if pdf(x[i]) >= y[i]:
                dot_0 = Dot(color=GREEN).move_to(grid.c2p(x[i], y[i], 0))
                self.add(dot_0)
                self.play(FadeIn(dot_0))
            else:
                dot_0 = Dot(color=RED).move_to(grid.c2p(x[i], y[i], 0))
                self.add(dot_0)
                self.play(FadeIn(dot_0))
                cross = Cross(scale_factor=0.1).move_to(dot)
                self.add(cross)
                dot.set_opacity(0.2)
