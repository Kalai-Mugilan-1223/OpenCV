# Explanation: Image/Video Resizing and Live Video Resolution Changing
## Introduction
This program demonstrates how to:
    
    -Resize images to a new width and height.
    -Resize videos frame by frame.
    -Change live video resolution while capturing from a webcam.
    -Resizing is an essential preprocessing step in many Computer Vision tasks, such as when working with neural networks that require fixed input sizes.

# Resizing an Image

## Explanation:
    
    -cv2.resize() scales the image to the specified dimensions.
    -The original and resized images are displayed side by side for comparison.

# Resizing a Video

## Explanation:
    
    -Each frame is resized using cv2.resize() with the specified dimensions.
    -The resized frames are displayed as a video stream.

# Changing Live Video Resolution

## Explanation

    -capture.set(3,width) and capture.set(4,height) adjust the webcam's resolution.
    -The live video stream reflects the new resolution in real-time.
