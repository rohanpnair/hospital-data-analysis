# 📦 Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 📥 Load dataset (use your actual file)
df = pd.read_csv("HDHI Admission data.csv")

# 📊 Preview data
print("\n📊 First 5 rows of the data:")
print(df.head())
print("\n📊 Dataset columns:")
print(df.columns)

# 📅 Convert date columns to datetime (with dayfirst=True)
df['D.O.A'] = pd.to_datetime(df['D.O.A'], dayfirst=True, errors='coerce')
df['D.O.D'] = pd.to_datetime(df['D.O.D'], dayfirst=True, errors='coerce')


# ⏳ Calculate Length of Stay (if not present)
if 'DURATION OF STAY' not in df.columns:
    df['DURATION OF STAY'] = (df['D.O.D'] - df['D.O.A']).dt.days

# 📈 Daily Admissions Trend
daily_admissions = df.groupby('D.O.A').size()

plt.figure(figsize=(12,6))
daily_admissions.plot(kind='line', marker='o')
plt.title('Daily Patient Admissions')
plt.xlabel('Date')
plt.ylabel('Number of Admissions')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# 📋 Most Common Diagnoses — if Diagnosis column exists
if 'DIAGNOSIS' in df.columns:
    plt.figure(figsize=(10,6))
    sns.countplot(data=df, y='DIAGNOSIS', order=df['DIAGNOSIS'].value_counts().head(10).index, palette="viridis")
    plt.title('Top 10 Diagnoses')
    plt.xlabel('Number of Cases')
    plt.ylabel('Diagnosis')
    plt.tight_layout()
    plt.show()
else:
    print("\n⚠️ No 'DIAGNOSIS' column found — skipping diagnosis plot.")

# 📏 Average Length of Stay
avg_stay = df['DURATION OF STAY'].mean()
print(f"\n📏 Average Length of Stay: {avg_stay:.2f} days")

# 📊 Outcome Distribution
if 'OUTCOME' in df.columns:
    outcome_counts = df['OUTCOME'].value_counts()
    outcome_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, figsize=(6,6), colors=sns.color_palette('pastel'))
    plt.title('Outcome Distribution')
    plt.ylabel('')
    plt.show()
else:
    print("\n⚠️ No 'OUTCOME' column found — skipping outcome pie chart.")

# 📊 Department-wise Outcome Analysis — if both columns exist
if 'TYPE OF ADMISSION-EMERGENCY/OPD' in df.columns and 'OUTCOME' in df.columns:
    dept_outcome = df.groupby(['TYPE OF ADMISSION-EMERGENCY/OPD', 'OUTCOME']).size().unstack().fillna(0)
    print("\n📊 Admission Type vs Outcome table:\n", dept_outcome)

    dept_outcome.plot(kind='bar', stacked=True, figsize=(12,6), colormap='viridis')
    plt.title('Admission Type-wise Outcome Distribution')
    plt.ylabel('Number of Patients')
    plt.xlabel('Admission Type')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("\n⚠️ Missing 'TYPE OF ADMISSION-EMERGENCY/OPD' or 'OUTCOME' column — skipping department outcome plot.")

# 📅 Admissions by Day of the Week
df['Day_of_Week'] = df['D.O.A'].dt.day_name()

plt.figure(figsize=(10,5))
sns.countplot(data=df, x='Day_of_Week', order=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'], palette="Set2")
plt.title('Admissions by Day of the Week')
plt.ylabel('Number of Admissions')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n✅ All analyses and visualizations complete.")
