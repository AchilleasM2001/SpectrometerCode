# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import glob


# Read the data
data = pd.read_csv("log10_ratio_1.csv")

# Extract the data for plotting
wavelengths = data['Wavelength']
log10_mean_intensity_ratio = data['Log10MeanIntensityRatio']

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(wavelengths, log10_mean_intensity_ratio, marker='o', linestyle='-', color='blue')
plt.title('Log10 of Mean Intensity Ratio vs. Wavelength')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Log10(Mean Intensity Ratio)')
plt.grid(True)
plt.show()
