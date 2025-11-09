import numpy as np
import plotly.graph_objects as go

from .pair import Pair

class Manipulator:


    def __init__(self) -> None:
        self.pairs: list[Pair] = []
        self.positions: list[list[np.array]] = []
        self.work_times: list[list[int]] = []
        self.is_have_initial_position: bool = False


    def add_pair(self, pair: Pair) -> None:
        self.pairs.append(pair)


    def clear_pairs(self) -> None:
        self.pairs.clear()
        self.positions.clear()
        self.is_have_initial_position = False


    def clear_positions(self) -> None:
        self.positions.clear()
        self.is_have_initial_position = False


    def get_translation_matrix(self, lenght: int) -> np.array:
        """Матрица длины звена (всегда вдоль оси X)

        :return np.array: _description_
        """
        return np.array([
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, lenght],
                [0, 0, 0, 1]
            ])


    def forward_kinematics(self, work_time_set: list[int]) -> None:
        """_summary_

        :param list[int] work_time_set: время работы каждой пары (сек)
        """
        if len(work_time_set) != len(self.pairs):
            raise ValueError("Длина work_time_set должна быть равна количеству пар манипулятора.")

        # Добавляем к временам работы предыдущие времена работы (накопление времени)
        if len(self.work_times) != 0:
            work_time_set = [work_time_set[i] + t for i, t in enumerate(self.work_times[-1])]

        # Производи вычисления начальной позиции манипулятора
        if not self.is_have_initial_position:
            self.is_have_initial_position = True
            self.forward_kinematics([0 for _ in self.pairs])

        # Начальная точка (база)
        T = np.eye(4)  # Единичная матрица
        points = [T @ np.array([0, 0, 0, 1])]  # База

        for i, pair in enumerate(self.pairs):
            T = T @ pair.get_matrix(work_time_set[i])

            if pair.length != 0:
                T = T @ self.get_translation_matrix(pair.length)

            points.append(T @ np.array([0, 0, 0, 1]))

        self.positions.append(points)
        self.work_times.append(work_time_set)
        return points


    def visualize_manipulator(self) -> None:
        data = []

        # Для центрирования графика и фиксации масштаба на самое бОльшее значение
        all_x = []
        all_y = []
        all_z = []

        for i, i_positions in enumerate(self.positions):
            visible = False
            if i == 0:
                visible = True
            x_positions = [p[0] for p in i_positions]
            y_positions = [p[1] for p in i_positions]
            z_positions = [p[2] for p in i_positions]

            all_x.extend(x_positions)
            all_y.extend(y_positions)
            all_z.extend(z_positions)

            data.append(go.Scatter3d(visible=visible, x=x_positions, y=y_positions, z=z_positions, mode="lines+markers"))
        #
        max_range = max(max(all_x) - min(all_x),
                       max(all_y) - min(all_y),
                       max(all_z) - min(all_z))

        mid_x = (max(all_x) + min(all_x)) * 0.5
        mid_y = (max(all_y) + min(all_y)) * 0.5
        mid_z = (max(all_z) + min(all_z)) * 0.5

        fig = go.Figure(data=data)

        steps = []
        for i in range(len(self.positions)):
            step = dict(
                method = "restyle",
                args = ['visible', [False] * len(fig.data)]
            )
            step['args'][1][i] = True
            steps.append(step)

        sliders = [dict(steps=steps)]

        # Фиксируем масштаб осей
        fig.update_layout(
            width=800,
            height=800,
            sliders=sliders,
            scene=dict(
                xaxis=dict(range=[mid_x - max_range * 0.5, mid_x + max_range * 0.5]),
                yaxis=dict(range=[mid_y - max_range * 0.5, mid_y + max_range * 0.5]),
                zaxis=dict(range=[mid_z - max_range * 0.5, mid_z + max_range * 0.5]),
                aspectmode='cube'  # Сохраняем кубическую проекцию
            ),
            scene_camera=dict(
                eye=dict(x=1.5, y=1.5, z=1.5),  # Положение камеры по умолчанию
                up=dict(x=0, y=0, z=1),         # Ось Z - вверх
                center=dict(x=0, y=0, z=0)      # Центр в начале координат
            ),
        )

        fig.show()


    def __str__(self):
        string = "Manipulator:\n|-"
        for pair in self.pairs:
            string += str(pair)
        string += "C"

        return string
