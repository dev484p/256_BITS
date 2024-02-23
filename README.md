# 256_BITS
Project for Internship at 256_BITS Studio : This repository contains code to detects object (50 classes) and creates a Depth Map of Images also renders a 3d map.

## Overview
1. For Object detection we use open source YOLOv3 algorithm and a pre-trained model on 50 classes [coco]() 
2. For Depth Estimation we use Monocular Depth Estimation: Mixing Datasets for Zero-shot Cross-dataset Transfer(MiDaS). This method is based on the ResNet (Residual Network). Model consists of a multi-scale encoder-decoder architecture inspired by the ResNet architecture.

# Installation
1. Set up dependencies:
'''conda env create -f environment.yaml
conda activate midas-py310'''
