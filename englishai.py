import requests
import os
import sys

for i in range(10):
    a = requests.get("https://api.7585.net.cn/today/api.php?data=wk&type=text").text

    print(a)
print()
print("世界上无论发生多少事情，都和你没关系")
os.system("pause")