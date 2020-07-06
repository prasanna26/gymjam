import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from numpy import genfromtxt
my_data = genfromtxt('foo.csv', delimiter=',')


max_val=np.amax(my_data)
min_val=np.amin(my_data)
print('min before cleaning is',min_val)
no_contact_runs=my_data[my_data == -80]
print('no contact runs',no_contact_runs.shape)

removed_no_contact_runs=my_data[my_data >= 10]
min_val=np.amin(removed_no_contact_runs)
max_val=np.amax(removed_no_contact_runs)
print('min after cleaning is ',min_val)
print('max after cleaning is ',max_val)

avg=np.average(removed_no_contact_runs)
print('average after cleaning is',avg)

y_pos=np.arange(len(removed_no_contact_runs))

plt.bar(y_pos,removed_no_contact_runs, align='center', alpha=0.5)
plt.show()
# fig = px.bar(removed_no_contact_runs)
# fig.show()

print('maximum is ',max_val)