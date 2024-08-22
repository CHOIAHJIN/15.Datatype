import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 엑셀 파일 불러오기
file_path =pd.read_csv'./data/2.elevator_failure_prediction.csv'
df = pd.read_excel(file_path)

# 불필요한 열 제거 (Sensor1과 Sensor6)
df = df.drop(columns=['Sensor1', 'Sensor6'])

# 종속변수 설정 (0: 정상, 1: 비정상)
df['Dependent'] = df['Dependent'].replace(2, 1)

# Density Plot 그리기
def plot_density(df, independent_var, dependent_var='Dependent'):
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=df, x=independent_var, hue=dependent_var, common_norm=False)
    plt.title(f'Density Plot of {independent_var} vs {dependent_var}')
    plt.show()

# 그래프 그리기
plot_density(df, 'Time')
plot_density(df, 'Temperature')
plot_density(df, 'Humidity')
plot_density(df, 'RPM')
plot_density(df, 'Vibrations')
plot_density(df, 'Pressure')
plot_density(df, 'Sensor2')
plot_density(df, 'Sensor3')
plot_density(df, 'Sensor4')
