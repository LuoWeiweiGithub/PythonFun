# -*- coding: utf-8 -*-
# 有一张城市地图,图中的顶点为城市,无向边代表两个城市间的连通关系,边上的权为在这两个城市之间修
#  建高速公路的造价,研究后发现,这个地图有一个特点,即任一对城市都是连通的。现在的问题是,要修建若干
# 高速公路把所有城市联系起来,问如何设计可使得工程的总造价最少。
# [输入]
# n(城市数,1<=n<=100)
# e(边数)
# 以下 e 行,每行 3 个数 i,j,wij,表示在城市 i,j 之间修建高速公路的造价。
# [输出]
# n-1 行,每行为两个城市的序号,表明这两个城市间建一条高速公路。

def generateTree(n, e, g):
    s = [[i] for i in range(1,n+1)]
    te = []
    t = 0
    sg = sorted(g, key=lambda x:x[2])
    for g1 in sg:
        if len(te) >= n - 1:
            break
        l, r = -1, -1
        for i in range(len(s)):
            if g1[0] in s[i]:
                l = i
            if g1[1] in s[i]:
                r = i
            if l != -1 and r != -1:
                break
        if l != r:
            te.append([g1[0], g1[1]])
            ls = s[l]
            rs = s[r]
            del s[max(l, r)]
            del s[min(l, r)]
            s.append(ls + rs)
            t += g1[2]
    print t
    return te

#[举例]
#最小生成树的权和为 19。
n = 5
e = 8
g = [[1,2,2],
[1,3,12],
[1,4,10],
[2,3,8],
[2,5,9],
[3,4,6],
[3,5,3],
[4,5,7]]

print generateTree(n, e, g)