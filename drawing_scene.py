from PySide6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QGraphicsItem, QMenu, QColorDialog
from PySide6.QtGui import QPixmap, QPen, QColor, QPainterPath, QAction
from PySide6.QtCore import Qt, QRectF


class DrawableObject:
    """Класс, представляющий фигуру на сцене"""
    def __init__(self, shape, item):
        self.shape = shape  # Тип фигуры: 'circle', 'square', 'line'
        self.item = item  # Графический объект QGraphicsItem
        self.pen = item.pen()  # Сохранение параметров пера

    def set_pen(self, pen: QPen):
        """Изменение пера (цвет, толщина и т.д.)"""
        self.pen = pen
        self.item.setPen(pen)

    def move(self, dx, dy):
        """Перемещение объекта"""
        self.item.moveBy(dx, dy)

class DrawingScene(QGraphicsScene):
    """Сцена для рисования с поддержкой фигур и кисти"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pen_color = QColor(0, 255, 0, 255)  # Зеленый цвет по умолчанию
        self.pen_width = 2  # Толщина кисти
        self.shape_mode = None
        self.current_path = None
        self.current_item = None
        self.start_point = None
        self.image_item = None
        self.image_rect = None
        self.drawing = False
        self.temp_item = None
        self.objects = []  # ✅ Список всех объектов на сцене
        self.active_scene = None  # ✅ Текущий sceen или sub_sceen
        self.selected_object = None

    def set_active_scene(self, scene):
        """Устанавливает, в каком sceen идет рисование"""
        self.active_scene = scene

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
        """Начинаем рисование"""
        if not self.active_scene:
            return  # Если не выбран sceen или sub_sceen, не рисуем

        self.drawing = True
        pen = QPen(self.pen_color, self.pen_width)
        self.start_point = event.scenePos()

        if self.shape_mode == "free":
            self.current_path = QPainterPath(event.scenePos())
            self.current_item = self.addPath(self.current_path, pen)
        elif self.shape_mode in ["circle", "square", "line"]:
            self.temp_item = None  # Будет создан в mouseMoveEvent

    def mouseMoveEvent(self, event):
        """Обрабатывает перемещение выделенного объекта с более плавным управлением"""
        if self.shape_mode is None:  # ✅ Если включён режим "Мышь"
            if self.selected_object and self.selected_object != self.image_item:
                delta = event.scenePos() - self.start_point
                self.selected_object.setPos(self.selected_object.pos() + delta)  # ✅ Плавно перемещаем объект
                self.start_point = event.scenePos()  # ✅ Обновляем начальную точку
            return

        # ✅ Обычный режим рисования
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
                if self.start_point is None:
                    return
                if self.temp_item:
                    self.removeItem(self.temp_item)

                x1, y1 = self.start_point.x(), self.start_point.y()
                x2, y2 = event.scenePos().x(), event.scenePos().y()

                rect = QRectF(x1, y1, x2 - x1, y2 - y1).normalized()  # ✅ Исправление!
                self.temp_item = self.addRect(rect, pen)

            elif self.shape_mode == "line":
                self.temp_item = self.addLine(self.start_point.x(), self.start_point.y(), event.scenePos().x(),
                                              event.scenePos().y(), pen)
                self.temp_item.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)

    def mouseReleaseEvent(self, event):
        """Завершаем рисование и добавляем объект в sceen"""
        if not self.active_scene:
            return

        if self.shape_mode in ["circle", "square", "line"] and self.temp_item:
            drawable = DrawableObject(self.shape_mode, self.temp_item)
            self.temp_item.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)

            # ✅ Добавляем объект в активную сцену и общий список
            self.active_scene.objects.append(drawable)
            self.objects.append(drawable)

            self.temp_item = None

        self.drawing = False

    def enable_selection(self):
        """Включает возможность выделять и перемещать фигуры, кроме фонового изображения"""
        for obj in self.objects:
            if obj.item != self.image_item:  # ✅ Запрещаем перемещение изображения
                obj.item.setFlags(
                    QGraphicsItem.ItemIsSelectable |
                    QGraphicsItem.ItemIsMovable |
                    QGraphicsItem.ItemSendsScenePositionChanges  # ✅ Обновление позиции при перемещении
                )

        # ✅ Применяем флаги ко всем элементам, кроме фонового изображения
        for item in self.items():
            if isinstance(item, QGraphicsItem) and item != self.image_item and item not in [obj.item for obj in
                                                                                            self.objects]:
                item.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)

    def contextMenuEvent(self, event):
        """Обрабатывает клик ПКМ (правой кнопкой) по объекту"""
        item = self.itemAt(event.scenePos(), self.views()[0].transform())
        if item:
            menu = QMenu()

            delete_action = QAction("Удалить", self)
            delete_action.triggered.connect(lambda: self.remove_object(item))
            menu.addAction(delete_action)

            menu.exec(event.screenPos())

    def remove_object(self, item):
        """Удаляет объект со сцены"""
        for obj in self.objects[:]:  # Создаём копию списка, чтобы безопасно изменять
            if obj.item == item:
                self.removeItem(item)
                self.objects.remove(obj)
                break  # ✅ Выходим после удаления, чтобы не было ошибок

    def keyPressEvent(self, event):
        """Обрабатывает нажатия клавиш"""
        if event.key() == Qt.Key_Delete:
            selected_items = self.selectedItems()
            for item in selected_items:
                self.remove_object(item)

    def change_selected_color(self, color):
        """Меняет цвет выделенного объекта"""
        for obj in self.objects:
            if obj.item.isSelected():
                pen = QPen(color, obj.pen.width())
                obj.set_pen(pen)

    def choose_color(self):
        """Выбирает цвет кисти и меняет цвет выделенной фигуры"""
        color = QColorDialog.getColor()
        if color.isValid():
            self.change_selected_color(color)