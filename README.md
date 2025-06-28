# 🤖 Robot Movement Simulator

A command-line robot simulation program where multiple robots can be created, assigned unique IDs, and moved on a grid-based terrain. Built in Python, this program was developed as part of an internship assignment.

---

## 📌 Features

- ✅ Create multiple robots with unique IDs.
- ✅ Move robots using directional commands (e.g., N3, E2).
- ✅ Prevent robots from entering already occupied cells.
- ✅ Display robot's current location.
- ✅ Track and display full movement path.
- ✅ Boundary detection with clear warnings (e.g., can't go North from row 0).
- ✅ Remove robots from the grid.
- ✅ Check if a specific cell is occupied.
- ✅ List all robots and their positions.

---

## 🗂️ Folder Structure

```
robot-movement-simulator/
├── terrain.py             # Terrain/grid logic
├── robot.py               # Robot movement and tracking logic
├── robot_manager.py       # Manages robot creation and interaction
├── main.py                # CLI-based main execution program
└── README.md              # Project documentation (this file)
```

---

## ▶️ How to Run

### ✅ Using Google Colab 

1. Open Google Colab: [https://colab.research.google.com](https://colab.research.google.com)
2. Upload all Python files.
3. Run cells in this order:
   - `terrain.py`
   - `robot.py`
   - `robot_manager.py`
   - `main.py` (contains the `main()` function that launches the program)
4. You’ll get a CLI-style input interface in the Colab output.



You’ll get interactive prompts like:

```
🔧 Options: create, move, location, path, remove, check, all, exit
Enter command:
```

---

## 💡 Command Reference

- `create` → Create a robot with unique ID.
- `move` → Move robot with directional command (N, S, E, W).
- `location` → Show robot's current position.
- `path` → Show full path history of robot.
- `remove` → Remove robot from grid.
- `check` → Check if a cell is occupied.
- `all` → List all robot positions.
- `exit` → Exit the program.

---

## 🧪 Sample Output

```
✅ Robot 1 created at (0, 0)
✅ Robot 2 created at (0, 0)
✅ Robot 1 moved to (0, 3)
✅ Robot 2 moved to (1, 3)
📍 Robot 1 is at (0, 3)
📜 Robot 1 path: [(0, 0), (0, 1), (0, 2), (0, 3)]
```

---

## 📝 Notes

- Grid is 5x5 (positions range from (0,0) to (4,4)).
- Robot cannot move outside grid boundaries.
- Robot will stop one cell before another robot if path is blocked.
- Input like `W5`, `N2`, etc. are valid.

---

## 📫 Contact

Developed by: *Krija Subramanian*  


---
