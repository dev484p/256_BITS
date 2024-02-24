# 256_BITS
Project for Internship at 256_BITS Studio : This repository contains code to detects object (50 classes) and creates a Depth Map of Images also renders a 3d map.

## Overview
1. For Object detection we use You Only Look Once: Unified, Real-Time Object Detection (YOLOv3) algorithm and a pre-trained model on 50 classes [coco](https://github.com/dev484p/256_BITS/blob/main/Obj_detection/coco.names). YOLO architecture is designed to simultaneously predict bounding boxes and class probabilities for multiple objects in an image. It divides the input image into a grid of cells and makes predictions for each cell. Each cell is responsible for predicting bounding boxes and associated class probabilities for objects that fall within that cell.
2. For Depth Estimation we use Monocular Depth Estimation: Mixing Datasets for Zero-shot Cross-dataset Transfer(MiDaS). This method is based on the ResNet (Residual Network). Model consists of a multi-scale encoder-decoder architecture inspired by the ResNet architecture.

# Installation
Set up dependencies:
```
conda env create -f environment.yaml
conda activate bits_256
```
# ERROR
I'm figuring out how to upload weights of the model in git repo
# Setup
1. Place one or more input images in the folder \images\input
2. Run the python file `Main.py`
3. The resulting depth maps and detected objects are written to the \images\Output_DepthMap and  \images\Output_ObjDetection folder respectively.

   Optional :
   You can run Intrinsics_Calibration.py to calibrate your camera before process. [refrence](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html)
# Render in Blender
You can render the obtained depth map to obtain the 3d model :
1. Create a mesh plane and subdevide it into 100-200 cuts.
2. Apply the depth map as a displacement : Select the plane mesh and switch to the "Modifiers" tab in the Properties panel. Add a "Deform - Displace" modifier to the plane.
3. Add a "new texture" from "Modifiers" tab and select the depth map texture from `/images/Output_DepthMap` from "Texture" tab.
4. To add image texture to the model : Go to "Shading" window and add a new material type. Now press `Shift + A` add "Texture -> Image Texture". Select the orignal image and link the color of "image texture" to "Principal BSDF"
5. You can further modify/ make changes as per your need.
# Refrence
1. https://arxiv.org/abs/1907.01341v3
2. https://pjreddie.com/darknet/yolo/#google_vignette
