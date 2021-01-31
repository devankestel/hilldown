import drawSvg as draw
from hilldown_draw import HilldownDraw, Color, Dot, Zone, LabelOrientation

# Draw Arcs
e = draw.Drawing(200, 100, origin='center', displayInline=False)
e.append(draw.ArcLine(60,-20,20,60,270,
            stroke='red', stroke_width=5, fill='red', fill_opacity=0.2))
e.saveSvg('arc1.svg')

f = draw.Drawing(200, 100, origin='center', displayInline=False)
f.append(draw.Arc(60,-10,20,60,270,cw=False,
            stroke='green', stroke_width=3, fill='none'))
f.saveSvg('arc2.svg')

g = draw.Drawing(200, 100, origin='center', displayInline=False)
g.append(draw.Arc(60,-20,20,270,60,cw=True,
            stroke='blue', stroke_width=1, fill='black', fill_opacity=0.3))
g.saveSvg('arc3.svg')

my_drawing = HilldownDraw(width=500, height=500)


yaxis_points = [(250, 0), (250, 500)]
my_drawing.unclosed_path(yaxis_points)

xaxis_points = [(0, 250), (500, 250)]
my_drawing.unclosed_path(xaxis_points)

bell_curve_points = HilldownDraw.get_bell_curve()
my_drawing.unclosed_path(bell_curve_points)

my_drawing.circle(x0=125, y0=60, radius=15)
my_yellow_dot = Dot(position=(253, 265), description='Write unit test', label_orientation=LabelOrientation.TOP, color=Color.YELLOW)
dot_x, dot_y = my_yellow_dot.position
my_drawing.circle(x0=dot_x, y0=dot_y, radius=15, color=my_yellow_dot.color.name)
my_drawing.circle(x0=347, y0=142, radius=15, color='blue')
my_drawing.save()

print(bell_curve_points)



