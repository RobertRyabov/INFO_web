import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

df_addiction = pd.read_csv('social_media_vs_productivity.csv')

# Check if column exists
if 'perceived_productivity_score' not in df_addiction.columns:
    print("Error: 'perceived_productivity_score' column not found in df_addiction.")
else:
    # Drop missing values in the two columns
    df_clean = df_addiction[['daily_social_media_time', 'perceived_productivity_score']].dropna()

    # Calculate correlation coefficient
    corr, p_value = pearsonr(df_clean['daily_social_media_time'], df_clean['perceived_productivity_score'])
    print(f"Correlation between daily_social_media_time and perceived_productivity_score: {corr:.3f} (p-value: {p_value:.3f})")

    # Print basic descriptive stats
    print(f"\nDescriptive statistics:")
    print(df_clean.describe())

    # Plot
    plt.figure(figsize=(10,6))
    sns.scatterplot(
        x='daily_social_media_time',
        y='perceived_productivity_score',
        data=df_clean,
        alpha=0.6
    )
    sns.regplot(
        x='daily_social_media_time',
        y='perceived_productivity_score',
        data=df_clean,
        scatter=False,
        color='red'
    )
    plt.title('Daily Social Media Time vs Perceived Productivity')
    plt.xlabel('Daily Social Media Time (hours)')
    plt.ylabel('Perceived Productivity Score')
    plt.show()
