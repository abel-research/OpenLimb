#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 16:38:36 2022

@author: fiona1

The following files should be downloaded prior to running this script:
Size Normalised Mean Limb shape (STL)
Full Statistical shape model modes (NPY)
Linear Regression Model (PKL)


This script allows for generation of synthetic residual limbs using the mode eigenvectors from the statistical shape model 
The eigenvalues (components) for each eigenvector controls the variation of each models shape from mean

Latter modes may be biased by the small training sample so have been commented out
but can be introduced to the random generated model if desired by uncommenting line 102

The current PCA model produces some mode combinations that result in limbs that are not anatomically possible
To combat this a skin only PCA model has been produced to generate the initial random shape
This script generates 100 possible values for each eigenvalue for the skin only modes (eigenvectors) 
which are evenly spaced between the max and min eigenvalues foreach mode found in the training data
A linear regression model has been made to preduct full mode scores from the skin only mode scores
100^10 possible generations exist 
The predicted eigenvalues and full model eigenvectors are then used to generate a model

The random generated model will be in its size normalised state
To create a 'real' size model a uniform scaling will need to be applied
To do this line 103 can be uncommented and [scale factor] replaced with the scale factor desired
The scale factor should represent the length of the complete (unamputated) tibia for the subject
Suggested value is 38.3076923 (average of the training data)


Include path to full mode eigenvectors (modes) as described in line 88
and Save path desired as described in line 131/134
Path to size normalised mean shape should be included in line 59
Path to linear regression pickled model should be included in line 82

"""



import numpy as np
import matplotlib.pyplot as plt
from ampscan import AmpObject
from ampscan.vis import vtkRenWin
import os
import random
import copy
import pickle
#%%

mean = AmpObject('Mean_Limb_Shape.stl', unify=False)


component = np.zeros([10,1])

component[0] = random.choice(np.linspace(0.431601080577505, -0.64019625102681, 100))

component[1] = random.choice(np.linspace(0.723425197902353, -0.311187317443235, 100))

component[2] = random.choice(np.linspace(0.582674704249994, -0.528299522762733, 100))

component[3] = random.choice(np.linspace(0.4029384683945435, -0.523554505179206, 100))

component[4] = random.choice(np.linspace(0.54674400016384,   -0.516577656488615, 100))

component[5] = random.choice(np.linspace(0.4949067620149133, -0.488697317341855, 100))

component[6] = random.choice(np.linspace(0.579899683618919, -0.643448957107683, 100))

component[7] = random.choice(np.linspace(0.539433628209152, -0.4367108140878626, 100))

component[8] = random.choice(np.linspace(0.4885733446644169, -0.38809672712546, 100))

component[9] = random.choice(np.linspace(0.501956586173615, -0.700663343671086, 100))

component = np.transpose(component)
#%%

pickled_model = pickle.load(open('/LR.pkl', 'rb'))
pickled_model.predict(component)

newcomponent = pickled_model.predict(component)[0,:]


X = np.load('/Modes.npy')

mode1 = X[:,0]
mode2 = X[:,1]
mode3 = X[:,2]
mode4 = X[:,3]
mode5 = X[:,4]
mode6 = X[:,5]
mode7 = X[:,6]
mode8 = X[:,7]
mode9 = X[:,8]
mode10 = X[:,9]
synthetic = copy.deepcopy(mean)
synthetic.vert = mean.vert + (mode1*newcomponent[0]).reshape([98412,3]) + (mode2*newcomponent[1]).reshape([98412,3]) + (mode3*newcomponent[2]).reshape([98412,3]) + (mode4*newcomponent[3]).reshape([98412,3]) + (mode5*newcomponent[4]).reshape([98412,3]) + (mode6*newcomponent[5]).reshape([98412,3]) 
#synthetic.vert = synthetic.vert + (mode7*newcomponent[6]).reshape([98412,3]) + (mode8*newcomponent[7]).reshape([98412,3]) + (mode9*newcomponent[8]).reshape([98412,3]) + (mode10*newcomponent[9]).reshape([98412,3])
#synthetic.vert = (synthetic.vert)* [scale factor]

synthetic.addActor()
win = vtkRenWin()
win.setnumViewports(1)
win.setBackground([1,1,1])
win.setView([0, -1, 0], 0)
win.SetSize(512, 512)
win.Modified()
win.OffScreenRenderingOn()
win.renderActors([synthetic.actor])
win.Render()
win.rens[0].GetActiveCamera().Azimuth(0)
win.rens[0].GetActiveCamera().Elevation(0)
win.rens[0].GetActiveCamera().SetParallelProjection(False)
win.Render()
im = win.getImage()

plt.axis('off')
plt.imshow(im, interpolation='bicubic')
plt.show()


#%%
i = 1
while os.path.exists("Random/Random%s.stl" % i):
    i += 1
   
synthetic.save('Random/' + "Random%s.stl" % i)