# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 22:01:45 2019

@author: mirab
"""
from matplotlib.pyplot import figure, show
import numpy as np
from scipy.io import loadmat
from toolbox_02450 import clusterplot
from sklearn.mixture import GaussianMixture
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium
import os
from geocluster import GeoCluster

file_path = os.getcwd()
print(file_path)
df_hubs = pd.read_csv(file_path+"/DR_Data/Hubs_2019-4-2_1201.csv", parse_dates=[0,-1])

# Centered location (latitude, longitude) which we will use in all our following plots
initial_location = [55.6775757, 12.579571639999999]
#hub_map = folium.Map(location=initial_location, zoom_start=13)

X = df_hubs[['latitude','longitude']].values
data = [{'latti': d[0], 'longi': d[1]} for d in X]
cluster = GeoCluster()
cluster.set_bounds(55.817509, 12.290956, 55.600000, 12.638134) #north,west,south,east
cluster.set_grid(5,5)
cluster.populate(data)
cluster.use_clustering(True)
a=cluster.to_json()