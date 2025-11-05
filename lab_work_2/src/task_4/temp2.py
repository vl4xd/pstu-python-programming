import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class RobotManipulator:
    def __init__(self):
        self.joints = []

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
            info.append(f"Сочленение {i+1}: {joint_type} по оси {joint['axis'].upper()}, "
                       f"значение: {joint['value']:.2f}, длина: {joint['length']:.2f} м")
        return info

def visualize_manipulator(robot, title="3D Манипулятор"):
    """Визуализация манипулятора в 3D"""

    # Вычисляем позиции всех точек
    points = robot.forward_kinematics()

    # Создаем 3D график
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Извлекаем координаты
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    z = [p[2] for p in points]

    # Рисуем звенья
    ax.plot(x, y, z, 'bo-', linewidth=3, markersize=8, label='Звенья манипулятора')

    # Подписываем точки
    labels = ['База'] + [f'Сочленение {i+1}' for i in range(len(points)-2)] + ['Схват']
    for i, label in enumerate(labels):
        ax.text(x[i], y[i], z[i], f'  {label}', fontsize=10)

    # Настройка графика
    ax.set_xlabel('X (м)')
    ax.set_ylabel('Y (м)')
    ax.set_zlabel('Z (м)')
    ax.set_title(title)

    # Устанавливаем равный масштаб по осям
    max_range = max(max(x)-min(x), max(y)-min(y), max(z)-min(z)) or 1
    mid_x = (max(x) + min(x)) * 0.5
    mid_y = (max(y) + min(y)) * 0.5
    mid_z = (max(z) + min(z)) * 0.5

    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    ax.legend()
    plt.tight_layout()
    plt.show()

    # Выводим координаты
    print("Координаты точек:")
    for i, point in enumerate(points):
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
    robot.add_joint('R', 'z', np.radians(45), 1.0)  # Вращение по Z, длина 1м
    robot.add_joint('R', 'y', np.radians(30), 0.8)  # Вращение по Y, длина 0.8м
    robot.add_joint('R', 'y', np.radians(-15), 0.6) # Вращение по Y, длина 0.6м

    visualize_manipulator(robot, "Классический 3-звенный манипулятор")

def example_2():
    """Пример 2: Смешанные типы сочленений"""
    print("\n=== Пример 2: Манипулятор со смешанными сочленениями ===")

    robot = RobotManipulator()
    # Комбинируем вращательные и поступательные сочленения
    robot.add_joint('R', 'z', np.radians(30), 0.5)  # Вращение по Z
    robot.add_joint('P', 'z', 0.3, 0.4)            # Поступательное по Z (телескоп)
    robot.add_joint('R', 'y', np.radians(45), 0.6)  # Вращение по Y
    robot.add_joint('P', 'x', 0.2, 0.3)            # Поступательное по X
    robot.add_joint('R', 'x', np.radians(-20), 0.2) # Вращение по X

    visualize_manipulator(robot, "Манипулятор со смешанными сочленениями")

def example_3():
    """Пример 3: SCARA-робот"""
    print("\n=== Пример 3: SCARA-робот ===")

    robot = RobotManipulator()
    # SCARA: два вращательных по Z и одно поступательное по Z
    robot.add_joint('R', 'z', np.radians(45), 0.8)  # Плечо
    robot.add_joint('R', 'z', np.radians(-30), 0.6) # Локоть
    robot.add_joint('P', 'z', -0.2, 0.1)           # Вертикальное перемещение

    visualize_manipulator(robot, "SCARA-робот")

def example_4():
    """Пример 4: Декартов робот (только поступательные сочленения)"""
    print("\n=== Пример 4: Декартов робот ===")

    robot = RobotManipulator()
    # Только поступательные движения
    robot.add_joint('P', 'x', 0.5, 0)  # Перемещение по X
    robot.add_joint('P', 'y', 0.3, 0)  # Перемещение по Y
    robot.add_joint('P', 'z', 0.4, 0)  # Перемещение по Z
    robot.add_joint('R', 'z', np.radians(90), 0.2)  # Вращение схвата

    visualize_manipulator(robot, "Декартов робот")

def interactive_example():
    """Интерактивный пример с возможностью задания параметров"""
    print("\n=== Интерактивный пример ===")

    robot = RobotManipulator()

    # Пользователь может настроить эти параметры:
    num_joints = 4  # Количество сочленений

    # Пример конфигурации (можно менять)
    configurations = [
        ('R', 'z', np.radians(30), 1.0),
        ('R', 'y', np.radians(45), 0.8),
        ('P', 'z', 0.5, 10),
        ('R', 'x', np.radians(-15), 0.4)
    ]

    for config in configurations:
        robot.add_joint(*config)

    # Можно изменить значения сочленений:
    new_values = [np.radians(45), np.radians(60), 0.3, np.radians(30)]
    robot.set_joint_values(new_values)

    visualize_manipulator(robot, "Интерактивный пример манипулятора")

if __name__ == "__main__":
    # Запуск примеров
    # example_1()  # Классический манипулятор
    # example_2()  # Смешанные сочленения
    example_3()  # SCARA-робот
    # example_4()  # Декартов робот
    # interactive_example()  # Интерактивный пример