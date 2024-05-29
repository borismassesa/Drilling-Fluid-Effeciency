import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Input parameters
speed = np.array([3, 6, 100, 200, 300, 600])
obs = 3  # Number of samples (set this value for simplicity)
initial_weight = 100.0  # Initial weight of cuttings placed in the bottomhole (in gm)

# Realistic dummy shear stress values for 3 samples
shear_stress = np.array([
    [12, 25, 70, 130, 180, 230],  # Sample 1
    [14, 30, 75, 140, 190, 240],  # Sample 2
    [16, 35, 80, 150, 200, 250]   # Sample 3
])

# Realistic dummy weight recovered values for 3 samples
weight_recovered = np.array([65, 70, 68])

# Perform calculations
plastic_viscosity = shear_stress[:, 5] - shear_stress[:, 4]
apparent_viscosity = 0.5 * shear_stress[:, 5]
yield_point = shear_stress[:, 4] - plastic_viscosity
true_yield_point = 0.75 * yield_point
weight_ratio = weight_recovered / initial_weight
efficiency = weight_ratio * 100  # Efficiency as a percentage

# Print results
results_df = pd.DataFrame({
    'Sample No.': range(1, obs + 1),
    'Plastic Viscosity (in cp)': plastic_viscosity,
    'Apparent Viscosity (in cp)': apparent_viscosity,
    'Yield Point (in cp)': yield_point,
    'True Yield Point (in cp)': true_yield_point,
    'Weight Recovered (in gm)': weight_recovered,
    'Weight Ratio': weight_ratio,
    'Efficiency (%)': efficiency
})

print('***************************************RESULTS*********************************')
print(f'Weight of cuttings placed initially in the wellbore = {initial_weight} gm')
print(results_df)

# Plot Shear Stress vs Speed for all samples
plt.figure()
for k in range(obs):
    plt.plot(speed, shear_stress[k, :], marker='o', label=f'Sample {k+1}')
plt.title('SHEAR STRESS vs SPEED')
plt.xlabel('Speed (in rpm)')
plt.ylabel('Shear Stress (in cp)')
plt.legend()
plt.grid(True)
plt.show()

# Plot Variation Between Weight Ratio and Plastic Viscosity for all samples
plt.figure()
for k in range(obs):
    plt.plot(plastic_viscosity[k], weight_ratio[k], marker='o', label=f'Sample {k+1}')
plt.xlabel('Plastic Viscosity (in cp)')
plt.ylabel('Weight Ratio')
plt.title('VARIATION BETWEEN WEIGHT RATIO WITH PLASTIC VISCOSITY')
plt.legend()
plt.grid(True)
plt.show()

# Save calculated data to a CSV file
results_df.to_csv('ViscosityVariationData.csv', index=False)