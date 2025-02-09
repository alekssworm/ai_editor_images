from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QDockWidget, QVBoxLayout
from PySide6.QtCore import Qt  # ✅ Импортируем Qt
from ui_editor import Ui_MainWindow
from ai_tools_logic import AiPanel  # AI Panel
from import_logic import ImageViewer, import_image  # Импорт логики изображений


class Editor(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Создаем QGraphicsView для изображения
        self.image_viewer = ImageViewer(self)
        self.frame_layout = QVBoxLayout(self.frame)  # Используем QVBoxLayout
        self.frame_layout.addWidget(self.image_viewer)
        self.frame.setLayout(self.frame_layout)

        # Добавляем кнопку "Import"
        if hasattr(self, "menuimport"):
            self.action_import = QAction("Import", self)
            self.menuimport.addAction(self.action_import)
            self.action_import.triggered.connect(lambda: import_image(self.image_viewer))
        else:
            print("❌ Ошибка: menuimport не найден в ui_editor.py!")

        # AI Panel (правый док-виджет)
        self.ai_panel = QDockWidget("AI Panel", self)
        self.ai_panel.setAllowedAreas(Qt.RightDockWidgetArea)  # ✅ Qt теперь определён
        self.ai_widget = AiPanel(self)  # Используем AiPanel из ai_tools_logic.py
        self.ai_panel.setWidget(self.ai_widget)  # Теперь это QWidget
        self.addDockWidget(Qt.RightDockWidgetArea, self.ai_panel)
        self.ai_panel.setVisible(False)  # По умолчанию скрыта

        # Подключаем кнопку "AI Tools"
        if hasattr(self, "menu_ai_tools"):
            self.action_ai_tools = QAction("AI Tools", self)
            self.menu_ai_tools.addAction(self.action_ai_tools)
            self.action_ai_tools.triggered.connect(self.toggle_ai_panel)

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
