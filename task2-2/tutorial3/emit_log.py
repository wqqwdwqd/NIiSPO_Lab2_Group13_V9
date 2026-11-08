import sys  # 读取消息内容
from connection import connect  # 连接函数

connection = connect()
channel = connection.channel()

# 创建fanout类型的交换机
channel.exchange_declare(
    exchange="logs_group13",
    exchange_type="fanout"
)

message = " ".join(sys.argv[1:]) or "Info from Group 13"

# 向所有订阅者广播消息
channel.basic_publish(
    exchange="logs_group13",
    routing_key="",
    body=message
)

print("Broadcast sent:", message)
connection.close()
