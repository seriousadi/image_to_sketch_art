import numpy as np
import cv2 as cv
import os


def main():

    abs_path = os.getcwd()  # get absolute path of current working directory

    img = cv.imread(os.path.join(
        abs_path, 'sketch check.jpg'))  # get image and convert it to numpy array

    # convert the image to grayscale
    grayscle_img = cv.cvtColor(img, code=cv.COLOR_BGRA2GRAY, dstCn=3)

    # inverting the image
    inv_gray_image = 255 - np.array(grayscle_img)

    # blurring the image
    blurred_image = cv.GaussianBlur(
        np.array(inv_gray_image), ksize=(99, 99), sigmaX=0, sigmaY=0)

    # dividing the greyscale value of the image by the inverse of blurred
    # image value which highlights the boldest edges.
    # This technique is used by traditional photographers to print photos from the reel.
    final_img = cv.divide(grayscle_img, 255 - blurred_image, scale=255)

    cv.imwrite("img.jpg", final_img)  # saving the image


if __name__ == '__main__':
    main()
