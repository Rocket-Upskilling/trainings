import pandas as pd

import plotly.express as px
from itertools import count

#this creates an all time high plot from a pandas series, t can be "max" or "min" for all time high or all time low.
def atm_plot(s, t="max"):
    if t == "max":
        q = s.cummax()
    elif t == "min":
        q = s.cummin()
    else:
        raise ValueError("t must be min or max")
    q2 = (q.shift(1) == q).diff()
    q2 = q2[q2 == 1]
    
    fig = px.line(x=coffee_daily.index, y=s)

    for d in q2.index:
        #print( str(d.year) + "-" + str(d.month) + "-" + str(d.day) )
        fig.add_vline(x=d, line_width=1)

    fig.show()

#description here
def dod(df):
    q = df.resample("1d").interpolate()
    return q.shift(1)/q

def nbest(r, n):
    q = r.sort_values().head(n)
    comos = list(q.index)
    values = list(q.values)
    counter = count()
    res_vals = [val for pair in zip(comos, values) for val in pair]
    columns = [val for pair in [(f"como {m}", f"yoy {m}") for m in range(1,n+1)] for val in pair ]
    q = pd.Series(data = res_vals, index = columns, name=r.name )
    return q

def find_best(df, n):
    df = df.shift(1)/df
    return df.progress_apply(nbest, axis=1, **{'n': n})

