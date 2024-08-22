import matplotlib.pyplot as plt

# 플롯 설정
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 15))
axes = axes.flatten()

# 각 독립변수에 대해 밀도 플롯 생성
for i, var in enumerate(independent_vars):
    ax = axes[i]
    # 정상 데이터의 밀도 플롯
    normal_data[var].plot(kind='density', ax=ax, label='Normal', color='blue')
    # 비정상 데이터의 밀도 플롯
    abnormal_data[var].plot(kind='density', ax=ax, label='Abnormal', color='red')
    ax.set_title(f'Density Plot of {var}')
    ax.set_xlabel(var)
    ax.set_ylabel('Density')
    ax.legend()

# 여유 공간 조정
plt.tight_layout()

# 저장
plt.savefig('./results/density.png')
plt.show()
