from PySide6.QtWidgets import QDialog, QColorDialog
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
from ui_ai_panel import Ui_Dialog


class AiPanel(QDialog, Ui_Dialog):
    """Панель инструментов AI"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Подключаем кнопки к функциям
        self.colour.clicked.connect(self.choose_color)
        self.pen.clicked.connect(self.toggle_drawing_mode)

        # Цвет для рисования
        self.pen_color = QColor(Qt.GlobalColor.black)
        self.drawing = False  # Флаг рисования

    def choose_color(self):
        """Выбор цвета кисти"""
        color = QColorDialog.getColor()
        if color.isValid():
            self.pen_color = color  # Обновляем цвет кисти

            # Получаем главное окно (Editor) и устанавливаем цвет кисти
            editor = self.get_editor()
            if editor:
                editor.pen_color = color

    def toggle_drawing_mode(self):
        """Переключение режима рисования"""
        self.drawing = not self.drawing

        # Получаем главное окно (Editor) и включаем режим рисования
        editor = self.get_editor()
        if editor:
            editor.toggle_drawing_mode()

    def get_editor(self):
        """Возвращает главный `Editor` из `QDockWidget`"""
        parent = self.parentWidget()
        while parent:
            if isinstance(parent, QDialog):  # Проверяем, является ли родитель Editor
                return parent
            parent = parent.parentWidget()
        return None
