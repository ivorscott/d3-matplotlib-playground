import mimetypes
mimetypes.add_type('image/svg+xml', '.svg')

import matplotlib
matplotlib.use('Agg') # this allows PNG plotting
import matplotlib.pyplot as plt
import base64

from flask import render_template
from app import app
from io import BytesIO

## navigation
graph_nav = [
    {'d3': [
        {'link': '/histogram'},
        {'link': '/bar_chart'}]},
    {'mpl': [
        {'link': '/bar_chart_mpl'},
        {'link': '/line_chart_mpl'}]}
]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',graphs=graph_nav)

## begins d3 examples ##
@app.route('/histogram')
def histogram():
    return render_template('histogram.html',graphs=graph_nav)

@app.route('/bar_chart')
def bar_chart():
    return render_template('bar_chart.html',graphs=graph_nav)
## ends d3 examples ##

## begins matplotlib examples  ##
@app.route('/bar_chart_mpl')
def bar_chart_mpl():

    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]

    # bars are by default width 0.8, so we'll add 0.1 to the left coordinates
    # so that each bar is centered

    xs = [i + 0.1 for i, _ in enumerate(movies)]

    # plot bars with left x-coordinates [xs], heights [num_oscars]
    plt.figure(1)
    plt.bar(xs, num_oscars)
    plt.ylabel("# of Academy Awards")
    plt.title("My Favorite Movies")

    # label x-axis with movie names at bar centers
    plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

    return render_mpl_template(plt, 1)

@app.route('/line_chart_mpl')
def line_chart_mpl():

    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

    # create a line chart, years on x-axis, gdp on y-axis
    plt.figure(2)
    plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

    # add a title
    plt.title("Nominal GDP")

    # add a label to the y-axis
    plt.ylabel("Billions of $")

    return render_mpl_template(plt,2)
## ends matplotlib examples  ##

def render_mpl_template(plt, fignum):
    # run plt.plot, plt.title, etc.
    plt.figure(fignum)
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)  # rewind to beginning of file

    #figfile.getvalue()  extracts string (stream of bytes)
    figdata_png = base64.b64encode(figfile.getvalue())

    return render_template('matplot.html',graphs=graph_nav,fig=figdata_png)
