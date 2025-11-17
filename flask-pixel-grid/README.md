# 🎨 _Pixel-Grid_

_A browser-based pixel grid for drawing with color, built using Flask, HTML, CSS, and JavaScript._  
_No libraries. No frameworks._

---

## 🧱 What's Inside

```
pixel-grid/
├── app.py                  # Flask routes
├── templates/
│   ├── index.html          # Intro screen with floating panel
│   └── pixel.html          # Drawing interface
├── static/
│   ├── style.css           # Dark theme, gradients, modular layout
│   └── script.js           # Grid logic, mouse drawing, clear/reset
└── README.md
```

---

## 🎛 Controls

- 🎚 Grid size slider (4–64)
- 🎨 Color picker
- 🧼 Clear button
- 🖱 Mouse-based drawing (click + drag)
- 📱 Responsive layout with hover feedback

---

## ▶️ Run Locally

```bash
# Step 1: Install Flask
pip install flask

# Step 2: Start the app
python app.py

# Step 3: Open in browser
http://localhost:5000/
```

---

## 🏁 Entry Points

- `/` → Intro screen  
- `/pixel` → Drawing interface
