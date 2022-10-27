#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright: Fiona Sunderland 2022, fes1g16@soton.ac.uk
Release 2022-10: Preliminary model featuring mean shape and four modes of varition.

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

As such, in this preliminary model, 100^10 possible generations exist. 
However, at first release (2022-10) only the first four modes of variation are used. 
Later modes may be biased by the small training sample so have been commented out but each can be introduced 
to the random generation model if desired by uncommenting any of lines 95-100. This will be resolved in a future release.

The current PCA model produces some mode combinations that result in limbs that are not anatomically possible
To combat this a skin-only PCA model has been produced to generate the initial random shape
Then, a linear regression model is used to predict full model mode scores from the skin-only model mode scores
The predicted eigenvalues and full model eigenvectors are then used to generate an anatomically feasible model

The random generated model is in a size-normalised state.
To create a 'real' size model a uniform scaling should be applied.
To do this line 103 can be uncommented and (scale factor) replaced with the scale factor desired
The scale factor represents the desired length of the intact (unamputated) tibia for the subject
Suggested value is 383 (average of the training data in mm), though this can also be randomised (line 102).
The training data estimated intact tibia length range was 342.8 - 439.8 mm.

Include:
- path to full mode eigenvectors (modes) as described in line 79
- path to size normalised mean shape should be included in line 57
- path to linear regression pickled model should be included in line 74, and
- save path desired as described in line 128/131

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

component1 = random.choice(np.linspace( 0.3969076507620939,-0.693289827256320, 100))
component2 = random.choice(np.linspace(0.430594696988562,-0.4724907683193347, 100))
component3 = random.choice(np.linspace(0.531412217079820,-0.63083215890658, 100))
component4 = random.choice(np.linspace(0.622259054873768,-0.414452990023473, 100))
component5 = random.choice(np.linspace(0.643015261426913,-0.46809955936989, 100))
component6 = random.choice(np.linspace(0.79657182847319,-0.429207998843599, 100))
component7 = random.choice(np.linspace(0.541086924942068,-0.520915078278279, 100))
component8 = random.choice(np.linspace(0.5687548026612682,-0.67646222966793, 100))
component9 = random.choice(np.linspace(0.6004166136508616,-0.4838476788057197, 100))
component10 = random.choice(np.linspace(0.681020348628366,-0.4013039906579941, 100))
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
r = np.shape(mean.vert)[0]

synthetic.vert = mean.vert + (mode1*newcomponent[0]).reshape([r,3]) + (mode2*newcomponent[1]).reshape([r,3]) + (mode3*newcomponent[2]).reshape([r,3]) + (mode4*newcomponent[3]).reshape([r,3]) 
#synthetic.vert = synthetic.vert + (mode5*newcomponent[4]).reshape([r,3])
#synthetic.vert = synthetic.vert + (mode6*newcomponent[5]).reshape([r,3]) 
#synthetic.vert = synthetic.vert + (mode7*newcomponent[6]).reshape([r,3])
#synthetic.vert = synthetic.vert + (mode8*newcomponent[7]).reshape([r,3]) 
#synthetic.vert = synthetic.vert + (mode9*newcomponent[8]).reshape([r,3])
#synthetic.vert = synthetic.vert + (mode10*newcomponent[9]).reshape([r,3])

#scale factor =  random.choice(np.linspace(342.8, 439.8 , 100))
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
