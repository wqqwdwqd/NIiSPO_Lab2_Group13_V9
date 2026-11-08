import sys  # 读取命令行参数
import pika  # 使用消息属性
from connection import connect  # 连接函数

connection = connect()
channel = connection.channel()

# 创建持久化工作队列
channel.queue_declare(
    queue="task_queue_group13",
    durable=True,
    arguments={"x-queue-type": "quorum"}
)

# 获取任务内容
message = " ".join(sys.argv[1:]) or "Hello World!"

# 发送持久化消息
channel.basic_publish(
    exchange="",
    routing_key="task_queue_group13",
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.DeliveryMode.Persistent
    )
)

print("Task sent:", message)
connection.close()
