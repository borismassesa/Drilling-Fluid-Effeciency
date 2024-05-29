import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Input parameters
speed = np.array([3, 6, 100, 200, 300, 600])
obs = int(input('\n Enter number of samples: '))
initial_weight = float(input('\n Enter weight of cuttings placed initially in the bottomhole (in gm): '))

# Initialize arrays to store results
shear_stress = np.zeros((obs, len(speed)))
plastic_viscosity = np.zeros(obs)
apparent_viscosity = np.zeros(obs)
yield_point = np.zeros(obs)
true_yield_point = np.zeros(obs)
weight_recovered = np.zeros(obs)
weight_ratio = np.zeros(obs)

# Collect data and perform calculations
for k in range(obs):
    print(f'\n Sample {k+1}')
    for j in range(len(speed)):
        shear_stress[k, j] = float(input(f'\n Enter shear stress at speed {speed[j]} rpm (in cp): '))
    
    plastic_viscosity[k] = shear_stress[k, 5] - shear_stress[k, 4]
    apparent_viscosity[k] = 0.5 * shear_stress[k, 5]
    yield_point[k] = shear_stress[k, 4] - plastic_viscosity[k]
    true_yield_point[k] = 0.75 * yield_point[k]
    weight_recovered[k] = float(input('Enter weight of cuttings recovered (in gm): '))
    weight_ratio[k] = weight_recovered[k] / initial_weight

    # Plot Shear Stress vs Speed for each sample
    plt.figure()
    plt.plot(speed, shear_stress[k, :], marker='o')
    plt.title(f'SHEAR STRESS vs SPEED (Sample {k+1})')
    plt.xlabel('Speed (in rpm)')
    plt.ylabel('Shear Stress (in cp)')
    plt.grid(True)
    plt.show()

# Display results in tabular form
results_df = pd.DataFrame({
    'Sample No.': range(1, obs + 1),
    'Plastic Viscosity (in cp)': plastic_viscosity,
    'Apparent Viscosity (in cp)': apparent_viscosity,
    'Yield Point (in cp)': yield_point,
    'True Yield Point (in cp)': true_yield_point,
    'Weight Recovered (in gm)': weight_recovered,
    'Weight Ratio': weight_ratio
})

print('***************************************RESULTS*********************************')
print(f'Weight of cuttings placed initially in the wellbore = {initial_weight} gm')
print(results_df)

# Plot Variation Between Weight Ratio and Plastic Viscosity
plt.figure()
plt.plot(plastic_viscosity, weight_ratio, marker='o')
plt.xlabel('Plastic Viscosity (in cp)')
plt.ylabel('Weight Ratio')
plt.title('VARIATION BETWEEN WEIGHT RATIO WITH PLASTIC VISCOSITY')
plt.grid(True)
plt.show()

# Save calculated data to a CSV file
results_df.to_csv('ViscosityVariationData.csv', index=False)