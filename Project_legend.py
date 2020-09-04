import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
service_district = gpd.read_file(r'F:\Visulaisation Geospatial\Project\SEC\sec1.shp')
Hospital= pd.read_csv(r'F:\Visulaisation Geospatial\Project\H_csv\Hospitals.csv')
leg_kwds={'title':'Legend', 'loc': 'upper left', 'bbox_to_anchor':(1, 1.03), 'ncol':3}
service_district.plot(column='Name', cmap='tab20b',legend=True, legend_kwds=leg_kwds)
plt.scatter(x = Hospital.lng, y = Hospital.lat, c='r', edgecolor = 'white')
plt.title('Medical Services in Alexandria',fontsize=10)
plt.xlabel("longitude")
plt.ylabel('latitude')
plt.grid()
plt.show();