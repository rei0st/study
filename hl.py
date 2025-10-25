import random

print("=== ハイアンドローゲームへようこそ！ ===")

while True:
    player_card=random.randint(1,13)
    cpu_card=random.randint(1,13)
    print(f"\nあなた {player_card} VS CPU ")
    print("あなたのカードはcpuよりも大きい？小さい？(1:大きい, 2:小さい)")

    choice=int(input("選択してください (1 or 2): "))
    print(f"\nあなた {player_card} VS CPU {cpu_card} ")
    if  (player_card > cpu_card and choice == 1)or(player_card < cpu_card and choice == 2):
        print("正解！おめでとう！")
    elif player_card == cpu_card:
        print("引き分けです！")
    else:
        print("残念！またチャレンジしてね！")

    again=input("もう一度遊びますか？ 再挑戦:y,終了:n ").lower()
    if again != 'y':
        print("ゲームを終了します")
        break