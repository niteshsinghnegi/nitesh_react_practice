# rubik_auto_fall_solve_fixed.py
# Self-falling, auto-scrambling, auto-solving 3D Rubik's Cube
# Try Kociemba solver if available; otherwise fall back to reversing scramble.
# Requires: vpython  (pip install vpython)
# Optional (for Kociemba): rubik-solver (pip install rubik-solver) -- but that may fail on Python 3.12/3.13

from vpython import box, vector, color, rate, scene, label
import math, time, random

# ---------- Try to import rubik-solver but do NOT fail if unavailable ----------
USE_KOCIEMBA = False
try:
    from rubik_solver import utils
    USE_KOCIEMBA = True
except Exception as e:
    # Could be ModuleNotFoundError or compatibility issue (e.g. 'imp' missing)
    print("rubik-solver not available or failed to import; falling back to inverse-scramble solver.")
    print("Import error:", repr(e))
    USE_KOCIEMBA = False

# ---------- Scene ----------
scene.title = "Auto-Fall & Auto-Solve Rubik's Cube (fixed fallback)"
scene.width = 1000
scene.height = 700
scene.background = vector(0.95, 0.95, 1)
scene.forward = vector(-1, -1, -2)

info = label(pos=vector(0, -3.6, 0), text="Starting...", height=14, box=False, opacity=0)

# ---------- Visual params ----------
SIZE = 0.95
GAP = 0.02
STICK_THICK = 0.05
GRID = SIZE + GAP
coords = [-1, 0, 1]

# Face colors (visual)
FACE_COLORS = {
    'U': color.white,
    'D': color.yellow,
    'F': color.green,
    'B': color.blue,
    'L': color.orange,
    'R': color.red
}

# Map face to axis and layer coordinate for visual rotation
FACE_MAP = {
    'F': ('z', 1), 'B': ('z', -1),
    'U': ('y', 1), 'D': ('y', -1),
    'L': ('x', -1), 'R': ('x', 1)
}

# ---------- Logical cube state ----------
def make_solved_state():
    return {
        'U': [[ 'U' for _ in range(3)] for __ in range(3)],
        'D': [[ 'D' for _ in range(3)] for __ in range(3)],
        'F': [[ 'F' for _ in range(3)] for __ in range(3)],
        'B': [[ 'B' for _ in range(3)] for __ in range(3)],
        'L': [[ 'L' for _ in range(3)] for __ in range(3)],
        'R': [[ 'R' for _ in range(3)] for __ in range(3)],
    }

cube_state = make_solved_state()

# ---------- Visual cubies ----------
cubies = {}

def sticker_map_for_pos(x,y,z):
    sm = {}
    if y == 1: sm['U'] = FACE_COLORS['U']
    if y == -1: sm['D'] = FACE_COLORS['D']
    if z == 1: sm['F'] = FACE_COLORS['F']
    if z == -1: sm['B'] = FACE_COLORS['B']
    if x == -1: sm['L'] = FACE_COLORS['L']
    if x == 1: sm['R'] = FACE_COLORS['R']
    return sm

def make_visual_cube():
    for x in coords:
        for y in coords:
            for z in coords:
                pos = vector(x*GRID, y*GRID + 10, z*GRID)  # start high (+10) for falling
                core = box(pos=pos, length=SIZE, height=SIZE, width=SIZE, color=vector(0.15,0.15,0.15))
                stickers = {}
                smap = sticker_map_for_pos(x,y,z)
                for face, col in smap.items():
                    if face == 'U':
                        s = box(pos=pos + vector(0, (SIZE/2 + STICK_THICK/2), 0),
                                length=SIZE*0.9, height=STICK_THICK, width=SIZE*0.9, color=col)
                    elif face == 'D':
                        s = box(pos=pos + vector(0, -(SIZE/2 + STICK_THICK/2), 0),
                                length=SIZE*0.9, height=STICK_THICK, width=SIZE*0.9, color=col)
                    elif face == 'F':
                        s = box(pos=pos + vector(0, 0, (SIZE/2 + STICK_THICK/2)),
                                length=SIZE*0.9, height=SIZE*0.9, width=STICK_THICK, color=col)
                    elif face == 'B':
                        s = box(pos=pos + vector(0, 0, -(SIZE/2 + STICK_THICK/2)),
                                length=SIZE*0.9, height=SIZE*0.9, width=STICK_THICK, color=col)
                    elif face == 'L':
                        s = box(pos=pos + vector(-(SIZE/2 + STICK_THICK/2), 0, 0),
                                length=STICK_THICK, height=SIZE*0.9, width=SIZE*0.9, color=col)
                    elif face == 'R':
                        s = box(pos=pos + vector((SIZE/2 + STICK_THICK/2), 0, 0),
                                length=STICK_THICK, height=SIZE*0.9, width=SIZE*0.9, color=col)
                    stickers[face] = s
                cubies[(x,y,z)] = {'core': core, 'stickers': stickers}

make_visual_cube()

# ---------- Utility functions ----------
def snap_coord(val):
    return int(round(val / GRID))

def animate_rotation(axis, layer_coord, clockwise=True, steps=20, pause=0.006):
    theta = (math.pi/2) / steps
    if not clockwise:
        theta = -theta
    # collect keys to rotate
    keys = []
    for pos in list(cubies.keys()):
        x,y,z = pos
        if axis == 'x' and x == layer_coord: keys.append(pos)
        if axis == 'y' and y == layer_coord: keys.append(pos)
        if axis == 'z' and z == layer_coord: keys.append(pos)
    # animate
    for _ in range(steps):
        rate(120)
        for pos in keys:
            entry = cubies[pos]
            for obj in [entry['core']] + list(entry['stickers'].values()):
                if axis == 'x':
                    obj.rotate(angle=theta, axis=vector(1,0,0), origin=vector(0,0,0))
                elif axis == 'y':
                    obj.rotate(angle=theta, axis=vector(0,1,0), origin=vector(0,0,0))
                elif axis == 'z':
                    obj.rotate(angle=theta, axis=vector(0,0,1), origin=vector(0,0,0))
        time.sleep(pause)
    # snap objects to integer grid and rebuild cubies mapping
    new_map = {}
    for pos in list(cubies.keys()):
        entry = cubies[pos]
        core = entry['core']
        nx = snap_coord(core.pos.x)
        ny = snap_coord(core.pos.y)
        nz = snap_coord(core.pos.z)
        new_map[(nx,ny,nz)] = entry
    cubies.clear()
    cubies.update(new_map)

# ---------- Logical face rotation ----------
def rotate_face_logical(state, face, clockwise=True):
    # rotate face matrix
    def rot(mat, cw=True):
        if cw:
            return [ [mat[2-col][row] for col in range(3)] for row in range(3) ]
        else:
            return [ [mat[col][2-row] for col in range(3)] for row in range(3) ]
    state[face] = rot(state[face], cw=clockwise)

    # edges mapping (face -> sequence)
    edges = {
        'F': [('U',2,'row'), ('R',0,'col'), ('D',0,'row'), ('L',2,'col')],
        'B': [('U',0,'row'), ('L',0,'col'), ('D',2,'row'), ('R',2,'col')],
        'U': [('B',0,'row'), ('R',0,'row'), ('F',0,'row'), ('L',0,'row')],
        'D': [('F',2,'row'), ('R',2,'row'), ('B',2,'row'), ('L',2,'row')],
        'L': [('U',0,'col'), ('F',0,'col'), ('D',0,'col'), ('B',2,'col')],
        'R': [('U',2,'col'), ('B',0,'col'), ('D',2,'col'), ('F',2,'col')],
    }
    seq = edges[face]
    strips = []
    for (f, idx, axis) in seq:
        if axis == 'row':
            strips.append(state[f][idx][:])
        else:
            strips.append([state[f][r][idx] for r in range(3)])
    if clockwise:
        strips = [strips[-1]] + strips[:-1]
    else:
        strips = strips[1:] + [strips[0]]
    for i, (f, idx, axis) in enumerate(seq):
        if axis == 'row':
            state[f][idx] = strips[i][:]
        else:
            for r in range(3):
                state[f][r][idx] = strips[i][r]

# ---------- Visualize logical state onto stickers ----------
def apply_state_to_visual(state):
    for face in ['F','B','U','D','L','R']:
        mat = state[face]
        for r in range(3):
            for c in range(3):
                if face == 'F':
                    x = -1 + c; y = 1 - r; z = 1; sk = 'F'
                elif face == 'B':
                    x = 1 - c; y = 1 - r; z = -1; sk = 'B'
                elif face == 'U':
                    x = -1 + c; y = 1; z = -1 + r; sk = 'U'
                elif face == 'D':
                    x = -1 + c; y = -1; z = 1 - r; sk = 'D'
                elif face == 'L':
                    x = -1; y = 1 - r; z = 1 - c; sk = 'L'
                elif face == 'R':
                    x = 1; y = 1 - r; z = -1 + c; sk = 'R'
                pos = (x,y,z)
                if pos in cubies and sk in cubies[pos]['stickers']:
                    letter = mat[r][c]
                    col = FACE_COLORS[letter]
                    cubies[pos]['stickers'][sk].color = col

# apply initial solved state visuals
apply_state_to_visual(cube_state)

# ---------- Falling animation ----------
def fall_to_ground(ground_y=0, speed=0.12):
    moving = True
    while moving:
        rate(90)
        moving = False
        for pos, entry in list(cubies.items()):
            core = entry['core']
            if core.pos.y > ground_y:
                delta = min(speed, core.pos.y - ground_y)
                core.pos.y -= delta
                for s in entry['stickers'].values():
                    s.pos.y -= delta
                moving = True

info.text = "Falling..."
fall_to_ground(ground_y=0)
info.text = "Fallen. Scrambling..."

# ---------- Move animation wrapper ----------
def animate_move(face, clockwise=True, visual=True, pause=0.05):
    # visual rotate layer
    axis, layer = FACE_MAP[face]
    if visual:
        animate_rotation(axis, layer, clockwise=clockwise, steps=20, pause=0.006)
    # logical rotation and recolor
    rotate_face_logical(cube_state, face, clockwise=clockwise)
    apply_state_to_visual(cube_state)
    time.sleep(pause)

# ---------- Scramble ----------
def scramble(n=20):
    faces = ['F','B','U','D','L','R']
    seq = []
    for _ in range(n):
        f = random.choice(faces)
        cw = random.choice([True, False])
        seq.append((f, cw))
        animate_move(f, clockwise=cw, visual=True, pause=0.03)
    return seq

random.seed()
scramble_seq = scramble(18)
info.text = "Scrambled. Computing solution..."

# ---------- Convert state to solver string ----------
def cube_state_to_kociemba_string(state):
    s = ''
    for r in range(3):
        for c in range(3):
            s += state['U'][r][c]
    for r in range(3):
        for c in range(3):
            s += state['R'][r][c]
    for r in range(3):
        for c in range(3):
            s += state['F'][r][c]
    for r in range(3):
        for c in range(3):
            s += state['D'][r][c]
    for r in range(3):
        for c in range(3):
            s += state['L'][r][c]
    for r in range(3):
        for c in range(3):
            s += state['B'][r][c]
    return s

cube_str = cube_state_to_kociemba_string(cube_state)

# ---------- Solve via rubik-solver (Kociemba) if available ----------
solution_moves = []
if USE_KOCIEMBA:
    try:
        solution_moves = utils.solve(cube_str, 'Kociemba')
    except Exception as e:
        print("Kociemba solve failed:", repr(e))
        solution_moves = []

# ---------- Fallback: invert scramble sequence to get solution ----------
if not solution_moves:
    # scramble_seq is a list of (face, clockwise_bool)
    # inverse is reversing the scramble and inverting each move
    inv_moves = []
    for (f, cw) in reversed(scramble_seq):
        if cw:
            inv_moves.append(f + "'")   # inverse of clockwise 90° is counterclockwise (')
        else:
            inv_moves.append(f)         # inverse of counterclockwise is clockwise (no apostrophe)
    solution_moves = inv_moves
    info.text = "Using inverse-scramble fallback solver."
else:
    info.text = "Kociemba solution computed."

time.sleep(0.6)

# helper to parse moves like "R", "R'", "R2"
def exec_move_notation(notation):
    face = notation[0]
    if len(notation) == 1:
        animate_move(face, clockwise=True, visual=True, pause=0.06)
    elif notation[1] == "'":
        animate_move(face, clockwise=False, visual=True, pause=0.06)
    elif notation[1] == '2':
        animate_move(face, clockwise=True, visual=True, pause=0.03)
        animate_move(face, clockwise=True, visual=True, pause=0.03)

# animate the solver moves
for mv in solution_moves:
    exec_move_notation(mv)

info.text = "Solved ✅"

# keep rotating the full cube slowly for display
while True:
    rate(40)
    for pos, entry in list(cubies.items()):
        for obj in [entry['core']] + list(entry['stickers'].values()):
            obj.rotate(angle=0.01, axis=vector(0,1,0), origin=vector(0,0,0))
