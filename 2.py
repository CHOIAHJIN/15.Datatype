import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# CSV 파일 불러오기
data = pd.read_excel('./data/2.elevator_failure_prediction.xlsx')

# 불필요한 열 제거 (Sensor1과 Sensor6)
data = data.drop(columns=['Sensor1', 'Sensor6'])

# 종속변수 설정 (0: 정상, 1: 비정상)
data['Dependent'] = data['Dependent'].replace(2, 1)

# Density Plot 그리기
def plot_density(data, independent_var, dependent_var='Dependent'):
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=data, x=independent_var, hue=dependent_var, common_norm=False)
    plt.title(f'Density Plot of {independent_var} vs {dependent_var}')
    plt.show()

# 그래프 그리기
plot_density(data, 'Time')
plot_density(data, 'Temperature')
plot_density(data, 'Humidity')
plot_density(data, 'RPM')
plot_density(data, 'Vibrations')
plot_density(data, 'Pressure')
plot_density(data, 'Sensor2')
plot_density(data, 'Sensor3')
plot_density(data, 'Sensor4')
