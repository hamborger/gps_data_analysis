from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import gpxpy
#from geopy.distance import 

"""
Source: http://andykee.com/visualizing-strava-tracks-with-python.html
Current author: Himanshu Rajmane
"""

data_path = 'lpq'
data = [f for f in listdir(data_path) if isfile(join(data_path,f))]

lat = []
lon = []

fig = plt.figure(facecolor = '1.0')
ax = plt.Axes(fig, [0., 0., 1., 1.], )
ax.set_aspect('equal')
ax.set_axis_off()
fig.add_axes(ax)

print "\n"

for activity in data:
    gpx_filename = join(data_path,activity)
    gpx_file = open(gpx_filename, 'r')
    gpx = gpxpy.parse(gpx_file)

    for track in gpx.tracks:
    	print "Distance in 2D: {0} in 3D: {1} \n".format(track.length_2d(), track.length_3d())
        for segment in track.segments:
            for point in segment.points:
                lat.append(point.latitude)
                lon.append(point.longitude)
    plt.plot(lon, lat, marker='o', markerfacecolor = 'red', markeredgecolor = 'red', markersize = 2, lw = 0.8, alpha = 0.5)
    lat = []
    lon = []

filename = data_path + '.png'
plt.savefig(filename, facecolor = fig.get_facecolor(), bbox_inches='tight', pad_inches=0, dpi=300)