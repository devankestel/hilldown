import drawSvg as draw
# import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

class HilldownDraw:
    def __init__(self, width=200, height=100, name='hillchart'):
        # d = draw.Drawing(200, 100, origin='center', displayInline=False)
        self.drawing = draw.Drawing(width, height, origin=(0,0), displayInline=False)
        self.stroke_width = 2
        self.name = name
        self.greeting = 'Hello'
        print(self.greeting)
    
    @staticmethod
    def get_bell_curve(std_dev=30, mean=100, num_points=100, height=20000):
    
        start = mean - 3*std_dev
        stop = mean + 3*std_dev
        stretch_factor = 2.6
        xs = np.linspace(start=start,stop=stop, num=num_points)
        stretch_xs = []
        result = []
        for x in xs:
            y = height*stats.norm.pdf(x, mean, std_dev)
            stretched_rounded_x = round(stretch_factor*x)
            stretch_xs.append(stretched_rounded_x)
            round_y = round(y)
            result.append((stretched_rounded_x, round_y))
        # plt.plot(stretch_xs, height*stats.norm.pdf(xs, mean, std_dev))
        # plt.show()
        return result


    def circle(self, x0=-40, y0=-10, radius=30, color='red', border='black'):

        self.drawing.append(draw.Circle(x0, y0, radius,
            fill=color, stroke_width=self.stroke_width, stroke=border))

    def unclosed_path(self, points, stroke='black'):
        x0, y0 = points.pop(0)
        path = draw.Path(stroke_width=self.stroke_width, stroke=stroke, fill='transparent')
        path.M(x0, y0)
        for point in points:
            x, y = point
            path.L(x, y)
        self.drawing.append(path)

    def save(self):
        self.drawing.saveSvg('{}.svg'.format(self.name))
