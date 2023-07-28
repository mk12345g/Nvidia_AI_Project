from jetson_inference import imageNet
from jetson_utils import videoSource, videoOutput

net = imageNet(model="resnet18.onnx", labels="labels.txt", input_blob="input_0", output_blob="output_0") 
camera = videoSource("/dev/video0")      # '/dev/video0' for V4L2

while True:
    img = camera.Capture()

    if img is None: # capture timeout
        continue

    class_idx, confidence = net.Classify(img)
    if class_idx == 0 and confidence > 0.9:
        print("fire")
