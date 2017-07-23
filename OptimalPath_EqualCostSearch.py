# -*- coding: utf-8 -*-
#例 1、假设 A、B、C、D、E 各个城市之间旅费如下图所示。某人想从城市 A 出发游览各城市一遍,而所用旅费最少,试编程输出结果。
#首先,对于这类图,我们都应该先建立一个邻接矩阵,存放任意两点间的数据(距离、费用、时间等),以便在程序中方便调用,上图的邻接矩阵如下:
#const dis:array[1..5,1..5] of integer =( ( 0, 7, 3,10,15),
#( 7, 0, 5,13,12),
#( 3, 5, 0, 6, 5),
#(10,13, 6, 0,11),
#(15,12, 5,11, 0) );
import time 
import sys
from collections import deque

maxInt = sys.maxint

def bfs(n, g):
    result = [[[0,i], g[0][i]] for i in range(1, n)]
    allSet = set(range(n))
    while True:
        minIndex = -1
        minW = maxInt
        for i in range(len(result)):
            w = result[i][1]
            if w < minW:
                minIndex = i
                minW = result[i][1]
            elif w == minW:
                if len(result[i][0]) > len(result[minIndex][0]):
                    minIndex = i
                    minW = result[i]
        currentNode = result[minIndex]
        del result[minIndex]

        if len(currentNode[0]) == n:
            return currentNode
        
        currentVectors = currentNode[0]
        availSet = allSet - set(currentVectors)
        endPoint = currentVectors[-1]
        
        for i in availSet:
            result.append([currentVectors + [i], minW + g[endPoint][i]])

n = 5
g = [[0, 7, 3,10,15],
[7, 0, 5,13,12],
[3, 5, 0, 6, 5],
[10,13, 6, 0,11],
[15,12, 5,11, 0]]

t1 = time.time()
print bfs(n, g)
print '{}'.format(time.time() - t1)