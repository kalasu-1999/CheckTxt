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
		temp1 = c.trueNum
		temp2 = c.falseNum
		clean(c.trueLine, temp1)
		clean(c.falseLine, temp2)
        if c.trueLine[temp1 + 1] == c.falseLine[temp2 + 1]:
            return True
        else:
            return False


# 多出了一些行
def overTrue(c):

	return 0


# 少了一些行
def lessTrue(c):
    
	return 0 


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
                answerDir[c.falseNum + 1] = {"单行逻辑错误"}
            else:
				overReturn = overTrue(c)
				if overReturn != 0:
					answerDir[c.falseNum + 1] = {"相比于源代码多出了一些行，到" + overReturn + "行"}
					c.falseNum = overReturn + 1
					c.trueNum = c.trueNum + 1
				lessReturn = lessTrue(c)
				if lessReturn != 0:
					answerDir[c.falseNum + 1] = {"相比于源代码少了一些行，共少了" + (c.trueNum - lessReturn) + "行"}
					c.trueNum = lessReturn + 1
					c.falseNum = c.falseNum + 1
	# 运行到最后有剩余行
	# 正确程序还有剩余行
	if c.trueNum == c.trueLine.__len__() and c.falseNum != c.falseLine.__len__():
		answerDir[c.falseNum + 1] = {"此行开始至末尾，源程序代码中不存在"}
	elif c.falseNum == c.falseLine.__len__() and c.trueNum != c.trueLine.__len__():
		answerDir[c.falseNum + 1] = {"源程序代码中还未结束，缺少代码"}


class CheckCode:
    trueLine = []
    falseLine = []
    trueNum = 0
    falseNum = 0


if __name__ == '__main__':
    ck = CheckCode()
    ck.trueLine = getLine(
        "/mnt/e2ae2387-deae-49e8-bbbc-d48d4ca5897d/MyData/创新实践/CodeCheckTextDir/OldFile")
    ck.falseLine = getLine(
        "/mnt/e2ae2387-deae-49e8-bbbc-d48d4ca5897d/MyData/创新实践/CodeCheckTextDir/NewFile")
    check(ck)
