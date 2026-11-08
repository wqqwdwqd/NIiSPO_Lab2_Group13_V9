from pathlib import Path  # 导入文件路径工具
from shutil import move  # 导入文件移动工具

source = Path("/var/data")  # 原始数据目录
target = Path("/var/result/data.txt")  # 中间结果文件

files = sorted(
    (p for p in source.iterdir() if p.is_file()),
    key=lambda p: p.name
)  # 获取所有普通文件

if not files:
    raise ValueError("没有找到输入文件")

# 计算文件行数，选择行数最多的文件
def count_lines(path):
    with path.open("r", encoding="utf-8") as f:
        return sum(1 for line in f)

selected = max(files, key=count_lines)

# 创建输出目录并移动文件
target.parent.mkdir(parents=True, exist_ok=True)
if target.exists():
    target.unlink()

move(str(selected), str(target))
print("选中的文件:", selected.name)
print("文件行数:", count_lines(target))
