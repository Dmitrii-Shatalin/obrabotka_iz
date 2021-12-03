import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def get_spectrum(shifted):
    absolute = np.abs(shifted)
    min_val = np.amin(absolute)
    absolute[absolute == 0] = min_val
    spectrum = 35*np.log10(absolute)
    return spectrum, min_val


def DFFTnp(img, orig):
    n = np.fft.fft2(img)
    k = np.fft.fftshift(n)
    spectrum, min_val = get_spectrum(k)
    plt.subplot(141)
    plt.imshow(spectrum, cmap='gray', vmin=0, vmax=255)
    for a in k[0:337]: a[508:520] = min_val
    for a in k[345:]: a[508:520] = min_val
    for a in k[335:345]: a[0:508] = min_val
    for a in k[335:345]: a[515:] = min_val
    res, _ = get_spectrum(k)
    plt.subplot(142)
    plt.imshow(res, cmap='gray', vmin=0, vmax=255)

    final = np.real(np.fft.ifft2(np.fft.ifftshift(k)))
    plt.subplot(143)
    plt.imshow(final, cmap='gray', vmin=0, vmax=255)
    plt.subplot(144)
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)
    plt.show()
    


image = cv.imread('00_06.png', cv.IMREAD_GRAYSCALE)


n = np.float32(image)
DFFTnp(n, image)
