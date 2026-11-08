from connection import connect  # 导入连接函数

connection = connect()  # 连接RabbitMQ
channel = connection.channel()  # 创建通信通道

# 声明持久化消息队列
channel.queue_declare(
    queue="hello_group13",
    durable=True,
    arguments={"x-queue-type": "quorum"}
)

# 发送消息
channel.basic_publish(
    exchange="",
    routing_key="hello_group13",
    body="Hello World!"
)

print("Sent: Hello World!")  # 显示发送结果
connection.close()  # 关闭连接
