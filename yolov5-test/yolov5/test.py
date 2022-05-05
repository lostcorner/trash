import torch

aaa=torch.load('/home/ma-user/work/yolov5-test/yolov5/runs/train/exp29/weights/best.pt')
print(aaa['model'].names)