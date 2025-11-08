# http://cs101.openjudge.cn/practice/02808/

#%% 0.(1)自己写的
length, n = map(int, input().split())
part = []
for _ in range(n):
    part.append(list(map(int, input().split())))
tree = [-1] * (length + 1)
for i in range(n):
    for j in range(part[i][0],part[i][1]+1):
        if tree[j] == -1:
            tree[j] = 0
print(tree.count(-1))

#%% 0.(2)自己写的精简版
l, n = map(int, input().split())
list = [0] * (l + 1)
for _ in range(n):
    st, en = map(int, input().split())
    for i in range(st, en+1):
        list[i] = 1
print(list.count(0))

#%% 差分数组  优化了数据多的时候的时间
l, n = map(int, input().split())
diff = [0] * (l + 2)
#标记区间变化：O(n)
for _ in range(n):
    st, en = map(int, input().split())
    diff[st] += 1
    diff[en + 1] -= 1

#计算前缀和：O(l)
current = 0
remaining_trees = 0
for i in range(l + 1):
    current += diff[i]
    if current == 0:
        remaining_trees += 1
print(remaining_trees)