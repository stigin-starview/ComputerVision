from numpy import source
from capture import time_df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

time_df["Start_string"] = time_df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
time_df["End_string"] = time_df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(time_df) 

p = figure(x_axis_type = 'datetime', max_height=500, sizing_mode='stretch_width', title= "Motion Graph")

# removing small ticks from the y axis of the graph
p.yaxis.minor_tick_line_color = None

#removing the grid lines from graph 
p.yaxis.ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
p.add_tools(hover)
q= p.quad(left ="Start", right ="End" ,top = 1 ,bottom = 0, color = "green", source = cds)

output_file("MotionGraph.html")

show(p)