# GPT Practice
# List Comprehension

# Basic 1
n = int(input("請輸入一個整數: "))  # 加入提示訊息
squares = [i ** 2 for i in range(n)]
print("平方數列表:", squares)

# Basic 2
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in nums if num % 2 == 0]  # 變數名簡化
print("偶數列表:", evens)
