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

component[0] = random.choice(np.linspace(-0.645371785671189 , 0.427348443638382, 100))
component[1] = random.choice(np.linspace(-0.319324715542056 , 0.722859466781963, 100))
component[2] = random.choice(np.linspace(-0.531020004804175 , 0.568278628676119, 100))
component[3] = random.choice(np.linspace(-0.467105361820503 , 0.49082193703341, 100))
component[4] = random.choice(np.linspace(-0.507628442354328 , 0.588103917292995, 100))
component[5] = random.choice(np.linspace(-0.549401967215317 , 0.534452396815857, 100))
component[6] = random.choice(np.linspace(-0.638947839088717 , 0.527592448114315, 100))
component[7] = random.choice(np.linspace(-0.400322982137944 , 0.411645427775137, 100))
component[8] = random.choice(np.linspace(-0.389004095285248 , 0.600009817120308, 100))
component[9] = random.choice(np.linspace(-0.588154695574681 , 0.621355103202168, 100))
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
