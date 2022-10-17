import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def find_difference(image1, image2):
    assert image1.shape == image2.shape, "Specify 2 images with the same shape"
    gray_image1 = rgb2gray(image1)
