from manim import *
import random
from pynverse import inversefunc
from math import e


class ExampleFunctionGraph(Scene):
    def get_rectangle_corners(self, bottom_left, top_right):
        return [
            (top_right[0], top_right[1]),
            (bottom_left[0], top_right[1]),
            (bottom_left[0], bottom_left[1]),
            (top_right[0], bottom_left[1]),
        ]

    def construct(self):
        n = int(input())
        grid = Axes(
            x_range=[0, 1, 0.2],
            y_range=[-1, 1, 0.2],
            tips=False,
            axis_config={"include_numbers": True},
        )
        y_list = []
        dot_list = []
        graph = VGroup()
        graph += grid.plot(lambda x: 1 - (e ** (-x)), color=WHITE)
        for i in range(n):
            y_list.append(random.uniform(0, 1))
        inverse = inversefunc(lambda x: x**3)
        self.add(graph, grid)
        for element in y_list:
            dot = Dot(grid.coords_to_point(0, element, 0), color=RED)
            self.add(dot)
            dot_list.append(dot)
        self.wait(1)
        hline = VGroup()
        vline = VGroup()
        dot = VGroup()
        for element in y_list:
            hline += grid.get_horizontal_line(
                grid.c2p(abs(inverse(element)), element, 0), color=BLUE
            )
            vline += grid.get_vertical_line(
                grid.c2p(abs(inverse(element)), element, 0), color=BLUE
            )
            dot += Dot(grid.coords_to_point(abs(inverse(element)), 0, 0), color=YELLOW)
        self.add(hline)
        self.play(Create(hline))
        self.play(Create(vline))
        self.add(dot)
        self.wait(0.5)
        x = VGroup()
        for objects in dot_list:
            x += objects
        x += graph
        self.play(FadeOut(x))
        self.play(FadeOut(hline))
        self.play(FadeOut(vline))
        self.play(FadeOut(dot))
        dicto = {}
        for element in range(len(y_list)):
            y_list[element] = np.round(abs(inverse(y_list[element])), 1)
        for element in y_list:
            dicto[element] = dicto.get(element, 0) + 1
        Random = []
        pdf = []
        master = []
        for element in dicto:
            master.append((element, dicto[element]))
        master = sorted(master)
        for element in master:
            Random.append(element[0])
            pdf.append((element[1]) / (n * 0.1))
        grid2 = Axes(
            x_range=[0, max(Random), 0.1],
            y_range=[-max(pdf), max(pdf), 0.2],
            tips=False,
            axis_config={"include_numbers": True},
        )
        self.play(Transform(grid, grid2))
        grid = grid2
        rect = VGroup()
        for element in range(len(Random)):
            rect += Polygon(
                *[
                    grid.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (Random[element], 0), (Random[element] + 0.1, pdf[element])
                    )
                ],
                color=RED
            )
        self.play(FadeIn(rect))
