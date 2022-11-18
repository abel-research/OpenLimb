# OpenLimb: an Open Source Transtibial Residual Limb Model for Simulation and Design
F.E. Sunderland<sup>1</sup>, J.L. Bramley<sup>1,2</sup>, R.M.A. Al-Dirini<sup>3</sup>, J.W. Steer<sup>1,2</sup>, A.S. Dickinson<sup>1</sup>

1 Faculty of Engineering & Physical Sciences, University of Southampton, Southampton, UK

2 Radii Devices Ltd., Bristol, UK

3 College of Science & Engineering, Flinders University, Adelaide, Australia 

## Background: 
Computer aided design and manufacturing (CAD/CAM) may enable evidence based socket design through data science methods by leveraging prior CAD/CAM records [1] or when matched with simulation for socket fit prediction [2]. However, few researchers have access to the required volumetric medical imaging data, and there is cost, inconvenience, and risk associated with putting our relatively small community of eligible participants through CT or MRI scanning. 

## Aim: 
To produce an ‘openlimb’ open-access Statistical Shape Model (SSM), describing a population of residual limb shapes in a general manner, that can be published and shared with other researchers whilst preserving the security of the underlying imaging data. 

## Methods: 
<p align="center">
  <img src="../main/abstract/Process.png" alt="Generating a transtibial residual limb Statistical Shape Model from MRI data (1), segmented, aligned and registered (2) to produce a mean shape (3) and principal modes of shape variability (4) shown in anterior and lateral views, with associated variance %" width="600"/>
</p>
An SSM was generated using 11 MRI scans of transtibial residual limbs collected with ethical approval and written consent (Figure left). Scans were segmented (ScanIP, Synopsis Inc) to describe the skin surface and bones, exported as .stl meshes, and size normalised to intact tibia length, estimated using the person’s height [3]. Meshes were aligned by the residual tibia, and registered (Figure middle top). Finally, the mean vertex locations were calculated (Figure middle bottom), and Principal Component Analysis (PCA) was used to extract the dataset’s variation (Figure right). Results: Principal modes of variation represented independent changes in the length and profile of both bone and soft tissues. Synthetic individuals around the mean shape were created by selecting characteristics from these modes of variation. This model is only preliminary, as it is trained upon a limited population of residual limbs with similar morphology and ethnicity. Assumptions cannot be made about how it will represent limbs outside the training dataset. In a Leave-One-Out cross-validation test, the mean shape was reconstructed with root-mean-squared-error (RMSE) of 0.64–2.51mm (median 1.05mm). However, the left-out shapes were reconstructed with higher RMSE (3.27–11.3mm, median 4.8mm), indicating the training dataset must be expanded. However, to provide access and encourage other researchers to contribute their data, following appropriate approvals, this resource has been made publicly available at https://github.com/abel-research/openlimb, open access. 

## Discussion and Conclusion: 
Previously SSMs have described the exterior limb surface [1], but this is the first open access residual limb SSM, and includes bone geometry. This can provide researchers a wider pool of limb shapes for biomechanical analysis of socket designs and materials, and may enable estimation of personalised models to assess socket fit, predicting the bone geometry from external limb shape data. However, the model must be expanded with additional data, and we invite the community to contribute. 

## References: 
[1] Dickinson et al (2021), Prosthesis, https://doi.org/10.3390/prosthesis3040027;
[2] Steer et al. (2020), Biomech Model Mechanobiol, https://doi.org/10.1007/s10237-019- 01195-5; 
[3] M. Trotter (1970), Estimation of stature from intact long limb bones. 

## Approvals: 
ERGO65748.A1, ERGO41864.A1, ERGO29927, 2016_BLM_0009, HREC/18/SAC/225.

## Acknowledgments and Funding: 
RAEng (RF/130), EPSRC (EP/S02249X/1, EP/N509747/1, EP/M508147/1), and Alan Turing Institute (EP/N510129/1). We acknowledge Dr Peter Worsley, imaging centres at University Hospital Southampton NHS Foundation Trust (Southampton, UK) and Radiologie im Zentrum (Augsburg, Germany), and our study participants.
