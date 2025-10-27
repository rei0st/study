import random

#カードのデッキを作成
suits=["♠","♥","♦","♣"] #トランプの**4つのマーク（スート）**をリストにしています
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] #トランプの数字や絵札をリストにしています
deck=[f"{rank}{suit}"for suit in suits for rank in ranks] #すべての組み合わせを作るトランプ52枚分のリストを作るコード

#for suit in suits が 外側のループ（まずマークを1つ選ぶ）
#for rank in ranks が 内側のループ（そのマークの下で全てのランクを回す）
#f"{rank}{suit}" は各反復で作る「要素」（ここではカード文字列）

#デッキをシャッフル
random.shuffle(deck)

#プレイヤーとコンピューターにカードを配る
player_hand=[deck.pop() for _ in range(5)]
computer_hand=[deck.pop() for _ in range(5)]

print("あなたの手札",player_hand)
print("コンピューターの手札",["*****"]*5)

#カードの交換
change=input("交換したいカードの番号を入力してください(例:1 3 5)、交換しない場合は Enter:")
if change:
    for i in map(int,change.split()): #入力された番号（1, 3, 5）を順番に i に代入して繰り返す
        player_hand[i-1]=deck.pop()
#player_hand … プレイヤーの手札（例：5枚のカードのリスト）
#deck … 残りの山札（リスト）
#deck.pop() … 山札の一番最後のカードを取り出す
#Pythonのリストは 0番目から数える からです。
print("あなたの新しい手札です",player_hand)

#単純な勝敗判定(Aの枚数で判定)
player_score=sum(1 for card in player_hand if card[0] == "A")
computer_score=sum(1 for card in computer_hand if card[0] == "A")

print("コンピューターの手札",computer_hand)
print(f"あなたのスコア:{player_score}")
print(f"コンピューターのスコア:{computer_score}")

if player_score>computer_score:
    print("あなたの勝ちです")
elif player_score<computer_score:
    print("コンピューターの勝ちです")
else:
    print("引き分けです。")