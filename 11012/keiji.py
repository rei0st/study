from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 投稿を保存するリスト（本来はデータベースを使用）
posts = []

@app.route("/")
def index():
    return render_template("index.html", posts=posts)

@app.route("/post", methods=["GET", "POST"])
def post():
    if request.method == "POST":
        # フォームからデータを取得
        name = request.form["name"]
        message = request.form["message"]
        
        # 投稿をリストに追加
        posts.append({"name": name, "message": message})
        
        # ホームページにリダイレクト
        return redirect(url_for("index"))
    
    return render_template("post.html")

if __name__ == "__main__":
    app.run(debug=True)