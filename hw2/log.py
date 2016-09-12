
from __future__ import division
import plotly.plotly as plot
import plotly.graph_objs as graph
from numpy import arange
from math import log

def f():
    return log(2)
def fAlt():
    result = 0
    for n in range(1,100000):
        result += (pow(-1,n-1)/n)
    return result


plot.sign_in('kablaa', 'hyi1epcr60')

hVals = arange(0,1,.01)

trace1 = graph.Scatter(
        x = hVals,
        y = [f() for h in hVals ],
        mode="lines",
        name="exact"
        )

trace2 = graph.Scatter(
        x = hVals,
        y = [fAlt() for h in hVals],
        mode = 'lines',
        name = 'approx'
        )


layout = graph.Layout(
        title='aproximating log(2)',
        width=600,
        height=740,
        xaxis = dict(title ='x'),
        yaxis = dict(title = 'log(2)')
        )
fig = graph.Figure(data =[trace1,trace2], layout=layout)
plot.image.save_as(fig, filename='images/log.png')
