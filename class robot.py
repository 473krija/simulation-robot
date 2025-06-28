class Robot:
    """
    Represents a single robot that can move on the terrain.
    Tracks position, movement, and history.
    """

    DIRECTION_MAP = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1),
    }

    def __init__(self, robot_id: int):
        self.robot_id = robot_id
        self.position = (0, 0)
        self.path_history = [self.position]

    def get_position(self):
        return self.position

    def get_path_history(self):
        return self.path_history

    def move(self, direction: str, steps: int, terrain):
        dr, dc = self.DIRECTION_MAP.get(direction, (0, 0))
        row, col = self.position

        for _ in range(steps):
            new_row = row + dr
            new_col = col + dc

            # Check bounds with detailed message
            if not terrain.is_within_bounds(new_row, new_col):
                boundary_reason = ""
                if direction == 'N' and row == 0:
                    boundary_reason = "top edge"
                elif direction == 'S' and row == terrain.rows - 1:
                    boundary_reason = "bottom edge"
                elif direction == 'W' and col == 0:
                    boundary_reason = "left edge"
                elif direction == 'E' and col == terrain.cols - 1:
                    boundary_reason = "right edge"
                else:
                    boundary_reason = "grid boundary"

                print(f"⚠️ Robot {self.robot_id} is at {self.position} and cannot move {direction} — it’s at the {boundary_reason}.")
                break

            if terrain.is_occupied(new_row, new_col):
                print(f"⚠️ Robot {self.robot_id} stopped before collision at ({row}, {col})")
                break

            row, col = new_row, new_col
            self.path_history.append((row, col))

        self.position = (row, col)
        terrain.update_position(self.robot_id, row, col)
        print(f"✅ Robot {self.robot_id} moved to {self.position}")
