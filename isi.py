# 入力された石の数が有効かどうかを判定する関数
def is_valid_move(stones, move):
    return 1 <= move <= 3 and move <= stones 
#1 <= move <= 3 → 一度に取れる石の数は1〜3個だけ
#move <= stones → 残りの石より多く取れない

# プレイヤーの入力を受け取り、バリデーション関数でチェックする関数
#正しい入力が入るまで while True で繰り返します。
def get_move(player, stones, is_valid_move):
    while True:
        try:#エラーが起きるかもしれない処理
            move = int(input(f"{player}, 何個の石を取りますか？（1~3個まで選べます）："))
            if is_valid_move(stones, move):  # is_valid_move() を使って入力が正しいか確認
                return move
            else:
                print("無効な選択です。もう一度選んでください。")
        except ValueError:#エラーが起きたときに実行される処理,数字以外を入力されたら ValueError で捕まえて「数値を入力してください」と警告
            print("数値を入力してください。")

# 1ターン分の処理を行い、残りの石の数を更新する関数
def take_turn(player, stones, is_valid_move):
    print(f"\n{player}の番です。残りの石は {stones} 個です。")#どちらのプレイヤーか表示、残りの石の数を見せる
    move = get_move(player, stones, is_valid_move) #get_move() で石を取る数をもらう
    return stones - move#石を減らして返す

# ゲーム全体の進行を管理するメイン関数
def play_game():
    print("石取りゲームへようこそ！")
    stones = 15  # ゲーム開始時の石の数
    turn = 1     # 1ならプレイヤー1、2ならプレイヤー2

    while stones > 0:
        current_player = "プレイヤー1" if turn == 1 else "プレイヤー2" #プレイヤー1（turn=1）からスタート、誰の番かを決定
        stones = take_turn(current_player, stones, is_valid_move)#take_turn() でターンを進める

        if stones == 0:#石が0個になったら、その人の負け
            print(f"\n{current_player}が最後の石を取りました。{current_player}の負けです！")
            break

        turn = 3 - turn  # 1⇔2を切り替え順番を交代

# ゲームの実行
if __name__ == "__main__":
    play_game()

#play_game() でスタート
#take_turn() が呼ばれ、
#get_move() で入力をもらい、
#is_valid_move() でチェック
#有効なら石の数を減らし
#石がなくなったらその人の負け