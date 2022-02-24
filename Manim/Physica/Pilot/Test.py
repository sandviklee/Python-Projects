from cv2 import FONT_ITALIC
from manim import *

class Banner(Scene):
    def construct(self):
        self.camera.background_color = "#181818"
        logo_green = "#FF4000"
        logo_blue = "#01A9DB"
        logo_red = "#4B088A"
        circle = Circle(color=logo_green, fill_opacity=1).shift(0.9*RIGHT).scale(1.2)
        square = Square(color=logo_blue, fill_opacity=1).shift(0.2 *DOWN).scale(0.9)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(1.2*LEFT).scale(1.5)
        grid = NumberPlane()
        grid.set_opacity(opacity = 1)
        title = Text("φσκα", font_size=70)
        second_title = Text("(or Physica if you can't read greek letters.)", font_size = 14)
        second_title.shift(0.72*DOWN)
        self.add(grid, title, second_title)
