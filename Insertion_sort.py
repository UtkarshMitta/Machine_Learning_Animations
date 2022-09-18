from manim import *
import sorter
import numpy


class TextBox(Scene):
    def construct(self):
        n = int(input())
        arr = numpy.zeros(n)
        for i in range(n):
            arr[i] = int(input())
        sorter.make_textbox_system(arr, sorter.textboxlist, self)
        for i in range(n - 1):
            sorter.arrow_i.next_to(sorter.textboxlist[i], 2 * UP)
            self.play(FadeIn(sorter.arrow_i.next_to(sorter.textboxlist[i], 2 * UP)))
            for j in range(i + 1, n, 1):
                sorter.arrow_j.next_to(sorter.textboxlist[j], 2 * UP)
                self.play(FadeIn(sorter.arrow_j.next_to(sorter.textboxlist[j], 2 * UP)))
                if arr[i] > arr[j]:
                    sorter.swap(arr, sorter.textboxlist, i, j, self)
                self.play(
                    FadeOut(sorter.arrow_j.next_to(sorter.textboxlist[j], 2 * UP))
                )
                self.wait(1)
            self.play(FadeOut(sorter.arrow_i.next_to(sorter.textboxlist[i], 2 * UP)))
            self.wait(1)
