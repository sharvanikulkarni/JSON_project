"""
Process the JSON file named univ.json. Create 3 maps per instructions below.
The size of the point on the map should be based on the size of total enrollment. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons (refer to valueLabels.csv file)
The school name and the specific map criteria should be displayed when you hover over it.
(For example for Map 1, when you hover over Baylor, it should display "Baylor University, 81%")
Choose appropriate tiles for each map.


Map 1) Graduation rate for Women is over 50%
Map 2) Percent of total enrollment that are Black or African American over 10%
Map 3) Total price for in-state students living off campus over $50,000

"""
'''Map 1)Graduation rate for Women is over 50%'''
from cgitb import html
from importlib.metadata import metadata
import json

infile = open('univ.json','r')
outfile = open('univ_readable.json', 'w')

school_data = json.load(infile)

json.dump(school_data, outfile, indent=4)

'''================================='''

mags = []
lons = []
lats = []
hover_texts = []
graduation_women = []
qualified_schools = False

valuelabelfile = open("ValueLabels.csv", 'r')

for sc in school_data:
    mag = sc["Total  enrollment (DRVEF2020)"]
    lon1 = sc["Longitude location of institution (HD2020)"] 
    lat1 = sc["Latitude location of institution (HD2020)"]
    title = sc["instnm"]
    graduation_women = int(sc["Graduation rate  women (DRVGR2020)"] or 0)
    #print(graduation_women)
    #print(type(graduation_women))
    ncaa_status = sc["NCAA"]["NAIA member for football (IC2020)"]
    
    if(sc["NCAA"]["NAIA conference number football (IC2020)"]==132 or sc["NCAA"]["NAIA conference number football (IC2020)"]==107 or 
        sc["NCAA"]["NAIA conference number football (IC2020)"]==108 or sc["NCAA"]["NAIA conference number football (IC2020)"]==127 or 
        sc["NCAA"]["NAIA conference number football (IC2020)"]==130):
        qualified_schools = True
    else: qualified_schools = False
    #print(qualified_schools)
    

    title_percentage = sc["instnm"]+", " +str(graduation_women) + "%"
    if((graduation_women)>= 50 and ncaa_status==1 and qualified_schools == True):
        mags.append(mag)
        lons.append(lon1)
        lats.append(lat1)
        hover_texts.append(title_percentage)


'''
print(ncaa_status)
print(type(percentageofwomen))
print(mags[:10])
print(lons[:10])
print(lats[:10])
print(hover_texts[:10])
'''

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_texts,
    'marker':{
        'size':[0.0005*mag for mag in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Total  enrollment'}
    },
    }]

my_layout = Layout(title='universities with percentage of women over 50%')
fig ={'data':data, 'layout':my_layout}
#print(mags)

offline.plot(fig,filename='universities with percentage of women over 50%.html')


'''============================================================================='''
'''Map 2) Percent of total enrollment that are Black or African American over 10%'''

from cgitb import html
from importlib.metadata import metadata
import json

infile = open('univ.json','r')
outfile = open('univ_readable.json', 'w')

school_data = json.load(infile)

json.dump(school_data, outfile, indent=4)

'''================================='''

mags = []
lons = []
lats = []
hover_texts = []
graduation_women = []
qualified_schools = False
black_africanamerican = []

valuelabelfile = open("ValueLabels.csv", 'r')

for sc in school_data:
    mag = sc["Total  enrollment (DRVEF2020)"]
    lon1 = sc["Longitude location of institution (HD2020)"] 
    lat1 = sc["Latitude location of institution (HD2020)"]
    title = sc["instnm"]
    
    black_africanamerican = int(sc["Percent of total enrollment that are Black or African American (DRVEF2020)"] or 0)
    ncaa_status = sc["NCAA"]["NAIA member for football (IC2020)"]
    
    if(sc["NCAA"]["NAIA conference number football (IC2020)"]==132 or sc["NCAA"]["NAIA conference number football (IC2020)"]==107 or 
        sc["NCAA"]["NAIA conference number football (IC2020)"]==108 or sc["NCAA"]["NAIA conference number football (IC2020)"]==127 or 
        sc["NCAA"]["NAIA conference number football (IC2020)"]==130):
        qualified_schools = True
    else: qualified_schools = False
    
    title_percentage = sc["instnm"]+", " +str(black_africanamerican) + "%"
    if((black_africanamerican)>= 10 and ncaa_status==1 and qualified_schools == True):
        mags.append(mag)
        lons.append(lon1)
        lats.append(lat1)
        hover_texts.append(title_percentage)


'''
print(ncaa_status)
print(type(percentageofwomen))
print(mags[:10])
print(lons[:10])
print(lats[:10])
print(hover_texts[:10])
'''

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_texts,
    'marker':{
        'size':[0.001*mag for mag in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Total  enrollment'}
    },
    }]

my_layout = Layout(title='universities with black or african american population over 10%')
fig ={'data':data, 'layout':my_layout}
#print(mags)

offline.plot(fig,filename='universities with percentage of black or african american over 10%.html')


'''========================================================================================'''
'''Map 3) Total price for in-state students living off campus over $50,000'''

from cgitb import html
from importlib.metadata import metadata
import json

infile = open('univ.json','r')
outfile = open('univ_readable.json', 'w')

school_data = json.load(infile)

json.dump(school_data, outfile, indent=4)

'''================================='''

mags = []
lons = []
lats = []
hover_texts = []
graduation_women = []
qualified_schools = False
instate_offcampus = []


valuelabelfile = open("ValueLabels.csv", 'r')

for sc in school_data:
    mag = sc["Total  enrollment (DRVEF2020)"]
    lon1 = sc["Longitude location of institution (HD2020)"] 
    lat1 = sc["Latitude location of institution (HD2020)"]
    title = sc["instnm"]
    
    instate_offcampus = int(sc["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"] or 0)
    ncaa_status = sc["NCAA"]["NAIA member for football (IC2020)"]
    
    if(sc["NCAA"]["NAIA conference number football (IC2020)"]==132 or sc["NCAA"]["NAIA conference number football (IC2020)"]==107 or 
        sc["NCAA"]["NAIA conference number football (IC2020)"]==108 or sc["NCAA"]["NAIA conference number football (IC2020)"]==127 or 
        sc["NCAA"]["NAIA conference number football (IC2020)"]==130):
        qualified_schools = True
    else: qualified_schools = False
    
    title_percentage = sc["instnm"]+", " +str(instate_offcampus) + "%"
    if((instate_offcampus)>= 50000 and ncaa_status==1 and qualified_schools == True):
        mags.append(mag)
        lons.append(lon1)
        lats.append(lat1)
        hover_texts.append(title_percentage)


'''
print(ncaa_status)
print(type(percentageofwomen))
print(mags[:10])
print(lons[:10])
print(lats[:10])
print(hover_texts[:10])
'''

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_texts,
    'marker':{
        'size':[0.001*mag for mag in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Total  enrollment'}
    },
    }]

my_layout = Layout(title='universities with students from in-state living off campus')
fig ={'data':data, 'layout':my_layout}
#print(mags)

offline.plot(fig,filename='universities with students from in-state living off campus.html')

