import drawSvg as draw

class HilldownDraw:
    def __init__(self, width=200, height=100, name='hillchart'):
        # d = draw.Drawing(200, 100, origin='center', displayInline=False)
        self.drawing = draw.Drawing(width, height, origin='center', displayInline=False)
        self.stroke_width = 2
        self.name = name
        self.greeting = 'Hello'
        print(self.greeting)

    def Circle(self, x0=-40, y0=-10, radius=30, color='red', border='black'):

        self.drawing.append(draw.Circle(x0, y0, radius,
            fill=color, stroke_width=self.stroke_width, stroke=border))

    def Line(self):
        pass

    def save(self):
        self.drawing.saveSvg('{}.svg'.format(self.name))