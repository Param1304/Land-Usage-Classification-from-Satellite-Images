#      Land-Usage-Classification-from-Satellite-Images

EuroSAT is a labelled dataset of 27000 Sentinel-2 satellite images. The Sentinel-2 satellite images are openly and freely accessible provided in the Earth observation program Copernicus. Satellite labels are divided into 10 categories. Sentinel-2 images are geo-referenced images covering 13 spectral-bands. 

![overview](https://github.com/Param1304/Land-Usage-Classification-from-Satellite-Images/blob/main/EuroSat/eurosat_overview_small.jpg?raw=True) 
The 10 classes are :-
'AnnualCrop','Forest','HerbaceousVegetation','Highway','Industrial','Pasture','PermanentCrop','Residential','River','SeaLake'

This Deep Learning projects aims at utilizing the deep CNN technology for Earth Observation tasks through satellite imagery. Our model is based ResNet-50 with input image dimensions 224X224X3. Trained on 21600 randomly shuffled images with GPU T4x2 and tested on 5400 images, a train accuracy of 95.12% and test accuracy of 40.17% was obtained. 

### Results Obtained:
![r1](https://github.com/Param1304/Land-Usage-Classification-from-Satellite-Images/blob/main/Results/Screenshot%20from%202024-03-11%2018-39-41.png?raw=True)
![](https://github.com/Param1304/Land-Usage-Classification-from-Satellite-Images/blob/main/Results/Screenshot%20from%202024-03-11%2018-41-38.png?raw=True)
![](https://github.com/Param1304/Land-Usage-Classification-from-Satellite-Images/blob/main/Results/Screenshot%20from%202024-03-11%2018-42-19.png?raw=True)
![](https://github.com/Param1304/Land-Usage-Classification-from-Satellite-Images/blob/main/Results/Screenshot%20from%202024-03-16%2001-06-09.png?raw=True)

### Tech Stack
1. Torch 
2. Torchvision
3. Torchsummary
4. pandas
5. ssl
6. GPU T4x2 


### Get this repo: 

```git clone https://github.com/Param1304/Land-Usage-Classification-from-Satellite-Images```

