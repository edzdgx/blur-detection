import numpy as np
import argparse
import imutils
import cv2
import os
import time
import detector
import utils

if __name__ == '__main__':
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", type=str, default=None,
        help="input path")
    ap.add_argument("-t", "--thresh", type=int, default=10,
        help="threshold for our blur detector")
    # ap.add_argument("-v", "--vis", type=int, default=-1,
    #     help="whether or not we are visualizing intermediary steps")
    # ap.add_argument("-d", "--test", type=int, default=-1,
    #     help="whether or not we should progressively blur the image")
    # ap.add_argument("-m", "--mode", type=str, default="image",
    #     help="image/video/file")
    ap.add_argument("-a", "--algorithm", type=int, default=1,
        help="choose algorithm to apply\n1=FFT\n2=Laplacian\n3=Sobel")
    args = vars(ap.parse_args())

    # load images from folder
    images = utils.load_images(args['image'])
    isBlur = []

    # case FFT
    if args['algorithm'] == 1:
        for orig in images:
            orig = utils.resize(orig, width=500)
            gray = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
            # apply our blur detector using the FFT
            (mean, blurry) = detector.detect_blur_fft(gray, size=60,
                thresh=args["thresh"], vis=args["vis"] > 0)
            # draw on the image, indicating whether or not it is blurry
            image = np.dstack([gray] * 3)
            color = (0, 0, 255) if blurry else (0, 255, 0)
            text = "Blurry ({:.4f})" if blurry else "Not Blurry ({:.4f})"
            text = text.format(mean)
            cv2.putText(image, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                color, 2)
            print("[INFO] {}".format(text))
            isBlur.append(blurry)
            # show the output image
            # cv2.imshow("Output", image)
            # cv2.waitKey(0)
        print(sum(isBlur)/len(isBlur))
    # case Laplacian
    elif args['algorithm'] == 2:
        for orig in images:
            orig = utils.resize(orig, width=500)
            gray = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
            # apply our blur detector using the FFT
            (mean, blurry) = detector.detect_blur_laplacian(gray, thresh=args["thresh"])
            # draw on the image, indicating whether or not it is blurry
            image = np.dstack([gray] * 3)
            color = (0, 0, 255) if blurry else (0, 255, 0)
            text = "Blurry ({:.4f})" if blurry else "Not Blurry ({:.4f})"
            text = text.format(mean)
            cv2.putText(image, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                color, 2)
            print("[INFO] {}".format(text))
            isBlur.append(blurry)
            # show the output image
            # cv2.imshow("Output", image)
            # cv2.waitKey(0)
        print(sum(isBlur)/len(isBlur))
    elif args['algorithm'] == 3:
        for orig in images:
            orig = utils.resize(orig, width=500)
            gray = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
            # apply our blur detector using the FFT
            (mean, blurry) = detector.detect_blur_sobel(gray, thresh=args["thresh"])
            # draw on the image, indicating whether or not it is blurry
            image = np.dstack([gray] * 3)
            color = (0, 0, 255) if blurry else (0, 255, 0)
            text = "Blurry ({:.4f})" if blurry else "Not Blurry ({:.4f})"
            text = text.format(mean)
            cv2.putText(image, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                color, 2)
            print("[INFO] {}".format(text))
            isBlur.append(blurry)
            # show the output image
            # cv2.imshow("Output", image)
            # cv2.waitKey(0)
        print(sum(isBlur)/len(isBlur))






