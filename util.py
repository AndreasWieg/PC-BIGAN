import numpy as np
from matplotlib.pylab import scatter
import random
from plyfile import PlyData, PlyElement
import matplotlib.pyplot as plt
from pylab import scatter
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import time
from pyntcloud import PyntCloud
import os
import sys
import itertools
import re


def shuffle_data(training_data):
     np.random.shuffle(training_data)
     return training_data

def save_pointcloud(leaf,counter,leaf_name,number_points):
	leaf = np.asarray(leaf)
	leaf = np.reshape(leaf,(number_points,3))
	leaf_final = []
	x = 0
	for e in enumerate(leaf):
		leaf_final.append(tuple(leaf[x]))
		x = x +1
	vertex = np.array(leaf_final,dtype=[('x', 'f4'), ('y', 'f4'),('z', 'f4')])
	el = PlyElement.describe(vertex, 'vertex')
	PlyData([el]).write('%s_%d.ply' % (leaf_name,counter))


def load_data(number_points,reduction_step):
	training_data = []
	#counter = 1
	for file in os.listdir("C:/Users/Andreas/Desktop/PG-PGGAN/table_new_%d" % (reduction_step)):
		if file.endswith(".ply"):
			cloud = PyntCloud.from_file("C:/Users/Andreas/Desktop/PG-PGGAN/table_new_%d/%s" % (reduction_step,file))
			cloud_array = np.asarray(cloud.points)
			training_data.append(cloud_array)
	return training_data

def load_data_table(number_points,reduction_step):
    training_data = []
    counter = 1
    if not os.path.exists("C:/Users/Andreas/Desktop/PG-PGGAN/table_new_%d" % reduction_step):
        os.mkdir("C:/Users/Andreas/Desktop/PG-PGGAN/table_new_%d" % reduction_step)
        table_uri = ("C:/Users/Andreas/Desktop/PG-PGGAN/table_new_%d" % reduction_step)
        print(table_uri)
        for file in os.listdir("C:/Users/Andreas/Desktop/PG-PGGAN/table"):
            if file.endswith(".ply"):
                cloud = PyntCloud.from_file("C:/Users/Andreas/Desktop/PG-PGGAN/table/%s" % file)
                cloud = cloud.get_sample(name="points_random",n = number_points)
                cloud = PyntCloud(cloud)
                cloud_array = np.asarray(cloud.points)
                cloud.to_file(table_uri + "/out_file_%d.ply" % (counter))
                counter = counter + 1
                training_data.append(cloud_array)

    else:
        training_data = load_data(number_points,reduction_step)
    print(len(training_data))
    print("data loaded")
    training_data = np.asarray(training_data)
    print(training_data.shape)
    print("getting Trainingdata into the right format")
    #training_data = training_data.reshape(8509,3072)
    print(training_data.shape)
    print(" trainingdata formated")
    return training_data
