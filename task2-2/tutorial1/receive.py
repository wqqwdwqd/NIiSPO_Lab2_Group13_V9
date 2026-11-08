from connection import connect  # 导入连接函数

connection = connect()  # 连接服务器
channel = connection.channel()  # 创建通道

# 声明相同的消息队列
channel.queue_declare(
    queue="hello_group13",
    durable=True,
    arguments={"x-queue-type": "quorum"}
)

# 收到消息后的处理函数
def callback(ch, method, properties, body):
    print("Received:", body.decode("utf-8"))

# 注册消费者
channel.basic_consume(
    queue="hello_group13",
    on_message_callback=callback,
    auto_ack=True
)

print("Waiting for messages. Press Ctrl+C to stop.")

try:
    channel.start_consuming()  # 持续接收消息
except KeyboardInterrupt:
    channel.stop_consuming()  # 停止监听
finally:
    connection.close()  # 关闭连接
