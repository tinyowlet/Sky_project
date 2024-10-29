import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage import label
file_path = 'sky2.csv'


data = pd.read_csv(file_path, header=None).values

plt.imshow(data, cmap='gray')  
plt.colorbar()                 
plt.title("Изображение неба из sky2.csv") 
plt.show()                     


threshold = np.median(data) + (np.std(data) * 1.5)
binary_image = data > threshold

plt.imshow(binary_image, cmap='gray')  
plt.title("Бинарное изображение (звезды)")  
plt.show()                    

threshold = np.median(data) + (np.std(data) * 1.5)  

labeled_array, num_stars = label(binary_image)  

print(f"Число звезд на изображении: {num_stars}") 