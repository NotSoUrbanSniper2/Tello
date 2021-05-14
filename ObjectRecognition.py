import cv2
import matplotlib.pyplot as plt
config_file = 'ObjectRecognition/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'ObjectRecognition/frozen_inference_graph.pb'
model = cv2.dnn_DetectionModel(frozen_model,config_file)
classLabels = []
file_name = 'ObjectRecognition/Coco.txt'
with open(file_name,'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').split('\n')
print(len(classLabels))

model.setInputSize(320,320)
model.setInputScale(1.0/127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)

while True:
    success, img = cap.read()
    classIds, confs, bbox = model.detect(img, confThreshold=0.5)

    for classId, confidence, box in zip(classIds.flatten(), confs.flatten(),bbox):
        cv2.rectangle(img,box,color=(0,255,0),thickness=3)
        cv2.putText(img, classNames[classId-1].upper(),(box[0]+10,box[1]+30),cv2.FONT_HERSHEY_XOMPLEX,1,(0,255,0), 2)
    cv2.imshow("Output",img)
    cv2.waitKey(1)
