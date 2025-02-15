from PySide6.QtWidgets import QDialog, QColorDialog, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem,QGraphicsRectItem, QGraphicsPolygonItem, QGraphicsPathItem
from PySide6.QtGui import QPainterPath, QPen, QColor, QPolygonF
from PySide6.QtCore import Qt, QPointF
from ui_allocation import Ui_Dialog


class AllocationWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Создаем графическую сцену и виджет
        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene, self)
        self.gridLayout.addWidget(self.view, 1, 0, 1, 2)  # Добавляем в layout

        # Настройки инструмента
        self.current_tool = "pen"  # По умолчанию кисть
        self.current_color = QColor(Qt.black)

        # Подключаем кнопки
        if hasattr(self, "checkBox"):
            self.checkBox.clicked.connect(lambda: self.set_tool("pen"))
        if hasattr(self, "checkBox_2"):
            self.checkBox_2.clicked.connect(lambda: self.set_tool("rectangle"))
        if hasattr(self, "checkBox_3"):
            self.checkBox_3.clicked.connect(lambda: self.set_tool("circle"))
        if hasattr(self, "pushButton_4"):
            self.pushButton_4.clicked.connect(lambda: self.set_tool("polygon"))
        if hasattr(self, "color_wheel"):
            self.color_wheel.mousePressEvent = self.choose_color

    def set_tool(self, tool):
        self.current_tool = tool

    def choose_color(self, event):
        color = QColorDialog.getColor()
        if color.isValid():
            self.current_color = color

    def mousePressEvent(self, event):
        """Создает объект при нажатии в зависимости от выбранного инструмента."""
        pos = self.view.mapToScene(event.pos())

        if self.current_tool == "pen":
            self.current_path = QPainterPath()
            self.current_path.moveTo(pos)
            self.current_item = QGraphicsPathItem(self.current_path)
            self.scene.addItem(self.current_item)

        elif self.current_tool == "rectangle":
            rect = QGraphicsRectItem(pos.x(), pos.y(), 50, 50)
            rect.setBrush(self.current_color)
            self.scene.addItem(rect)

        elif self.current_tool == "circle":
            ellipse = QGraphicsEllipseItem(pos.x(), pos.y(), 50, 50)
            ellipse.setBrush(self.current_color)
            self.scene.addItem(ellipse)

        elif self.current_tool == "polygon":
            self.current_polygon = QGraphicsPolygonItem()
            self.current_polygon.setPen(QPen(self.current_color, 2))
            self.scene.addItem(self.current_polygon)
            self.polygon_points = [pos]

    def mouseMoveEvent(self, event):
        pos = self.view.mapToScene(event.pos())

        if self.current_tool == "pen" and hasattr(self, "current_item"):
            self.current_path.lineTo(pos)
            self.current_item.setPath(self.current_path)

        elif self.current_tool == "polygon" and hasattr(self, "polygon_points"):
            self.polygon_points.append(pos)
            self.current_polygon.setPolygon(QPolygonF(self.polygon_points))

    def mouseReleaseEvent(self, event):
        pass  # Можно добавить логику для завершения многоугольника


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = AllocationWindow()
    window.show()
    sys.exit(app.exec())
