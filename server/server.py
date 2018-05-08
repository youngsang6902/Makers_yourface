#!/usr/bin/env python3
#
# Example to compare the faces in two images.
# Brandon Amos
# 2015/09/29
#
# Copyright 2015-2016 Carnegie Mellon University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import visitor
import message
import path
import time
start = time.time()

import argparse
import cv2
import itertools
import os
from socket import *
TCP_IP = '[Server IP]'
TCP_PORT = [port_number]

import numpy as np
np.set_printoptions(precision=2)

import openface

member = ['[member1 name]','[member2 name]','[member3 name]',...,'[memberN name]','Visitor']

def getRep(imgPath):
    if args.verbose:
        print("Processing {}.".format(imgPath))
    bgrImg = cv2.imread(imgPath)
    if bgrImg is None:
        raise Exception("Unable to load image: {}".format(imgPath))
    rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)

    if args.verbose:
        print("  + Original size: {}".format(rgbImg.shape))

    start = time.time()
    bb = align.getLargestFaceBoundingBox(rgbImg)
    if bb is None:
        raise Exception("Unable to find a face: {}".format(imgPath))
    if args.verbose:
        print("  + Face detection took {} seconds.".format(time.time() - start))

    start = time.time()
    alignedFace = align.align(args.imgDim, rgbImg, bb,
                              landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
    if alignedFace is None:
        raise Exception("Unable to align image: {}".format(imgPath))
    if args.verbose:
        print("  + Face alignment took {} seconds.".format(time.time() - start))

    start = time.time()
    rep = net.forward(alignedFace)
    if args.verbose:
        print("  + OpenFace forward pass took {} seconds.".format(time.time() - start))
        print("Representation:")
        print(rep)
        print("-----\n")
    return rep

while True:
	
	visit = visitor.check()
	
	if visit == True:
	    	    
	    fileDir = os.path.dirname('~/openface/demos/')
	    print(fileDir)
	    modelDir = os.path.join(fileDir, '..', 'models')
	    print(modelDir)
	    dlibModelDir = os.path.join(modelDir, 'dlib')
	    print(dlibModelDir)
	    openfaceModelDir = os.path.join(modelDir, 'openface')
	    print(openfaceModelDir)

	    parser = argparse.ArgumentParser()
	    parser.add_argument('imgs', type=str, nargs='+', help="Input images.")
	    parser.add_argument('--dlibFacePredictor', type=str, help="Path to dlib's face predictor.",default=os.path.join(dlibModelDir, "shape_predictor_68_face_landmarks.dat"))
	    parser.add_argument('--networkModel', type=str, help="Path to Torch network model.",default=os.path.join(openfaceModelDir, 'nn4.small2.v1.t7'))
	    parser.add_argument('--imgDim', type=int,help="Default image dimension.", default=96)
	    parser.add_argument('--verbose', action='store_true')
	    args = parser.parse_args()

	    if args.verbose:
	        print("Argument parsing and loading libraries took {} seconds.".format(time.time()-start))
	    start = time.time()
	    align = openface.AlignDlib(args.dlibFacePredictor)
	    net = openface.TorchNeuralNet(args.networkModel, args.imgDim)
	    if args.verbose:
	        print("Loading the dlib and OpenFace models took {} seconds.".format(time.time()-start))

	    i = 0
	    percent = 0
	    msg = '0'
	    for (img1, img2) in itertools.combinations(args.imgs, 2):
	        
	        i = i+1
	        if i<len(member):
	            try:
	                d = getRep(img1) - getRep(img2)
	                percent = -25*np.dot(d,d)+100
	                print("Comparing {} with {}.".format(img1, img2))
	                print("  + Squared l2 distance between representations: {:0.3f}".format(np.dot(d, d)))
	                print("{:0.2f}".format(percent))
	            except Exception as err:
	                print(err)
	                i=len(member)
	                break

	            if percent > 90:
	                msg = '1'
	                message.send(i-1)
	                break
	        else:
	            break

	    path.move(member[i-1])

	    c=socket(AF_INET, SOCK_STREAM)
	    c.connect((TCP_IP,TCP_PORT))
	    c.sendall(msg.encode())
	    c.close()
