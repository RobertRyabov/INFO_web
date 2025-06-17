import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_addiction = pd.read_csv('P/social_media_vs_productivity.csv')

# Drop rows with missing social media time or job satisfaction
df_clean = df_addiction[['daily_social_media_time', 'job_satisfaction_score']].dropna()

# Create usage category bins
df_clean['usage_category'] = pd.cut(
    df_clean['daily_social_media_time'], 
    bins=[0, 2, 4, 6, 24], 
    labels=['Low', 'Moderate', 'High', 'Very High'],
    include_lowest=True
)

# Print count per category
print("Number of users in each social media usage category:")
print(df_clean['usage_category'].value_counts().sort_index())

# Print median job satisfaction by category
median_satisfaction = df_clean.groupby('usage_category')['job_satisfaction_score'].median()
print("\nMedian Job Satisfaction Score by Social Media Usage Category:")
print(median_satisfaction)

# Print mean and std for more detail
mean_satisfaction = df_clean.groupby('usage_category')['job_satisfaction_score'].mean()
std_satisfaction = df_clean.groupby('usage_category')['job_satisfaction_score'].std()
print("\nMean ± SD Job Satisfaction Score by Social Media Usage Category:")
for cat in median_satisfaction.index:
    print(f"{cat}: {mean_satisfaction[cat]:.2f} ± {std_satisfaction[cat]:.2f}")

# Plot boxplot
plt.figure(figsize=(10,6))
sns.boxplot(
    x='usage_category', 
    y='job_satisfaction_score', 
    data=df_clean,
    order=['Low', 'Moderate', 'High', 'Very High']
)
plt.title('Job Satisfaction by Social Media Usage Category')
plt.xlabel('Social Media Usage Category (hours per day)')
plt.ylabel('Job Satisfaction Score')
plt.show()
