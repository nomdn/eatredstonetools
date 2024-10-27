import random

print("看什么看做数学题去")
for i in range(50):
    question1 = random.randint(1,100)
    question2 = random.randint(1, 100)
    yunsuanfu =  random.choice("+-x/")
    if yunsuanfu == "+":
        answer = question1 +question2
    elif yunsuanfu == "-":
        answer = question1 - question2
    elif yunsuanfu == "x":
        answer=question1 * question2
    elif yunsuanfu =="/":
        answer = question1 / question2
    print(question1,yunsuanfu,question2,end="")
    print("的运算结果",end="")
    try:
        user_answer = int(input())
        if user_answer == answer:
            print("还点有脑子")
        else:
            print("蠢")
    except:
        print("你输入的是数字吗")



