# Depth-estimation
Depth estimation using a stereo pair

## Theory
Here we use a stereo pair and obtain depth map of the corresponding scene.Depth map is equivalent with Disparity map as depth and disparity have a direct relationship i.e, less depth - more disparity.
So by obtaining depth map, it means that we obtain a gray scale image ,high intensity means less depth and vice-versa.

### Simple Depth by only Data Cost:
We proceed as follows to obtain the disparity map.

We select a fixed number of disparity levels and a Data Cost D for each pixel having a disparity value d

D(i,j,d)= squared difference between PxP patch centered at (i,j) in left image and at (i,j+d) in right image.

This makes sense if the stereo pair is vertically adjusted and the disparity is only along horizontal direction which is always usually the case.

We then assign that diparity to each pixel which gives minimun Data cost.

### Cost using both Data Cost and Smoothness Cost

Along with the data cost D(i,j,d) we need to consider another cost which accounts for the affinity of neighbourhood pixels, meaning the disparity should vary gradually along the neighbourhood.

                                        E = D + pS   - p is regularizing parameter
                                        
We need to use graph cut algorithm to solve the above cost minimization to arrive at a local minima.

## Results

## Simple Data Cost

### 1x1 Patch
<img src="https://github.com/sarath-mutnuru/Depth-estimation/blob/master/Results/map_P1.png" width="300" title="1x1 Patch"><img src="https://github.com/sarath-mutnuru/Depth-estimation/blob/master/Results/tsukuba_P1.png" width="300">

### 11x11 Patch
<img src="https://github.com/sarath-mutnuru/Depth-estimation/blob/master/Results/map_P11.png" width="300"><img src="https://github.com/sarath-mutnuru/Depth-estimation/blob/master/Results/tsukuba_P11.png" width="300">

### 23x23 Patch

<img src="https://github.com/sarath-mutnuru/Depth-estimation/blob/master/Results/map_P23.png" width="300"><img src="https://github.com/sarath-mutnuru/Depth-estimation/blob/master/Results/tsukuba_P23.png" width="300">



