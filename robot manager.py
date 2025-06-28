class RobotManager:
    def __init__(self, terrain):
        self.terrain = terrain
        self.robots = {}

    def create_robot(self, robot_id: int):
        if robot_id in self.robots:
            print(f"⚠️ Robot {robot_id} already exists.")
            return

        robot = Robot(robot_id)
        self.robots[robot_id] = robot
        self.terrain.update_position(robot_id, 0, 0)
        print(f"✅ Robot {robot_id} created at (0, 0)")

    def move_robot(self, robot_id: int, command: str):
        if robot_id not in self.robots:
            print(f"❌ Robot {robot_id} does not exist.")
            return

        if len(command) < 2 or not command[1:].isdigit():
            print(f"❌ Invalid command format: {command}")
            return

        direction = command[0].upper()
        steps = int(command[1:])
        self.robots[robot_id].move(direction, steps, self.terrain)

    def get_robot_location(self, robot_id: int):
        if robot_id in self.robots:
            print(f"📍 Robot {robot_id} is at {self.robots[robot_id].get_position()}")

    def get_robot_path(self, robot_id: int):
        if robot_id in self.robots:
            print(f"📜 Robot {robot_id} path: {self.robots[robot_id].get_path_history()}")
