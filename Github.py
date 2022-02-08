from shutil import move
from manim import *
import manimpango

class Vectors(ThreeDScene):
    def construct(self):
        # vec_txt = MarkupText("<u>Vectors</u>")
        # base1 = MathTex(r"\begin{bmatrix} 5 \\ 2 \end{bmatrix}")
        # VGroup(vec_txt, base1).arrange(DOWN)
        # self.play(
        #     Write(vec_txt),
        #     FadeIn(base1, shift=DOWN),
        # )
        # self.wait(2)
        # transform_title = Tex("How do they work geometrically?")
        # transform_title.to_corner(UP + LEFT)
        # self.play(
        #     Transform(vec_txt, transform_title),
        #     LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in base1]),
        # )
        
        grid = NumberPlane()
        axes = ThreeDAxes()
        self.add(grid, axes)
        self.play(
            Create(grid, run_time = 1.5, lag_ratio = 0.1),
        )
        # self.wait()

        dot = Dot(ORIGIN, color = "RED", radius= 0.1)
        Origin_txt = Text("This is the Origin", font_size = "30").next_to(dot, DOWN + LEFT)
        self.play(
            Create(dot, run_time = 1),
        )
        # self.wait(0.5)
        self.play(
            Write(Origin_txt, run_time = 0.5),
        )
        # self.wait()
        transform_Origin_txt = Text("(0,0)", font_size = "40")
        transform_Origin_txt.move_to([-1,-1,1])
        self.play(
            Transform(Origin_txt, transform_Origin_txt),
        )

        def ArrowMaker(vector):
            arrow = Arrow(ORIGIN, vector, buff = 0)
            return arrow

        def ArrowTextMaker(vectortext, text):
            point = Text(text, font_size="40")
            point.move_to(vectortext)
            return point

        def DotMaker(vector):
            dot = Dot(vector, color = "RED", radius= 0.1, fill_opacity=0.5)
            return dot

        arrow1 = ArrowMaker([2,2,0])
        text1 = ArrowTextMaker([3, 2,0], "(2,2)")
        dot1 = DotMaker([2,2,0])
        
        self.play(
            Create(arrow1, run_time = 1),
            Create(dot1),
            FadeIn(text1),
            # FadeOut(vec_txt),
        )

        # self.wait(1)
        # arrow2 = ArrowMaker([-2,3,0])
        # text2 = ArrowTextMaker([-3, 3,0], "(-2,3)")
        # dot2 = DotMaker([-2,3,0])

        # self.play(
        #     FadeOut(text1, dot1, ),
        #     Transform(arrow1, arrow2),
        #     Create(dot2),
        #     FadeIn(text2),
        # )

        # self.wait(0.5)
        # arrow3 = ArrowMaker([-4,1,0])
        # text3 = ArrowTextMaker([-5,1,0], "(-4,1)")
        # dot3 = DotMaker([-4,1,0])
        # self.play(
        #     FadeOut(text2, dot2),
        #     Transform(arrow1, arrow3),
        #     Create(dot3),
        #     FadeIn(text3)
        # )

        self.wait(0.5)
        arrow4 = ArrowMaker([5,-2,0])
        text4 = ArrowTextMaker([6,-2,0], "(5,-2)")
        dot4 = DotMaker([5,-2,0])
        self.play(
            # FadeOut(text3, dot3),
            Transform(arrow1, arrow4),
            Create(dot4),
            FadeIn(text4)
        )
        self.wait()

        # self.camera.frame.save_state()
        # self.play(self.camera.frame.animate.set(width=Origin_txt.width * 4))
        # self.play(self.camera.frame.animate.move_to(dot4))
        # self.wait(0.3)
        # self.play(Restore(self.camera.frame))

        self.play(FadeOut(dot1, dot4, text4, text1))
        self.set_camera_orientation(phi=0 * DEGREES, theta=270 * DEGREES)
        self.move_camera(phi= 0*DEGREES, theta=270*DEGREES, gamma = 0*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.3, about="phi")
        self.begin_ambient_camera_rotation(rate=0.3, about="theta")

        self.wait(2)
        arrow5 = ArrowMaker([5,-2, 3])
        text5 = ArrowTextMaker([6,-2, 3], "(5,-2, 3)")
        dot5 = DotMaker([5,-2, 3])
        self.play(
            # FadeOut(text3, dot3),
            Transform(arrow1, arrow5),
            Create(dot5),
            FadeIn(text5)
            )
        self.wait(3)





        # self.play(FadeOut(text4, dot4, grid, Origin_txt, arrow1, dot))
        
