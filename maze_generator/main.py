from config import MAZE_HEIGHT, MAZE_WIDTH

class MazeTiles:
    def __init__(self):
        self.air = " "
        self.wall = "#"
        self.start = "S"
        self.end = "E"

maze_tiles = MazeTiles()

class MazeGenerator:
    def __init__(self, file_name):
        self.output_file = file_name
        self.setup()

    def setup(self):
        self.maze = [[maze_tiles.air for i in range(MAZE_WIDTH)] for i in range(MAZE_HEIGHT)]

    def generate(self):
        pass

