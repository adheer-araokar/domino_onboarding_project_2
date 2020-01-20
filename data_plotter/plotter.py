

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from itertools import chain
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io
from flask import Response



plt.switch_backend('Agg')


def draw_map(m, scale=1.0):
    # draw a shaded-relief image
    # m.shadedrelief(scale=scale)
    m.shadedrelief()

    # lats and longs are returned as a dictionary
    lats = m.drawparallels(np.linspace(-90, 90, 13))
    lons = m.drawmeridians(np.linspace(-180, 180, 13))

    # keys contain the plt.Line2D instances
    lat_lines = chain(*(tup[1][0] for tup in lats.items()))
    lon_lines = chain(*(tup[1][0] for tup in lons.items()))
    all_lines = chain(lat_lines, lon_lines)

    # cycle through these lines and set the desired style
    for line in all_lines:
        line.set(linestyle='-', alpha=0.3, color='w')


def plot_from(data_sink):

    # fig = plt.figure(figsize=(8, 8), edgecolor='w', frameon=False)
    # fig = plt.figure(1, figsize=(8, 14), frameon=True, dpi=100)
    fig = plt.figure(num=None, figsize=(8, 8), edgecolor='w')
    m = Basemap(projection='cyl', resolution=None,
                llcrnrlat=-90, urcrnrlat=90,
                llcrnrlon=-180, urcrnrlon=180)

    draw_map(m)

    for data in data_sink:
        x, y = m(data["lat"], data["lon"])
        # plt.plot(x, y, 'ok', markersize=5)
        plt.plot(x, y)
        plt.text(x, y, data["name"], fontsize=6)

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
