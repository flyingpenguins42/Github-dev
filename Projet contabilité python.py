# # importing packages and modules
# import numpy as np
# import matplotlib.pyplot as plt
  
# # average marks data for 5 consecutive years
# data = [[98, 95,  93, 96,  97],
#         [97, 92,  95, 94,  96],
#         [98, 95,  93, 95,  94],
#         [96, 94,  94, 92,  95],
#         [95, 90,  91, 94,  98]]
  
# columns = ('English', 'Maths', 'Physics',
#            'Chemistry', 'Biology')
# rows = ['%d academic year' % x for x in (2015, 2016, 2017, 2018, 2019)]
  
# # Get some pastel shades for the colors
# colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
# n_rows = len(data)
  
# index = np.arange(len(columns)) + 0.3
# bar_width = 0.4
  
# # Initialize the vertical-offset for
# # the line plots.
# y_offset = np.zeros(len(columns))
  
# # Plot line plots and create text labels 
# # for the table
# cell_text = []
# for row in range(n_rows):
#     plt.plot(index, data[row], color=colors[row])
#     y_offset = data[row]
#     cell_text.append([x for x in y_offset])
  
# # Reverse colors and text labels to display
# # the last value at the top.
# colors = colors[::-1]
# cell_text.reverse()
  
# # Add a table at the bottom of the axes
# the_table = plt.table(cellText=cell_text,
#                       rowLabels=rows,
#                       rowColours=colors,
#                       colLabels=columns,
#                       loc='bottom')
  
# # Adjust layout to make room for the table:
# plt.subplots_adjust(left=0.2, bottom=0.2)
  
# plt.ylabel("marks".format(value_increment))
# plt.xticks([])
# plt.title('average marks in each consecutive year')
  
# plt.show()