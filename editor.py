from PySide6.QtWidgets import QMainWindow, QColorDialog, QFileDialog, QDockWidget
from PySide6.QtGui import QColor, QIcon
from PySide6.QtCore import Qt
from ui_editor import Ui_MainWindow
from drawing_scene import DrawingScene
from graphics_view import GraphicsViewWithZoom
from ai_tools_logic import AiPanel
from drawing_tools import DrawingTools
from PySide6.QtGui import QAction

class Editor(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # ✅ Используем GraphicsViewWithZoom
        self.graphicsView = GraphicsViewWithZoom(self)
        self.setCentralWidget(self.graphicsView)

        # ✅ Создаём сцену для рисования
        self.scene = DrawingScene(self)
        self.graphicsView.setScene(self.scene)

        # ✅ Добавляем кнопку "Импорт"
        self.import_action = QAction("Импорт", self)
        self.menuimport.addAction(self.import_action)
        self.import_action.triggered.connect(self.import_image)

        # ✅ Добавляем кнопку AI Tools
        self.ai_tools_action = QAction("AI Tools", self)
        self.menu_ai_tools.addAction(self.ai_tools_action)
        self.ai_tools_action.triggered.connect(self.open_ai_panel)

        self.selected_color = QColor(Qt.black)  # Чёрный цвет по умолчанию
        self.ai_panel = None
        self.drawing_tools = None  # Панель рисования создаётся при нажатии

    def import_image(self):
        """Открывает диалог выбора файла и загружает изображение"""
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "",
                                                   "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_path:
            self.scene.load_image(file_path)

    def open_ai_panel(self):
        """Открывает `AiPanel` и подключает кнопку `pen`"""
        if self.ai_panel is None:
            self.ai_panel = AiPanel(self)
            self.ai_panel.pen.clicked.connect(self.open_drawing_settings)  # Подключаем кнопку
            self.addDockWidget(Qt.RightDockWidgetArea, self.ai_panel)

        self.ai_panel.show()
        self.ai_panel.raise_()

    def open_drawing_settings(self):
        """Открывает `ui_settings_draw`"""
        if self.drawing_tools is None:
            self.create_drawing_tools()
        self.drawing_tools.show()

    def create_drawing_tools(self):
        """Создаёт `ui_settings_draw` (панель инструментов рисования) как отдельное окно"""
        if self.ai_panel is None:
            self.open_ai_panel()  # ✅ Убедимся, что `ai_panel` создан

        self.drawing_tools = DrawingTools(self, self.ai_panel.pen)  # ✅ Передаем `pen`
        self.drawing_tools.set_scene(self.scene)

        # ✅ Делаем `ui_settings_draw` отдельным окном
        self.drawing_tools.setFloating(True)
        self.drawing_tools.setAllowedAreas(Qt.NoDockWidgetArea)  # ❌ Отключаем привязку к краям

        self.addDockWidget(Qt.LeftDockWidgetArea, self.drawing_tools)  # ✅ Нужно добавить, но без привязки
        self.drawing_tools.hide()  # ✅ Скрываем при запуске

    def open_drawing_settings(self):
            """Открывает `ui_settings_draw` как отдельное окно"""
            if self.drawing_tools is None:
                self.create_drawing_tools()

            self.drawing_tools.show()
            self.drawing_tools.raise_()  # ✅ Поднимаем окно наверх

    def choose_color(self):
        """Выбирает цвет кисти и обновляет цвет кнопки 'pen'"""
        color = QColorDialog.getColor()
        if color.isValid():
            self.selected_color = color
            self.scene.set_pen_color(color)  # Меняем цвет кисти в сцене

