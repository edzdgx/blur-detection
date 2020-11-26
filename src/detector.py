# import the necessary packages
from scipy.ndimage.filters import convolve
import numpy as np
import utils
import cv2
'''
image: image to be determined whether blur or not
size: The size of the radius around the centerpoint of the image
        for which we will zero out the FFT shift
thresh: A value which the mean value of the magnitudes will be compared
        to for determining whether an image is considered blurry or not blurry
'''
def detect_blur_fft(image, size=60, thresh=10):
    # grab the dimensions of the image and use the dimensions to
    # derive the center (x, y)-coordinates
    (h, w) = image.shape
    (cX, cY) = (int(w / 2.0), int(h / 2.0))
    # compute the FFT to find the frequency transform, then shift
    # the zero frequency component (i.e., DC component located at
    # the top-left corner) to the center where it will be more
    # easy to analyze
    fft = np.fft.fft2(image)
    fftShift = np.fft.fftshift(fft)

    # zero-out the center of the FFT shift (i.e., remove low
    # frequencies), apply the inverse shift such that the DC
    # component once again becomes the top-left, and then apply
    # the inverse FFT
    fftShift[cY-size : cY+size, cX-size : cX+size] = 0
    fftShift = np.fft.ifftshift(fftShift)
    recon = np.fft.ifft2(fftShift)
    # compute the magnitude spectrum of the reconstructed image,
    # then compute the mean of the magnitude values
    magnitude = 20 * np.log(np.abs(recon))
    mean = np.mean(magnitude)
    # blurry if the mean value of the magnitudes is less than threshold
    return (mean, mean <= thresh)

def detect_blur_laplacian(image, thresh):
    # compute laplacian
    lap = utils.variance_of_laplacian(image)
    # blurry if lap is less than thresh
    return (lap, lap <= thresh)

def detect_blur_LoG(image, thresh):
    # apply Gaussian filter to remove noise
    gaus = cv2.GaussianBlur(image, (3,3), 0)
    lap = utils.variance_of_laplacian(gaus)
    # blurry if lap is less than thresh
    return (lap, lap <= thresh)

def detect_blur_Tenengrad(image, thresh):

    # try using Gaussian to remove noise first
    # image = cv2.GaussianBlur(image, (3,3), 0)
    Sobel_x=cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    Sobel_y=cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    S = np.hypot(Sobel_x, Sobel_y).astype(np.uint8)

    # cv2.imshow('s', np.hstack([image, S]))
    # cv2.waitKey(0)

    TEN = np.var(S)
    # print('Sobel_x:{}\n\nSx:{}\n\n'.format(Sobel_x, Gx))
    # print('TEN={:2f}'.format(TEN))
    return (TEN, TEN <= thresh)

def calc_laplacian_thresh(image, total):
    lap = utils.variance_of_laplacian(image)
    return total + lap





