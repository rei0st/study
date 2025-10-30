#数値と演算子を入力してもらう
num1=float(input("1つ目の数字を入力してください:")) #floatは小数を扱えるようにするやつ
op=input("演算子を入力してください(+ - * /):")
num2=float(input("2つ目の数字を入力してください:"))

if op=="+": #== は「比較（ひかく）」 左と右が同じか比較している感じ
    result=num1+num2
elif op=="-":
    result=num1-num2
elif op=="*":
    result=num1*num2
elif op=="/":
    if num2==0:
        result="0では割り切れません"
    else:
        result=num1/num2
else:
    result="演算子が無効です + - * / のいずれかを使用してください。"

print(f"結果{result}") #(f"文字列{変数}")文字列の中に変数を埋め込み