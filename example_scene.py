from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

class BasicShapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.play(Create(circle), Create(square), Create(triangle))
        self.wait(1)

class TextExample(Scene):
    def construct(self):
        # Create text objects
        text1 = Text("Hello Manim", font_size=48)
        text2 = MathTex(r"\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}", font_size=48)

        # Position text objects
        text1.to_edge(UP)
        text2.next_to(text1, DOWN, buff=0.5)

        # Animate text objects
        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(2)