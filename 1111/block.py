import hashlib #文字列をハッシュ化(暗号のような固定長データに変換)するため。
import json #辞書型(dict)をjson形式(文字列)に変換する為
import datetime

class Block:
    def __init__(self,index,timestamp,transaction,previous_hash):
        self.index=index #ブロックの番号
        self.timestamp=timestamp #ブロックが作られた日時
        self.transaction=transaction #トランザクション(誰から誰へいくら送ったか？)
        self.previous_hash=previous_hash #ひとつ前のブロックハッシュ値
        self.property_dict = {str(i): j for i, j in self.__dict__.items()}#ブロックの中身をdictにまとめる
        #self.__dict__ は「このオブジェクトの変数を全部まとめた辞書」です。それを {キー: 値} の形に整えて、property_dict に保存しています。ハッシュ計算のときに使います。
        self.now_hash=self.calc_hash() #ブロックの中身をもとにcalc_hash()関数でハッシュを作る。ハッシュ値はブロックの"指数"のようなもの
    
    def calc_hash(self):
        block_string=json.dumps(self.property_dict,sort_keys=True).encode("utf-8")
        #json.dump()で辞書をjson文字列にします。 sort_keys=Trueにするとキーの順番がバラバラでも常に同じ順序で並び変えれる
        #encode("utf-8")は日本語を含む文字列をバイト列に変換
        return hashlib.sha256(block_string).hexdigest()#hashlib.sha256()でハッシュを作りhexdigest() で16進数文字列に変換 ブロックの内容 → 固定長の文字列 に変換ということ
    
def new_transaction(sender,recipient,amount):
    transaction={
        "差出人":sender,
        "宛先":recipient,
        "金額":amount,
     }#dictにまとめる
    return transaction #作ったトランザクションを返す

block_chain=[]#ブロックチェーンを作成ここにブロックを順番に追加していきます

genesis_block=Block(0,str(datetime.datetime.now()),"Genesis Block","-")#ブロックチェーンでは最初のブロックだけ特別扱いで前のブロックがないので"-"を入れています
block_chain.append(genesis_block)#ジェネシスブロックにブロックチェーンを追加

transaction=new_transaction("一郎","次郎",100)#ここでtransactionに一郎→次郎へ100円の情報が入ります
new_block=Block(1,str(datetime.datetime.now()),transaction,block_chain[0].now_hash)
#index=1(2番目のブロック) transactionは一郎→次郎 previous_hashはジェネシスブロックのハッシュ

block_chain.append(new_block)

for block in block_chain:#ブロックの内容を表示
    print(f"インデックス:{block.index}")
    print(f"タイムスタンプ:{block.timestamp}")
    print(f"トランザクション:{block.transaction}")
    print(f"前のハッシュ:{block.previous_hash}")
    print(f"現在のハッシュ:{block.now_hash}")
    print("-"*50)



