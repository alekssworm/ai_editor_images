# Animated Wallpaper Creator (Work in Progress)

This project is a desktop application built with PySide6 that allows users to import images, select regions, assign animation types, and render seamless animated video loops for use as desktop wallpapers.

## 🚧 Status: In Development

> ⚠️ This application is currently under active development. Some features may be incomplete or subject to change.

---

## ✨ Features (Planned and In Progress)

- **Image Importing**: Load static images into the editor.
- **Region Selection Tools**: Draw and define areas of the image for animation (e.g. brush, circle, square, line).
- **AI Panel**: Organize animated "scenes" and "sub-scenes" via a dockable UI panel.
- **Animation Options (WIP)**:
  - **Water**: Gentle ripple, fast stream, waterfall
  - **Fire**: Intensity, glow, sparks, color variation
  - **Lightning**: Direction, glow, color, strike behavior
- **Drawing Settings**: Customize brush size, color, and transparency.
- **Scene Export**: Save selected and drawn shapes, possibly for further animation.
- **Looping Video Output**: Generate seamless videos for wallpaper use (to be implemented).

---

## 🛠️ Technologies Used

- **Python 3**
- **PySide6** (Qt for Python)
- **QGraphicsScene / QGraphicsView** for interactive canvas
- Modular UI system built from `.ui` files using Qt Designer

---

## 💡 How It Works (Workflow)

1. **Import** a background image.
2. **Draw** or select regions of interest using tools like brush, shapes, or free-form lines.
3. **Organize** animated elements into scenes and sub-scenes using the AI tools panel.
4. **Assign Animations** to each region (animations coming soon).
5. **Render & Export** selected areas for animation (looped video export is upcoming).
6. **Set as Wallpaper** using external wallpaper software (planned integration).

---

## 📂 Project Structure

- `main.py` – Application entry point
- `editor.py` – Core image editor with canvas and menu integration
- `drawing_scene.py` – Scene handling and drawing logic
- `ai_tools_logic.py` – Scene/sub-scene and animation logic
- `ui_*.py` – Generated Qt UI files from `.ui` designs

---

## 🧪 Development Setup

```bash
pip install -r requirements.txt
python main.py
```

---

## 📌 To Do

- Integrate animation engine (possibly via shaders, GANs, or procedural generation)
- Export to video (MP4/WebM loop)
- Desktop wallpaper playback (possibly via Lively or Wallpaper Engine integration)
- Animation presets and effects library
- Scene saving/loading

---

## 📃 License

This project is currently private and under development. Licensing will be defined later.

---

Made with ❤️ and PySide6.
