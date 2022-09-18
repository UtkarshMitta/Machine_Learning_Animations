from manim import *
import numpy
from math import e
from math import log
from scipy.stats import norm
from scipy.stats import expon


class ExampleFunctionGraph(Scene):
    def construct(self):
        def func(x, choose):
            return expon.pdf(x) if choose else norm.pdf(x)

        def cdf_func(x, choose):
            return expon.cdf(x) if choose else norm.cdf(x)

        def inverse_func(x, choose):
            if choose:
                if x >= 0:
                    return -log(1 - x)
                else:
                    return 0
            else:
                return norm.ppf(x)

        def pdf_init(choose, axis, scene):
            ans = VGroup()
            ans += axis.plot(lambda x: func(x, choice), color=GREEN)
            text = Tex("Actual pdf:")
            axis.fade(darkness=0.8, family=True)
            scene.add(text)
            scene.play(FadeIn(text))
            scene.wait(0.5)
            scene.play(FadeOut(text))
            axis.set_opacity(1)
            scene.wait(0.5)
            scene.add(ans)
            scene.play(FadeIn(ans))
            scene.wait(0.5)
            scene.play(FadeOut(ans))
            scene.wait(0.5)

        n = int(input())
        choice = int(input())
        grid = Axes(
            x_range=[-1, 1, 0.2],
            y_range=[-1, 1, 0.2],
            tips=False,
            axis_config={"include_numbers": True},
        )
        dot_list = []
        graph = VGroup()
        graph += grid.plot(
            lambda x: cdf_func(x, choice),
            color=WHITE,
        )
        y_list = numpy.random.uniform(0, 1, n)
        vfunc = numpy.vectorize(inverse_func)
        inverse_list = vfunc(y_list, choice)
        self.add(grid)
        pdf_init(choice, grid, self)
        text = Tex("CDF of the distribution")
        grid.set_opacity(0.2)
        self.add(text)
        self.play(FadeOut(text))
        grid.set_opacity(1)
        self.add(graph)
        self.play(FadeIn(graph))
        self.wait(0.5)
        graph.set_color(BLACK)
        grid.set_opacity(0.2)
        text = Tex("taking samples")
        self.add(text)
        self.play(FadeIn(text))
        self.wait(0.5)
        self.play(FadeOut(text))
        graph.set_color(WHITE)
        grid.set_opacity(1)
        for element in y_list:
            dot = Dot(grid.coords_to_point(0, element, 0), color=RED)
            self.add(dot)
            dot_list.append(dot)
        self.wait(1)
        hline = []
        vline = []
        for i in range(10):
            horizontal = VGroup()
            vertical = VGroup()
            hline.append(horizontal)
            vline.append(vertical)
        dot = VGroup()
        for i in range(n):
            hline[i % 10] += grid.get_horizontal_line(
                grid.c2p(inverse_list[i], y_list[i], 0), color=BLUE
            )
            vline[i % 10] += grid.get_vertical_line(
                grid.c2p(inverse_list[i], y_list[i], 0), color=BLUE
            )
            dot += Dot(grid.coords_to_point(inverse_list[i], 0, 0), color=YELLOW)
        for i in range(len(hline)):
            self.add(hline[i])
            self.play(Create(hline[i]))
            self.add(vline[i])
            self.play(Create(vline[i]))
        self.add(dot)
        self.wait(0.5)
        x = VGroup()
        for objects in dot_list:
            x += objects
        x += graph
        self.play(FadeOut(x))
        for i in range(len(hline)):
            self.play(FadeOut(hline[i]))
            self.play(FadeOut(vline[i]))
        self.play(FadeOut(dot))

        def kde(x, inv):
            sum = 0
            for entry in inv:
                sum += norm.pdf(x, entry)
            return sum / len(inv)

        graph2 = grid.plot(lambda x: kde(x, inverse_list), color=WHITE)
        text = Tex("KDE Plot")
        grid.set_opacity(0.2)
        self.add(text)
        self.play(FadeIn(text))
        self.wait(0.5)
        self.play(FadeOut(text))
        grid.set_opacity(1)
        self.add(graph2)
        self.play(FadeIn(graph2))
        self.wait(1)
        self.play(FadeOut(graph2))
        text = Tex("K-L Divergence")
        self.play(FadeOut(grid))
        self.add(text)
        self.play(FadeIn(text))
        self.wait(0.5)
        self.play(FadeOut(text))
        eq1 = Tex("KL divergence = ").shift(5 * LEFT)
        self.add(eq1)
        self.play(FadeIn(eq1))
        eq2 = MathTex(r"\int_{-\infty}^{\infty}P(x) log\frac{P(x)}{Q(x)}dx = ").next_to(
            eq1, 2 * RIGHT
        )
        self.add(eq2)
        self.play(FadeIn(eq2))
        kde_list = numpy.zeros(n)
        for i in range(len(kde_list)):
            kde_list[i] = kde(inverse_list[i], inverse_list)
        pdf_func = numpy.vectorize(func)
        actual = pdf_func(inverse_list, choice)
        kl_divergence = 0
        for element in range(len(kde_list)):
            kl_divergence += kde_list[element] * log(
                kde_list[element] / actual[element]
            )
        eq3 = MathTex(kl_divergence).next_to(eq2, 2 * RIGHT)
        self.add(eq3)
        self.play(FadeIn(eq3))
