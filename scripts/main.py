""" This Code is an Example of finding H U and S letters in Pictures
"""
import cv2 as cv
import params
import os
import sys
import RCJRVision
import time


def main(verbose=params.verbose):
    start = time.time()
    """ There are three ways to use pre-defined comparable contours
           1. Use default saved contours from params
           2. Use a string path to .npy files (Only use files which generated by saveSampleContours.py script
                E.g. RCJRVision.HSUVision(h_cnt = '../Contours/H_Contour.npy')
           3. Numpy ndarrays with (n,1,2) shape (n is the number of contour points)
                E.g. RCJRVision.HSUVision(h_cnt = my_ndarray)
    """
    my_test_vision = RCJRVision.HSUVision()
    # To use your image files just change the params.test_img_dir with your image dir
    for filename in os.listdir(params.test_img_dir):
        if filename.endswith(".jpg"):
            img = cv.imread(os.path.join(params.test_img_dir, filename))
            if verbose:
                print('Analysing pic {} ...'.format(filename))
            letter, center = my_test_vision.find_HSU(img, verbose)
            if verbose:
                print('         ... Pic {0} contains {1} letter'.format(filename, letter))
                print('         ... Pic {0} letter location is {1}'.format(filename, center))
    end = time.time()
    print('Test code took {0} ms'.format((end - start) * 1000))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()
    elif len(sys.argv) == 2 and sys.argv[1].lower() in ['true', 'false']:
        main(eval(sys.argv[1].upper()[0] + sys.argv[1].lower()[1:]))
    else:
        raise ValueError('Expect a True or False but but something else is passed as input')
