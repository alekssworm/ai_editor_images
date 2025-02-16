from PySide6.QtGui import QAction, QPixmap, QPainterPath, QPen, QColor, QWheelEvent
from PySide6.QtWidgets import QMainWindow, QDockWidget, QVBoxLayout, QGraphicsScene, QGraphicsView, QFileDialog, \
    QGraphicsPixmapItem, QGraphicsPathItem, QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsLineItem, \
    QColorDialog, QPushButton, QWidget, QLabel, QSlider
from PySide6.QtCore import Qt, QRectF, QPointF

from ui_editor import Ui_MainWindow
from ai_tools_logic import AiPanel  # AI Panel


class DrawingScene(QGraphicsScene):
    """Сцена для рисования и добавления фигур"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pen_color = QColor(Qt.GlobalColor.black)
        self.pen_width = 2
        self.drawing = False
        self.current_item = None
        self.img_item = None
        self.shape_mode = None  # None, "rectangle", "ellipse", "line"

    def set_drawing_enabled(self, enabled):
        """Включает/выключает рисование кистью"""
        self.drawing = enabled
        self.shape_mode = None  # Отключаем фигуры

    def set_pen_color(self, color):
        """Устанавливает цвет кисти"""
        self.pen_color = color

    def set_pen_width(self, width):
        """Устанавливает толщину кисти"""
        self.pen_width = width

    def set_image_item(self, img_item):
        """Устанавливает загруженное изображение"""
        self.img_item = img_item

    def set_shape_mode(self, shape):
        """Устанавливает режим рисования фигур"""
        self.shape_mode = shape
        self.drawing = False  # Отключаем кисть

    def is_inside_image(self, pos):
        """Проверяет, внутри ли курсор изображения"""
        if self.img_item:
            img_rect: QRectF = self.img_item.sceneBoundingRect()
            return img_rect.contains(pos)
        return False

    def mousePressEvent(self, event):
        """Начинает рисование (кисть или фигура)"""
        pos = event.scenePos()
        if not self.is_inside_image(pos):
            return

        if self.drawing:
            # Рисуем кистью
            self.current_item = QGraphicsPathItem()
            self.current_item.setPen(QPen(self.pen_color, self.pen_width))
            self.addItem(self.current_item)
            self.current_path = self.current_item.path()
            self.current_path.moveTo(pos)
            self.current_item.setPath(self.current_path)
        elif self.shape_mode:
            # Запоминаем начальную точку фигуры
            self.start_pos = pos

    def mouseMoveEvent(self, event):
        """Обновляет рисование кистью или фигуры"""
        pos = event.scenePos()
        if not self.is_inside_image(pos):
            return

        if self.drawing and self.current_item:
            self.current_path.lineTo(pos)
            self.current_item.setPath(self.current_path)
        elif self.shape_mode:
            if self.current_item:
                self.removeItem(self.current_item)

            start_x, start_y = self.start_pos.x(), self.start_pos.y()
            width, height = pos.x() - start_x, pos.y() - start_y

            if self.shape_mode == "rectangle":
                self.current_item = QGraphicsRectItem(start_x, start_y, width, height)
            elif self.shape_mode == "ellipse":
                self.current_item = QGraphicsEllipseItem(start_x, start_y, width, height)
            elif self.shape_mode == "line":
                self.current_item = QGraphicsLineItem(start_x, start_y, pos.x(), pos.y())

            self.current_item.setPen(QPen(self.pen_color, self.pen_width))
            self.addItem(self.current_item)

    def mouseReleaseEvent(self, event):
        """Завершает рисование"""
        if self.drawing:
            self.current_item = None
        elif self.shape_mode:
            self.current_item = None


class Editor(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Создаем сцену для рисования
        self.scene = DrawingScene(self)
        self.graphicsView.setScene(self.scene)

        # Включаем зум
        self.zoom_factor = 1.0
        self.min_zoom = 0.1
        self.max_zoom = 5.0

        # Кнопка для импорта изображения
        if hasattr(self, "menuimport"):
            self.action_import = QAction("Import", self)
            self.menuimport.addAction(self.action_import)
            self.action_import.triggered.connect(self.load_image)

        # Создаем левую панель инструментов
        self.create_tools_panel()

    def create_tools_panel(self):
        """Создает левую панель инструментов"""
        self.tools_panel = QDockWidget("Инструменты", self)
        self.tools_panel.setAllowedAreas(Qt.LeftDockWidgetArea)

        tools_widget = QWidget()
        layout = QVBoxLayout()

        # Кнопки кисти и фигур
        self.pen_button = QPushButton("Кисть")
        self.pen_button.clicked.connect(lambda: self.scene.set_drawing_enabled(True))
        layout.addWidget(self.pen_button)

        self.color_button = QPushButton("Выбрать цвет")
        self.color_button.clicked.connect(self.choose_color)
        layout.addWidget(self.color_button)

        self.rect_button = QPushButton("Прямоугольник")
        self.rect_button.clicked.connect(lambda: self.scene.set_shape_mode("rectangle"))
        layout.addWidget(self.rect_button)

        self.ellipse_button = QPushButton("Круг")
        self.ellipse_button.clicked.connect(lambda: self.scene.set_shape_mode("ellipse"))
        layout.addWidget(self.ellipse_button)

        self.line_button = QPushButton("Линия")
        self.line_button.clicked.connect(lambda: self.scene.set_shape_mode("line"))
        layout.addWidget(self.line_button)

        self.size_label = QLabel("Толщина:")
        layout.addWidget(self.size_label)

        self.size_slider = QSlider(Qt.Horizontal)
        self.size_slider.setMinimum(1)
        self.size_slider.setMaximum(10)
        self.size_slider.setValue(self.scene.pen_width)
        self.size_slider.valueChanged.connect(self.change_pen_size)
        layout.addWidget(self.size_slider)

        tools_widget.setLayout(layout)
        self.tools_panel.setWidget(tools_widget)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.tools_panel)

    def choose_color(self):
        """Выбирает цвет"""
        color = QColorDialog.getColor()
        if color.isValid():
            self.scene.set_pen_color(color)

    def change_pen_size(self, value):
        """Меняет толщину кисти"""
        self.scene.set_pen_width(value)

    def load_image(self):
        """Загружает изображение"""
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "",
                                                   "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_path:
            pixmap = QPixmap(file_path)
            self.scene.clear()
            img_item = QGraphicsPixmapItem(pixmap)
            self.scene.addItem(img_item)
            self.scene.set_image_item(img_item)
