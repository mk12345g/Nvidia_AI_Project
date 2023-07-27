from jetson_inference import imageNet
from jetson_utils import videoSource, videoOutput

net = imageNet(model="resnet18.onnx", labels="labels.txt")
camera = videoSource("csi://0")      # '/dev/video0' for V4L2
display = videoOutput("display://0") # 'my_video.mp4' for file

while display.IsStreaming():
    img = camera.Capture()

    if img is None: # capture timeout
        continue

    detections = net.Detect(img)
    
    display.Render(img)
    display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))