from numba import njit
import numpy as np
import glm
import math

# resolution
WIN_RES = glm.vec2(1600, 900)
FPS = 240

# world generator
SEED = 16

# ray casting
MAX_RAY_DIST = 6

# chunk
CHUNK_SIZE = 32
H_CHUNK_SIZE = CHUNK_SIZE // 2
CHUNK_AREA = CHUNK_SIZE * CHUNK_SIZE
CHUNK_VOL = CHUNK_AREA * CHUNK_SIZE
CHUNK_SPHERE_RADIUS = H_CHUNK_SIZE * math.sqrt(3) * 2

# world
WORLD_W, WORLD_H = 4, 2
WORLD_D = WORLD_W
WORLD_AREA = WORLD_D * WORLD_W
WORLD_VOL = WORLD_AREA * WORLD_H

# world center
CENTER_XZ = WORLD_W * H_CHUNK_SIZE
CENTER_Y = WORLD_H * H_CHUNK_SIZE

# camera
ASPECT_RATIO = WIN_RES.x / WIN_RES.y
FOV_DEG = 50
V_FOV = glm.radians(FOV_DEG)
H_FOW = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO)
NEAR = 0.1
FAR = 2000.0
PITCH_MAX = glm.radians(89)

# player
PLAYER_SPEED = 0.005
PLAYER_ROT_SPEED = 0.003
PLAYER_POS = glm.vec3(CENTER_XZ, WORLD_H * CHUNK_SIZE, CENTER_XZ)
MOUSE_SENSITIVITY = 0.002

# colors
BG_COLOR = glm.vec3(0.1, 0.16, 0.25)