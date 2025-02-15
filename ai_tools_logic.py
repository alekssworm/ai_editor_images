from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QDockWidget, QWidget, QDialog
from PySide6.QtCore import Qt
from ui_ai_panel import Ui_Dialog as Ui_AiPanel
from ui_editor import Ui_MainWindow
from ui_allocation import Ui_Dialog as Ui_Allocation


class AiPanel(QWidget, Ui_AiPanel):
    """Класс панели AI Tools"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Подключаем кнопку pen к открытию ui_allocation
        self.pen.clicked.connect(self.open_allocation)

    def open_allocation(self):
        """Открывает окно ui_allocation"""
        self.allocation_window = QDialog()
        self.ui_allocation = Ui_Allocation()
        self.ui_allocation.setupUi(self.allocation_window)
        self.allocation_window.show()




class Editor(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        if hasattr(self, "menu_ai_tools"):
            self.action_ai_tools = QAction("AI Tools", self)
            self.menu_ai_tools.addAction(self.action_ai_tools)
            self.action_ai_tools.triggered.connect(self.toggle_ai_panel)
        else:
            print("⚠ Ошибка: menu_ai_tools не найден в ui_editor.py!")

        # Создаем и настраиваем AI Panel как QDockWidget
        self.ai_panel = QDockWidget("AI Panel", self)
        self.ai_panel.setAllowedAreas(Qt.RightDockWidgetArea)
        self.ai_widget = AiPanel()
        self.ai_panel.setWidget(self.ai_widget)
        self.addDockWidget(Qt.RightDockWidgetArea, self.ai_panel)
        self.ai_panel.setVisible(False)

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
