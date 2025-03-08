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

        self.scene.set_drawing_mode(None)

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

        self.create_tools_menu()



        # ✅ Проверяем, что панель создана перед вызовом метода
        if self.drawing_tools:
            self.drawing_tools.update_pen_button()


    def import_image(self):
        """Открывает диалог выбора файла и загружает изображение"""
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "",
                                                   "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_path:
            self.scene.load_image(file_path)

    def open_ai_panel(self):
        """Открывает `AiPanel`"""
        if self.ai_panel is None:
            self.ai_panel = AiPanel(self)
            self.addDockWidget(Qt.RightDockWidgetArea, self.ai_panel)

        self.ai_panel.show()
        self.ai_panel.raise_()

    def open_drawing_settings(self, pen_button=None, *_):
        """Открывает панель рисования, передавая конкретную кнопку `pen`"""
        if self.drawing_tools is None:
            self.create_drawing_tools()

        if pen_button:
            self.drawing_tools.set_pen_button(pen_button)  # ✅ Передаём кнопку

        self.drawing_tools.show()

    def create_drawing_tools(self):
        """Создаёт `ui_settings_draw` (панель инструментов рисования) как отдельное окно"""
        if self.ai_panel is None:
            self.open_ai_panel()  # ✅ Убедимся, что `ai_panel` создан

        self.drawing_tools = DrawingTools(self)  # ✅ Убираем передачу `pen`
        self.drawing_tools.set_scene(self.scene)

        # ✅ Делаем `ui_settings_draw` отдельным окном
        self.drawing_tools.setFloating(True)
        self.drawing_tools.setAllowedAreas(Qt.NoDockWidgetArea)  # ❌ Отключаем привязку к краям

        self.addDockWidget(Qt.LeftDockWidgetArea, self.drawing_tools)  # ✅ Нужно добавить, но без привязки
        self.drawing_tools.hide()  # ✅ Скрываем при запуске

    def open_drawing_settings(self, pen_button=None, sceen=None):
        """Открывает панель рисования и устанавливает active_scene"""
        if self.drawing_tools is None:
            self.create_drawing_tools()

        if pen_button:
            self.drawing_tools.set_pen_button(pen_button)

        if sceen:
            self.scene.set_active_scene(sceen)  # ✅ Устанавливаем текущий sceen

        self.drawing_tools.show()

    def choose_color(self):
        """Выбирает цвет кисти и обновляет цвет кнопки 'pen'"""
        color = QColorDialog.getColor()
        if color.isValid():
            self.selected_color = color
            self.scene.set_pen_color(color)  # Меняем цвет кисти в сцене

    def create_tools_menu(self):
        """Создаёт список инструментов в меню menutools"""
        self.menutools.clear()

        # Инструмент "Мышь" (для взаимодействия с объектами)
        self.mouse_action = QAction("Мышь", self, checkable=True)
        self.mouse_action.triggered.connect(lambda: self.set_tool("mouse"))
        self.menutools.addAction(self.mouse_action)

        # Инструмент "Круг"
        self.circle_action = QAction("Круг", self, checkable=True)
        self.circle_action.triggered.connect(lambda: self.set_tool("circle"))
        self.menutools.addAction(self.circle_action)

        # Инструмент "Квадрат"
        self.square_action = QAction("Квадрат", self, checkable=True)
        self.square_action.triggered.connect(lambda: self.set_tool("square"))
        self.menutools.addAction(self.square_action)

        # Инструмент "Линия"
        self.line_action = QAction("Линия", self, checkable=True)
        self.line_action.triggered.connect(lambda: self.set_tool("line"))
        self.menutools.addAction(self.line_action)

        # Инструмент "Кисть"
        self.free_action = QAction("Кисть", self, checkable=True)
        self.free_action.triggered.connect(lambda: self.set_tool("free"))
        self.menutools.addAction(self.free_action)

        # ✅ Группируем кнопки, чтобы работала система "только одна активная"
        self.tool_actions = [self.mouse_action, self.circle_action, self.square_action, self.line_action,
                             self.free_action]

    def set_tool(self, tool):
        """Устанавливает выбранный инструмент"""
        # ✅ Снимаем выделение со всех кнопок перед активацией одной
        for action in self.tool_actions:
            action.setChecked(False)

        # ✅ Выделяем текущий инструмент
        sender = self.sender()
        if sender:
            sender.setChecked(True)

        # ✅ Устанавливаем режим в `DrawingScene`
        if tool == "mouse":
            self.scene.set_drawing_mode(None)  # ✅ Отключаем рисование
            self.scene.enable_selection()  # ✅ Включаем выделение объектов
            self.mouse_action.setChecked(True)  # ✅ Активируем кнопку "Мышь"
        else:
            self.scene.set_drawing_mode(tool)



