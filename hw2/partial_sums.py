from __future__ import division
import plotly.plotly as plot
import plotly.graph_objs as graph
import numpy

def arctan(x,N):
    result = 0;
    for k in range(1,N+1):
        result += pow(-1,k+1)*pow(x,2*k-1)/(2*k-1)
    return result


xVals = numpy.arange(-1,1,.01)
plot.sign_in('kablaa', 'hyi1epcr60')

traces = []

for n in range(0,5):
    yVals = []
    for x in xVals:
        yVals.append(arctan(x,n+1))
    traces.append(
            graph.Scatter(
                x = xVals,
                y = yVals,
                mode = "lines",
                name = "n = %d" % (n+1)
            )
    )


layout = graph.Layout(
        title='approximating arctan(x) with partial sums',
        width=600,
        height=740,
        xaxis = dict(title ='x'),
        yaxis = dict(title = 'arctan(x)')
        )
fig = graph.Figure(data =traces, layout=layout)
plot.image.save_as(fig, filename='images/partial.png')

