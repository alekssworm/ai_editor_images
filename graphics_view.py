from PySide6.QtWidgets import QGraphicsView
from PySide6.QtGui import QWheelEvent, QMouseEvent
from PySide6.QtCore import Qt

class GraphicsViewWithZoom(QGraphicsView):
    """Расширенный QGraphicsView с поддержкой зума и панорамирования"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragMode(QGraphicsView.NoDrag)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.zoom_factor = 1.15
        self.min_zoom = 0.5
        self.max_zoom = 3.0
        self.current_zoom = 1.0
        self.is_panning = False

    def wheelEvent(self, event: QWheelEvent):
        """Масштабирование при прокрутке колесика мыши"""
        if event.modifiers() == Qt.ControlModifier:
            if event.angleDelta().y() > 0:
                if self.current_zoom < self.max_zoom:
                    self.scale(self.zoom_factor, self.zoom_factor)
                    self.current_zoom *= self.zoom_factor
            else:
                if self.current_zoom > self.min_zoom:
                    self.scale(1 / self.zoom_factor, 1 / self.zoom_factor)
                    self.current_zoom /= self.zoom_factor
        else:
            super().wheelEvent(event)

    def mousePressEvent(self, event: QMouseEvent):
        """Обрабатываем рисование и панорамирование"""
        if event.button() == Qt.MiddleButton:
            self.is_panning = True
            self.setCursor(Qt.ClosedHandCursor)
            self.start_pan = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        """Обрабатываем движение мыши"""
        if self.is_panning:
            delta = event.pos() - self.start_pan
            self.start_pan = event.pos()
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - delta.x())
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - delta.y())
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        """Отпускаем кнопку мыши (завершаем панорамирование)"""
        if event.button() == Qt.MiddleButton:
            self.is_panning = False
            self.setCursor(Qt.ArrowCursor)
        else:
            super().mouseReleaseEvent(event)
