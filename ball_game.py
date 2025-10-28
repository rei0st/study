import random
GAME_COUNT=5 #ゲーム回数
balls=list(range(1,100)) #range=1～99の連続した数字をつくる list(range(1,100)) でリスト [1, 2, 3, ..., 99] に変換
random.shuffle(balls) #random.shuffle(balls) でそのリストをランダムにシャッフル。
awin=bwin=0 #AとBの勝ち数をカウントする変数を初期化（どちらも0勝からスタート）
for i in range(GAME_COUNT): #5回ゲームを繰り返します（i は 0〜4）
    print(f"{i+1}回戦") #現在が第何回戦かを表示（i+1 にして人間向けの番号に）
    a,b=balls.pop(),balls.pop() #balls.pop() はリストの最後の要素を取り出して削除します。2回呼んでAさんとBさんが1枚ずつカードを引いた感じ
    #Aの数字が大きければAの勝ち、そうでなければBの勝ち。勝った方のカウント（awinまたはbwin）を1増やします。
    if a>b:
        awin+=1;winner="A"
    else:
        bwin+=1;winner="B"
    print(f'A:{a},B:{b}...{winner}の勝ち')
#最後に5回の勝負の合計結果を表示。
#max(awin,bwin) → 勝った方の勝数
#min(awin,bwin) → 負けた方の勝数
# 'A' if awin > bwin else 'B' → Aの勝ち数が多ければ"A"、そうでなければ"B
print('{}対{}で{}の勝ち'.format(max(awin,bwin),min(awin,bwin),'A'if awin > bwin else 'B'))