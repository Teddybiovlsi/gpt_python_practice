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

