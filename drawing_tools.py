from PySide6.QtWidgets import QDockWidget, QColorDialog
from PySide6.QtGui import QColor, QIcon
from ui_settings_draw import Ui_DockWidget

class DrawingTools(QDockWidget, Ui_DockWidget):
    """Панель инструментов рисования"""

    def __init__(self, parent=None, pen_button=None):
        super().__init__(parent)
        self.setupUi(self)
        self.scene = None  # Ссылка на сцену
        self.pen_button = None

        self.pushButton_30.clicked.connect(lambda: self.set_drawing_mode("free"))
        self.pushButton_21.clicked.connect(lambda: self.set_drawing_mode("circle"))
        self.pushButton_27.clicked.connect(lambda: self.set_drawing_mode("square"))
        self.colour_2.clicked.connect(lambda: self.set_drawing_mode("line"))
        self.colour_3.clicked.connect(self.choose_color)

        self.horizontalSlider.valueChanged.connect(self.change_pen_size)
        self.horizontalSlider_2.valueChanged.connect(self.change_pen_opacity)



    def set_scene(self, scene):
        """Устанавливает ссылку на сцену"""
        self.scene = scene

    def set_drawing_mode(self, mode):
        """Устанавливает режим рисования"""
        if self.scene:
            self.scene.set_drawing_mode(mode)

    def change_pen_size(self, value):
        """Меняет толщину кисти"""
        if self.scene:
            self.scene.set_pen_width(value)

    def change_pen_opacity(self, value):
        """Меняет прозрачность кисти"""
        if self.scene:
            self.scene.set_pen_opacity(value)

    def choose_color(self):
        """Выбор цвета кисти"""
        color = QColorDialog.getColor()
        if color.isValid() and self.scene:
            self.scene.set_pen_color(color)

    def set_pen_button(self, pen_button):
        """Устанавливает, какая кнопка 'pen' была нажата"""
        self.pen_button = pen_button

    def update_pen_button(self):
        """Обновляет только ту кнопку 'pen', которая вызвала панель"""
        if not self.pen_button or not self.scene:
            return  # Если кнопка не задана, ничего не делаем

        icons = {
            "free": "icons/attribution-pencil.svg",
            "circle": "icons/circle.svg",
            "square": "icons/stop.svg",
            "line": "icons/algorithm.svg",
        }

        # ✅ Меняем иконку только у нажатой кнопки
        icon_path = icons.get(self.scene.shape_mode, "icons/attribution-pencil.svg")
        self.pen_button.setIcon(QIcon(icon_path))

        # ✅ Меняем цвет только у нажатой кнопки
        color = self.scene.pen_color
        rgba_color = f"rgba({color.red()}, {color.green()}, {color.blue()}, {color.alpha()})"
        self.pen_button.setStyleSheet(f"background-color: {rgba_color}; border-radius: 5px;")

    def set_drawing_mode(self, mode):
        """Устанавливает режим рисования и обновляет кнопку 'pen'"""
        if self.scene:
            self.scene.set_drawing_mode(mode)
            self.update_pen_button()  # 🔥 Обновляем кнопку

    def change_pen_size(self, value):
        """Меняет толщину кисти и обновляет кнопку 'pen'"""
        if self.scene:
            self.scene.set_pen_width(value)
            self.update_pen_button()  # 🔥 Обновляем кнопку

    def change_pen_opacity(self, value):
        """Меняет прозрачность кисти и обновляет кнопку 'pen'"""
        if self.scene:
            self.scene.set_pen_opacity(value)
            self.update_pen_button()  # 🔥 Обновляем кнопку

    def choose_color(self):
        """Выбор цвета кисти и обновление кнопки 'pen'"""
        color = QColorDialog.getColor()
        if color.isValid() and self.scene:
            self.scene.set_pen_color(color)
            self.update_pen_button()  # 🔥 Обновляем кнопку










