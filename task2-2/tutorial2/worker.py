import time  # 模拟任务处理时间
from connection import connect  # 连接函数

connection = connect()
channel = connection.channel()

channel.queue_declare(
    queue="task_queue_group13",
    durable=True,
    arguments={"x-queue-type": "quorum"}
)

# 任务处理函数
def callback(ch, method, properties, body):
    message = body.decode("utf-8")
    print("Task received:", message)

    # 每个点代表一秒工作量
    time.sleep(message.count("."))

    print("Task completed:", message)

    # 通知RabbitMQ任务已经完成
    ch.basic_ack(delivery_tag=method.delivery_tag)

# 每次先处理一条尚未确认的任务
channel.basic_qos(prefetch_count=1)
channel.basic_consume(
    queue="task_queue_group13",
    on_message_callback=callback
)

print("Worker started. Press Ctrl+C to stop.")

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
finally:
    connection.close()
