import numpy as np
import argparse
import cv2
import detector
import utils
def main():
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", type=str, required=True,
        help="input image folder path")
    ap.add_argument("-t", "--thresh", type=float, default=10,
        help="threshold for our blur detector")
    ap.add_argument("-gt", "--get_thresh", type=bool, default=False,
        help="get thresh by averaging outputs")
    ap.add_argument("-a", "--algorithm", type=int, default=1,
        help="algorithm to apply\n1=FFT\n2=Laplacian\n3=LoG\n4=Tenengrad")
    args = vars(ap.parse_args())
    folder = args['image']
    thresh = args['thresh']
    algo = args['algorithm']
    gt = args['get_thresh']

    # get threshold by averaging output of algorithm
    # then use calculated threshold instead of the default threshold
    if gt:
        thresh = utils.get_thresh(algo)

    # load images from folder
    images = utils.load_images(folder)
    isBlur = []
    for idx, orig in enumerate(images, 0):
        orig = utils.resize(orig, width=500)
        gray = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
        # case FFT
        if algo == 1:
            (mean, blurry) = detector.detect_blur_fft(gray, size=80,
                thresh=thresh)
        # case Laplacian
        elif algo == 2:
            (mean, blurry) = detector.detect_blur_laplacian(gray,
                thresh=thresh)
        # case LoG
        elif algo == 3:
            (mean, blurry) = detector.detect_blur_LoG(gray,
                thresh=thresh)
        # case Tenengrad
        elif algo == 4:
            (mean, blurry) = detector.detect_blur_Tenengrad(gray,
                thresh=thresh)
        # draw on the image, indicating whether or not it is blurry
        utils.print_result(image=gray, isBlur=blurry, mean=mean,
                            index=idx, show=False)
        isBlur.append(blurry)

    print('Blur image percentage: {:.2f}%'.format(sum(isBlur)/len(isBlur)*100))

if __name__ == '__main__':
    main()

