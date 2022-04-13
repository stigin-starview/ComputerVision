from capture import time_df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool

p = figure(x_axis_type = 'datetime', max_height=500, sizing_mode='stretch_width', title= "Motion Graph")

# removing small ticks from the y axis of the graph
p.yaxis.minor_tick_line_color = None

#removing the grid lines from graph 
p.yaxis.ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("Start: ","@Start"),("End: ","@End")])
p.add_tools(hover)
q= p.quad(left = time_df['Start'], right = time_df['End'],top = 1,bottom = 0, color = "green")

output_file("MotionGraph.html")

show(p)