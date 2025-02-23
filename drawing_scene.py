from PySide6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from PySide6.QtGui import QPixmap, QPen, QColor, QPainterPath
from PySide6.QtCore import Qt

class DrawingScene(QGraphicsScene):
    """Сцена для рисования с поддержкой фигур и кисти"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pen_color = QColor(0, 255, 0, 255)  # Зеленый цвет по умолчанию
        self.pen_width = 2  # Толщина кисти
        self.shape_mode = "free"  # Режим рисования
        self.current_path = None
        self.current_item = None
        self.start_point = None
        self.image_item = None
        self.image_rect = None
        self.drawing = False
        self.temp_item = None



    def set_drawing_mode(self, mode):
        """Устанавливает режим рисования"""
        self.shape_mode = mode

    def set_pen_width(self, width):
        """Изменяет толщину кисти"""
        self.pen_width = width

    def set_pen_color(self, color):
        """Изменение цвета кисти"""
        self.pen_color = QColor(color.red(), color.green(), color.blue(), self.pen_color.alpha())

    def set_pen_opacity(self, value):
        """Меняет прозрачность кисти (0-100 -> 0-255)"""
        alpha = int((value / 100) * 255)  # ✅ Преобразуем 0-100 в 0-255
        self.pen_color.setAlpha(alpha)  # ✅ Изменяем только прозрачность



    def load_image(self, image_path):
        """Загружает изображение в сцену"""
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print("Ошибка: невозможно загрузить изображение")
            return
        if self.image_item:
            self.removeItem(self.image_item)
        self.image_item = QGraphicsPixmapItem(pixmap)
        self.addItem(self.image_item)
        self.image_item.setZValue(-1)
        self.image_rect = self.image_item.boundingRect()

    def mousePressEvent(self, event):
        """Начало рисования"""
        if self.image_item and not self.image_rect.contains(self.image_item.mapFromScene(event.scenePos())):
            return
        self.drawing = True
        pen = QPen(self.pen_color, self.pen_width)
        if self.shape_mode == "free":
            self.current_path = QPainterPath(event.scenePos())
            self.current_item = self.addPath(self.current_path, pen)
        elif self.shape_mode in ["circle", "square", "line"]:
            self.start_point = event.scenePos()

    def mouseMoveEvent(self, event):
        """Процесс рисования"""
        if not self.drawing:
            return
        pen = QPen(self.pen_color, self.pen_width)
        if self.shape_mode == "free" and self.current_item:
            path = self.current_path
            path.lineTo(event.scenePos())
            self.current_item.setPath(path)
        elif self.shape_mode in ["circle", "square", "line"]:
            if self.start_point is None:
                return
            if self.temp_item:
                self.removeItem(self.temp_item)
            if self.shape_mode == "circle":
                radius = abs(event.scenePos().x() - self.start_point.x())
                self.temp_item = self.addEllipse(self.start_point.x(), self.start_point.y(), radius, radius, pen)
            elif self.shape_mode == "square":
                size = abs(event.scenePos().x() - self.start_point.x())
                self.temp_item = self.addRect(self.start_point.x(), self.start_point.y(), size, size, pen)
            elif self.shape_mode == "line":
                self.temp_item = self.addLine(self.start_point.x(), self.start_point.y(), event.scenePos().x(), event.scenePos().y(), pen)

    def mouseReleaseEvent(self, event):
        """Завершение рисования"""
        if self.shape_mode in ["circle", "square", "line"] and self.temp_item:
            self.temp_item = None
        self.drawing = False
