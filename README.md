# openlimb
An Open-Source transtibial residual limb anatomic dataset

**License:** [![License](https://img.shields.io/badge/license-CC--BY--SA--4.0-green](../main/LICENSE)

There are over 5,000 new lower limb amputations every year in the UK, and a major challenge is rehabilitating people with amputations by enabling them to return to normal activities, using a prosthetic limb. However, the stump (or ‘residual limb’) is not initially suited for supporting the loads associated with standing or walking, and discomfort is common. The production of an appropriate patient-specific prosthetic socket is key, and today this is designed as a work of sculpture, by a highly experienced prosthetist. 

Many patient anatomy, surgery and disease factors can influence the socket design; however, few researchers have access to volumetric medical imaging data required to perform biomechanical analysis of socket designs. 

openlimb is a resource which contains a statistical description of transtibial amputated residual limbs based upon MRI scan data collected by the University of Southampton, UK, and Flinders University, Australia, in ethically-approved research projects. These descriptions include the external surface of the residual limb, the distal femur, patella, and residual tibia and fibula.

The Machine Learning method Principal Component Analysis (PCA) has been used to reduce the dimensionality of this anatomic dataset to generate a mean residual limb shape, and independent modes of shape variation (Figure 1, below). As such, the dataset describes the anatomic variation across the training dataset without including any identifiable representation of the individuals.

![A graphical summary of the mean limb shape and its variation in the first two principal modes](../main/abstract/Modes1and2.png)

This dataset is intended to allow the research community to perform more statistically robust prosthetic biomechanics research, without the costs, inconvenience, and risk of putting our relatively small community of eligible research participants through medical imaging.

This first version of openlimb is not fully statistically robust as it is based upon only eleven training datasets, who are representative only of individuals of a narrow ethnic diversity. We are keen however to build further individuals into the dataset subject to completing data sharing agreements between our institutions, and will acknowledge contributing researchers here.

For more detailed descriptions of the dataset and statistical testing behind it, please refer to the publication linked below.

Funding
--------

The research behind this dataset was funded by the following organisations:
- the Royal Academy of Engineering (RAEng), UK (grant no. RF/130, Principal Investigator A Dickinson)
- the Engineering & Physical Sciences Research Council (EPSRC) Centre for Doctoral Training in Prosthetics & Orthotics (grant no. EP/S02249X/1, Doctoral Researcher F Sunderland)

License
--------

This dataset uses a Creative Commons Attribution Share Alike 4.0 International license, which can be found [here](../main/LICENSE)

How to acknowledge
------------------

openlimb has been submitted for publication at the 2023 International Society for Prosthetics & Orthotics World Congress, for which the abstract will be included in the journal Prosthetics & Orthotics International. Please check back here in time, for a doi and full reference for you to cite if you use the dataset. 

Please cite as:
Sunderland et al., (2023). openlimb: [https://github.com/abel-research/openlimb](https://github.com/abel-research/openlimb).
