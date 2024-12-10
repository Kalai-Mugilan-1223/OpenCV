
# Drawing Shapes and Text in OpenCV

This Python script demonstrates how to create and manipulate images using OpenCV. It covers methods to create a blank canvas, modify its color, and draw different shapes and text on it. Each method is highlighted with comments for easy understanding.

---

## Prerequisites
To run this script, make sure you have the following installed:
```
  - Python 3.x
  - OpenCV (`cv2`)
  - NumPy (`numpy`)
```

You can install the required libraries using:

    -pip install opencv-python numpy



## Features Demonstrated
The script includes the following functionalities:

### 1. **Creating a Blank Image**
- A blank image is created using `np.zeros()`. 
- Example:
  ```
  blank = np.zeros((500, 500), dtype='uint8')
  ```

### 2. **Changing Colors**
- The entire blank canvas or specific portions can be colored using slicing.
- Example:
  ```python
  blank[:] = 0, 255, 0  # Changes the entire canvas to green
  blank[200:300, 300:400] = 0, 255, 255  # Colors a specific portion yellow
  ```

### 3. **Drawing a Rectangle**
- Draws a rectangle on the canvas. The rectangle can have a border or be filled.
- Example:
  ```python
  cv.rectangle(blank, (0, 0), (250, 250), (0, 0, 255), thickness=3)  # Border
  cv.rectangle(blank, (250, 250), (500, 500), (0, 0, 255), thickness=-1)  # Filled
  ```

### 4. **Drawing a Circle**
- Draws a circle on the canvas.
- Example:
  ```python
  cv.circle(blank, (250, 250), 40, (255, 0, 0), thickness=3)
  ```

### 5. **Drawing a Line**
- Draws a straight line from one point to another.
- Example:
  ```python
  cv.line(blank, (0, 0), (500, 500), (255, 255, 255), thickness=3)
  ```

### 6. **Adding Text**
- Writes text on the canvas.
- Example:
  ```python
  cv.putText(blank, 'Hello World', (0, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (200, 255, 200), 2)
  ```

---

## Usage Instructions
1. Clone this repository or download the script.
2. Run the script in any Python environment:
   ```bash
   python draw.py
   ```
3. Each shape or text is displayed in a separate window. Close the window to view the next one.

---

## Notes
- **Thickness**:
  - Use `thickness=-1` or `cv.FILLED` to fill a shape.
- **Coordinates**:
  - Shapes are drawn using coordinates relative to the canvas dimensions.
  - Example: `(0, 0)` refers to the top-left corner.

---

## Sample Output
Here are some results you can expect:
1. A blank green canvas with yellow-colored portions.
2. Rectangles (bordered and filled) in red.
3. A blue circle.
4. A white diagonal line.
5. Text "Hello World" in a custom font.

---
