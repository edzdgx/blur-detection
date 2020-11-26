# blur-detection

Blur detection with different algorithms and parameters

* Fast Fourier Transform (FFT)
* Laplacian (Lap)
* Laplacian of Gaussian (LoG)
* Tenengrad (TEN)

# Blur Detection Accuracy

| Algorithm | Threshold | kaggle_sharp* | kaggle_defocused_blur* | kaggle_motion_blur* | CERTH_Undistorted* | CERTH_Blurred* |
| - | - | - | - | - | - | - |
| FFT | 10 | 8.57 | 87.71 | 67.71 | 8.25 | 44.32 |
| FFT | 11 | 10 | 89.14 | 70.29 | 9.21 | 48.38 |
| FFT | 12 | 11.43 | 90.29 | 72.57 | 9.84 | 50 |
| FFT | 13 | 12.86 | 91.43 | 76.29 | 11.11 | 53.24
| FFT | 14 | 15.71 | 92.29 | 78.29 | 13.33 | 57.3 |
| FFT | 15 | 18.29 | 93.71 | 82.57 | 15.24 | 61.62 |
| FFT | 16 | 21.14 | 95.14 | 86 | 17.62 | 64.32 |
| Lap | 140 | 7.71 | 97.43 | 78.29 | 4.92 | 61.62 |
| Lap | 150 | 8.86 | 98 | 78.86 | 5.71 | 63.51 |
| Lap | 160 | 9.14 | 98 | 80.57 | 6.03 | 64.32 |
| Lap | 170 | 9.71 | 98 | 80.86 | 6.35 | 66.49 |
| Lap | 180 | 10.29 | 98 | 81.71 | 6.98 | 67.03 |
| Lap | 190 | 11.71 | 98 | 82.29 | 7.46 | 68.65 |
| Lap | 200 | 14.29 | 98.29 | 83.14 | 7.94 | 68.92 |
| LoG | 28 | 11.71 | 94.57 | 78.57 | 6.98 | 52.16 |
| LoG | 30 | 13.14 | 94.86 | 79.43 | 8.41 | 55.14 |
| LoG | 32 | 14.29 | 95.71 | 80.29 | 9.37 | 57.57 |
| LoG | 34 | 15.43 | 95.71 | 81.43 | 10.16 | 58.92 |
| LoG | 36 | 17.71 | 96 | 82.57 | 10.63 | 61.35 |
| LoG | 38 | 19.71 | 96.57 | 82.86 | 11.9 | 62.97 |
| LoG | 40 | 21.43 | 96.57 | 84 | 12.86 | 63.51 |
| TEN | 1000 | 9.71 | 63.43 | 59.14 | 5.4 | 27.84 |
| TEN | 1100 | 10.57 | 67.43 | 65.43 | 7.3 | 30.27 |
| TEN | 1200 | 11.71 | 71.71 | 68 | 7.62 | 34.32 |
| TEN | 1300 | 15.71 | 76.57 | 69.71 | 9.84 | 40.27 |
| TEN | 1400 | 19.43 | 79.43 | 73.71 | 12.06 | 42.7 |
| TEN | 1500 | 22.29 | 83.14 | 76 | 14.44 | 46.49 |
| TEN | 1600 | 26 | 84.86 | 80.57 | 15.56 | 49.19 |
| TEN | 1700 | 28.57 | 87.71 | 82.86 | 16.98 | 53.51 |
| TEN | 1800 | 32 | 89.71 | 84.29 | 18.41 | 55.41 |

<sup>\* The "blur rate" in *%* of each set of images</sup>

# Blur Detection Time Complexity
| Algorithm | kaggle_sharp* | kaggle_defocused_blur* | kaggle_motion_blur* | CERTH_Blurred* |
| - | - | - | - | - |
| FFT | 24.5 | 25.9 | 22.2 | 18 |
| Lap | 4.6 | 4.6 | 4.4 | 7.2 |
| LoG | 4.7 | 4.8 | 4.6 | 7.7 |
| TEN | 6.4 | 6.2 | 6.2 | 8.7 |

<sup>\* Average time per frame in *ms* for processing a 1MB image</sup>

# Reference
1. E. Mavridaki, V. Mezaris, "No-Reference blur assessment in natural images using Fourier transform and spatial pyramids", Proc. IEEE International Conference on Image Processing (ICIP 2014), Paris, France, October 2014.

1. Mary, Leena & Sreenath, N.. (2019). Pre-processing Techniques for Detection of Blurred Images.

1. Pech Pacheco, Jose Luis & Cristobal, Gabriel & Chamorro-Martinez, J. & Fernandez-Valdivia, J.. (2000). Diatom autofocusing in brightfield microscopy: A comparative study. Pattern Recognition, Proceedings. 15th International Conference on. 3. 314-317 vol.3. 10.1109/ICPR.2000.903548.

1. X. He, Y. Lu and P. Shi, "A Fake Iris Detection Method Based on FFT and Quality Assessment," 2008 Chinese Conference on Pattern Recognition, Beijing, 2008, pp. 1-4, doi: 10.1109/CCPR.2008.68.
