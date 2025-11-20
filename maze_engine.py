import os, sys, time
from collections import deque

if os.name == "nt":
    import msvcrt


def get_key():
    if not msvcrt.kbhit():
        return None

    key = msvcrt.getch()
    if key == b"\xe0":
        key2 = msvcrt.getch()
        if key2 == b"H":
            return "up"
        if key2 == b"P":
            return "down"
        if key2 == b"K":
            return "left"
        if key2 == b"M":
            return "right"
        return None
    try:
        return key.decode("utf-8").lower()
    except:
        return None


class MazeGame:
    def __init__(self, map_data):
        self.maze = [list(r) for r in map_data]
        self.player = None
        self.enemy = None
        self.find_characters()

        self.height = len(self.maze) + 2

    def find_characters(self):
        for y, row in enumerate(self.maze):
            for x, c in enumerate(row):
                if c == "P":
                    self.player = [x, y]
                elif c == "S":
                    self.enemy = [x, y]

    def is_wall(self, x, y):
        return self.maze[y][x] == "█"

    def bfs(self, start, goal):
        sx, sy = start
        gx, gy = goal
        queue = deque()
        queue.append((sx, sy))
        visited = {(sx, sy): None}

        while queue:
            x, y = queue.popleft()

            if (x, y) == (gx, gy):
                path = []
                while (x, y) != (sx, sy):
                    path.append((x, y))
                    x, y = visited[(x, y)]
                path.reverse()
                return path

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy

                if ny < 0 or ny >= len(self.maze):
                    continue
                if nx < 0 or nx >= len(self.maze[ny]):
                    continue

                if (nx, ny) in visited:
                    continue
                if self.maze[ny][nx] == "█":
                    continue
                visited[(nx, ny)] = (x, y)
                queue.append((nx, ny))

        return None

    def move_enemy(self):
        if not self.enemy:
            return

        path = self.bfs(tuple(self.enemy), tuple(self.player))
        if not path:
            return

        nx, ny = path[0]
        ex, ey = self.enemy
        self.maze[ey][ex] = " "
        self.enemy[:] = [nx, ny]
        self.maze[ny][nx] = "S"

    def render_first(self):
        for row in self.maze:
            print("".join(row))
        print("\nUse WASD to move. Reach F.")

    def render_update(self):
        print(f"\033[{self.height}A", end="")  

        for row in self.maze:
            print("".join(row))
        print("\nUse WASD to move. Reach F.")

    def start(self):
        enemy_delay = 0.25
        last_enemy_time = time.time()

        self.render_first()

        while True:
            now = time.time()

            key = get_key()
            if key in ["w", "up", "s", "down", "a", "left", "d", "right"]:
                dx = dy = 0
                if key in ["w", "up"]:
                    dy = -1
                elif key in ["s", "down"]:
                    dy = 1
                elif key in ["a", "left"]:
                    dx = -1
                elif key in ["d", "right"]:
                    dx = 1

                px, py = self.player
                nx, ny = px + dx, py + dy

                if not self.is_wall(nx, ny):

                    if self.maze[ny][nx] == "F":

                        finish_value = "WIN"

                        if (
                            nx + 1 < len(self.maze[0])
                            and self.maze[ny][nx + 1].isdigit()
                        ):
                            finish_value = self.maze[ny][nx] + self.maze[ny][nx + 1]

                        self.maze[py][px] = " "
                        self.maze[ny][nx] = "P"
                        self.player[:] = [nx, ny]

                        self.render_update()
                        return finish_value

                    self.maze[py][px] = " "
                    self.maze[ny][nx] = "P"
                    self.player[:] = [nx, ny]

            if self.enemy and now - last_enemy_time > enemy_delay:
                last_enemy_time = now
                self.move_enemy()

            if self.enemy and self.enemy == self.player:
                self.render_update()
                return "LOSE"

            self.render_update()
            time.sleep(0.02)
