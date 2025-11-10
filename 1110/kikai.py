import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score#正解率を計算する関数

df=pd.read_csv('iris.csv')
X=df[['Sepal.Length','Sepal.Width',
      'Petal.Length','Petal.Width']]#変数が大文字(X:特徴量)なのは機械学習のコードの習慣。特徴量の列だけ抽出

y=df['Species']#データを学習用と評価用に分ける　データをシャッフル80%を学習用20%を評価用に分ける　クロスバリデーションという分け方もある

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=77#0.2=20% random_state=再現性を保つ　データ分割
)

clf=RandomForestClassifier(random_state=77)
clf.fit(X_train,y_train) #学習
pred=clf.predict(X_test) #予測
accuracy=accuracy_score(y_test,pred) #評価用の正解データ,予測結果
print(accuracy)



#数値を予測する回帰、クラスを予測する分類用のモデルがある
#機械学習モデルを学習・予測した
#文字列がある場合は数値に置き換える必要がある

#注意点1
#label encodeing (赤=0 青=1 緑=2)等　文字列と数値を1:1で対応させる
#one-hot encodeing フラグが立っているような列　グラフ？のイメージ？

#注意点2　リーク
#本来与えられないデータが特徴に入り不正に精度が上がってしまうこと
#今回だとindexは入れていないのに入ってしまって花の特徴とは関係ない数値で制度が上がってしまうこと
