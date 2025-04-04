#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright: Fiona Sunderland 2025, fes1g16@soton.ac.uk
Release 2025-03: Preliminary model featuring mean shape and thirty-four modes of varition.

The following files should be downloaded prior to running this script:
Size Normalised Mean Limb shape (Mean_Limb_Shape.stl)
Full Statistical shape model modes (Modes.npy)
Linear Regression Model (LR.pkl)

The script requires the module ampscan.
ampscan can be found at https://github.com/abel-research/ampscan
Installation details can be found at https://ampscan.readthedocs.io/en/latest/

This script allows for generation of synthetic residual limbs using the eigenvectors (modes) from the statistical shape model.
The eigenvalues (components) for each eigenvector controls the variation of each model's shape from the mean.

This script generates 100 possible values for each eigenvalue which are evenly spaced between the max and min 
eigenvalues for each mode found in the training data. It then perturbs the mean shape by this amount in each eigenvector (mode)

As such, in this preliminary model, 100^34 possible generations exist. 

Later modes may be biased by the small training sample so can be removed by commenting out lines 159-190


The current PCA model produces some mode combinations that result in limbs that are not anatomically possible
To combat this a skin-only PCA model has been produced to generate the initial random shape
Then, a linear regression model is used to predict full model mode scores from the skin-only model mode scores
The predicted eigenvalues and full model eigenvectors are then used to generate an anatomically feasible model

The random generated model is in a size-normalised state.
To create a 'real' size model a uniform scaling should be applied.
To do this line 193 can be uncommented and (scale factor) replaced with the scale factor desired
The scale factor represents the desired length of the intact (unamputated) tibia for the subject
Suggested value is 378.52 (average of the training data in mm), though this can also be randomised (line 192).
The training data estimated intact tibia length range was 313.05 - 466.34113mm.

Include:
- path to full mode eigenvectors (components) as described in line 68
- path to size normalised mean shape should be included in line 57
- path to linear regression pickled model should be included in line 63, and
- save path desired as described in line 217/220

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

component = np.zeros([34,1])

#%%

pickled_model = pickle.load(open('/LR.pkl', 'rb'))
pickled_model.predict(component)

newcomponent = pickled_model.predict(component)[0,:]

X = np.load('/Components.npy')


component[0] = random.choice(np.linspace(-16.43, 25.46, 100))
component[1] = random.choice(np.linspace(-10.95 , 18.80, 100))
component[2] = random.choice(np.linspace(-9.59, 13.11, 100))
component[3] = random.choice(np.linspace(-7.40, 8.83, 100))
component[4] = random.choice(np.linspace(-5.68 , 7.40, 100))
component[5] = random.choice(np.linspace(-4.98 , 6.06, 100))
component[6] = random.choice(np.linspace(-4.07 , 5.14, 100))
component[7] = random.choice(np.linspace(-3.72, 3.92, 100))
component[8] = random.choice(np.linspace(-2.73 , 2.82, 100))
component[9] = random.choice(np.linspace(-2.35 , 2.60, 100))
component[10] = random.choice(np.linspace(-1.45, 2.71, 100))
component[11] = random.choice(np.linspace(-1.54 , 2.30, 100))
component[12] = random.choice(np.linspace(-1.09, 1.38, 100))
component[13] = random.choice(np.linspace(-0.93, 2.04, 100))
component[14] = random.choice(np.linspace(-0.94, 1.41, 100))
component[15] = random.choice(np.linspace(-1.00, 1.25, 100))
component[16] = random.choice(np.linspace(-1.07 , 1.16, 100))
component[17] = random.choice(np.linspace(-0.79, 0.82, 100))
component[18] = random.choice(np.linspace(-0.75 , 0.77, 100))
component[19] = random.choice(np.linspace(-0.72, 0.75, 100))
component[20] = random.choice(np.linspace(-0.61 , 0.71, 100))
component[21] = random.choice(np.linspace(-0.61 , 0.76, 100))
component[22] = random.choice(np.linspace(-0.49 , 0.51, 100))
component[23] = random.choice(np.linspace(-0.48, -0.48, 100))
component[24] = random.choice(np.linspace(-0.44 , 0.47, 100))
component[25] = random.choice(np.linspace(-0.40 , 0.45, 100))
component[26] = random.choice(np.linspace(-0.40 , 0.58, 100))
component[27] = random.choice(np.linspace(-0.41 , 0.51, 100))
component[28] = random.choice(np.linspace(-0.32, 0.41, 100))
component[29] = random.choice(np.linspace(-0.28 , 0.34, 100))
component[30] = random.choice(np.linspace(-0.28 , 0.31, 100))
component[31] = random.choice(np.linspace(-0.23, 0.27, 100))
component[32] = random.choice(np.linspace(-0.22 , 0.24, 100))
component[33] = random.choice(np.linspace(-0.25 , 0.33, 100))




component = np.transpose(component)
#%%

pickled_model = pickle.load(open('LR.pkl', 'rb'))
pickled_model.predict(component)

newcomponent = pickled_model.predict(component)[0,:]


X = np.load('Components.npy')

mode1 = X[0,:]
mode2 = X[1,:]
mode3 = X[2,:]
mode4 = X[3,:]
mode5 = X[4,:]
mode6 = X[5,:]
mode7 = X[6,:]
mode8 = X[7,:]
mode9 = X[8,:]
mode10 = X[9,:]
mode11 = X[10,:]
mode12 = X[11,:]
mode13 = X[12,:]
mode14 = X[13,:]
mode15 = X[14,:]
mode16 = X[15,:]
mode17 = X[16,:]
mode18 = X[17,:]
mode19 = X[18,:]
mode20 = X[19,:]
mode21 = X[20,:]
mode22 = X[21,:]
mode23 = X[22,:]
mode24 = X[23,:]
mode25 = X[24,:]
mode26 = X[25,:]
mode27 = X[26,:]
mode28 = X[27,:]
mode29 = X[28,:]
mode30 = X[29,:]
mode31 = X[30,:]
mode32 = X[31,:]
mode33 = X[32,:]
mode34 = X[33,:]
synthetic = copy.deepcopy(mean)

a = int(mean.vert.size)
b = int(a/3)
synthetic.vert = mean.vert + (mode1*newcomponent[0]).reshape([b,3]) + (mode2*newcomponent[1]).reshape([b,3]) 
+ (mode3*newcomponent[2]).reshape([b,3]) 
+ (mode4*newcomponent[3]).reshape([b,3]) 
+ (mode5*newcomponent[4]).reshape([b,3]) 
+ (mode6*newcomponent[5]).reshape([b,3])
+ (mode7*newcomponent[6]).reshape([b,3]) 
+ (mode8*newcomponent[7]).reshape([b,3]) 
+ (mode9*newcomponent[8]).reshape([b,3]) 
+ (mode10*newcomponent[9]).reshape([b,3]) 
+ (mode11*newcomponent[10]).reshape([b,3]) 
+ (mode12*newcomponent[11]).reshape([b,3]) 
+ (mode13*newcomponent[12]).reshape([b,3]) 
+ (mode14*newcomponent[13]).reshape([b,3]) 
+ (mode15*newcomponent[14]).reshape([b,3]) 
+ (mode16*newcomponent[15]).reshape([b,3]) 
+ (mode17*newcomponent[16]).reshape([b,3]) 
+ (mode18*newcomponent[17]).reshape([b,3]) 
+ (mode19*newcomponent[18]).reshape([b,3]) 
+ (mode20*newcomponent[19]).reshape([b,3]) 
+ (mode21*newcomponent[20]).reshape([b,3]) 
+ (mode22*newcomponent[21]).reshape([b,3]) 
+ (mode23*newcomponent[22]).reshape([b,3]) 
+ (mode24*newcomponent[23]).reshape([b,3]) 
+ (mode25*newcomponent[24]).reshape([b,3]) 
+ (mode26*newcomponent[25]).reshape([b,3]) 
+ (mode27*newcomponent[26]).reshape([b,3]) 
+ (mode28*newcomponent[27]).reshape([b,3]) 
+ (mode29*newcomponent[28]).reshape([b,3]) 
+ (mode30*newcomponent[29]).reshape([b,3]) 
+ (mode31*newcomponent[30]).reshape([b,3]) 
+ (mode32*newcomponent[31]).reshape([b,3]) 
+ (mode33*newcomponent[32]).reshape([b,3]) 
+ (mode34*newcomponent[33]).reshape([b,3])

#scale factor =  random.choice(np.linspace(313.05, 466.34, 100))
#synthetic.vert = (synthetic.vert)* (scale factor)

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
