# Image Processing with OpenCV

This Python program demonstrates various basic image processing techniques using the OpenCV library. Each operation is applied to an input image and displayed in a new window for easy visualization.


## How to Use

1. Ensure the image you want to process is available at the specified path (`4.basic_functions\src\img.jpg`).
2. Run the Python script in an environment that supports GUI windows (e.g., your local machine, not online editors without GUI support).
3. The program will display several windows, each showcasing a specific image processing technique.
4. Close all windows by pressing any key to end the program.

## Features

### 1. **Reading an Image**
The program reads the input image using the `cv.imread()` function and displays it using `cv.imshow()`.

### 2. **Converting to Grayscale**
The image is converted to grayscale using `cv.cvtColor()` with the `cv.COLOR_BGR2GRAY` flag.

### 3. **Blurring the Image**
The image is blurred using Gaussian Blur with a kernel size of `(7,7)` using `cv.GaussianBlur()`.

### 4. **Creating Edge Cascade**
Edges in the image are detected using the Canny Edge Detection method (`cv.Canny()`), with threshold values of `200` and `100`.

### 5. **Dilating the Image**
The edges detected by the Canny function are dilated using `cv.dilate()` with a kernel size of `(7,7)` to join broken parts and remove noise.

### 6. **Eroding the Image**
The dilated image is eroded using `cv.erode()` with a kernel size of `(3,3)` to remove small white noises and detach connected objects.

### 7. **Resizing the Image**
The image is resized to dimensions `(540, 675)` using `cv.resize()`.

### 8. **Cropping the Image**
A specific region of the image (coordinates `[75:500, 200:500]`) is cropped and displayed using slicing.

## Output

Each processing step will open a separate window displaying the result:
- `Image`: Original image.
- `Gray Image`: Grayscale version of the image.
- `Blurred Image`: Blurred version of the image.
- `Edged Image`: Edges detected using Canny Edge Detection.
- `Dilated Image`: Dilated edges.
- `Eroded Image`: Eroded edges.
- `Resized`: Resized image.
- `Cropped-Image`: Cropped portion of the image.

## Notes
- Ensure the file path to the input image is correct.
- The program may not work in environments that do not support GUI (e.g., some remote servers or online IDEs).
- You can adjust parameters like kernel size and thresholds to experiment with the output.

## Example Input
An image file, such as `img.jpg`, located at `4.basic_functions\src\`.

## Example Output
The program creates a series of windows displaying the results of each image processing step.

