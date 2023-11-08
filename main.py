import numpy as np
import cv2 as cv
import os


def main():

    abs_path = os.getcwd()  # get absolute path of current working directory

    img = cv.imread(os.path.join(
        abs_path, 'sketch check.jpg'))  # get image and convert it to numpy array

    # converted pixels of coloured image will be stored here (will be used later)
    graysclae_pixels = []

    # grayscale the image
    for _ in img:
        converted_pixels = []
        for n in _:
            # converting coloured values to grayscale using NTSC formula
            g = 0.299*n[0] + 0.587*n[1] + 0.114 * n[2]
            converted_pixels.append(g)
        graysclae_pixels.append(converted_pixels)

    grayscale_img = np.array(graysclae_pixels)


if __name__ == '__main__':
    main()
