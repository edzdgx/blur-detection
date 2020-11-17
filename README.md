# blur-detection

Blur detection with different algorithms and parameters

* Tenengrad
* Laplacian
* Laplacian of Gaussian (LoG)
* Fast Fourier Transform (FFT)

# Testing Reuslts for Kaggle dataset

| Algorithm | Threshold | Window Size | Undistorted* | Motion Blurred* | Defocused Blurred* |
| - | - | - | - | - | - |
| Tenengrad | 10 | 3 | 16.85 | 83.14 | 96.28 |
| Laplacian | 100 | 3 | 4.85 | 69.14 | 96.28 |
| Laplacian | 528 | 3 | 54.86 | 91.42 | 99.42 |
| LoG | 69 | 3 | 49.71 | 86.57 | 98.28 |
| FTT | 10 | 60 | 8.57 | 67.71 | 87.71 |
| FTT | 10 | 80 | 16.86 | 83.14 | 96.28 |

<sup>\* The "blur rate" of each set of images</sup>

# Testing Results for CERTH Image Blur Training Dataset

| Algorithm | Threshold | Window Size | Undistorted* | Naturally Blurred* | Artificially Blurred* |
| - | - | - | - | - | - |
| Tenengrad | 10 | 3 | - | - | - |
| Laplacian | 100 | 3 | 3.02 | 32.27 | 77.33 |
| LoG | 69 | 3 | - | - | - |
| FTT | 10 | 60 | - | - | - |
| FTT | 10 | 80 | 13.97 | 53.18 | 82.67 |

# Reference
1. E. Mavridaki, V. Mezaris, "No-Reference blur assessment in natural images using Fourier transform and spatial pyramids", Proc. IEEE International Conference on Image Processing (ICIP 2014), Paris, France, October 2014.

1. Mary, Leena & Sreenath, N.. (2019). Pre-processing Techniques for Detection of Blurred Images.

1. Pech Pacheco, Jose Luis & Cristobal, Gabriel & Chamorro-Martinez, J. & Fernandez-Valdivia, J.. (2000). Diatom autofocusing in brightfield microscopy: A comparative study. Pattern Recognition, Proceedings. 15th International Conference on. 3. 314-317 vol.3. 10.1109/ICPR.2000.903548.

1. X. He, Y. Lu and P. Shi, "A Fake Iris Detection Method Based on FFT and Quality Assessment," 2008 Chinese Conference on Pattern Recognition, Beijing, 2008, pp. 1-4, doi: 10.1109/CCPR.2008.68.