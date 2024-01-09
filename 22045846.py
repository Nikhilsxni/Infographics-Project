# -*- coding: utf-8 -*-
"""
Created on Tue Jan 2 08:43:26 2024

@author: Nikhil Soni
studentID: 22045846
"""
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Read and process data for Plot 1
data = pd.read_csv("AGR_LAND.csv")
agriculture_data = pd.DataFrame(data)
agriculture_data.set_index('Country Name', inplace=True)
agriculture_data.drop('Year', axis=1, inplace=True)
agriculture_data_transposed = agriculture_data.transpose()

# Read data for Plot 2
data_plot2 = pd.read_csv("electricity_prod.csv")
df_plot2 = pd.DataFrame(data_plot2)
df_plot2.set_index('Country Name', inplace=True)

# Read data for Plot 3
greenhouse_gas_df = pd.read_csv("greenhouse_gas_emi.csv")

# Read data for Plot 4
data_plot4 = pd.read_csv("urban_pop.csv")
df_plot4 = pd.DataFrame(data_plot4)
df_plot4.set_index('Year', inplace=True)

# 2x2 grid for plots
fig = plt.figure(figsize=(50, 25))
gs = GridSpec(2, 2, width_ratios=[2, 1])

# Plot 1
ax1 = plt.subplot(gs[0, 0])
agriculture_data_transposed.plot(kind='bar', colormap='viridis', ax=ax1)
ax1.set_xlabel('Year', fontsize=14, color='blue', fontstyle='italic')
ax1.set_ylabel('Percentage', fontsize=14, color='green', fontstyle='italic')
ax1.set_title('Agriculture Land % by Year (2015-2021)',
              fontsize=18, color='red', fontweight='bold')

# Plot 2
ax2 = plt.subplot(gs[0, 1])
df_plot2.plot(kind='bar', legend=False, ax=ax2)
ax2.set_title('Electricity Production by Oil, Gas, and Coal Sources (2015)',
              fontsize=18, color='purple', fontweight='bold')
ax2.set_xlabel('Country', fontsize=14, color='blue', fontstyle='italic')
ax2.set_ylabel('Electricity Production', fontsize=14,
               color='green', fontstyle='italic')

# Plot 3
ax3 = plt.subplot(gs[1, 0])
greenhouse_gas_df.plot.pie(y='2000', labels=greenhouse_gas_df['Country Name'],
                           autopct='%1.1f%%', startangle=160, ax=ax3, legend=False)
ax3.set_title('Greenhouse Gas Emissions in 2000',
              fontsize=18, color='orange', fontweight='bold')

# Plot 4
ax4 = plt.subplot(gs[1, 1])
df_plot4.plot(marker='o', ax=ax4)
ax4.set_title('Urban Population Over Years (2010-2022)',
              fontsize=18, color='brown', fontweight='bold')
ax4.set_xlabel('Year', fontsize=14, color='blue', fontstyle='italic')
ax4.set_ylabel('Urban Population', fontsize=14,
               color='green', fontstyle='italic')
ax4.legend(title='Country', fontsize=12)  # Adjust legend fontsize

# points
points_text = (
    'The Dashboard analyzes the climate change due to urbanization in different countries:\n'
    '1. Countries under 50% with little or no change in agriculture land percentage over time\n'
    '2. Except Norway at under 10%, rest all countries burn fossil fuels for electricity production\n'
    '3. Australia(40.8%) and U.A.E(20.8%) emissions in 2000 due to rapid urbanization\n'
    '4. Most of the countries have urban population between 80%-90%'
)

plt.figtext(0.5, 0.05, points_text, size=18, ha="center")

# Adjust layout
plt.tight_layout(h_pad=2)
plt.subplots_adjust(top=0.9)
plt.suptitle('URBANIZATION AND CLIMATE CHANGE', fontsize=60, weight="bold")

# student information 
student_info_text = 'Name: Nikhil Soni\nStudent ID: 22045846'
plt.figtext(0.02, 0.02, student_info_text, size=18, weight="bold", ha="left")

# Saving the figure as PNG with 300 dpi
plt.savefig('22045846.png', dpi=300)
