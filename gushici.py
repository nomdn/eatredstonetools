import requests
import os
import sys
import random


a = (requests.get("https://xiaoapi.cn/API/game_gs.php?msg=开始游戏&id=GitHubwsmdn")).text
print(a)
right = 0
cuo = 0
for i in range(1, 100):

    answer = input()

    while True:
        try:
            answer = int(answer)
            if answer == 1:
                b = (requests.get("https://xiaoapi.cn/API/game_gs.php?msg=答1&id=GitHubwsmdn")).text
                right +=1
            elif answer ==2:
                b = (requests.get("https://xiaoapi.cn/API/game_gs.php?msg=答2&id=GitHubwsmdn")).text
                right += 1
            elif answer == 3:
                b = (requests.get("https://xiaoapi.cn/API/game_gs.php?msg=答3&id=GitHubwsmdn")).text
                right += 1
            elif answer == 4:
                b = (requests.get("https://xiaoapi.cn/API/game_gs.php?msg=答4&id=GitHubwsmdn")).text
                right += 1

            if b == "抱歉，答案不对哦！":
                print("你错了awa")
                cuo += 1
                b = (requests.get("https://xiaoapi.cn/API/game_gs.php?msg=开始游戏&id=GitHubwsmdn")).text
            break
        except:
            print("好好看看你输入的对吗")
            break
    print(b)

print("来让我看看！")
print("在50道古诗题里")
print("你错了这么多",cuo)
print("你对了这么多",right)
print((requests.get("https://xiaoapi.cn/API/yiyan.php")).text)
print("片就不给你看了( つ•̀ω•́)つ")
os.system("pause")
sys.exit()
