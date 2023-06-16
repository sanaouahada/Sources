import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Circle, Rectangle

plt.rcParams['font.size'] = 14

# Load data
def load_data(filename):
    data = pd.read_csv(filename, sep=',')
    data['r_position'] = np.sqrt(
        data['x_position']**2 + data['y_position']**2)
    return data

# Plot data
def plot_xy(data, title): 
    plt.figure() 
    shifted_y = data['y_position'] + 25
    plt.scatter(data['x_position'], shifted_y, s=8, c='#364B9A', label = 'Interaction vertices') 
    plt.gca().set_aspect('equal')
    plt.gca().add_patch(Circle((0, 0), 75, linewidth=1.5, color='#F67E4B', 
                               fill=False, label = 'TPC'), 
                        )
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)
    plt.xlabel('x [mm]')
    plt.ylabel('y [mm]')
    plt.legend(loc = 'upper right')
    plt.title(title)
    plt.savefig('figures/'f"xy_{title}.png")
    plt.show()
    plt.close() 

def plot_rz(data, title):
    # Filter outliers
    filtered_data = data[(data['z_position'] <= 2600) & (data['z_position'] > 0)]
    
    plt.figure()
    plt.scatter(filtered_data['r_position'], filtered_data['z_position'], s=10, c='#364B9A')
    plt.ylabel('z [mm]')
    plt.xlabel('r [mm]')
    plt.ylim(0, 3000)
      
    # Add a line at z = 2.6 m
    plt.axhline(y=2600, color='#F67E4B', linestyle='--', label='TPC length : 2.6 m')
    plt.legend(loc = 'upper right')
    plt.title(title)
    
    plt.savefig('figures/' + f"rz_{title}.png")
    plt.show()
    plt.close()
    

def plot_energy_spectrum(data, title):
    plt.figure()
    plt.hist(data['energy_dep']*1e6, bins=100, color='#364B9A')
    plt.xlabel('Energy [keV]')
    plt.ylabel('Number of events')
    plt.title(f"Energy spectrum of the {title} source")
    plt.savefig('figures/'f"energy_spectrum_{title}.png")
    plt.show()
    plt.close()
