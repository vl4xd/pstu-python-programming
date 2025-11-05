import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def rotation_matrix_z(theta):
    """Матрица поворота вокруг оси Z"""
    return np.array([
        [np.cos(theta), -np.sin(theta), 0, 0],
        [np.sin(theta), np.cos(theta), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def rotation_matrix_y(theta):
    """Матрица поворота вокруг оси Y"""
    return np.array([
        [np.cos(theta), 0, np.sin(theta), 0],
        [0, 1, 0, 0],
        [-np.sin(theta), 0, np.cos(theta), 0],
        [0, 0, 0, 1]
    ])

def translation_matrix(x, y, z):
    """Матрица перемещения"""
    return np.array([
        [1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1]
    ])

def forward_kinematics(theta1, theta2, theta3, L1=1.0, L2=0.8, L3=0.6):
    """
    Прямая кинематика для 3-звенного манипулятора

    theta1: угол поворота первого сочленения (рад)
    theta2: угол поворота второго сочленения (рад)
    theta3: угол поворота третьего сочленения (рад)
    """

    # Начальная точка (база)
    base = np.array([0, 0, 0, 1])

    # Преобразование для первого звена
    T1 = rotation_matrix_z(theta1) @ translation_matrix(L1, 0, 0)
    joint1 = T1 @ np.array([0, 0, 0, 1])  # Конец первого звена

    # Преобразование для второго звена
    T2 = T1 @ rotation_matrix_y(theta2) @ translation_matrix(L2, 0, 0)
    joint2 = T2 @ np.array([0, 0, 0, 1])  # Конец второго звена

    # Преобразование для третьего звена (схват)
    T3 = T2 @ rotation_matrix_y(theta3) @ translation_matrix(L3, 0, 0)
    end_effector = T3 @ np.array([0, 0, 0, 1])  # Конец третьего звена

    return base, joint1, joint2, end_effector

def visualize_manipulator(theta1, theta2, theta3):
    """Визуализация манипулятора в 3D"""

    # Вычисляем позиции всех точек
    base, joint1, joint2, end_effector = forward_kinematics(theta1, theta2, theta3)

    # Создаем 3D график
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Извлекаем координаты
    points = [base, joint1, joint2, end_effector]
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    z = [p[2] for p in points]

    # Рисуем звенья
    ax.plot(x, y, z, 'bo-', linewidth=3, markersize=8, label='Звенья манипулятора')

    # Подписываем точки
    labels = ['База', 'Сочленение 1', 'Сочленение 2', 'Схват']
    for i, label in enumerate(labels):
        ax.text(x[i], y[i], z[i], f'  {label}', fontsize=10)

    # Настройка графика
    ax.set_xlabel('X (м)')
    ax.set_ylabel('Y (м)')
    ax.set_zlabel('Z (м)')
    ax.set_title(f'3D Манипулятор: θ1={np.degrees(theta1):.1f}°, '
                 f'θ2={np.degrees(theta2):.1f}°, '
                 f'θ3={np.degrees(theta3):.1f}°')

    # Устанавливаем равный масштаб по осям
    max_range = max(max(x)-min(x), max(y)-min(y), max(z)-min(z))
    mid_x = (max(x) + min(x)) * 0.5
    mid_y = (max(y) + min(y)) * 0.5
    mid_z = (max(z) + min(z)) * 0.5
    ax.set_xlim(mid_x - max_range/2, mid_x + max_range/2)
    ax.set_ylim(mid_y - max_range/2, mid_y + max_range/2)
    ax.set_zlim(mid_z - max_range/2, mid_z + max_range/2)

    ax.legend()
    plt.tight_layout()
    plt.show()

    # Выводим координаты
    print("Координаты точек:")
    print(f"База: ({base[0]:.2f}, {base[1]:.2f}, {base[2]:.2f})")
    print(f"Сочленение 1: ({joint1[0]:.2f}, {joint1[1]:.2f}, {joint1[2]:.2f})")
    print(f"Сочленение 2: ({joint2[0]:.2f}, {joint2[1]:.2f}, {joint2[2]:.2f})")
    print(f"Схват: ({end_effector[0]:.2f}, {end_effector[1]:.2f}, {end_effector[2]:.2f})")

# Пример использования
if __name__ == "__main__":
    # Углы в радианах
    theta1 = np.radians(0)  # 45 градусов
    theta2 = np.radians(0)  # 30 градусов
    theta3 = np.radians(190) # -15 градусов

    visualize_manipulator(theta1, theta2, theta3)