from pathlib import Path  # 导入文件路径工具

source = Path("/var/data/data.txt")  # 输入文件
target = Path("/var/result/result.txt")  # 输出文件

# 读取整数
numbers = [
    int(x)
    for x in source.read_text(encoding="utf-8").split()
]

if not numbers:
    raise ValueError("文件中没有整数")

# 查找最大值并计算平方
maximum = max(numbers)
result = maximum ** 2

# 保存计算结果
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(str(result) + "\n", encoding="utf-8")

# 在终端显示结果
print("最大整数:", maximum)
print("平方结果:", result)
