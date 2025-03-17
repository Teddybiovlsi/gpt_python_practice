# GPT Practice
# List Comprehension

# expert 1
# 轉換數字列表
# 給定一個數字列表 nums，請使用 列表解析式 來執行以下邏輯：

# 如果數字是偶數，將其平方
# 如果數字是奇數，將其轉為字串
nums = [1, 2, 3, 4, 5, 6]
# 我的寫法
result = [str(num) if num % 2 != 0 else num ** 2 for num in nums]
# 改進後寫法
result = [str(num) if num % 2 else num ** 2 for num in nums]
print(result)

# expert 2
# 轉換矩陣
# 給定一個 二維數字矩陣，請使用 列表解析式 轉換矩陣，要求：

# 每個數字 +1
# 轉換為新的二維列表
matrix = [[1, 2, 3], [4, 5, 6]]
# 我的寫法
result = [[matrix[row][col] + 1 for col in range(len(matrix[0]))]for row in range(len(matrix)) ]
# 改進寫法
result = [[num + 1 for num in row] for row in matrix]
print(result)
# 推導式
# new_matrix = []
# final_matrix = []
# for row in range(len(matrix)):
#     for col in range(len(matrix[0])):
#         new_matrix.append(matrix[row][col] + 1)
#     final_matrix.append(new_matrix)
#     new_matrix = []
# print(final_matrix)

# expert 3
# 數字映射成英文字母
# 給定一個數字列表 nums，將其轉換成對應的 小寫英文字母：
nums = [1, 5, 26, 30, 10]

print([chr(num + 96) if 1 <= num <= 26 else "?" for num in nums ])

# expert 4
# 交集過濾
# 給定兩個數字列表 list1 和 list2，請使用 列表解析式 找出它們的交集，並返回新的列表
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
# 第一種解法(使用「交集」方式)
common = list(set(list1) & set(list2))
# 第二種解法
common = [x for x in list1 if x in list2]

print(common)

# expert 5
# 給定一個字典 scores，請使用 字典解析式 篩選出分數 >= 60 的學生
scores = {"Alice": 85, "Bob": 55, "Charlie": 78, "David": 42}

print({name:score for name, score in scores.items() if score >= 60 })

# expert 6
# 轉置矩陣
matrix = [[1, 2, 3], 
          [4, 5, 6]]

print([[row[i] for row in matrix] for i in range(len(matrix[0]))])
# 推導式
# for i in range(len(matrix[0])):
#     for row in matrix:
#         print(row[i])





