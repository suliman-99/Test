import cv2
import base64
import numpy as np


def compare_and_visualize_drawing_similarity(Drawing):

    # Replace this with your actual Base64-encoded image data
    base64_image_data = Drawing

    # Decode the Base64 data
    image_binary = base64.b64decode(base64_image_data)

    # Convert binary image data to a NumPy array
    image_np = np.frombuffer(image_binary, dtype=np.uint8)

    # Decode the NumPy array using OpenCV
    decoded_image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)


    # # Paths to the image
    image_path1 = 'Assets/9.jpg'
    # image_path2 = 'Assets/10.jpg'

    # Read and resize images
    image1 = cv2.imread(image_path1)
    image2 = decoded_image
    image1 = cv2.resize(image1, (150, 150))
    image2 = cv2.resize(image2, (150, 150))

    # Convert images to grayscale
    img1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Apply image processing operations
    _, edges1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY_INV)
    _, edges2 = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY_INV)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    edges1 = cv2.dilate(edges1, kernel, iterations=1)
    edges1 = cv2.morphologyEx(edges1, cv2.MORPH_CLOSE, kernel)
    edges1 = cv2.morphologyEx(edges1, cv2.MORPH_OPEN, kernel)

    edges2 = cv2.dilate(edges2, kernel, iterations=1)
    edges2 = cv2.morphologyEx(edges2, cv2.MORPH_CLOSE, kernel)
    edges2 = cv2.morphologyEx(edges2, cv2.MORPH_OPEN, kernel)

    # Find contours and draw them on images
    Contours1, _ = cv2.findContours(edges1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    Cnt1 = Contours1[0]
    cv2.drawContours(image1, [Cnt1], -1, (255, 0, 0), 2)

    Contours2, _ = cv2.findContours(edges2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    Cnt2 = Contours2[0]
    cv2.drawContours(image2, [Cnt2], -1, (255, 0, 0), 2)

    # Calculate shape similarity using matchShapes
    ret = cv2.matchShapes(Cnt1, Cnt2, 1, 0.0)

    print("Shape Similarity Score:", ret)
    if ret <= 0.1:
        print('Shapes are similar')
        return 1
    else:
        print('Shapes are not similar')
        return 0