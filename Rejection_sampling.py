from manim import *
import numpy
from scipy.stats import norm
import matplotlib.pyplot as plt
from math import pi

n = int(input())
x = numpy.random.uniform(-1, 1, n)
y = numpy.random.uniform(0, 1/(2*pi)**0.5, n)
filter = y <= norm.pdf(x)
plt.style.use("seaborn-whitegrid")
plt.plot(x[filter], y[filter], "o", color="green")
plt.plot(x[~filter], y[~filter], "o", color="red")
plt.show()


class RejectionSampling(Scene):
    def construct(self):
        grid = Axes(
            x_range=[-5, 5, 1],
            y_range=[0, 0.5, 0.1],
        ).add_coordinates()
        graph = grid.plot(lambda x: norm.pdf(x), color=GREEN)
        graph2 = grid.plot(
            lambda x: 1 / (2 * pi) ** 0.5 if (x > -1 and x < 1) else 0, color=YELLOW
        )
        graph2.make_jagged()
        self.add(grid, graph, graph2)
        for i in range(n):
            dot=Dot(color=WHITE).move_to(grid.c2p(x[i],0,0))
            self.add(dot)
            self.play(FadeIn(dot))
            START = grid.c2p(x[i],0,0)
            END =   grid.c2p(x[i],1,0)
            line = DashedLine(START,END,color=BLUE)
            self.add(line)
            self.play(Create(line))
            if (norm.pdf(x[i])>=y[i]):
                dot=Dot(color=GREEN).move_to(grid.c2p(x[i],y[i],0))
                self.add(dot)
                self.play(FadeIn(dot))
            else:
                dot=Dot(color=RED).move_to(grid.c2p(x[i],y[i],0))
                self.add(dot)
                self.play(FadeIn(dot))
