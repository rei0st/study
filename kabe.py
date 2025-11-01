from tkinter import *

# ボール設定
ball = {
    "dirx": 10, #"dirx", "diry" … 進む方向と速さ
    "diry": -10,
    "x": 300, #"x", "y" … 現在の位置（中央あたり）
    "y": 300,
    "w": 10, #"w" … 半径
}

# ブロック設定ブロック1つの大きさを指定して、9列 × 5段 のブロックを配置します。
blocks = []
block_w = 60
block_h = 20
cols = 9  # 横のブロック数
rows = 5  # 縦のブロック数
margin = 5  # ブロック間のすきま

# 中央に並べるための左端の位置を計算
canvas_width = 600
total_width = cols * block_w + (cols - 1) * margin #これはブロック群の横幅全体を計算して
start_x = (canvas_width - total_width) // 2  # 中央寄せ開始位置それが画面中央にくるように左端の座標 (start_x) を決めています。

for y in range(rows): #"x" と "y" … ブロック左上の座標
    for x in range(cols):
        blocks.append({
            "x": start_x + x * (block_w + margin),
            "y": 30 + y * (block_h + margin),
            "alive": True #"alive": True … 生きている（消えていない）ブロック
        })

win = Tk() #Tk() … Tkinterのウィンドウを作る
cv = Canvas(win, width=canvas_width, height=400, bg="black") #Canvas … 図形（円・四角など）を描くエリアbg="black" … 背景を黒に設定
cv.pack() #pack() … 画面に表示

def draw_objects():
    cv.delete("all") #cv.delete("all") … 毎回いったん全消去（前フレームを消す）

    # ボール描画
    cv.create_oval( #create_oval() … ボールを描く
        ball["x"] - ball["w"], ball["y"] - ball["w"],
        ball["x"] + ball["w"], ball["y"] + ball["w"],
        fill="lime"
    )

    # ブロック描画
    for b in blocks:
        if b["alive"]:
            cv.create_rectangle( #create_rectangle() … ブロックを描く
                b["x"], b["y"],
                b["x"] + block_w, b["y"] + block_h,
                fill="orange"
            )

def move_ball(): #次の位置を仮計算します。
    bx = ball["x"] + ball["dirx"]
    by = ball["y"] + ball["diry"]

    # 壁との反射
    if bx < 0 or bx > 600: #左右・上下の壁に当たると向きを反転（跳ね返る）
        ball["dirx"] *= -1
    if by < 0 or by > 400:
        ball["diry"] *= -1

    # ブロックとの当たり判定
    for b in blocks: #まだ生きているブロックだけ調べる
        if not b["alive"]:
            continue
        if (b["x"] <= bx <= b["x"] + block_w) and (b["y"] <= by <= b["y"] + block_h): #ボールの座標がブロック範囲内なら「当たった」と判断
            b["alive"] = False #そのブロックを消して（alive=False）反射させる
            ball["diry"] *= -1
            break
#位置を更新
    ball["x"] = bx
    ball["y"] = by

def game_loop():
    draw_objects() #draw_objects() … 画面更新
    move_ball() #move_ball() … 位置更新
    win.after(30, game_loop) #after(30, ...) … 30ミリ秒後にもう一度 game_loop を呼ぶ（繰り返し）

game_loop()
win.mainloop()

