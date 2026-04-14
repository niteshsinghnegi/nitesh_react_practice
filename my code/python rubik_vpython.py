# rubik_vpython.py
# 3D Rubik's Cube visualiser using VPython
# Controls: F/f, B/b, U/u, D/d, L/l, R/r to rotate faces (cw/ccw)

from vpython import box, vector, color, scene, rate, keysdown, canvas
import math
import time

# small helpers
WHITE = color.white
YELLOW = color.yellow
GREEN = color.green
BLUE = color.blue
ORANGE = color.orange
RED = color.red
BLACK = color.black
GRAY = vector(0.1, 0.1, 0.1)

SIZE = 0.95            # cubie size
GAP = 0.02             # small gap
STICKER_THICK = 0.05   # thickness of sticker

# coordinates used: x (left-right), y (up-down), z (front-back)
coords = [-1, 0, 1]   # layer positions

scene.title = "3D Rubik's Cube - VPython"
scene.width = 900
scene.height = 700
scene.center = vector(0,0,0)
scene.background = vector(0.9, 0.9, 0.95)

# mapping face name to axis and layer coordinate
face_map = {
    'F': ('z', 1), 'B': ('z', -1),
    'U': ('y', 1), 'D': ('y', -1),
    'L': ('x', -1), 'R': ('x', 1)
}

# default solved colors for outer faces
# stickers are defined on outer cubies depending on their world position
face_colors = {
    'U': WHITE, 'D': YELLOW, 'F': GREEN,
    'B': BLUE, 'L': ORANGE, 'R': RED
}

# Store cubies: mapping from (x,y,z) -> dict with 'core' (box) and 'stickers' list
cubies = {}

def sticker_color_for_pos(x,y,z):
    # returns dict mapping face key to color if face is on outside
    res = {}
    if y == 1: res['U'] = face_colors['U']
    if y == -1: res['D'] = face_colors['D']
    if z == 1: res['F'] = face_colors['F']
    if z == -1: res['B'] = face_colors['B']
    if x == -1: res['L'] = face_colors['L']
    if x == 1: res['R'] = face_colors['R']
    return res

def make_cubies():
    for x in coords:
        for y in coords:
            for z in coords:
                pos = vector(x*(SIZE+GAP), y*(SIZE+GAP), z*(SIZE+GAP))
                core = box(pos=pos, length=SIZE, height=SIZE, width=SIZE, color=BLACK)
                # create stickers (thin boxes) on visible faces
                stickers = []
                sticker_map = sticker_color_for_pos(x,y,z)
                for face, col in sticker_map.items():
                    if face == 'U':
                        s = box(pos=pos + vector(0, (SIZE/2+STICKER_THICK/2), 0),
                                length=SIZE*0.9, height=STICKER_THICK, width=SIZE*0.9, color=col)
                    elif face == 'D':
                        s = box(pos=pos + vector(0, -(SIZE/2+STICKER_THICK/2), 0),
                                length=SIZE*0.9, height=STICKER_THICK, width=SIZE*0.9, color=col)
                    elif face == 'F':
                        s = box(pos=pos + vector(0, 0, (SIZE/2+STICKER_THICK/2)),
                                length=SIZE*0.9, height=SIZE*0.9, width=STICKER_THICK, color=col)
                    elif face == 'B':
                        s = box(pos=pos + vector(0, 0, -(SIZE/2+STICKER_THICK/2)),
                                length=SIZE*0.9, height=SIZE*0.9, width=STICKER_THICK, color=col)
                    elif face == 'L':
                        s = box(pos=pos + vector(-(SIZE/2+STICKER_THICK/2), 0, 0),
                                length=STICKER_THICK, height=SIZE*0.9, width=SIZE*0.9, color=col)
                    elif face == 'R':
                        s = box(pos=pos + vector((SIZE/2+STICKER_THICK/2), 0, 0),
                                length=STICKER_THICK, height=SIZE*0.9, width=SIZE*0.9, color=col)
                    stickers.append((face, s))
                cubies[(x,y,z)] = {'core': core, 'stickers': stickers}

make_cubies()

# utility: round small floats to nearest -1,0,1
def snap_coord(val):
    # val close to -something, 0, or something
    return int(round(val / (SIZE+GAP)))

# rotate group of objects around axis by angle (animate)
def animate_rotation(cubie_positions, axis, layer_coord, clockwise=True, steps=20, pause=0.01):
    # axis: 'x','y','z'; layer_coord: -1,0,1
    theta = (math.pi/2) / steps
    if not clockwise:
        theta = -theta
    # choose the objects (core + stickers) in the layer
    objs = []
    keys = []
    for pos in list(cubies.keys()):
        x,y,z = pos
        if axis == 'x' and x == layer_coord:
            keys.append(pos)
        if axis == 'y' and y == layer_coord:
            keys.append(pos)
        if axis == 'z' and z == layer_coord:
            keys.append(pos)
    # animation - rotate objects around axis through origin
    for _ in range(steps):
        rate(120)
        for pos in keys:
            entry = cubies[pos]
            for obj in [entry['core']] + [s for _, s in entry['stickers']]:
                # rotate around origin
                if axis == 'x':
                    obj.rotate(angle=theta, axis=vector(1,0,0), origin=vector(0,0,0))
                elif axis == 'y':
                    obj.rotate(angle=theta, axis=vector(0,1,0), origin=vector(0,0,0))
                elif axis == 'z':
                    obj.rotate(angle=theta, axis=vector(0,0,1), origin=vector(0,0,0))
        time.sleep(pause)

    # After animation, compute new integer positions and re-key cubies dict
    new_map = {}
    for pos in list(cubies.keys()):
        x,y,z = pos
        if axis == 'x' and x == layer_coord or axis == 'y' and y == layer_coord or axis == 'z' and z == layer_coord:
            # find object's current core pos and compute snapped coords
            core = cubies[pos]['core']
            newx = snap_coord(core.pos.x)
            newy = snap_coord(core.pos.y)
            newz = snap_coord(core.pos.z)
            new_map[(newx,newy,newz)] = cubies[pos]
        else:
            new_map[pos] = cubies[pos]
    # replace global cubies mapping
    cubies.clear()
    cubies.update(new_map)

# high-level rotate function mapping face to axis/layer and cw/ccw
def rotate_face(face, clockwise=True):
    face = face.upper()
    if face not in face_map:
        print("Invalid face:", face)
        return
    axis, layer = face_map[face]
    # axis char is 'x','y','z' already
    animate_rotation(cubies, axis, layer, clockwise=clockwise)

# handle keyboard input
def key_handler(evt):
    key = evt.key
    if not key: 
        return
    if key == 'F':
        rotate_face('F', clockwise=True)
    elif key == 'f':
        rotate_face('F', clockwise=False)
    elif key == 'B':
        rotate_face('B', clockwise=True)
    elif key == 'b':
        rotate_face('B', clockwise=False)
    elif key == 'U':
        rotate_face('U', clockwise=True)
    elif key == 'u':
        rotate_face('U', clockwise=False)
    elif key == 'D':
        rotate_face('D', clockwise=True)
    elif key == 'd':
        rotate_face('D', clockwise=False)
    elif key == 'L':
        rotate_face('L', clockwise=True)
    elif key == 'l':
        rotate_face('L', clockwise=False)
    elif key == 'R':
        rotate_face('R', clockwise=True)
    elif key == 'r':
        rotate_face('R', clockwise=False)

scene.bind('keydown', key_handler)

# helpful label
from vpython import label
lbl = label(pos=vector(0,-2.5,0), text="""
Rubik Visual (VPython)
Keys: F/f, B/b, U/u, D/d, L/l, R/r
Mouse: drag to rotate camera, scroll to zoom.
""", height=12, box=False, opacity=0.0)

# keep window alive
while True:
    rate(30)
    # idle loop; interactions handled via events---