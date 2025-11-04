#5教科のテストの点数を下記のscoresという辞書で表したとして
#この時理科は社会より何点高いかを「〇点」という文字で出力するプログラムを作成
scores={"数学":82,"国語":74,"英語":60,"理科":92,"社会":70}

kei=scores["理科"]-scores["社会"]
print(f"{kei}点")

#先ほどの辞書から平均点を「〇点」という文字で出力するプログラムを作成
score=list(scores.values())
avg_score=sum(score)/len(score)
print(f"{avg_score}点")

#yearという変数に西暦年の数値が代入されていますこの西暦年が閏年かどうか判別
#閏年なら「閏年です」平成なら「平成です」と表示する
#4で割り切れない年は閏年ではない　4で割り切れる年は閏年です
#ただし、100で割り切れる年は閏年ではありません
#ただし、400で割り切れる年は閏年です

year=2025
if year%400==0:
    print("閏年です")
elif year%100==0:
    print("平年です")
elif year%4==0:
    print("閏年です")
else:
    print("平年です")

#1から100までの数字を出力させるプログラムを作りましょう
#3の倍数の場合は数字の代わりにFizz
#5の倍数の場合は数字の代わりにBazz
#15の倍数の場合は数字の代わりにFizzBuzz と表示させてください
for number in range(1,101):
    if number%15==0:
        print("FizzBuzz")
    elif number%5==0:
        print("Bazz")
    elif number%3==0:
        print("Fizz")
    else:
        print(number)

#アパレルのネット通販のアプリで商品クラスを作るケース
class Fuku:
    def __init__(self,id,name,price,purchase_price):
        self.id=id
        self.name=name
        self.price=price
        self.purchase_price=purchase_price

    def genka(self):
        gen=self.purchase_price/self.price
        return gen

fuku1=Fuku("A0001","半袖クールTシャツ",5000,2250)
fuku1.price=6000
f1_gen=fuku1.genka()
print(f1_gen)