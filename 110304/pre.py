apple_price=100
a_type=type(apple_price)

name="斎藤"
n_type=type(name)

weight=54.5
w_type=type(weight)

print(a_type,n_type,w_type)

#辞書key=科目value=点数
scores={"数学":82,"国語":74,"英語":60,"理科":92,"社会":70}
science=scores["理科"]
print(science)

#辞書の編集
prices={"バナナ":250,"みかん":300,"いちご":500}
result=prices["みかん"]
prices["ぶどう"]=400
prices["バナナ"]=200
fruits=list(prices.values())#keysにもできる
print(fruits)
#追加 prices["いちご"]=560
#更新 prices["バナナ"]=350
#valueの表示 result=prices["みかん"]

surname="川上"
givenname="零治"
full_name=surname+givenname
print(full_name)

price=100
text=f"この商品は{price}円です"
print(text)

#リスト
student_names=["斎藤","小林","佐々木","田中"]
a=student_names[0]
b=student_names[2]
c=student_names[-1]
d=student_names[-3]

x=["a","b","c","d","e","f","g"]
y=x[:3]
z=len(x)
print(y)
print(z)

#要素の追加削除
x=[20,12,40]
x.append(5)
x.remove(12)
y=max(x)
z=sum(x)
k=sorted(x) #k=sorted(x,reverse=True)大きい順にできる
print(x)
print(y)
print(z)
print(k)

#集合 タプル
#集合:複数の値を1つにまとめたもので順序をもたず、同じ値を要素として持てない
x={1,2,4}#順序をもたない
x.add(7)
x.remove(2)#指定した値が無いとエラー
x.discard(7)#指定した値が無くてもOK
print(x)

#和集合
x={0,1,3,6}
y={0,2,5,6}
z=x|y
print(z)
#差集合
x={0,1,3,6}
y={0,2,5,6}
z=x-y
print(z)
#積集合
x={0,1,3,6}
y={0,2,5,6}
z=x&y
print(z)

#タプル:複数の値を1つにまとめたもので順序を持ち、同じ値で要素を持てて、値が変更できない
x=(1,2,3)#順序を持つ

#1インデント半角スペース4つ

#if文　条件分岐
#値が同じであるという条件式==
login_cnt=1
if login_cnt==1:
    print("初回ログインユーザーです")

#値が同じではない!=（==と逆の動きになる）
item="りんご"

if item=="りんご":#りんごで動作
    print("これはりんごです")

if item!="りんご":#りんごいがいで動作
    print("これはりんごではないです")

#値の大きさの比較
age=20

if age>=20:
    print("成人です")
elif age>=18:
    print("成人ですが飲酒はできません")
else:
    print("未成年です")  

#含まれるという条件式　変数 in リスト
fruit=["バナナ","りんご","もも"]
x="りんご"

print(x in fruit)

#条件式を組み合わせる　条件式A and 条件式B(AかつB)　条件式A or 条件式B(AまたはB)
age>=20 and login_cnt==1
age>=20 or login_cnt==1

#notで否定の条件式
"りんご"not in fruit

prefecture="東京"

if prefecture=="東京":
    print("日本の首都です")
elif prefecture=="ワシントン":
    print("アメリカの首都です")

number=11
if number%2==0: #偶数である
    print("偶数です")
else:
    print("奇数です")

#繰り返し処理 
# #for 変数　in 繰り返しオブジェクト: 
# #繰り返したい処理
scores=[90,30,49]
for x in scores:
    print(x)

#辞書　for 変数1 変数2 in 辞書.items()
#繰り返したい処理
for name,price in prices.items():
    print(f"{name}は{price}円です")

#rangeは連続した整数を取り出すことができる
for x in range(5):
    print(x)

for y in range(1,6):
    print(y)

#breakはfor文を抜けたいときに使う
numbers=[10,21,100,18,2]
for n in numbers:
    if n>=100:
        break
    print(f"{n}:繰り返し")
print("for文の外")

#continueは後続の処理をスキップして次に行く
number=[10,21,32,65]
for j in number:
    print(f"{j}:前処理")
    if j % 2 ==0:
        continue
    print(f"{j}:後処理")


scores={"数学":82,"国語":74,"英語":60,"理科":92,"社会":70}
for k,v in scores.items():
    print(f"{k}は{v}点です")

for i in range (1,11):
    print(i)

#関数 関数とは一連の処理をまとめることができるもの
#関数定義
def print_hello():#関数の名前
    print("こんにちは") #関数の処理
#関数呼び出し
print_hello()

#引数:関数に渡す値が代入された変数
#戻り値:関数が返す値
#2つの値を受け取って足し合わせた数を返す関数
def add_numbers(a,b):#def add_number(引数1,引数2)
    c=a+b
    d=a-b
    return c,d

added,subed=add_numbers(10,100)#c=added,d=subdedにはいる
print(added,subed)

#位置引数とキーワード引数
#位置引数:順序(位置)によって決定(上記でやったもの)
#キーワード引数:引数名を指定して値をわたす　関数名(引数=値)
def add_number(a,b):
    c=a+b
    return c

add=add_number(b=10,a=100)
print(add)#関数名(引数=値)

#type:型を取得 print:文字を出力 range:連続した数値を取り出す sum:合計計算
#これらも関数でpython側が用意している関数「組み込み関数」という

def is_leap_yeas(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year=2024
result=is_leap_yeas(year)
print(result)

#クラス
#class クラス名:
    #インスタンス変数やメソッドを書く
    #インスタンス変数の初期化はイニシャライザーと呼ばれる特殊なメソッドで行うのが一般的
    #selfは自分自身のこと
class User:
    def __init__(self,name,mail_address,point):
        self.name=name#引数nameで受け取った値をインスタンス変数nameに代入
        self.mail_address=mail_address
        #各オブジェクトが持っているポイントに引数で受け取った値を加算
        self.point=point#インスタンス変数→self.変数名
    
    def add_point(self,point):
        self.point+=point#オブジェクトが持つインスタンス変数pointに引数で受け取った値を加算
#オブジェクトの作成→クラス名(イニシャライザの引数に渡す値) 
user_1=User("佐藤葵","sato@example.com",500)#佐藤葵さんのユーザーオブジェクト
#user_1=User(self,"name","mail_address","point")に渡される
user_2=User("小林ゆい","kobayashi@example.com",1000)
#値を取得→オブジェクト.インスタンス変数名
x=user_1.name#佐藤葵(名前が取得)
y=user_2.name
#メソッドの呼び出し→オブジェクト名.メソッド名(引数に渡す値)
user_1.add_point(100)#葵さんのポイント100加算
print(user_1.point)
#オブジェクト作成後にインスタンス変数に値を代入→オブジェクト.インスタンス変数=新しい値
user_2.point=0#0ポイントになる
print(user_2.point)

#生徒のテストの点数を管理するアプリ
class Student:
    def __init__(self,name,math,japanese,english,science,society):
        self.name=name
        self.math=math
        self.japanese=japanese
        self.english=english
        self.science=science
        self.society=society

    def average_score(self):
        avg=(self.math+self.japanese+self.english+self.science+self.society)/5
        return avg

student_1=Student("斎藤そうま",82,74,60,92,72)
s1_avg=student_1.average_score()
print(s1_avg)

student_2=Student("田中かなで",75,78,80,85,68)
s2_avg=student_2.average_score()
print(s2_avg)

#モジュール
from my_module import print_module,add_numbers 
#from my_module import print_module as pmにしたらpm()で呼べる
#もう一つ奥に入っているパターン from サブディレクトリ名.モジュール名 import 関数名・クラス

print("script 開始")
print_module()
x=add_numbers(1,2)
print(x)
print("script 終了")

#外部ライブラリーpipでインストール
