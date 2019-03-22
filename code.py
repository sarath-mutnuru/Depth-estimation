# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 22:50:16 2019

@author: SARATHKUMAR
"""

import cv2
import numpy as np
#read stereo images
# =============================================================================
# imL=cv2.imread('map0.pgm',-1).astype('float32')/255.0
# imR=cv2.imread('map1.pgm',-1).astype('float32')/255.0
# #Ground-truth
# imGT=cv2.imread('disp0.pgm',-1)
# =============================================================================

imL=cv2.imread('tsukuba0.ppm',0).astype('float32')/255.0
imR=cv2.imread('tsukuba1.ppm',0).astype('float32')/255.0
#Ground-truth
imGT=cv2.imread('disp0.pgm',-1)

k=31 # no of disparity levels
B=5# Patch size of 2B+1 x 2B+1

D      = np.ones( list( imL.shape )+[ k ] )
d_list = [ int( x ) for x in np.linspace( 0, k-1, k ) ]

for d in d_list:
    sq_diff = np.square( imR[ :, d: ] - imL[ :, 0:imL.shape[ 1 ] - d ] )
    result  = np.zeros_like(sq_diff)
    padded  = np.pad( sq_diff, B, mode = 'constant' )
    for r in range( B, padded.shape[ 0 ] - B ):
        for c in range( B, padded.shape[ 1 ] - B):       
            vals = [ padded[ rr ][ cc ] for rr in range( r-B, r+B+1 ) for cc in range( c-B, c+B+1 ) ]
            result[ r-B, c-B ] = np.mean( vals )   
    D[ :, 0:imL.shape[ 1 ] - d, d ] = result
    
dm_est    = np.argmin( D, axis = 2 )
dm_est_img= ( dm_est*8 ).astype( np.uint8 )
            
            
    