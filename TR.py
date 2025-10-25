import tkinter

CELLSIZE = 48
FONTSIZE = ("", 24)
BOARDW = 8

OFSX = 2 * CELLSIZE
OFSY = 1 * CELLSIZE

TYPE_BLACK = 0
TYPE_WHITE = 1
TYPE_NONE = 255

turn = TYPE_BLACK
passcnt = 0
endflag = False

board = bytearray(BOARDW * BOARDW)

playtbl = ["黒", "白"]
colortbl = ["black", "white"]

vectable = [
    (0, -1), (1, -1), (1, 0), (1, 1),
    (0, 1), (-1, 1), (-1, 0), (-1, -1),
]


def setpiece(pos, num):
    index = (pos[1] * BOARDW) + pos[0]
    board[index] = num


def getpiece(pos):
    index = (pos[1] * BOARDW) + pos[0]
    return board[index]


def initboard():
    global turn, passcnt, endflag
    for y in range(BOARDW):
        for x in range(BOARDW):
            setpiece((x, y), TYPE_NONE)

    # 初期配置（好みで変更可）
    setpiece((3, 3), TYPE_WHITE)
    setpiece((4, 3), TYPE_BLACK)
    setpiece((3, 4), TYPE_BLACK)
    setpiece((4, 4), TYPE_WHITE)

    turn = TYPE_BLACK
    passcnt = 0
    endflag = False
    redraw()


def isinside(pos):
    if pos[0] < 0 or pos[0] >= BOARDW: return False
    if pos[1] < 0 or pos[1] >= BOARDW: return False
    return True


def moveposition(pos, vectol):
    x = pos[0] + vectable[vectol][0]
    y = pos[1] + vectable[vectol][1]
    return (x, y)


def search(pos, vectol, num):
    # pos から vectol 方向に進んで、挟める相手石の数を返す
    cnt = 0
    p = pos
    p = moveposition(p, vectol)  # まず1歩進める
    if not isinside(p):
        return 0
    if getpiece(p) == TYPE_NONE:
        return 0
    # 最初のマスが自分の石なら0
    if getpiece(p) == num:
        return 0
    # 相手石を数える
    while True:
        if not isinside(p):
            return 0
        if getpiece(p) == TYPE_NONE:
            return 0
        if getpiece(p) == num:
            return cnt
        cnt += 1
        p = moveposition(p, vectol)


def turnablepiece(pos, num):
    if not isinside(pos): return 0
    if getpiece(pos) != TYPE_NONE:
        return 0
    total = 0
    for vectol in range(8):
        total += search(pos, vectol, num)
    return total


def nextturn():
    global turn, passcnt, endflag
    turn ^= 1
    empty = 0
    for y in range(BOARDW):
        for x in range(BOARDW):
            p = (x, y)
            if getpiece(p) == TYPE_NONE:
                empty += 1
            if turnablepiece(p, turn) > 0:
                passcnt = 0
                return
    if empty == 0:
        endflag = True
        return
    passcnt += 1
    if passcnt >= 2:
        endflag = True


def canvas_click(event):
    global turn
    if endflag:
        initboard()
        return

    x = int((event.x - OFSX) / CELLSIZE)
    y = int((event.y - OFSY) / CELLSIZE)
    pos = (x, y)

    if not isinside(pos):
        return
    if turnablepiece(pos, turn) == 0:
        return

    # 石をひっくり返す
    for vectol in range(8):
        cnt = search(pos, vectol, turn)
        if cnt > 0:
            p = pos
            for _ in range(cnt):
                p = moveposition(p, vectol)
                setpiece(p, turn)

    setpiece(pos, turn)
    nextturn()
    redraw()


def drawpiece(pos, num):
    xa = pos[0] * CELLSIZE + OFSX
    ya = pos[1] * CELLSIZE + OFSY
    xb = xa + CELLSIZE
    yb = ya + CELLSIZE
    canvas.create_rectangle(xa, ya, xb, yb, fill="green", width=1)
    if num == TYPE_NONE:
        return
    d = int(CELLSIZE / 10)
    canvas.create_oval(xa + d, ya + d, xb - d, yb - d, fill=colortbl[num], width=1)


def redraw():
    canvas.delete("all")
    # 背景（任意）
    canvas.create_rectangle(0, 0, 576, 480, fill="khaki", width=0)

    black = 0
    white = 0
    for y in range(BOARDW):
        for x in range(BOARDW):
            pos = (x, y)
            num = getpiece(pos)
            if num == TYPE_BLACK: black += 1
            if num == TYPE_WHITE: white += 1
            drawpiece(pos, num)

    msg = "黒" + str(black) + "対白" + str(white)
    canvas.create_text(288, 456, text=msg, font=FONTSIZE)
    msg2 = playtbl[turn] + "の番"
    if passcnt > 0:
        msg2 += "(パス)"
    if endflag:
        msg2 = "終了です"
    canvas.create_text(288, 24, text=msg2, font=FONTSIZE)


# GUI 作成
root = tkinter.Tk()
root.title("Reversi")
root.geometry("576x480")
canvas = tkinter.Canvas(root, width=576, height=480)
canvas.pack()
canvas.bind("<Button-1>", canvas_click)

initboard()
root.mainloop()