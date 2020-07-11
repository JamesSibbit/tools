import csv
from bokeh.io import output_file, show
from bokeh.models import (GMapPlot, GMapOptions, ColumnDataSource, Circle, Range1d, PanTool, WheelZoomTool, BoxSelectTool)


lats = ['54.653468']
longs = ['-3.380473']
# f = open('countries.csv', encoding='ISO-8859-1')
# countries = csv.reader(f)
# for ab, lat, long, name in list(countries)[1:]:
#     lats.append(float(lat))
#     longs.append(float(long))

map_options = GMapOptions(lat=0, lng=0, zoom=3)
plot = GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options)
plot.title.text = 'Our Plot'
plot.api_key = 'Enter API key here'

source = ColumnDataSource(data=dict(lat=lats, lon=longs))

circle = Circle(x='lon', y='lat', size=10, fill_color='blue', fill_alpha=0.6)

plot.add_glyph(source, circle)
plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())

output_file('example_gmaps.html')
show(plot)
