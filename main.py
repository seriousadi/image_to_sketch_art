import numpy as np
import cv2 as cv
import os


def main():

    abs_path = os.getcwd()  # get absolute path of current working directory

    img = cv.imread(os.path.join(
        abs_path, 'testing.png'))  # get image and convert it to numpy array

    # converted pixels of coloured image will be stored here (will be used later)
    graysclae_pixels = []

    # converts the image to grayscale
    for _ in img:
        converted_pixels = []
        for n in _:
            # converting coloured values to grayscale using NTSC formula
            gray_pixel = 0.299*(n[0]) + \
                0.587*(n[1]) + 0.114 * (n[2])
            converted_pixels.append(gray_pixel)
        graysclae_pixels.append(converted_pixels)

    inv_gray_scale = 255 - np.array(graysclae_pixels)  # inverting the image
    # blurring the image
    blurred_image = cv.GaussianBlur(
        np.array(graysclae_pixels), ksize=(11, 11), sigmaX=0, sigmaY=0)
    # blending the images using colour dodge method
    final_img = inv_gray_scale + blurred_image

    cv.imwrite("img.jpg", final_img)  # saving the image


if __name__ == '__main__':
    main()
