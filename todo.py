import tkinter as tk #tk という短い名前で使えるようにしています。
from tkinter import messagebox #messagebox は警告や確認の**ダイアログ（ポップアップ）**を出すための部品
class ToDoApp: #ToDoアプリ全体をまとめる
    def __init__(self,root):
         self.root=root
         self.root.title("TO DO リストアプリ") #タイトルバーに「TO DO リストアプリ」と表示します。

         self.tasks=[] #ここに「やること（タスク）」をPythonのリストとして保存します。

         self.task_input=tk.Entry(root,width=50) #Entry → テキストを1行入力する部品 width=50 → 入力欄の幅
         self.task_input.pack(pady=10) #上下方向の**余白（パディング）**を10ピクセル入れます。

         self.add_button=tk.Button(root,text="タスクを追加",command=self.add_task) #text="タスクを追加" → ボタンに書く文字 command=self.add_task → 押したときに add_task() 関数を実行
         self.add_button.pack(pady=5) #.pack(pady=5) → ボタンを配置して上下5pxの余白

         self.task_listbox=tk.Listbox(root,width=50,height=10) #Listbox → 項目を一覧で表示する部品。width=50 → 横幅。height=10 → 表示できる行数
         self.task_listbox.pack(pady=10)

         self.deleate_button=tk.Button(root,text="選択したタスクを削除",command=self.delete_task) #ボタンを押すと delete_task() 関数が実行されます。Listbox で選択したタスクを削除します。
         self.deleate_button.pack(pady=5)

    def add_task(self):
        task=self.task_input.get() #→ 入力欄から文字を取り出す。
        if task !="": #空でなければ：
            self.tasks.append(task) #タスクをリストに追加。
            self.update_task_list() #画面のリストを更新。
            self.task_input.delete(0,tk.END) #入力欄を空に戻す。
        else: #もし空文字なら：
            messagebox.showwarning("警告","タスクを入力してください") #警告ダイアログを表示。

    def delete_task(self):
        try:
            selected_task_index=self.task_listbox.curselection()[0] #curselection() → 選択中の行番号を取得。[0] → 最初の選択項目を取り出す。
            del self.tasks[selected_task_index] #その番号のタスクを削除。
            self.update_task_list() #画面を更新。
        except IndexError:
            messagebox.showwarning("警告","削除するタスクを選択してください") #何も選択されていないときは警告
    
    def update_task_list(self):
        self.task_listbox.delete(0,tk.END) #一度リストボックスを空にする。
        for task in self.tasks: 
            self.task_listbox.insert(tk.END,task) #self.tasks の中身を1つずつ画面に挿入。

if __name__ == "__main__":
    root=tk.Tk() #ウィンドウを作る。
    app=ToDoApp(root) #アプリのクラスを作成してウィンドウに部品を配置。
    root.mainloop() #ウィンドウを開いたまま動かし続ける。