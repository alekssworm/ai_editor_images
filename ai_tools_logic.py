from PySide6.QtWidgets import QDockWidget, QDialog, QVBoxLayout
from ui_ai_panel import Ui_DockWidget  # ✅ Импортируем `ui_ai_panel`

class AiPanel(QDockWidget, Ui_DockWidget):
    """Панель инструментов AI"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Устанавливаем основное содержимое виджета
        self.setWidget(self.dockWidgetContents)

        # ✅ Проверяем правильное имя кнопки
        if hasattr(self, "pushButton_27"):  # Проверяем альтернативное имя
            self.pushButton_27.clicked.connect(self.open_drawing_settings)  # Если кнопка нашлась
        else:
            print("Ошибка: Кнопка 'pen' не найдена в AiPanel")

    def open_drawing_settings(self):
        """Открывает окно настроек рисования"""
        self.draw_settings = QDialog(self)  # Создаем диалоговое окно
        self.ui_draw = Ui_DockWidget()
        self.ui_draw.setupUi(self.draw_settings)

        # ✅ Убираем `setWidget()`, заменяем на `setLayout()`
        layout = QVBoxLayout()
        layout.addWidget(self.ui_draw.dockWidgetContents)
        self.draw_settings.setLayout(layout)

        self.draw_settings.setWindowTitle("Настройки рисования")
        self.draw_settings.exec()  # Открываем окно как модальное
