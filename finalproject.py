from jetson_inference import imageNet
from jetson_utils import videoSource, videoOutput

net = imageNet(model="resnet18.onnx", labels="labels.txt")
camera = videoSource("csi://0")      # '/dev/video0' for V4L2

while True:
    img = camera.Capture()

    if img is None: # capture timeout
        continue

    detections = net.Detect(img)
    
   
