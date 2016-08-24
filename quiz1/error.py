import math
import plotly.plotly as py
from plotly.graph_objs import *

def f(x):
    return math.sin(x)

def error(f1,f2):
    return abs(f1-f2)

def approx(x,h):
    return float((f(x + h) - f(x))/h)

hVals = []
approxVals = []
exactVlas = []
errVals = []
x = float(math.pi/3)

#getting our h values
for i in range(0,100):
    hVals.append(float(1/float(pow(2,i))))

for h in hVals:
    approxVals.append(approx(x,h))
    exactVlas.append(math.cos(x))
    hVals.append(h)
    errVals.append(error(approx(x,h),math.cos(x)))
    print " %f  %f   %f  %f" % (h,approx(x,h) , math.cos(x), error(approx(x,h),math.cos(x)))


trace1 = Scatter(
        x =hVals,
        y = errVals,
        line=Line(color='rgb(231,107,243)'),
        mode = "lines"
        )

layyout = Layout(
    paper_bgcolor='rgb(255,255,255)',
    plot_bgcolor='rgb(229,229,229)',
    xaxis=XAxis(
        gridcolor='rgb(255,255,255)',
        range=[1,10],
        showgrid=True,
        showline=False,
        showticklabels=True,
        tickcolor='rgb(127,127,127)',
        ticks='outside',
        zeroline=False
    ),
    yaxis=YAxis(
        gridcolor='rgb(255,255,255)',
        showgrid=True,
        showline=False,
        showticklabels=True,
        tickcolor='rgb(127,127,127)',
        ticks='outside',
        zeroline=False
    ),
)
fig = Figure(data=data, layout=layout)
py.iplot(fig, filename= 'shaded_lines')
