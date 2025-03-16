import os

from PySide6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QGraphicsItem, QMenu, QColorDialog, QWidget, \
    QGraphicsPolygonItem, QGraphicsLineItem
from PySide6.QtGui import QPixmap, QPen, QColor, QPainterPath, QAction, QPainter, QPolygonF
from PySide6.QtCore import Qt, QRectF, QDateTime


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
        self.item.update()  # 🔥 Обновляем объект
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
        self.current_polygon = []  # 🔥 Хранит точки соединённой фигуры

    def set_active_scene(self, scene):
        """Устанавливает, в каком sceen идет рисование"""
        self.active_scene = scene

    def set_drawing_mode(self, mode):
        """Устанавливает режим рисования"""
        self.shape_mode = mode

    def set_pen_width(self, width):
        """Изменяет толщину кисти"""
        self.pen_width = width
        self.update_scene_objects()  # 🔥 Обновляем уже нарисованные объекты

    def set_pen_color(self, color):
        """Изменение цвета кисти"""
        self.pen_color = QColor(color.red(), color.green(), color.blue(), self.pen_color.alpha())
        self.update_scene_objects()  # 🔥 Обновляем уже нарисованные объекты

    def set_pen_opacity(self, value):
        """Меняет прозрачность кисти (0-100 -> 0-255)"""
        alpha = int((value / 100) * 255)
        self.pen_color.setAlpha(alpha)
        self.update_scene_objects()  # 🔥 Обновляем уже нарисованные объекты

    def update_scene_objects(self):
        """Обновляет цвет и прозрачность всех объектов в текущем sceen или sub_sceen"""
        if not self.active_scene:
            return  # Если нет активной сцены, ничего не делаем

        new_pen = QPen(self.pen_color, self.pen_width)  # ✅ Создаём новый `QPen`

        for obj in self.active_scene.objects:
            if isinstance(obj, DrawableObject):
                obj.set_pen(new_pen)  # ✅ Применяем новый цвет и прозрачность

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

    def save_shapes_in_scene(self, scene, base_folder, scene_index, project_folder=None):
        """
        Сохраняет `scene`, обрезая её по границам нарисованных фигур, и `sub_sceen`, вырезая `sub_sceen` области.
        - scene: текущая главная сцена.
        - base_folder: корневая папка для сохранения.
        - scene_index: индекс сцены.
        - project_folder: путь к общей папке проекта (чтобы `scene` и `sub_sceen` не создавали разные папки).
        """

        if not scene or not hasattr(scene, "objects"):
            print(f"Ошибка: scene {scene_index} не содержит объектов!")
            return

        # ✅ Создаём папку проекта только один раз
        if project_folder is None:
            timestamp = QDateTime.currentDateTime().toString("yyyyMMdd_HHmmss")
            project_folder = os.path.join(base_folder, f"Project_{timestamp}")
            os.makedirs(project_folder, exist_ok=True)

        # ✅ Создаём папку для главной сцены
        scene_folder = os.path.join(project_folder, f"scene_{scene_index}")
        os.makedirs(scene_folder, exist_ok=True)

        # ✅ Функция для сбора объектов сцены и `sub_sceen`
        def collect_objects(scene_obj):
            objects_dict = {"scene": [], "sub_scenes": {}, "excluded_areas": [], "bounding_rects": []}

            if hasattr(scene_obj, "objects"):
                for obj in scene_obj.objects:
                    if isinstance(obj, DrawableObject) and obj.shape in {"circle", "square", "polygon"}:
                        objects_dict["scene"].append(obj)
                        objects_dict["bounding_rects"].append(obj.item.sceneBoundingRect())
                    elif isinstance(obj, QWidget):  # Это sub_sceen
                        sub_index = len(objects_dict["sub_scenes"]) + 1
                        sub_folder = os.path.join(scene_folder, f"sub_sceen_{sub_index}")
                        os.makedirs(sub_folder, exist_ok=True)

                        # 🔥 ВАЖНО: передаём `project_folder`, чтобы не создавать новую папку
                        sub_data = collect_objects(obj)
                        objects_dict["sub_scenes"][sub_folder] = sub_data["scene"]
                        objects_dict["excluded_areas"].extend(
                            [obj.item.sceneBoundingRect() for obj in sub_data["scene"]])

            return objects_dict

        objects_data = collect_objects(scene)

        # ✅ Вычисляем bounding box всех фигур
        if objects_data["bounding_rects"]:
            min_x = min(rect.left() for rect in objects_data["bounding_rects"])
            min_y = min(rect.top() for rect in objects_data["bounding_rects"])
            max_x = max(rect.right() for rect in objects_data["bounding_rects"])
            max_y = max(rect.bottom() for rect in objects_data["bounding_rects"])
            scene_bbox = QRectF(min_x, min_y, max_x - min_x, max_y - min_y)
        else:
            print("Ошибка: Нет фигур в сцене для сохранения!")
            return

        # ✅ Создаём QPixmap для рендеринга `scene`
        pixmap_scene = QPixmap(scene_bbox.size().toSize())
        pixmap_scene.fill(Qt.transparent)

        # ✅ Рендерим только область фигур
        painter_scene = QPainter(pixmap_scene)
        self.render(painter_scene, QRectF(pixmap_scene.rect()), scene_bbox)
        painter_scene.end()

        # ✅ Создаём маску `sub_sceen`
        mask_pixmap = QPixmap(scene_bbox.size().toSize())
        mask_pixmap.fill(Qt.transparent)

        painter_mask = QPainter(mask_pixmap)
        painter_mask.setBrush(QColor(0, 0, 0, 255))  # Чёрный цвет для маскировки
        painter_mask.setPen(QColor(0, 0, 0, 255))

        for exclusion in objects_data["excluded_areas"]:
            exclusion_mapped = exclusion.translated(-scene_bbox.topLeft())  # Перенос координат
            painter_mask.drawRect(exclusion_mapped)

        painter_mask.end()

        # ✅ Применяем маску к `scene`
        final_scene = QPixmap(pixmap_scene.size())
        final_scene.fill(Qt.transparent)

        painter_final = QPainter(final_scene)
        painter_final.drawPixmap(0, 0, pixmap_scene)  # Основное изображение
        painter_final.setCompositionMode(QPainter.CompositionMode_DestinationOut)  # Вырезаем `sub_sceen`
        painter_final.drawPixmap(0, 0, mask_pixmap)
        painter_final.end()

        # ✅ Сохраняем `scene` с обрезанными границами
        scene_save_path = os.path.join(scene_folder, "scene.png")
        if final_scene.save(scene_save_path):
            print(f"Сцена сохранена: {scene_save_path}")
        else:
            print(f"Ошибка при сохранении сцены: {scene_save_path}")

        # ✅ Сохраняем `sub_sceen_X`, передавая общий `project_folder`
        for sub_folder, sub_objects in objects_data["sub_scenes"].items():
            for idx, obj in enumerate(sub_objects):
                rect = obj.item.sceneBoundingRect()
                rect = rect.intersected(scene_bbox)

                if rect.isEmpty():
                    continue

                cropped_pixmap = pixmap_scene.copy(rect.translated(-scene_bbox.topLeft()).toRect())
                save_path = os.path.join(sub_folder, f"shape_{idx}.png")

                if cropped_pixmap.save(save_path):
                    print(f"Фигура сохранена в под-сцене: {save_path}")
                else:
                    print(f"Ошибка при сохранении в под-сцене: {save_path}")

    def mousePressEvent(self, event):
        """Обрабатывает начало рисования"""
        if not self.active_scene:
            return  # Если нет активной сцены, не рисуем

        point = event.scenePos()
        pen = QPen(self.pen_color, self.pen_width)

        if self.shape_mode == "line":
            if not self.current_polygon:
                # 🔥 Начинаем новый путь линий
                self.current_polygon.append(point)
            else:
                last_point = self.current_polygon[-1]

                # 🔥 Проверяем, замкнулась ли фигура
                if len(self.current_polygon) > 2 and (point - self.current_polygon[0]).manhattanLength() < 10:
                    self.current_polygon.append(self.current_polygon[0])  # Замыкаем фигуру
                    self.create_polygon()
                else:
                    # 🔥 Добавляем новую линию
                    line = QGraphicsLineItem(last_point.x(), last_point.y(), point.x(), point.y())
                    line.setPen(pen)
                    self.addItem(line)
                    self.active_scene.objects.append(DrawableObject("line", line))
                    self.current_polygon.append(point)  # Добавляем точку в список

        elif self.shape_mode in ["circle", "square"]:
            self.start_point = point
            self.drawing = True

            # Имитация mouseMoveEvent, чтобы сразу отобразить фигуру
            if self.shape_mode == "circle":
                radius = 10  # Начальный радиус
                self.temp_item = self.addEllipse(point.x(), point.y(), radius, radius, pen)
            elif self.shape_mode == "square":
                rect = QRectF(point.x(), point.y(), 10, 10)  # Начальный квадрат
                self.temp_item = self.addRect(rect, pen)

    def create_polygon(self):
        """Создаёт полигон из соединённых линий"""
        if len(self.current_polygon) < 3:
            return  # 🔥 Минимум 3 точки для фигуры

        pen = QPen(self.pen_color, self.pen_width)
        polygon_item = QGraphicsPolygonItem(QPolygonF(self.current_polygon))
        polygon_item.setPen(pen)
        polygon_item.setBrush(QColor(self.pen_color.red(), self.pen_color.green(), self.pen_color.blue(), 100))

        self.addItem(polygon_item)
        self.active_scene.objects.append(DrawableObject("polygon", polygon_item))
        self.current_polygon.clear()  # 🔥 Очищаем временные линии

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
        """Выбор нового цвета кисти и обновление всех фигур в sceen/sub_sceen"""
        color = QColorDialog.getColor()
        if color.isValid() and self.scene:
            self.scene.set_pen_color(color)  # Меняем цвет кисти
            self.scene.update_scene_objects()  # 🔥 Обновляем все фигуры в sceen или sub_sceen

    def update_scene_objects(self):
        """Обновляет цвет и прозрачность всех объектов в текущем sceen или sub_sceen"""
        if not self.active_scene:
            return  # Если нет активной сцены, ничего не делаем

        for obj in self.active_scene.objects:
            if isinstance(obj, DrawableObject):  # Убеждаемся, что объект рисуемый
                pen = QPen(self.pen_color, obj.pen.width())  # Используем новый цвет и прозрачность
                obj.set_pen(pen)

    def change_pen_opacity(self, value):
        """Меняет прозрачность кисти и обновляет все фигуры"""
        if self.scene:
            self.scene.set_pen_opacity(value)
            self.scene.update_scene_objects()  # 🔥 Обновляем все фигуры в sceen или sub_sceen



