# Operation Pixel Merge

## Open CV
- images are treated as multidimensional arrays (numpy array).
- A coloured image has 3 channels(rbg) and each pixel is represented by an array with 3 values which correspond to the RBG color format.
- imread() is used to load the image and imwrite() is used to save a image
- Contour detection is the the feature which is used to find the shapes or boundaries within an image (here the shape is dot)
- Pillow here is mainly used to draw the final image using the co-ordinates of the dots and color, it can also be used to load and save the images.

### How code works:
- os is imported to interact with the file system
- I used hsv instead of rbg for the coloured dot because the first output i got was blue in color. Full form of hsv is Hue,saturation and value which give more precise color
- I find the co ordinates of the dots using the formula x = M["m10"] / M["m00"] and y = M["m01"] / M["m00"]
- I use the regex to find the images according to the number from assets
- Im using the above formula because i coudnt get the proper cordinates at first and had to use a function called moments which helps to calculate the centre of mass and using the this property we get a more precise x and y co ordinate of the dots
- To get the color of the dot we use the co ordinate x and y to access the color of the pixel in the original picture using the RBG format.
- For the blank images its skipped by appending None to the image im creating
- The lines are drawn using the draw.line() by the pillow but before giving the colors to it is reversed as as the original color is in the BGR format but pillow uses RBG format