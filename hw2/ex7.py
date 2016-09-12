from __future__ import division
import plotly.plotly as plot
import plotly.graph_objs as graph
from numpy import arange
from math import sqrt

def f(h):
    return sqrt(1+h)

def fAlt(h):
    return 1 + (1/2)*h - (1/8)*pow(h,2) + (1/16)*pow(h,3)

plot.sign_in('kablaa', 'hyi1epcr60')

hVals = arange(0,5,.01)

trace1 = graph.Scatter(
        x = hVals,
        y = [f(h) for h in hVals ],
        mode="lines",
        name="exact"
        )

trace2 = graph.Scatter(
        x = hVals,
        y = [fAlt(h) for h in hVals],
        mode = 'lines',
        name = 'approx'
        )


layout = graph.Layout(
        title='aproximating sqrt(1+h)',
        width=600,
        height=740,
        xaxis = dict(title ='x'),
        yaxis = dict(title = 'sqrt(1+h)')
        )
fig = graph.Figure(data =[trace1,trace2], layout=layout)
plot.image.save_as(fig, filename='images/sqrt.png')
