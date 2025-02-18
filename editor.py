from PySide6.QtWidgets import (
    QMainWindow, QColorDialog, QGraphicsScene, QGraphicsPixmapItem,
    QGraphicsView, QDockWidget, QPushButton, QSlider, QLabel, QVBoxLayout, QWidget, QFileDialog
)
from PySide6.QtGui import QPixmap, QPen, QColor, QPainterPath
from PySide6.QtCore import Qt, QPointF
from ai_tools_logic import AiPanel
from ui_editor import Ui_MainWindow
from ui_settings_draw import Ui_DockWidget  # ✅ Импортируем ui_settings_draw
from PySide6.QtGui import QAction





class DrawingScene(QGraphicsScene):
    """✅ Сцена для рисования только внутри изображения"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pen_color = Qt.green  # ✅ Цвет кисти
        self.pen_width = 2  # ✅ Толщина кисти
        self.shape_mode = "free"  # ✅ Режим рисования
        self.current_path = None
        self.current_item = None  # ✅ Переменная для текущего рисунка
        self.start_point = None
        self.image_item = None  # ✅ Изображение
        self.drawing = False  # ✅ Флаг нажатия мыши

    def set_pen_color(self, color):
        """✅ Изменение цвета кисти"""
        self.pen_color = color

    def set_pen_width(self, width):
        """✅ Изменение толщины кисти"""
        self.pen_width = width

    def set_drawing_mode(self, mode):
        """✅ Устанавливает режим рисования (кисть, круг, квадрат, линия)"""
        self.shape_mode = mode

    def load_image(self, image_path):
        """✅ Загружает изображение в сцену"""
        pixmap = QPixmap(image_path)
        if self.image_item:
            self.removeItem(self.image_item)  # Удаляем старое изображение
        self.image_item = QGraphicsPixmapItem(pixmap)
        self.addItem(self.image_item)
        self.image_item.setZValue(-1)  # ✅ Размещаем изображение под слоями рисования
        self.image_rect = self.image_item.boundingRect()  # ✅ Сохраняем границы изображения

    def is_inside_image(self, point):
        """✅ Проверяет, находится ли точка внутри изображения"""
        return self.image_item and self.image_rect.contains(self.image_item.mapFromScene(point))

    def mousePressEvent(self, event):
        """✅ Начало рисования (только на изображении)"""
        if not self.is_inside_image(event.scenePos()):
            return  # ❌ Игнорируем, если клик за границами изображения

        self.drawing = True  # ✅ Устанавливаем флаг рисования

        if self.shape_mode == "free":
            self.current_path = QPainterPath(event.scenePos())
            self.current_item = self.addPath(self.current_path, QPen(self.pen_color, self.pen_width))
        elif self.shape_mode in ["circle", "square", "line"]:
            self.start_point = event.scenePos()  # ✅ Запоминаем начальную точку

    def mouseMoveEvent(self, event):
        """✅ Процесс рисования"""
        if not self.is_inside_image(event.scenePos()) or not self.drawing:
            return  # ❌ Игнорируем, если движение за границами или нет нажатия

        if self.shape_mode == "free" and self.current_item:
            path = self.current_path
            path.lineTo(event.scenePos())  # ✅ Добавляем линию к текущему положению мыши
            self.current_item.setPath(path)

        elif self.shape_mode in ["circle", "square", "line"]:
            if self.start_point is None:
                return  # ❌ Игнорируем, если `start_point` не установлен

            if hasattr(self, "temp_item") and self.temp_item:
                self.removeItem(self.temp_item)  # ✅ Удаляем старую временную фигуру

            pen = QPen(self.pen_color, self.pen_width)

            if self.shape_mode == "circle":
                radius = abs(event.scenePos().x() - self.start_point.x())
                self.temp_item = self.addEllipse(self.start_point.x(), self.start_point.y(), radius, radius, pen)
            elif self.shape_mode == "square":
                size = abs(event.scenePos().x() - self.start_point.x())
                self.temp_item = self.addRect(self.start_point.x(), self.start_point.y(), size, size, pen)
            elif self.shape_mode == "line":
                self.temp_item = self.addLine(self.start_point.x(), self.start_point.y(), event.scenePos().x(), event.scenePos().y(), pen)

    def mouseReleaseEvent(self, event):
        """✅ Завершение рисования"""
        if self.shape_mode in ["circle", "square", "line"]:
            self.temp_item = None  # ✅ Оставляем фигуру на холсте

        self.drawing = False  # ✅ Сбрасываем флаг рисования


from PySide6.QtWidgets import QGraphicsView
from PySide6.QtGui import QWheelEvent
from PySide6.QtCore import Qt

from PySide6.QtWidgets import QGraphicsView
from PySide6.QtGui import QWheelEvent, QMouseEvent
from PySide6.QtCore import Qt

from PySide6.QtWidgets import QGraphicsView
from PySide6.QtGui import QWheelEvent, QMouseEvent
from PySide6.QtCore import Qt

class GraphicsViewWithZoom(QGraphicsView):
    """✅ Расширенный QGraphicsView с поддержкой зума и без блокировки рисования"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragMode(QGraphicsView.NoDrag)  # ❌ Убираем режим перетаскивания (мешал рисованию)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)  # ✅ Зум вокруг мыши
        self.zoom_factor = 1.15  # Коэффициент масштабирования
        self.min_zoom = 0.5  # Минимальный масштаб (чтобы изображение не исчезло)
        self.max_zoom = 3.0  # Максимальный масштаб
        self.current_zoom = 1.0  # Текущее увеличение
        self.is_panning = False  # ✅ Флаг панорамирования

    def wheelEvent(self, event: QWheelEvent):
        """✅ Масштабирование при прокрутке колесика мыши (только при зажатом Ctrl)"""
        if event.modifiers() == Qt.ControlModifier:  # ✅ Увеличение только при зажатом Ctrl
            if event.angleDelta().y() > 0:  # Прокрутка вверх (увеличение)
                if self.current_zoom < self.max_zoom:
                    self.scale(self.zoom_factor, self.zoom_factor)
                    self.current_zoom *= self.zoom_factor
            else:  # Прокрутка вниз (уменьшение)
                if self.current_zoom > self.min_zoom:
                    self.scale(1 / self.zoom_factor, 1 / self.zoom_factor)
                    self.current_zoom /= self.zoom_factor
        else:
            super().wheelEvent(event)  # ✅ Если нет Ctrl, передаем событие дальше

    def mousePressEvent(self, event: QMouseEvent):
        """✅ Обрабатываем рисование и панорамирование"""
        if event.button() == Qt.MiddleButton:  # ✅ Панорамирование по средней кнопке мыши
            self.is_panning = True
            self.setCursor(Qt.ClosedHandCursor)
            self.start_pan = event.pos()
        else:
            super().mousePressEvent(event)  # ✅ Передаем событие сцене (рисование)

    def mouseMoveEvent(self, event: QMouseEvent):
        """✅ Обрабатываем движение мыши (рисование и панорамирование)"""
        if self.is_panning:
            delta = event.pos() - self.start_pan
            self.start_pan = event.pos()
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - delta.x())
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - delta.y())
        else:
            super().mouseMoveEvent(event)  # ✅ Передаем событие сцене (рисование)

    def mouseReleaseEvent(self, event: QMouseEvent):
        """✅ Отпускаем кнопку мыши (завершаем панорамирование)"""
        if event.button() == Qt.MiddleButton:
            self.is_panning = False
            self.setCursor(Qt.ArrowCursor)
        else:
            super().mouseReleaseEvent(event)  # ✅ Передаем событие сцене (рисование)



class Editor(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # ✅ Используем `GraphicsViewWithZoom`
        self.graphicsView = GraphicsViewWithZoom(self)
        self.setCentralWidget(self.graphicsView)

        # ✅ Устанавливаем сцену для рисования
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

        self.ai_panel = None  # ✅ Панель создается только при нажатии
        self.drawing_tools = None  # ✅ Создаем переменную, но не инициализируем

    def import_image(self):
        """✅ Открывает диалог выбора файла и загружает изображение"""
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "",
                                                   "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_path:
            self.scene.load_image(file_path)  # ✅ Загружаем изображение в сцену

    def open_ai_panel(self):
        """✅ Открывает `AiPanel` при нажатии"""
        if self.ai_panel is None:
            self.ai_panel = AiPanel(self)
            self.ai_panel.pen.clicked.connect(self.open_drawing_settings)  # ✅ Подключаем кнопку "pen"
            self.addDockWidget(Qt.RightDockWidgetArea, self.ai_panel)

        self.ai_panel.show()
        self.ai_panel.raise_()

    def open_drawing_settings(self):
        """✅ Открывает `ui_settings_draw` (панель инструментов рисования)"""
        if self.drawing_tools is None:  # ✅ Проверяем, существует ли панель
            self.create_drawing_tools()  # ✅ Создаем панель, если её нет
        self.drawing_tools.show()

    def create_drawing_tools(self):
        """✅ Создает `ui_settings_draw` (панель инструментов рисования)"""
        self.drawing_tools = QDockWidget("Настройки рисования", self)
        self.drawing_tools.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

        # ✅ Подключаем `ui_settings_draw`
        self.ui_draw = Ui_DockWidget()
        self.ui_draw.setupUi(self.drawing_tools)

        # ✅ Подключаем кнопки к логике рисования
        self.ui_draw.pushButton_30.clicked.connect(lambda: self.scene.set_drawing_mode("free"))  # Кисть
        self.ui_draw.pushButton_21.clicked.connect(lambda: self.scene.set_drawing_mode("circle"))  # Круг
        self.ui_draw.pushButton_27.clicked.connect(lambda: self.scene.set_drawing_mode("square"))  # Квадрат
        self.ui_draw.colour_2.clicked.connect(lambda: self.scene.set_drawing_mode("line"))  # Линия
        self.ui_draw.colour_3.clicked.connect(self.choose_color)  # Выбор цвета

        # ✅ Подключаем ползунки
        self.ui_draw.horizontalSlider.valueChanged.connect(self.change_pen_size)

        self.addDockWidget(Qt.LeftDockWidgetArea, self.drawing_tools)
        self.drawing_tools.hide()  # ✅ Скрываем панель при запуске

    def choose_color(self):
        """✅ Выбирает цвет кисти"""
        color = QColorDialog.getColor()
        if color.isValid():
            self.scene.set_pen_color(color)

    def change_pen_size(self, value):
        """✅ Меняет толщину кисти"""
        self.scene.set_pen_width(value)

