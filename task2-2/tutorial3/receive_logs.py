from connection import connect  # 连接函数

connection = connect()
channel = connection.channel()

# 声明fanout交换机
channel.exchange_declare(
    exchange="logs_group13",
    exchange_type="fanout"
)

# 创建当前消费者专用的临时队列
result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue

# 将临时队列绑定到交换机
channel.queue_bind(
    exchange="logs_group13",
    queue=queue_name
)

# 收到消息后打印内容
def callback(ch, method, properties, body):
    print("Broadcast received:", body.decode("utf-8"))

channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True
)

print("Waiting for broadcasts. Press Ctrl+C to stop.")

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
finally:
    connection.close()
