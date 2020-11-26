import os
import cv2
import numpy as np

def get_thresh(algo):
    # sample datum to compute average threshold
    # folders = ['./img/kaggle_dataset/sharp',
    #            './img/kaggle_dataset/motion_blurred'
    #            './img/kaggle_dataset/defocused_blurred']
    folders = ['img/CERTH_ImageBlurDataset/TrainingSet/Naturally-Blurred',
               'img/CERTH_ImageBlurDataset/TrainingSet/Undistorted',
               'img/CERTH_ImageBlurDataset/TrainingSet/Artificially-Blurred']
    total = 0
    count = 0
    # iterate through each dataset
    for folder in folders:
        images = load_images(folder)
        for idx, orig in enumerate(images, 0):
            orig = resize(orig, width=500)
            gray = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
            if algo == 1:
                pass
            # case Laplacian
            elif algo == 2:
                total += variance_of_laplacian(gray)
            # case Sobel
            elif algo == 3:
                gaus = cv2.GaussianBlur(gray, (3,3), 0)
                total += variance_of_laplacian(gaus)
            elif algo == 4:
                gaus = cv2.GaussianBlur(gray, (3,3), 0)
                Sobel_x=cv2.Sobel(gaus, cv2.CV_64F, 1, 0, ksize=3)
                Sobel_y=cv2.Sobel(gaus, cv2.CV_64F, 0, 1, ksize=3)
                S = np.hypot(Sobel_x, Sobel_y).astype(np.uint8)
                TEN = np.var(S)
                total += TEN
        count += (idx+1)
        print('current average = {:.2f}'.format(total/count))
    print('total is: {:.2f}\ncount is: {}\naverage is: {:.2f}'
                    .format(total, count, total/count))
    return total/count

def load_images(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img.any():
            images.append(img)
    return images

def print_result(image, isBlur, mean, index, show=False):
    image = np.dstack([image] * 3)
    color = (0, 0, 255) if isBlur else (0, 255, 0)
    text = "Blurry ({:.2f})" if isBlur else "Not Blurry ({:.2f})"
    text = text.format(mean)
    cv2.putText(image, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
        color, 2)
    print("[INFO] {:3.0f} {}".format(index, text))
    # show the output image
    if show:
        cv2.imshow("Output", image)
        cv2.waitKey(0)

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # get height width from original image
    (h, w) = image.shape[:2]
    dim = None
    if width is None and height is None:
        # return original if no inputs given
        return image
    if width is None:
        # get width ratio w.r.t. height, calculate resized dimension
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        # get height ratio w.r.t. width, calculate resized dimension
        r = width / float(w)
        dim = (width, int(h * r))
    # resize the image to desired dimension
    return cv2.resize(image, dim, interpolation=inter)

def variance_of_laplacian(image):
    # calculate LoG variance
    return cv2.Laplacian(image, cv2.CV_64F).var()




