import random
import time

print("""Chatwai
版权所有 (C) MDN Factory(2024~9999)。保留所有权利。
""")
while True:
    input("用户:")


    cishu = random.randint(1,100)
    print("外星人:",end="")
    for i in range(cishu):
        a = random.choice("abcdefghijklmnopqrstuvwxyz")
        time2 = random.uniform(0.01,0.05)
        time.sleep(time2)
        print(a,end="")
    print()