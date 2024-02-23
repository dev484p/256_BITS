# 256_BITS
Project for Internship at 256_BITS Studio : This repository contains code to detects object (50 classes) and creates a Depth Map of Images also renders a 3d map.

## Overview
1. For Object detection we use open source YOLOv3 algorithm and a pre-trained model on 50 classes [coco]() 
2. For Depth Estimation we use Monocular Depth Estimation: Mixing Datasets for Zero-shot Cross-dataset Transfer(MiDaS). This method is based on the ResNet (Residual Network). Model consists of a multi-scale encoder-decoder architecture inspired by the ResNet architecture.

# Installation
Set up dependencies:
```
conda env create -f environment.yaml
conda activate bits_256
```

# Setup
1. Place one or more input images in the folder \images\input
2. Run the python file `Main.py`
3. The resulting depth maps and detected objects are written to the \images\Output_DepthMap and  \images\Output_ObjDetection folder respectively.

   Optional :
   You can run Intrinsics_Calibration.py to calibrate your camera before process.

# Refrence
1. https://arxiv.org/abs/1907.01341v3
2. https://pjreddie.com/darknet/yolo/#google_vignette
