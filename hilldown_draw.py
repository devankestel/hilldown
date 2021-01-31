import enum
import drawSvg as draw
# import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

class Zone(enum.Enum):
    QUEUED = 1
    ASC_BASE = 2
    ASC_PEAK = 3
    APEX = 4
    DESC_PEAK = 5
    DESC_BASE = 6
    CONQUERED = 7

class LabelOrientation(enum.Enum):
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    LEFT = 4

class Color(enum.Enum):
    RED = 1
    YELLOW = 2
    BLUE = 3
    GREEN = 4

class Dot: 
    def __init__(self, position=(0, 0), description='My Item', label_orientation=LabelOrientation.RIGHT, zone=Zone.QUEUED, color=Color.RED):
        self.position = position
        self. description = description
        self.label_orientation = label_orientation
        self.zone = zone
        self.color = color
    
    def change_position(self, new_position):
        self.position = new_position
    
    def change_zone(self, new_zone):
        self.zone = new_zone
    
    def change_label_orientation(self, new_label_orientation):
        self.label_orientation = new_label_orientation

    def change_description(self, new_descripiton):
        self.description = new_descripiton

    def change_color(self, new_color):
        self.color = new_color
    


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
