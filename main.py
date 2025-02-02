import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow  # Импортируем сгенерированный UI
from ui_editor import Ui_Dialog  # Импортируем редактор

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Подключаем кнопку custom_image к функции
        self.ui.custom_image.clicked.connect(self.open_editor)

    def open_editor(self):
        """Закрываем текущее окно и открываем редактор"""
        self.editor = EditorApp()
        self.editor.show()
        self.close()  # Закрываем главное окно

class EditorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
