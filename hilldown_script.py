import drawSvg as draw
from hilldown_draw import HilldownDraw

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

yaxis = draw.Path(stroke_width=2, stroke='black', fill='transaparent')
my_drawing.path_segment(yaxis, (250, 0), start=True)
my_drawing.path_segment(yaxis, (250, 500))
my_drawing.drawing.append(yaxis)

xaxis = draw.Path(stroke_width=2, stroke='black', fill='transaparent')
my_drawing.path_segment(xaxis, (0, 250), start=True)
my_drawing.path_segment(xaxis, (500, 250))
my_drawing.drawing.append(xaxis)

path = draw.Path(stroke_width=2, stroke='green', fill='transparent')
bell_curve_points = HilldownDraw.get_bell_curve()
# my_drawing.path_segment(path, (5, 5), start=True)
# my_drawing.path_segment(path, (30, 150))
# my_drawing.path_segment(path, (15, 75))
# my_drawing.path_segment(path, (5, 200))
my_drawing.path_segment(path, (0, 0), start=True)
for point in bell_curve_points: 
    my_drawing.path_segment(path, point)
my_drawing.drawing.append(path)
my_drawing.circle(x0=125, y0=60, radius=15)
my_drawing.circle(x0=253, y0=265, radius=15, color='yellow')
my_drawing.circle(x0=347, y0=142, radius=15, color='blue')
my_drawing.save()

print(bell_curve_points)



