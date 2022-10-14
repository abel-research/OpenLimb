"""
Created on Thu Oct 13 12:18:13 2022

@author: fiona1


This script allows for generation of synthetic residual limbs using the mode eigenvectors from the statistical shape model 
The eigenvalues (components) for each eigenvector controls the variation of each models shape from mean
This script generates 100 possible values for each eigenvalue which are evenly spaced between the max and min eigenvalues for
each mode found in the training data
The script randomnly selects one of these values for each mode and uses these to generate a model
100^10 possible generations exist

The random generated model will be in its size normalised state
To create a 'real' size model a uniform scaling will need to be applied
To do this line 80 can be uncommented and [scale factor] replaced with the scale factor desired
The scale factor should represent the length of the complete (unamputated) tibia for the subject
Suggested value is 38.3076923 (average of the training data)

Include path to files as described in line 32
and Save path desired as described in line 105
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
from ampscan import AmpObject
from ampscan.vis import vtkRenWin
import os
import random
import copy
#%%
'''
INCLUDE PATH FILE TO THE MEAN LIMB SHAPE (SIZE NORMALISED VERSION NOT FULL SIZE)

AND PATH TO THE MODE EIGENVECTOR NUMPY FILE

'''
mean = AmpObject('openlimb/version-2022-10/Mean_Limb_Shape.stl', unify=False)

X = np.load('openlimb/version-2022-10//Modes.npy')


#%%

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

component1 = random.choice(np.linspace(0.3864223,-0.71002353, 100))

component2 = random.choice(np.linspace(0.42787370,-0.447640182, 100))

component3 = random.choice(np.linspace(0.74776385,-0.40564438, 100))

component4 = random.choice(np.linspace(0.57879674,-0.5025366, 100))

component5 = random.choice(np.linspace(0.41903860,-0.45823058, 100))

component6 = random.choice(np.linspace(0.41079892,-0.64177206, 100))

component7 = random.choice(np.linspace(0.59457931,-0.4494440, 100))

component8 = random.choice(np.linspace(0.399288,-0.7517587, 100))

component9 = random.choice(np.linspace(0.57239728,-0.49338007, 100))

component10 = random.choice(np.linspace(0.65234080,-0.39862027, 100))

#%%

synthetic = copy.deepcopy(mean)
synthetic.vert = mean.vert + (mode1*component1).reshape([46665,3]) + (mode2*component2).reshape([46665,3]) + (mode3*component3).reshape([46665,3]) + (mode4*component4).reshape([46665,3]) + (mode5*component5).reshape([46665,3]) + (mode6*component6).reshape([46665,3]) + (mode7*component7).reshape([46665,3]) + (mode8*component8).reshape([46665,3]) + (mode9*component9).reshape([46665,3]) + (mode10*component10).reshape([46665,3])
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
'''
INCLUDE SAVE PATH LOCATION LEAVE RANDOM%S IN NAME TO ALLOW FOR AUTOMATIC INCREMENTAL NUMBERING TO SAVE MULTIPLE
RANDOM GENERATIONS
'''
i = 1
while os.path.exists("openlimb/version-2022-10/Synthetic/Random/Random%s.stl" % i):
    i += 1
   
synthetic.save('openlimb/version-2022-10/Synthetic/Random/' + "Random%s.stl" % i)