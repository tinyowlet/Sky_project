import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import label
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename

fits_path = 'photometry/M6707HH.fits'
fits_file = get_pkg_data_filename(fits_path)
data = fits.getdata(fits_file, ext=0)

plt.imshow(data, cmap='gray')
plt.colorbar()
plt.title("Изображение неба из FITS-файла")
plt.show()

threshold = np.median(data) + (np.std(data) * 1.5)

binary_image = (data > threshold).astype(int)

plt.imshow(binary_image, cmap='gray')
plt.title("Бинарное изображение (звезды)")
plt.show()

labeled_array, num_stars = label(binary_image)

print(f"Число звезд на изображении: {num_stars}")

# 8. Визуализация результатов с контуром
plt.figure()
plt.imshow(data, cmap='gray')
plt.contour(binary_image, colors='red', linewidths=0.5)  # Добавляем контуры в красном цвете
plt.title("Контуры звезд в M67")
plt.colorbar()
plt.show()