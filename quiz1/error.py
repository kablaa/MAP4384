import math
import plotly.plotly as py
import plotly.graph_objs as go

def f(x):
    return math.sin(x)

def error(f1,f2):
    return abs(f1-f2)

def approx(x,h):
    return float((f(x + h) - f(x))/h)

hVals = []
errVals = []
x = float(math.pi/3)

#getting our h values
for i in range(0,10):
    hVals.append(float(1/float(pow(2,i))))

for h in hVals:
    errVals.append(error(approx(x,h),math.cos(x)))
    print "%f           %f" % (h,errVals[len(errVals)-1])


py.sign_in('kablaa', 'hyi1epcr60')
errAxis = ["h = %f" % h for h in hVals]
trace = go.Scatter(
        x =errAxis,
        y = errVals
        )
data = [trace]


layout = go.Layout(
        title='Approximating the derivative using the limit definition',
        width=800,
        height=640,
        xaxis = dict(title ='h valyes'),
        yaxis = dict(title = 'error')
        )
fig = go.Figure(data =data, layout=layout)
py.image.save_as(fig, filename='graph.png')


