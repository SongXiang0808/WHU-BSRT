import openpyxl
import pandas as pd
import time

# 记录开始时间
start_time = time.time()

# 读取 Excel 文件
workbook = openpyxl.load_workbook("年份和关键词.xlsx")
sheet = workbook.active

# 创建一个空的列表，用于存放结果
data = []

# 遍历每一行
for row in sheet.iter_rows(min_row=2, values_only=True):  # 从第二行开始，第一行是标题
    year = row[0]  # 第一列为年份
    keywords = [keyword for keyword in row[1:] if keyword]  # 获取非空关键词

    # 将每个关键词添加到结果列表中
    for keyword in keywords:
        data.append({"Year": year, "Keyword": keyword})

# 将列表转换为 DataFrame
new_df = pd.DataFrame(data)

# 将结果保存到新的 Excel 文件
new_df.to_excel("处理后的年份和关键词.xlsx", index=False)

# 记录结束时间
end_time = time.time()

# 计算运行时间
running_time = end_time - start_time
print("代码运行时间：", running_time, "秒")
