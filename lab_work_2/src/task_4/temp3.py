import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class RobotManipulator:
    def __init__(self):
        self.joints = []
        self.initial_joint_values = []  # Сохраняем начальные значения

    def add_joint(self, joint_type, axis, value=0, length=0):
        """
        Добавляет сочленение к манипулятору

        Parameters:
        joint_type: 'R' - вращательное, 'P' - поступательное
        axis: 'x', 'y', 'z' - ось вращения/перемещения
        value: начальное значение угла (рад) или смещения (м)
        length: длина звена после этого сочленения
        """
        self.joints.append({
            'type': joint_type,
            'axis': axis,
            'value': value,
            'length': length
        })
        self.initial_joint_values.append(value)  # Сохраняем начальное значение

    def rotation_matrix(self, axis, theta):
        """Матрица поворота вокруг заданной оси"""
        if axis == 'x':
            return np.array([
                [1, 0, 0, 0],
                [0, np.cos(theta), -np.sin(theta), 0],
                [0, np.sin(theta), np.cos(theta), 0],
                [0, 0, 0, 1]
            ])
        elif axis == 'y':
            return np.array([
                [np.cos(theta), 0, np.sin(theta), 0],
                [0, 1, 0, 0],
                [-np.sin(theta), 0, np.cos(theta), 0],
                [0, 0, 0, 1]
            ])
        elif axis == 'z':
            return np.array([
                [np.cos(theta), -np.sin(theta), 0, 0],
                [np.sin(theta), np.cos(theta), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ])

    def translation_matrix(self, axis, distance):
        """Матрица перемещения вдоль заданной оси"""
        if axis == 'x':
            return np.array([
                [1, 0, 0, distance],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ])
        elif axis == 'y':
            return np.array([
                [1, 0, 0, 0],
                [0, 1, 0, distance],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ])
        elif axis == 'z':
            return np.array([
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, distance],
                [0, 0, 0, 1]
            ])

    def forward_kinematics(self, joint_values=None):
        """
        Прямая кинематика для манипулятора с произвольными сочленениями

        Parameters:
        joint_values: список значений для каждого сочленения (None - использовать сохраненные значения)
        """
        if joint_values is None:
            joint_values = [joint['value'] for joint in self.joints]

        # Начальная точка (база)
        T = np.eye(4)  # Единичная матрица
        points = [T @ np.array([0, 0, 0, 1])]  # База

        # Проходим по всем сочленениям
        for i, joint in enumerate(self.joints):
            joint_type = joint['type']
            axis = joint['axis']
            value = joint_values[i]
            length = joint['length']

            # Применяем преобразование сочленения
            if joint_type == 'R':  # Вращательное
                T = T @ self.rotation_matrix(axis, value)
            elif joint_type == 'P':  # Поступательное
                T = T @ self.translation_matrix(axis, value)

            # Применяем длину звена (всегда вдоль локальной оси X)
            if length != 0:
                T = T @ self.translation_matrix('x', length)

            # Сохраняем позицию после этого звена
            points.append(T @ np.array([0, 0, 0, 1]))

        return points

    def set_joint_values(self, values):
        """Устанавливает значения для всех сочленений"""
        for i, value in enumerate(values):
            if i < len(self.joints):
                self.joints[i]['value'] = value

    def get_joint_info(self):
        """Возвращает информацию о сочленениях"""
        info = []
        for i, joint in enumerate(self.joints):
            joint_type = "Вращательное" if joint['type'] == 'R' else "Поступательное"
            unit = "рад" if joint['type'] == 'R' else "м"
            initial_value = self.initial_joint_values[i]
            info.append(f"Сочленение {i+1}: {joint_type} по оси {joint['axis'].upper()}, "
                       f"текущее: {joint['value']:.2f}{unit}, начальное: {initial_value:.2f}{unit}, длина: {joint['length']:.2f} м")
        return info

def visualize_manipulator(robot, title="3D Манипулятор"):
    """Визуализация манипулятора в 3D с отображением начального положения"""

    # Вычисляем позиции всех точек для текущего и начального положений
    points_current = robot.forward_kinematics()
    points_initial = robot.forward_kinematics(robot.initial_joint_values)

    print(points_current)

    # Создаем 3D график
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Извлекаем координаты для текущего положения
    x_current = [p[0] for p in points_current]
    y_current = [p[1] for p in points_current]
    z_current = [p[2] for p in points_current]

    # Извлекаем координаты для начального положения
    x_initial = [p[0] for p in points_initial]
    y_initial = [p[1] for p in points_initial]
    z_initial = [p[2] for p in points_initial]

    # Рисуем начальное положение (прерывистые линии и серые точки)
    ax.plot(x_initial, y_initial, z_initial, 'k--', linewidth=2, markersize=6,
            label='Начальное положение', alpha=0.7)
    ax.scatter(x_initial, y_initial, z_initial, c='gray', s=50, alpha=0.5, marker='s')

    # Рисуем текущее положение (сплошные линии и цветные точки)
    ax.plot(x_current, y_current, z_current, 'bo-', linewidth=3, markersize=8,
            label='Текущее положение')
    ax.scatter(x_current, y_current, z_current, c='red', s=80, alpha=0.8)

    # Подписываем точки текущего положения
    labels = ['База'] + [f'Сочл. {i+1}' for i in range(len(points_current)-2)] + ['Схват']
    for i, label in enumerate(labels):
        ax.text(x_current[i], y_current[i], z_current[i], f'  {label}', fontsize=10)

    # Настройка графика
    ax.set_xlabel('X (м)')
    ax.set_ylabel('Y (м)')
    ax.set_zlabel('Z (м)')
    ax.set_title(title)

    # Устанавливаем равный масштаб по осям
    all_x = x_current + x_initial
    all_y = y_current + y_initial
    all_z = z_current + z_initial

    max_range = max(max(all_x)-min(all_x), max(all_y)-min(all_y), max(all_z)-min(all_z)) or 1
    mid_x = (max(all_x) + min(all_x)) * 0.5
    mid_y = (max(all_y) + min(all_y)) * 0.5
    mid_z = (max(all_z) + min(all_z)) * 0.5

    ax.set_xlim(mid_x - max_range/2, mid_x + max_range/2)
    ax.set_ylim(mid_y - max_range/2, mid_y + max_range/2)
    ax.set_zlim(mid_z - max_range/2, mid_z + max_range/2)

    ax.legend()
    plt.tight_layout()
    plt.show()

    # Выводим координаты
    print("Координаты точек (текущее положение):")
    for i, point in enumerate(points_current):
        print(f"{labels[i]}: ({point[0]:.2f}, {point[1]:.2f}, {point[2]:.2f})")

    print("\nКоординаты точек (начальное положение):")
    for i, point in enumerate(points_initial):
        print(f"{labels[i]}: ({point[0]:.2f}, {point[1]:.2f}, {point[2]:.2f})")

    # Выводим информацию о сочленениях
    print("\nИнформация о сочленениях:")
    for info in robot.get_joint_info():
        print(info)

# Примеры использования:

def example_1():
    """Пример 1: Классический 3-звенный манипулятор (только вращательные сочленения)"""
    print("=== Пример 1: Классический 3-звенный манипулятор ===")

    robot = RobotManipulator()
    # Добавляем сочленения: тип, ось, начальное значение, длина звена
    robot.add_joint('R', 'z', np.radians(0), 1.0)   # Начальное положение: 0°
    robot.add_joint('R', 'y', np.radians(0), 0.8)   # Начальное положение: 0°
    robot.add_joint('R', 'y', np.radians(0), 0.6)   # Начальное положение: 0°

    # Устанавливаем новые значения (отличные от начальных)
    robot.set_joint_values([np.radians(45), np.radians(30), np.radians(-15)])

    visualize_manipulator(robot, "Классический 3-звенный манипулятор")

def example_2():
    """Пример 2: Смешанные типы сочленений"""
    print("\n=== Пример 2: Манипулятор со смешанными сочленениями ===")

    robot = RobotManipulator()
    # Комбинируем вращательные и поступательные сочленения
    robot.add_joint('R', 'z', np.radians(0), 0.5)   # Начальное: 0°
    robot.add_joint('P', 'z', 0, 0.4)              # Начальное: 0 м
    robot.add_joint('R', 'y', np.radians(0), 0.6)   # Начальное: 0°
    robot.add_joint('P', 'x', 0, 0.3)              # Начальное: 0 м
    robot.add_joint('R', 'x', np.radians(0), 0.2)   # Начальное: 0°

    # Устанавливаем новые значения
    robot.set_joint_values([
        np.radians(30),  # 30°
        0.3,             # 0.3 м
        np.radians(45),  # 45°
        0.2,             # 0.2 м
        np.radians(-20)  # -20°
    ])

    visualize_manipulator(robot, "Манипулятор со смешанными сочленениями")

def example_3():
    """Пример 3: SCARA-робот"""
    print("\n=== Пример 3: SCARA-робот ===")

    robot = RobotManipulator()
    # SCARA: два вращательных по Z и одно поступательное по Z
    robot.add_joint('R', 'z', np.radians(0), 0.8)   # Начальное: 0°
    robot.add_joint('R', 'z', np.radians(0), 0.6)   # Начальное: 0°
    robot.add_joint('P', 'z', 0, 0.1)              # Начальное: 0 м

    # Устанавливаем новые значения
    robot.set_joint_values([
        np.radians(45),   # 45°
        np.radians(-30),  # -30°
        -0.2              # -0.2 м
    ])

    visualize_manipulator(robot, "SCARA-робот")

def example_4():
    """Пример 4: Декартов робот (только поступательные сочленения)"""
    print("\n=== Пример 4: Декартов робот ===")

    robot = RobotManipulator()
    # Только поступательные движения
    robot.add_joint('P', 'x', 0, 0)               # Начальное: 0 м
    robot.add_joint('P', 'y', 0, 0)               # Начальное: 0 м
    robot.add_joint('P', 'z', 0, 0)               # Начальное: 0 м
    robot.add_joint('R', 'z', np.radians(0), 0.2) # Начальное: 0°

    # Устанавливаем новые значения
    robot.set_joint_values([
        0.5,               # 0.5 м по X
        0.3,               # 0.3 м по Y
        0.4,               # 0.4 м по Z
        np.radians(90)     # 90°
    ])

    visualize_manipulator(robot, "Декартов робот")

def interactive_example():
    """Интерактивный пример с возможностью задания параметров"""
    print("\n=== Интерактивный пример ===")

    robot = RobotManipulator()

    # Пример конфигурации (можно менять)
    configurations = [
        ('R', 'z', np.radians(2), 2.0),    # Начальное: 0°
        ('R', 'y', np.radians(0), 0.8),    # Начальное: 0°
        ('P', 'x', 0, 10),                 # Начальное: 0 м
        ('R', 'x', np.radians(0), 0.4)     # Начальное: 0°
    ]

    for config in configurations:
        robot.add_joint(*config)

    # Устанавливаем новые значения
    new_values = [
        np.radians(0),   # 45°
        np.radians(0),   # 60°
        -9.5,              # 0.3 м
        np.radians(0)    # 30°
    ]
    robot.set_joint_values(new_values)

    visualize_manipulator(robot, "Интерактивный пример манипулятора")

if __name__ == "__main__":
    # Запуск примеров
    # example_1()  # Классический манипулятор
    # example_2()  # Смешанные сочленения
    # example_3()  # SCARA-робот
    # example_4()  # Декартов робот
    interactive_example()  # Интерактивный пример