import os
import random
import subprocess
import tkinter as tk
root = tk.Tk()
number = random.randint(1, 100)
print("版本号:1.2.2.0")
print("作者:一一宝宝，抖音号:2169831898")
root.geometry("300x200")
root.title("猜数字游戏")
entry = tk.Entry(root)
entry.pack()
label = tk.Label(root, text="1-100猜数字")
label.pack()
def print_number():
    labal2 = tk.Label(root, text="答案是：" + str(number))
    labal2.pack()
def guess_number():
    guess = int(entry.get())
    if guess < number:
        label.config(text="猜小了，请再试一次。")
    elif guess > number:
        label.config(text="猜大了，请再试一次。")
    else:
        label.config(text="恭喜你，猜对了！, 答案是：" + str(number))
button1 = tk.Button(root, text="确定", command=guess_number)
button1.pack()

def open_update_log():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    update_log_path = os.path.join(current_dir, 'dist','update_log.exe')
    if os.path.exists(update_log_path):
        subprocess.Popen(update_log_path)
    else:
        OSError("不存在更新日志文件！")
        
button2 = tk.Button(root, text="更新日志", command=open_update_log)
button2.pack()

button3 = tk.Button(root, text="展示答案", command=print_number)
button3.pack()

button4 = tk.Button(root,text="退出",command=root.quit)
button4.pack()
# 运行主循环
root.mainloop()
