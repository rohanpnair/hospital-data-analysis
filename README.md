# 🏥 Hospital Data Analysis Project

This project performs exploratory data analysis (EDA) and visualization on real-world hospital data covering patient admissions, mortality records, and environmental pollution indicators to uncover actionable insights for improving healthcare service delivery.

## 📂 Datasets

The project uses the following CSV datasets:

- `HDHI Admission data.csv` — Patient admission details  
- `HDHI Mortality Data.csv` — Mortality records  
- `HDHI Pollution Data.csv` — Air quality and environmental conditions  
- `table_headings.csv` — Additional metadata  

**Source**: [Kaggle Dataset — Hospital Admissions Data](https://www.kaggle.com/datasets/ashishsahani/hospital-admissions-data)

## 🛠️ Tools & Libraries

- Python 3.x  
- Pandas  
- Matplotlib  
- Seaborn  

## 📊 Analysis Modules

### 1️⃣ `hospital_analysis.py`
- Visualizes daily hospital admissions over time  
- Identifies peak admission periods  
- Calculates average stay duration  
- Explores gender-wise and age-wise admissions

### 2️⃣ `hospital_mortality_analysis.py`
- Analyzes mortality trends  
- Visualizes age-wise and gender-wise death counts  
- Highlights seasonal patterns in mortality rates  

### 3️⃣ `pollution_data.py`
- Visualizes AQI trends over time  
- Distribution of major pollutants (PM2.5, PM10, NO2, etc.)  
- Correlation heatmap of pollutants  
- Maximum temperature trend analysis  

## 🚀 How to Run

1️⃣ Install dependencies:
pip install pandas matplotlib seaborn

2️⃣ Clone the repository:
git clone https://github.com/rohanpnair/hospital-data-analysis.git
cd hospital-data-analysis

3️⃣ Run analysis scripts:
python hospital_analysis.py
python hospital_mortality_analysis.py
python pollution_data.py
