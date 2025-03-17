# GPT Practice

# Basic 1
import re

s = "今天的溫度是25度，昨天是30度，明天可能是28度。"
find = re.findall(r'\d+', s)

print(find)

# Basic 2
# 給定一個字串 s，請使用 re.findall() 提取所有 Email 地址。

import re

s = "請寄信到 support@example.com 或 contact@domain.org，謝謝！"
# \w+@\w+.\w+ 可能會錯誤匹配 something@123（缺少 . 後的 domain 部分）。
# find = re.findall(r'\w+@\w+.\w+', s)

find = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', s)


print(find)

# Basic 3
# 給定一個字串 s，請使用 re.sub() 移除所有非數字的字元，只保留數字。
s = "商品編號: A123B456C789"

remove_none_num = re.sub(r'\D', '', s)
print(remove_none_num)

# Basic 4
# 給定一個字串 s，請使用 re.match() 檢查是否符合台灣手機號碼格式（09 開頭，共 10 位數）。
# 若符合，回傳 True，否則回傳 False。
import re

s1 = "0912345678"
s2 = "0812345678"

# 但 re.match(r'[0][9]', s1) 只匹配前兩個數字，不確保是完整的 10 碼手機號碼。
# find = re.match(r'[0][9]', s1)
# find2 = re.match(r'[0][9]', s2)

pattern = r'^09\d{8}$'  # 09 開頭，後面接 8 個數字

print(bool(re.match(pattern, s1)))  # True
print(bool(re.match(pattern, s2)))  # False

# Basic 5
# 過濾 HTML 標籤
# 給定一個 HTML 字串 s，請使用 re.sub() 移除所有 HTML 標籤
import re

s = "<p>Hello <b>World</b></p>"

remove_tag = re.sub(r'<[^>]+>', '', s)
print(remove_tag)
