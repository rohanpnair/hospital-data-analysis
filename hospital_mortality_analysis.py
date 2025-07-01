import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('HDHI Mortality Data.csv')
df.columns = df.columns.str.strip()
if "DATE OF BROUGHT DEAD" in df.columns:
    df['DATE OF BROUGHT DEAD'] = pd.to_datetime(df['DATE OF BROUGHT DEAD'], dayfirst=True, errors='coerce')
else:
    print("⚠️ 'DATE OF BROUGHT DEAD' column not found.")
if 'GENDER' in df.columns:
    gender_counts = df['GENDER'].value_counts()
    gender_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, figsize=(6, 6),colors=sns.color_palette('pastel'))
    plt.title('Mortality by Gender')
    plt.ylabel('')
    plt.show()
else:
    print("⚠️ 'GENDER' column not found.")
if 'AGE' in df.columns:
    bins = [0, 20, 40, 60, 80, 100]
    labels = ['0-20', '21-40', '41-60', '61-80', '81-100']
    df['Age Group'] = pd.cut(df['AGE'], bins=bins, labels=labels)
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='Age Group', order=labels, palette="Set3")
    plt.title('Mortality by Age Group')
    plt.ylabel('Number of Deaths')
    plt.tight_layout()
    plt.show()
else:
    print("⚠️ 'AGE' column not found.")
if 'DATE OF BROUGHT DEAD' in df.columns:
    daily_deaths = df.groupby('DATE OF BROUGHT DEAD').size()
    plt.figure(figsize=(12, 6))
    daily_deaths.plot(kind='line', marker='o')
    plt.title('Deaths Over Time')
    plt.xlabel('Date of Death')
    plt.ylabel('Number of Deaths')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
else:
    print("⚠️ 'DATE OF BROUGHT DEAD' column not found.")
print("\n✅ Mortality analysis completed.")