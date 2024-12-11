# Image Processing with OpenCV

This Python program demonstrates various basic image processing techniques using the OpenCV library. Each operation is applied to an input image and displayed in a new window for easy visualization.


## How to Use

1. Ensure the image you want to process is available at the specified path (`5.image-transformations\src\img.jpg`).
2. Run the Python script in an environment that supports GUI windows (e.g., your local machine, not online editors without GUI support).
3. The program will display several windows, each showcasing a specific image processing technique.
4. Close all windows by pressing any key to end the program.

## Features

### 1. **Reading an Image**
The program reads the input image using the `cv.imread()` function and displays it using `cv.imshow()`.

### 2. **Translating an Image**
The image is translated (shifted) along the x and y axes using the `cv.warpAffine()` function. The translation matrix is defined using NumPy's `np.float32`:
- Example: Shift the image by `-50` units along the x-axis and `100` units along the y-axis.

### 3. **Rotating an Image**
The image is rotated around a specified point using `cv.getRotationMatrix2D()` and `cv.warpAffine()`. The rotation point defaults to the center of the image if not provided.
- Example: Rotate the image by `45` degrees.
- Note: Rotating an already rotated image will not produce the same result as rotating the original image directly to the same angle.

### 4. **Resizing an Image**
The image is resized to specific dimensions using `cv.resize()`. Different interpolation methods can be used:
- For shrinking: `cv.INTER_AREA` (default)
- For enlarging: `cv.INTER_LINEAR` or `cv.INTER_CUBIC` (higher quality but slower)

Example: Resize the image to `500x500` pixels.

### 5. **Flipping an Image**
The image is flipped along specified axes using `cv.flip()`:
- `0`: Flips along the x-axis
- `1`: Flips along the y-axis
- `-1`: Flips along both axes

Example: Flip the image along the x-axis.

### 6. **Cropping an Image**
A specific region of the image is cropped using array slicing. Example: Crop the region from `[200:400, 100:400]` (y-axis range: 200-400, x-axis range: 100-400).

## Output

Each processing step will open a separate window displaying the result:
- `Image`: Original image.
- `Translated`: Translated image.
- `Rotated`: Rotated image.
- `Resized`: Resized image.
- `Flipped`: Flipped image.
- `Crop`: Cropped portion of the image.

## Notes

- Ensure the file path to the input image is correct.
- The program may not work in environments that do not support GUI (e.g., some remote servers or online IDEs).
- Adjust parameters (e.g., translation offsets, rotation angle, resizing dimensions) to experiment with the output.


