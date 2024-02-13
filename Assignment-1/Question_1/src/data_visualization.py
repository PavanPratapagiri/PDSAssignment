import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
file_path = "/Users/pavanpratapagiri/PDS/PDSAssignment/Assignment-1/Question_1/clean_data/clean_frailty_data1.csv"
frailty_data = pd.read_csv(file_path)

# Visualize the distribution of Weight by Frailty
plt.figure(figsize=(8, 6))
sns.boxplot(x='Frailty', y='Weight', data=frailty_data)
plt.title('Boxplot of Weight by Frailty')
plt.xlabel('Frailty')
plt.ylabel('Weight (lbs)')
plt.show()

# Visualize the distribution of Age by Frailty
plt.figure(figsize=(8, 6))
sns.boxplot(x='Frailty', y='Age', data=frailty_data)
plt.title('Boxplot of Age by Frailty')
plt.xlabel('Frailty')
plt.ylabel('Age (years)')
plt.show()

# Visualize the relationship between Grip Strength and Weight
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Grip_Strength', y='Weight', hue='Frailty', data=frailty_data)
plt.title('Scatterplot of Grip Strength vs. Weight')
plt.xlabel('Grip Strength (kg)')
plt.ylabel('Weight (lbs)')
plt.legend(title='Frailty')
plt.show()
