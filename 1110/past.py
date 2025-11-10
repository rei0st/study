import pandas as pd

df=pd.DataFrame({
    "名前":["佐藤","斎藤","鈴木"],
    "年齢":[21,30,18],
    "住所":["東京都","岐阜県","埼玉県"],
    "血液型":["A","AB","O"]
})
print(df)

df=pd.Series(
    ["佐藤","斎藤","鈴木"],
)
print(df)

#import pandas as pd
#df=pd.read_excel("エクセル名")
#print(df)
#エクセルの出力をする

df=pd.read_csv(r"C:\Users\rei15\python勉強\1110\Iris.csv")
print(df)
#df.loc[[インデックスの値のリスト],[カラムのリスト]]
#df.loc[["001","002","003"],:]001～003のすべての列を指定
#df.loc[:,["名前","年齢"]]名前と年齢のすべての行を指定
#df.loc["001":"003","名前":"住所"]001～003 名前～住所の中を指定

#df.iloc[行の位置の番号,列の番号]
#df.iloc[[2,3],[1,2]]

#ブールインデックス(True or False)
#df(df["年齢"]>=20)&(df["血液型"]!="A") 20歳以上でA型ではない人　orは|をつける
#concat 結合
#marge結合→キーを指定して結合　how="left"で左のデータを残したりできる
#mao+lambda式　lambda式なに？→一行で書ける短い関数　便利そうなので今度やる

#import japanize_matplotlib
#df=(x="名前",y="購入額",kind="bar") デフォルトは折れ線　kind="bar"で棒グラフになる