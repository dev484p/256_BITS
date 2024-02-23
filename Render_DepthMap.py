# Importing the Libraries
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt

def render_3d(path):
    # Importing Depth Map of the Stereo Images.
    depth_map=cv2.imread(path,cv2.IMREAD_GRAYSCALE)
    depth_map =depth_map.astype(np.uint8)
    print(depth_map.shape)
    # Creating Coordinate-Matrices from Coordinate-Vectors
    x, y = np.meshgrid(range(depth_map.shape[1]), range(depth_map.shape[0]))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(-x, y, depth_map, cmap='plasma')

    # Set axis and labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Depth')
    plt.show()

if __name__ == "__main__":
    render_3d(f"{os.getcwd()}\images\Outut_DepthMap\dataset_img3-dpt_beit_large_512.png")
