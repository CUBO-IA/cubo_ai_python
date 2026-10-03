import math
import random
import sys
import pygame

pygame.init()

# ============================================================
# SETTINGS
# ============================================================

TILE = 24
COLS = 35
ROWS = 25

GAME_WIDTH = COLS * TILE
GAME_HEIGHT = ROWS * TILE
HUD_HEIGHT = 70

WIDTH = GAME_WIDTH
HEIGHT = GAME_HEIGHT + HUD_HEIGHT

FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("Pacman")

clock = pygame.time.Clock()

# ============================================================
# COLORS
# ============================================================

BLACK = (3, 3, 8)
NAVY = (6, 8, 25)

BLUE = (30, 80, 230)
BLUE_DARK = (10, 30, 120)

YELLOW = (255, 225, 20)
WHITE = (245, 245, 245)

RED = (235, 45, 55)
PINK = (255, 120, 180)
CYAN = (50, 220, 235)
ORANGE = (255, 165, 40)

FRIGHTENED_BLUE = (35, 70, 255)

# ============================================================
# FONTS
# ============================================================

font_big = pygame.font.SysFont("Arial", 32, bold=True)
font = pygame.font.SysFont("Arial", 22, bold=True)

# ============================================================
# DIRECTIONS
# ============================================================

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

DIRECTIONS = [UP, DOWN, LEFT, RIGHT]


def opposite(direction):
    return (-direction[0], -direction[1])


# ============================================================
# MAZE
# ============================================================

maze = [[" " for _ in range(COLS)] for _ in range(ROWS)]

# Outer walls
for x in range(COLS):
    maze[0][x] = "#"
    maze[ROWS - 1][x] = "#"

for y in range(ROWS):
    maze[y][0] = "#"
    maze[y][COLS - 1] = "#"


def hwall(y, x1, x2, gaps=()):
    for x in range(x1, x2 + 1):
        if x not in gaps:
            maze[y][x] = "#"


def vwall(x, y1, y2, gaps=()):
    for y in range(y1, y2 + 1):
        if y not in gaps:
            maze[y][x] = "#"


hwall(4, 2, 12, gaps=(6, 7))
hwall(4, 22, 32, gaps=(26, 27))

hwall(8, 2, 10, gaps=(5, 6))
hwall(8, 14, 20, gaps=(16, 17))
hwall(8, 24, 32, gaps=(27, 28))

hwall(16, 2, 10, gaps=(5, 6))
hwall(16, 14, 20, gaps=(16, 17))
hwall(16, 24, 32, gaps=(27, 28))

hwall(20, 2, 12, gaps=(6, 7))
hwall(20, 22, 32, gaps=(26, 27))

vwall(7, 5, 7, gaps=(6,))
vwall(7, 17, 19, gaps=(18,))

vwall(14, 2, 6, gaps=(4, 5))
vwall(14, 18, 22, gaps=(20, 21))

vwall(21, 2, 6, gaps=(4, 5))
vwall(21, 18, 22, gaps=(20, 21))

vwall(28, 5, 7, gaps=(6,))
vwall(28, 17, 19, gaps=(18,))

# ============================================================
# GHOST HOUSE
# ============================================================

# Clear ghost house
for y in range(10, 15):
    for x in range(15, 20):
        maze[y][x] = " "

# Top of ghost house with doorway
for x in range(15, 20):
    maze[10][x] = "#"

maze[10][17] = " "

# Main horizontal corridor
for x in range(11, 25):
    maze[12][x] = " "

# ============================================================
# MOVEMENT HELPERS
# ============================================================

def is_wall(x, y):
    if x < 0 or x >= COLS:
        return True

    if y < 0 or y >= ROWS:
        return True

    return maze[y][x] == "#"


def can_move(x, y, direction):
    return not is_wall(
        x + direction[0],
        y + direction[1]
    )


def is_centered(x, y):
    return (
        abs(x - round(x)) < 0.06 and
        abs(y - round(y)) < 0.06
    )


# ============================================================
# PELLETS
# ============================================================

def create_pellets():

    result = set()

    for y in range(1, ROWS - 1):
        for x in range(1, COLS - 1):

            if maze[y][x] != "#":
                result.add((x, y))

    # Player starting area
    result.discard((3, 12))

    # Ghost house
    for y in range(10, 15):
        for x in range(15, 20):
            result.discard((x, y))

    return result


def create_power_pellets():

    return {
        (2, 2),
        (32, 2),
        (2, 22),
        (32, 22)
    }


pellets = create_pellets()
power_pellets = create_power_pellets()

# ============================================================
# PACMAN
# ============================================================

class Player:

    def __init__(self):

        self.start_x = 3
        self.start_y = 12

        self.x = float(self.start_x)
        self.y = float(self.start_y)

        self.direction = RIGHT
        self.next_direction = RIGHT

        self.speed = 6.0

        self.mouth_time = 0.0

        self.alive = True
        self.death_timer = 0.0

    def reset(self):

        self.x = float(self.start_x)
        self.y = float(self.start_y)

        self.direction = RIGHT
        self.next_direction = RIGHT

        self.alive = True
        self.death_timer = 0

    def start_death(self):

        if not self.alive:
            return

        self.alive = False
        self.death_timer = 1.0

    def update(self, dt):

        if not self.alive:

            self.death_timer -= dt

            if self.death_timer <= 0:
                self.reset()

            return

        tx = round(self.x)
        ty = round(self.y)

        # Snap to exact tile center.
        if is_centered(self.x, self.y):

            self.x = tx
            self.y = ty

            # Try requested direction first.
            if can_move(tx, ty, self.next_direction):
                self.direction = self.next_direction

            # Stop if current direction is blocked.
            if not can_move(tx, ty, self.direction):
                return

        self.x += self.direction[0] * self.speed * dt
        self.y += self.direction[1] * self.speed * dt

        self.mouth_time += dt * 12

    def draw(self):

        px = int(self.x * TILE + TILE / 2)
        py = int(self.y * TILE + TILE / 2)

        radius = TILE // 2 - 2

        # Death animation
        if not self.alive:

            progress = max(
                0,
                min(1, 1 - self.death_timer)
            )

            mouth_angle = progress * math.pi

        else:

            mouth_angle = (
                0.12 +
                abs(math.sin(self.mouth_time)) * 0.42
            )

        # Correct direction angle.
        if self.direction == RIGHT:
            facing = 0

        elif self.direction == DOWN:
            facing = math.pi / 2

        elif self.direction == LEFT:
            facing = math.pi

        else:
            facing = -math.pi / 2

        # Draw body.
        pygame.draw.circle(
            screen,
            YELLOW,
            (px, py),
            radius
        )

        # Cut out the mouth using a black wedge.
        a1 = facing - mouth_angle
        a2 = facing + mouth_angle

        p1 = (
            px + int(math.cos(a1) * radius * 1.15),
            py + int(math.sin(a1) * radius * 1.15)
        )

        p2 = (
            px + int(math.cos(a2) * radius * 1.15),
            py + int(math.sin(a2) * radius * 1.15)
        )

        pygame.draw.polygon(
            screen,
            BLACK,
            [
                (px, py),
                p1,
                p2
            ]
        )


player = Player()

# ============================================================
# GHOST
# ============================================================

# ============================================================
# GHOST
# ============================================================

class Ghost:

    def __init__(
        self,
        x,
        y,
        color,
        name,
        release_delay
    ):

        self.start_x = x
        self.start_y = y

        self.x = float(x)
        self.y = float(y)

        self.color = color
        self.name = name

        self.direction = LEFT

        self.normal_speed = 4.0
        self.frightened_speed = 3.0
        self.return_speed = 5.0

        self.frightened = 0.0

        # ----------------------------------------------------
        # Ghost house / release system
        # ----------------------------------------------------

        self.release_delay = release_delay
        self.release_timer = release_delay

        self.in_house = True
        self.returning_home = False

        # Position the ghost inside the house.
        self.x = float(x)
        self.y = float(y)

        self.ai_timer = 0.0

    # --------------------------------------------------------
    # Reset
    # --------------------------------------------------------

    def reset(self):

        self.x = float(self.start_x)
        self.y = float(self.start_y)

        self.direction = LEFT

        self.frightened = 0.0

        self.release_timer = self.release_delay

        self.in_house = True
        self.returning_home = False

        self.ai_timer = 0.0

    # --------------------------------------------------------
    # Get available directions
    # --------------------------------------------------------

    def get_available_directions(self):

        tx = round(self.x)
        ty = round(self.y)

        result = []

        for direction in DIRECTIONS:

            nx = tx + direction[0]
            ny = ty + direction[1]

            if not is_wall(nx, ny):
                result.append(direction)

        return result

    # --------------------------------------------------------
    # Choose direction
    # --------------------------------------------------------

    def choose_direction(self):

        tx = round(self.x)
        ty = round(self.y)

        available = self.get_available_directions()

        if not available:
            return

        # ----------------------------------------------------
        # Returning to ghost house
        # ----------------------------------------------------

        if self.returning_home:

            target_x = self.start_x
            target_y = self.start_y

            available.sort(
                key=lambda d:
                abs((tx + d[0]) - target_x)
                +
                abs((ty + d[1]) - target_y)
            )

            self.direction = available[0]

            return

        # ----------------------------------------------------
        # Frightened mode
        # ----------------------------------------------------

        if self.frightened > 0:

            # Don't immediately reverse unless necessary.
            choices = [
                d for d in available
                if d != opposite(self.direction)
            ]

            if not choices:
                choices = available

            self.direction = random.choice(choices)

            return

        # ----------------------------------------------------
        # Normal chase mode
        # ----------------------------------------------------

        px = round(player.x)
        py = round(player.y)

        choices = [
            d for d in available
            if d != opposite(self.direction)
        ]

        if not choices:
            choices = available

        # Occasionally make a random choice.
        if random.random() < 0.20:

            self.direction = random.choice(choices)

        else:

            choices.sort(
                key=lambda d:
                abs((tx + d[0]) - px)
                +
                abs((ty + d[1]) - py)
            )

            self.direction = choices[0]

    # --------------------------------------------------------
    # Enter ghost house
    # --------------------------------------------------------

    def eaten(self):

        self.returning_home = True
        self.frightened = 0.0

    # --------------------------------------------------------
    # Release from ghost house
    # --------------------------------------------------------

    def release(self):

        self.in_house = False

        # Start moving upward toward the doorway.
        self.direction = UP

        self.ai_timer = 0

    # --------------------------------------------------------
    # Safe movement
    # --------------------------------------------------------

    def move_safely(self, dt, speed):

        # Current tile.
        tx = round(self.x)
        ty = round(self.y)

        # Distance to the center of the current tile.
        dx = tx - self.x
        dy = ty - self.y

        # ----------------------------------------------------
        # If we're almost at the center, snap there.
        # ----------------------------------------------------

        if abs(dx) < 0.04:
            self.x = float(tx)

        if abs(dy) < 0.04:
            self.y = float(ty)

        # ----------------------------------------------------
        # Calculate proposed position.
        # ----------------------------------------------------

        new_x = self.x + self.direction[0] * speed * dt
        new_y = self.y + self.direction[1] * speed * dt

        # ----------------------------------------------------
        # CRITICAL WALL CHECK
        #
        # Check the tile we're moving toward BEFORE allowing
        # the ghost to enter it.
        # ----------------------------------------------------

        if self.direction == RIGHT:

            target_x = tx + 1

            if is_wall(target_x, ty):

                self.x = float(tx)
                return

        elif self.direction == LEFT:

            target_x = tx - 1

            if is_wall(target_x, ty):

                self.x = float(tx)
                return

        elif self.direction == DOWN:

            target_y = ty + 1

            if is_wall(tx, target_y):

                self.y = float(ty)
                return

        elif self.direction == UP:

            target_y = ty - 1

            if is_wall(tx, target_y):

                self.y = float(ty)
                return

        # ----------------------------------------------------
        # Apply movement.
        # ----------------------------------------------------

        self.x = new_x
        self.y = new_y

    # --------------------------------------------------------
    # Update
    # --------------------------------------------------------

    def update(self, dt):

        # ====================================================
        # GHOST IS INSIDE HOUSE
        # ====================================================

        if self.in_house:

            self.release_timer -= dt

            # Small vertical bobbing motion while waiting.
            # This keeps the ghosts visibly alive.
            self.y = (
                float(self.start_y)
                +
                math.sin(
                    pygame.time.get_ticks() / 250
                    + self.start_x
                ) * 0.12
            )

            if self.release_timer <= 0:

                self.release()

            return

        # ====================================================
        # FRIGHTENED TIMER
        # ====================================================

        if self.frightened > 0:

            self.frightened -= dt

            if self.frightened < 0:
                self.frightened = 0

        # ====================================================
        # RETURNING HOME
        # ====================================================

        if self.returning_home:

            speed = self.return_speed

            if is_centered(self.x, self.y):

                self.x = round(self.x)
                self.y = round(self.y)

                # Have we reached the house?
                if (
                    abs(self.x - self.start_x) < 0.1
                    and
                    abs(self.y - self.start_y) < 0.1
                ):

                    self.returning_home = False
                    self.frightened = 0

                    # Wait inside the house for a short time.
                    self.in_house = True
                    self.release_timer = 1.5

                    return

                self.choose_direction()

            self.move_safely(dt, speed)

            return

        # ====================================================
        # NORMAL / FRIGHTENED MOVEMENT
        # ====================================================

        speed = self.normal_speed

        if self.frightened > 0:
            speed = self.frightened_speed

        # At a tile center we are allowed to choose a new
        # direction.
        if is_centered(self.x, self.y):

            self.x = round(self.x)
            self.y = round(self.y)

            self.choose_direction()

        # Move, but NEVER through a wall.
        self.move_safely(dt, speed)

    # --------------------------------------------------------
    # Draw
    # --------------------------------------------------------

    def draw(self):

        px = int(self.x * TILE + TILE / 2)
        py = int(self.y * TILE + TILE / 2)

        r = TILE // 2 - 2

        # ----------------------------------------------------
        # Ghost returning home
        # ----------------------------------------------------

        if self.returning_home:

            pygame.draw.circle(
                screen,
                WHITE,
                (px - 5, py - 4),
                4
            )

            pygame.draw.circle(
                screen,
                WHITE,
                (px + 5, py - 4),
                4
            )

            pygame.draw.circle(
                screen,
                BLUE,
                (px - 5, py - 4),
                2
            )

            pygame.draw.circle(
                screen,
                BLUE,
                (px + 5, py - 4),
                2
            )

            return

        # ----------------------------------------------------
        # Frightened
        # ----------------------------------------------------

        if self.frightened > 0:

            if self.frightened < 2:

                if int(self.frightened * 10) % 2:
                    color = WHITE
                else:
                    color = FRIGHTENED_BLUE

            else:

                color = FRIGHTENED_BLUE

        else:

            color = self.color

        # ----------------------------------------------------
        # Body
        # ----------------------------------------------------

        pygame.draw.circle(
            screen,
            color,
            (px, py - 2),
            r
        )

        pygame.draw.rect(
            screen,
            color,
            pygame.Rect(
                px - r,
                py - 2,
                r * 2,
                r + 5
            )
        )

        # Feet
        for fx in (-r + 3, 0, r - 3):

            pygame.draw.circle(
                screen,
                color,
                (
                    px + fx,
                    py + r - 1
                ),
                4
            )

        # ----------------------------------------------------
        # Eyes
        # ----------------------------------------------------

        pygame.draw.circle(
            screen,
            WHITE,
            (px - 5, py - 5),
            4
        )

        pygame.draw.circle(
            screen,
            WHITE,
            (px + 5, py - 5),
            4
        )

        dx, dy = self.direction

        pygame.draw.circle(
            screen,
            BLACK,
            (
                px - 5 + dx * 2,
                py - 5 + dy * 2
            ),
            2
        )

        pygame.draw.circle(
            screen,
            BLACK,
            (
                px + 5 + dx * 2,
                py - 5 + dy * 2
            ),
            2
        )

ghosts = [
    Ghost(16, 12, RED, "Blinky", 1.0),
    Ghost(18, 12, PINK, "Pinky", 3.0),
    Ghost(17, 11, CYAN, "Inky", 5.0),
    Ghost(17, 13, ORANGE, "Clyde", 7.0)
]


# ============================================================
# GAME VARIABLES
# ============================================================

score = 0
lives = 3
level = 1

power_timer = 0.0

game_over = False
paused = False


# ============================================================
# RESET
# ============================================================

def reset_positions():

    player.reset()

    for ghost in ghosts:
        ghost.reset()


def restart_game():

    global score
    global lives
    global level
    global pellets
    global power_pellets
    global power_timer
    global game_over

    score = 0
    lives = 3
    level = 1

    pellets = create_pellets()
    power_pellets = create_power_pellets()

    power_timer = 0

    game_over = False

    reset_positions()


def new_level():

    global level
    global pellets
    global power_pellets
    global power_timer

    level += 1

    pellets = create_pellets()
    power_pellets = create_power_pellets()

    power_timer = 0

    reset_positions()


# ============================================================
# COLLISIONS
# ============================================================

def check_collisions():

    global score
    global power_timer
    global lives
    global game_over

    if not player.alive:
        return

    # Pellet collision.
    tile = (
        round(player.x),
        round(player.y)
    )

    if tile in pellets:

        pellets.remove(tile)

        score += 10

    # Power pellet.
    if tile in power_pellets:

        power_pellets.remove(tile)

        score += 50

        power_timer = 8.0

        for ghost in ghosts:

            if not ghost.returning_home:
                ghost.frightened = power_timer

    # Level completed.
    if not pellets:

        new_level()

        return

    # Ghost collisions.
    for ghost in ghosts:

        if ghost.returning_home:
            continue

        distance = math.hypot(
            player.x - ghost.x,
            player.y - ghost.y
        )

        if distance < 0.65:

            # Frightened ghost gets eaten.
            if ghost.frightened > 0:

                score += 200

                ghost.eaten()

                # IMPORTANT:
                # Pac-Man does NOT move.
                # Only the ghost returns home.

            else:

                # Pac-Man dies.
                lives -= 1

                player.start_death()

                # Stop ghosts briefly.
                for g in ghosts:
                    g.ai_timer = 0.5

                if lives <= 0:
                    game_over = True

                break


# ============================================================
# DRAW MAZE
# ============================================================

def draw_maze():

    screen.fill(BLACK)

    pygame.draw.rect(
        screen,
        NAVY,
        pygame.Rect(
            0,
            0,
            GAME_WIDTH,
            GAME_HEIGHT
        )
    )

    for y in range(ROWS):

        for x in range(COLS):

            if maze[y][x] == "#":

                rect = pygame.Rect(
                    x * TILE,
                    y * TILE,
                    TILE,
                    TILE
                )

                pygame.draw.rect(
                    screen,
                    BLUE_DARK,
                    rect
                )

                pygame.draw.rect(
                    screen,
                    BLUE,
                    rect,
                    2
                )

    # Normal pellets.
    for x, y in pellets:

        cx = x * TILE + TILE // 2
        cy = y * TILE + TILE // 2

        pygame.draw.circle(
            screen,
            WHITE,
            (cx, cy),
            3
        )

    # Power pellets.
    pulse = int(
        5 +
        abs(
            math.sin(
                pygame.time.get_ticks() / 180
            )
        ) * 3
    )

    for x, y in power_pellets:

        cx = x * TILE + TILE // 2
        cy = y * TILE + TILE // 2

        pygame.draw.circle(
            screen,
            WHITE,
            (cx, cy),
            pulse
        )


# ============================================================
# HUD
# ============================================================

def draw_hud():

    pygame.draw.rect(
        screen,
        (15, 15, 25),
        pygame.Rect(
            0,
            GAME_HEIGHT,
            WIDTH,
            HUD_HEIGHT
        )
    )

    score_text = font.render(
        f"SCORE  {score}",
        True,
        WHITE
    )

    level_text = font.render(
        f"LEVEL  {level}",
        True,
        WHITE
    )

    lives_text = font.render(
        f"LIVES  {lives}",
        True,
        WHITE
    )

    screen.blit(
        score_text,
        (20, GAME_HEIGHT + 20)
    )

    screen.blit(
        level_text,
        (
            WIDTH // 2 - 55,
            GAME_HEIGHT + 20
        )
    )

    screen.blit(
        lives_text,
        (
            WIDTH - 130,
            GAME_HEIGHT + 20
        )
    )

    # Power indicator.
    if power_timer > 0:

        power_text = font.render(
            f"POWER {power_timer:.1f}",
            True,
            FRIGHTENED_BLUE
        )

        screen.blit(
            power_text,
            (
                WIDTH // 2 - 65,
                GAME_HEIGHT + 45
            )
        )


# ============================================================
# GAME OVER
# ============================================================

def draw_game_over():

    overlay = pygame.Surface(
        (WIDTH, GAME_HEIGHT),
        pygame.SRCALPHA
    )

    overlay.fill(
        (0, 0, 0, 200)
    )

    screen.blit(
        overlay,
        (0, 0)
    )

    title = font_big.render(
        "GAME OVER",
        True,
        YELLOW
    )

    text = font.render(
        "Press ENTER to play again",
        True,
        WHITE
    )

    screen.blit(
        title,
        title.get_rect(
            center=(
                WIDTH // 2,
                GAME_HEIGHT // 2 - 30
            )
        )
    )

    screen.blit(
        text,
        text.get_rect(
            center=(
                WIDTH // 2,
                GAME_HEIGHT // 2 + 25
            )
        )
    )


# ============================================================
# PAUSED
# ============================================================

def draw_paused():

    overlay = pygame.Surface(
        (WIDTH, GAME_HEIGHT),
        pygame.SRCALPHA
    )

    overlay.fill(
        (0, 0, 0, 120)
    )

    screen.blit(
        overlay,
        (0, 0)
    )

    text = font_big.render(
        "PAUSED",
        True,
        YELLOW
    )

    screen.blit(
        text,
        text.get_rect(
            center=(
                WIDTH // 2,
                GAME_HEIGHT // 2
            )
        )
    )


# ============================================================
# MAIN LOOP
# ============================================================

running = True

while running:

    dt = clock.tick(FPS) / 1000.0

    # Prevent huge movement if Windows temporarily pauses
    # the application.
    dt = min(dt, 0.05)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                running = False

            elif event.key == pygame.K_p:

                if not game_over:
                    paused = not paused

            elif event.key == pygame.K_RETURN:

                if game_over:
                    restart_game()

            elif not game_over and not paused:

                if event.key in (
                    pygame.K_UP,
                    pygame.K_w
                ):

                    player.next_direction = UP

                elif event.key in (
                    pygame.K_DOWN,
                    pygame.K_s
                ):

                    player.next_direction = DOWN

                elif event.key in (
                    pygame.K_LEFT,
                    pygame.K_a
                ):

                    player.next_direction = LEFT

                elif event.key in (
                    pygame.K_RIGHT,
                    pygame.K_d
                ):

                    player.next_direction = RIGHT

    # ========================================================
    # UPDATE
    # ========================================================

    if not game_over and not paused:

        player.update(dt)

        for ghost in ghosts:
            ghost.update(dt)

        # Global power timer.
        if power_timer > 0:

            power_timer -= dt

            if power_timer <= 0:

                power_timer = 0

                for ghost in ghosts:

                    if not ghost.returning_home:
                        ghost.frightened = 0

        check_collisions()

    # ========================================================
    # DRAW
    # ========================================================

    draw_maze()

    for ghost in ghosts:
        ghost.draw()

    player.draw()

    draw_hud()

    if paused:
        draw_paused()

    if game_over:
        draw_game_over()

    pygame.display.flip()


pygame.quit()
sys.exit()
