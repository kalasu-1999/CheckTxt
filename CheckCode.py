# -*- coding: UTF-8 -*-
# 文件多行不同判断


def clean(line, num):
    while line[num].strip() == '':
        num = num + 1


def getLine(path):
    file = open(path, 'r')
    return file.readlines()


def logic(c):
    # 最后一行
    if c.trueNum + 1 == c.trueLine.__len__() or c.falseNum + 1 == c.falseLine.__len__():
        return False
    # 中间行
    else:
        



def check(c):
    # 去空行
    clean(c.trueLine, c.trueNum)
    clean(c.falseLine, c.falseNum)
    while c.trueNum != c.trueLine.__len__() and c.falseNum != c.falseLine.__len__():
        # 相同行继续
        if c.trueLine[c.trueNum] == c.falseLine[c.falseNum]:
            c.trueNum = c.trueNum + 1
            c.falseNum = c.falseNum + 1
        # 不同行
        else:
            logic(c)




class CheckCode:
    trueLine = []
    falseLine = []
    trueNum = 0
    falseNum = 0


if __name__ == '__main__':
    ck = CheckCode()
    ck.trueLine = getLine("/mnt/e2ae2387-deae-49e8-bbbc-d48d4ca5897d/MyData/创新实践/CodeCheckTextDir/OldFile")
    ck.falseLine = getLine("/mnt/e2ae2387-deae-49e8-bbbc-d48d4ca5897d/MyData/创新实践/CodeCheckTextDir/NewFile")
    check(ck)
