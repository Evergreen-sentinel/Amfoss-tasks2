import os
import cv2
import numpy as np
from PIL import Image, ImageDraw
import re

def dot_color(image_path):
    image = cv2.imread(image_path)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    final_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

    contours_yellow, _ = cv2.findContours(final_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours_yellow:
        largest_yellow_contour = max(contours_yellow, key=cv2.contourArea)
        M = cv2.moments(largest_yellow_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            color = image[cy, cx].tolist()  
            return (cx, cy), color

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(largest_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            color = image[cy, cx].tolist() 
            return (cx, cy), color

    return None, None

def extract_number(filename):
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else float('inf')

def purewhite(image_path):
    image = cv2.imread(image_path)
    return np.all(image == 255)

def drawimage(folder_path, output_image_path):
    images = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    images.sort(key=extract_number)

    points_and_colors = []

    for img_name in images:
        img_path = os.path.join(folder_path, img_name)
        if purewhite(img_path):
            points_and_colors.append((None, None))
            continue

        dot_info, color = dot_color(img_path)
        if dot_info is not None:
            points_and_colors.append((dot_info, color))

    if points_and_colors:
        first_image = Image.open(os.path.join(folder_path, images[0]))
        canvas = Image.new('RGB', first_image.size, (255, 255, 255)) 
        draw = ImageDraw.Draw(canvas)

        for i in range(len(points_and_colors) - 1):
            start_point, start_color = points_and_colors[i]
            end_point, end_color = points_and_colors[i + 1]

            if start_point is None or end_point is None:
                continue
            
            start_color_rgb = (start_color[2], start_color[1], start_color[0])  
            draw.line([start_point, end_point], fill=start_color_rgb, width=5)

        canvas.save(output_image_path)
        print(f"Result saved at {output_image_path}")
    else:
        print("No points detected.")

folder_path = '/home/KID6/Desktop/Resources Used/Incomplete tasks/task-10/Operation-Pixel-Merge/assets'
output_image_path = '/home/KID6/Desktop/Resources Used/Incomplete tasks/task-10/output.png'

drawimage(folder_path, output_image_path)
