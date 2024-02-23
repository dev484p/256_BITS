# Importing the required Libraries
import cv2
import os
import numpy as np

def detect():
    print("\n-----OBJECT DETECTION-----\n")
    path=f"{os.getcwd()}\..\images\input"
    files = os.listdir(path)
    for file in files:
        if file.endswith('.png') or file.endswith('.jpg'):
            print(f"Processing Object Detection on {file}")
            t=file
            file =os.path.join(path, file)
            img = cv2.imread(file)
            img = cv2.resize(img, None, fx=0.4, fy=0.4)
            height, width, channels = img.shape

            classes = []
            with open("coco.names", "r") as f:    # Class names
                classes = [line.strip() for line in f.readlines()]

            net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg") # Loading the Pretrained-Model (YOLO_V3)

            # Preprocessing images before putting them in Neural Network
            blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
            net.setInput(blob)
            output_layers =net.getUnconnectedOutLayersNames()
            outs = net.forward(output_layers) # Output layer of network

            class_ids,confidences,boxes = [],[],[]
            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.6:                # Object detected with confidence more than 60%
                        center_x = int(detection[0] * width)
                        center_y = int(detection[1] * height)
                        w = int(detection[2] * width)
                        h = int(detection[3] * height)

                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)

                        boxes.append([x, y, w, h])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)

            indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)    # Performing non-maximum suppression (NMS) 

            font = cv2.FONT_HERSHEY_PLAIN
            colors = np.random.uniform(0, 255, size=(len(classes), 3))

            for i in indexes.flatten():
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[class_ids[i]]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2) 
                cv2.putText(img, label, (x, y + 30), font, 2, color, 2)    # Labeling the detected object
            
            # Specify the output path
            outp=f"{path}/../Output_ObjDetection/Object_detectection_[{t}].jpg"
            cv2.imwrite(outp, img)

            # cv2.imshow("out",img)
            # cv2.waitKey(1000)

if __name__=='__main__':
    detect()