# -*- coding: UTF-8 -*-
# 文件多行不同判断


def clean(line, num):
    while line[num].strip() == '':
        num = num + 1
    return num


def getLine(path):
    file = open(path, 'r')
    return file.readlines()


def logic(c):
    # 最后一行
    if c.trueNum + 1 == c.trueLine.__len__() or c.falseNum + 1 == c.falseLine.__len__():
        return False
    # 中间行
    else:
        temp1 = c.trueNum
        temp2 = c.falseNum
        clean(c.trueLine, temp1)
        clean(c.falseLine, temp2)
    if c.trueLine[temp1 + 1] == c.falseLine[temp2 + 1]:
        return True
    else:
        return False


# 少了一些行
def lessTrue(c):
    temp1 = c.falseNum + 1
    temp1 = clean(c.falseLine, temp1)
    temp2 = c.trueNum + 1
    temp2 = clean(c.trueLine, temp2)
    temp3 = temp2 + 1
    temp3 = clean(c.trueLine, temp3)
    while temp3 != c.trueLine:
        if c.trueLine[temp2] == c.falseLine[c.falseNum] and c.trueLine[temp3] == c.falseLine[temp1]:
            return temp2
        else:
            temp2 = temp2 + 1
            temp2 = clean(c.trueLine, temp2)
            temp3 = temp2 + 1
            temp3 = clean(c.trueLine, temp3)
    return -1


def check(c):
    # 去空行
    answerDir = {}
    clean(c.trueLine, c.trueNum)
    clean(c.falseLine, c.falseNum)
    while c.trueNum != c.trueLine.__len__() or c.falseNum != c.falseLine.__len__():
        # 相同行继续
        if c.trueLine[c.trueNum] == c.falseLine[c.falseNum]:
            c.trueNum = c.trueNum + 1
            c.falseNum = c.falseNum + 1
        # 不同行
        else:
            # 判断是否为逻辑错误
            if logic(c):
                answerDir[c.falseNum + 1] = {0}
                c.trueNum = c.trueNum + 1
                c.falseNum = c.falseNum + 1
            else:
                lessReturn = lessTrue(c)
                if lessReturn != 0:
                    answerDir[c.falseNum + 1] = {lessReturn - c.trueNum}
                    c.trueNum = lessReturn + 1
                    c.falseNum = c.falseNum + 1
    # 运行到最后有剩余行
    # 正确程序还有剩余行
    if c.trueNum == c.trueLine.__len__() and c.falseNum != c.falseLine.__len__():
        answerDir[c.falseNum + 1] = {-1}
    elif c.falseNum == c.falseLine.__len__() and c.trueNum != c.trueLine.__len__():
        answerDir[c.falseNum + 1] = {-1}
    print(answerDir)


class CheckCode:
    def __init__(self):
        pass

    trueLine = []
    falseLine = []
    trueNum = 0
    falseNum = 0


if __name__ == '__main__':
    ck = CheckCode()
    ck.trueLine = getLine("OldFile")
    ck.falseLine = getLine("NewFile")
    check(ck)
