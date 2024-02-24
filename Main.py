import os
from Obj_detection.YOLO_img import detect
from run import run

def obj_detection():
    os.chdir(f"{os.getcwd()}\Obj_detection")
    detect()

def Depth_Map():
    os.chdir(f"{os.getcwd()}\..")
    run(input_path=f"{os.getcwd()}\images\input",output_path=f"{os.getcwd()}\images\Outut_DepthMap",model_type="dpt_beit_large_512",model_path="weights/dpt_beit_large_512.pt")

if __name__=="__main__":
    obj_detection()
    Depth_Map()