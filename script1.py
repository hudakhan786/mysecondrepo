#### PROBLEM 1 ####
# Correc the mistakes and produce the following output:
# Johnny, the total of your purchase is $1,688.70

def calcTotal(amt, tax, name):
    mytotal = amt * (1 + tax)
    print(f"{name}, the total of your purchase is ${mytotal:,.2f}")

myname = 'Johnny'
price = 1560  # Corrected: Removed the comma to make it an integer
thetax = 0.0825  # Tax as a decimal

calcTotal(price, thetax, myname)





####  PROBLEM 2  ####
# print out ONLY the integers in the list below #
list1 = [1,'two',3.2,'four',5]

for i in list1:
    print(i)




#### PROBLEM 3 ####
# install the right library for the code below
# to work properly. The output will be a map.
# the filename is Baylor.html and it should
# open up in your browser. The library is Plotly.

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

lons = [-97.121041]
lats = [31.546872]
hover_texts = ['Baylor University<br>Enrollemt: 19,297<br>Male: 7,718<br>Female: 11,579']


data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'hovertext':hover_texts,
    'hoverinfo':"text",
    'marker': {'size':10,}
    }]

my_layout = Layout(title='Baylor University',geo_scope='usa')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig,filename='Baylor.html')
