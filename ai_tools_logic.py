from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QDockWidget, QWidget
from PySide6.QtCore import Qt
from ai_panel import Ui_Dialog  # Загружаем UI панели AI
from ui_editor import Ui_MainWindow


from PySide6.QtWidgets import QWidget
from ai_panel import Ui_Dialog  # UI AI Panel

class AiPanel(QWidget, Ui_Dialog):
    """Класс панели AI Tools"""
    def __init__(self, parent=None):  # ✅ Добавили parent
        super().__init__(parent)  # ✅ Передаём parent в QWidget
        self.setupUi(self)  # Загружаем UI



class Editor(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Проверяем, есть ли menu_ai_tools в UI
        if hasattr(self, "menu_ai_tools"):
            self.action_ai_tools = QAction("AI Tools", self)
            self.menu_ai_tools.addAction(self.action_ai_tools)
            self.action_ai_tools.triggered.connect(self.toggle_ai_panel)
        else:
            print("⚠ Ошибка: menu_ai_tools не найден в ui_editor.py!")

        # Создаем и настраиваем AI Panel как QDockWidget
        self.ai_panel = QDockWidget("AI Panel", self)
        self.ai_panel.setAllowedAreas(Qt.RightDockWidgetArea)
        self.ai_widget = AiPanel()  # Создаем виджет на основе UI
        self.ai_panel.setWidget(self.ai_widget)  # Теперь это QWidget
        self.addDockWidget(Qt.RightDockWidgetArea, self.ai_panel)
        self.ai_panel.setVisible(False)  # Скрываем панель при запуске

    def toggle_ai_panel(self):
        """Переключает видимость AI Panel."""
        self.ai_panel.setVisible(not self.ai_panel.isVisible())


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = Editor()
    window.show()
    sys.exit(app.exec())

