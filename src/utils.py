import os
import cv2
import numpy as np

def get_thresh(algo):
    # sample datum to compute average threshold
    folders = ['./img/kaggle_dataset/sharp',
               './img/kaggle_dataset/motion_blurred',
               './img/kaggle_dataset/defocused_blurred']
    total = 0

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
                pass
    print('total is: {:.2f}\naverage is: {:.2f}'.format(total, total/702))
    return total/351/3

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
    text = "Blurry ({:.4f})" if isBlur else "Not Blurry ({:.4f})"
    text = text.format(mean)
    cv2.putText(image, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
        color, 2)
    print("[INFO] {:3.0f} {}".format(index,text))
    # show the output image
    if show:
        cv2.imshow("Output", image)
        cv2.waitKey(0)

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation=inter)

    # return the resized image
    return resized

def variance_of_laplacian(image):
    # calculate LoG variance
    return cv2.Laplacian(image, cv2.CV_64F).var()




