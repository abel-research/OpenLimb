# OpenLimb
An Open-Source transtibial residual limb anatomic dataset

**DOI:** [![DOI](https://img.shields.io/badge/doi-10.1097/pxr.0000000000000240-brightgreen)](https://doi.org/10.1097/pxr.0000000000000240)
**Data License:** [![License](https://img.shields.io/badge/license-CC--BY--SA--4.0-green)](../main/DATA-LICENSE)
**Code License:** [![License](https://img.shields.io/badge/license-MIT-blueviolet)](../main/CODE-LICENSE)

There are over 5,000 new lower limb amputations every year in the UK, and a major challenge is rehabilitating people with amputations by enabling them to return to normal activities, using a prosthetic limb. However, the stump (or ‘residual limb’) is not initially suited for supporting the loads associated with standing or walking, and discomfort is common. The production of an appropriate patient-specific prosthetic socket is key, and today this is designed as a work of sculpture, by a highly experienced prosthetist. 

Many patient anatomy, surgery and disease factors can influence the socket design; however, few researchers have access to volumetric medical imaging data required to perform biomechanical analysis of socket designs. 

OpenLimb is a resource which contains a statistical description of transtibial amputated residual limbs based upon MRI scan data collected by the University of Southampton, UK, and Flinders University, Australia, in ethically-approved research projects. These descriptions include the external surface of the residual limb, the distal femur, patella, and residual tibia and fibula  (Figure 1, below).

<p align="center">
  <img src="../main/abstract/Process.png" alt="Generating a transtibial residual limb Statistical Shape Model from MRI data (1), segmented, aligned and registered (2) to produce a mean shape (3) and principal modes of shape variability (4) shown in anterior and lateral views, with associated variance %" width="600"/>
</p>

The Machine Learning method Principal Component Analysis (PCA) has been used to reduce the dimensionality of this anatomic dataset to generate a mean residual limb shape, and independent modes of shape variation (Figure 2, below). As such, the dataset describes the anatomic variation across the training dataset without including any identifiable representation of the individuals.

<p align="center">
  <img src="../main/abstract/Modes1&2.png" alt="Creating example virtual individuals from the mean limb shape and its variation in the first two principal modes" width="250"/>
</p>

This dataset is intended to allow the research community to perform more statistically robust prosthetic biomechanics research, without the costs, inconvenience, and risk of putting our relatively small community of eligible research participants through medical imaging.

This first version of openlimb is not fully statistically robust as it is based upon only eleven training datasets, who are representative only of individuals of a narrow ethnic diversity. We are keen however to build further individuals into the dataset subject to completing data sharing agreements between our institutions, and will acknowledge contributing researchers here.

In the meantime you can download the preliminary model's mean shape, and virtual patient shapes covering 95% of training dataset variation in residual limb length and soft tissue bulbous-conical profile, as .stl files. These are normalised to the fractional intact length of the tibia, so should be scaled up to the desired intact tibia length.

For more detailed descriptions of the dataset and statistical testing behind it, please refer to the publication linked below.

Funding
--------

The research behind this dataset was funded by the following organisations:
- the Royal Academy of Engineering (RAEng), UK (grant no. RF/130 (A Dickinson))
- the Alan Turing Institute, UK (grant no. EP/N510129/1 (A Dickinson))
- the Engineering & Physical Sciences Research Council (EPSRC), UK (grant nos. EP/S02249X/1 (F Sunderland), EP/N509747/1 (J Bramley), EP/M508147/1 (J Steer))
- the European Union 'Eurostars' programme (grant no. 9396 (A Dickinson & J Steer))

Ethical Approvals
--------

This secondary data analysis work was granted ethical approval by the University of Southampton's Ethics and Research Governance Office (ERGO 65748.A1)

Original MRI data collection work was granted ethical approval by the following committees:
- Fraunhofer IPA Biomechanics Laboratory (2016_BLM_0009)
- the University of Southampton's Ethics and Research Governance Office (ERGO 41864.A1, ERGO 29927)
- the Southern Adelaide Clinical Human Research Ethics Committee (HREC/18/SAC/225)

License
--------

This dataset uses a Creative Commons Attribution Share Alike 4.0 International license, which can be found [here](../main/LICENSE)
Share Alike means that if you remix, transform, or build upon the dataset, you must distribute your contributions under the same license.

How to acknowledge
------------------

OpenLimb has been accepted for presentation at the 2023 International Society for Prosthetics & Orthotics World Congress, for which the abstract is published in a special issue of the journal Prosthetics & Orthotics International, available at https://doi.org/10.1097/pxr.0000000000000240. 

Please cite as:
F.E. Sunderland, J.L. Bramley, R.M.A. Al-Dirini, J.W. Steer, P.R. Worsley & A.S. Dickinson (2023), OpenLimb: an Open Source Transtibial Residual Limb Model for Simulation and Design [https://github.com/abel-research/openlimb](https://github.com/abel-research/OpenLimb).
