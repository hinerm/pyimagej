import time
import imagej

ij = imagej.init('/Applications/Fiji.app', headless=False)
ij.ui().showUI("swing")

while True:
    time.sleep(1)
