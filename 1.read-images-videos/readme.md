# Explanation: Reading Images and Videos Using OpenCV
## Introduction
This program demonstrates how to use OpenCV to:

    -Read and display images.
    -Read and play videos.
    -Handle errors while loading files.
This is a fundamental operation in Computer Vision, serving as the foundation for many image and video processing tasks.

# Reading and Displaying an Image
## Explanation:
    
    -cv2.imread() reads the image file specified by its path.
    -cv2.imshow() displays the loaded image in a window named 'Image'.
    -cv2.waitKey(0) waits indefinitely until a key is pressed.

# Reading and Playing a Video

## Explanation:

    -cv2.VideoCapture() opens the video file.
    -The while loop reads and displays each frame using capture.read() and cv2.imshow().
    -The loop exits when there are no more frames (ret is False) or when the user presses 'd'.
    -capture.release() and cv2.destroyAllWindows() ensure proper resource cleanup.
