# GPT Practice
# List Comprehension

# Advanced 1
# 去除含有特定字母的單字
import re
words = ["apple", "banana", "cherry", "date", "fig", "grape"] # 給定一個單字列表

words_not_with_a = [word for word in words if not re.search(r"a", word)]  # 過濾掉含有字母 a 的單字
print("不含字母 a 的單字列表:", words_not_with_a)

# Advanced 2
# 產生 2D 陣列
rows = int(input("請輸入2-D陣列的列數: "))
cols = int(input("請輸入2-D陣列的行數: "))

# 使用列表解析式生成 (i, j) 座標
grid = [[(i, j) for j in range(cols)] for i in range(rows)]

print("生成的 2D 陣列:", grid)

# 其推導為以下
new_array = []
inside_array = []
for i in range(rows):
    for j in range(cols):
        inside_array.append((i, j))
    new_array.append(inside_array)
    inside_array = []

print(f"生成的 2D 陣列: {new_array}")