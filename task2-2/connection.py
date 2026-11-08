import os  # 读取环境变量
from pathlib import Path  # 处理文件路径
import pika  # RabbitMQ客户端
from dotenv import load_dotenv  # 读取本地配置

# 加载不上传GitHub的账号配置
load_dotenv(Path(__file__).resolve().parent / ".env")

def connect():
    # 获取本地实验账号
    user = os.environ["RABBITMQ_USER"]
    password = os.environ["RABBITMQ_PASSWORD"]

    # 创建连接参数
    parameters = pika.ConnectionParameters(
        host="localhost",
        port=5672,
        credentials=pika.PlainCredentials(user, password),
        connection_attempts=10,
        retry_delay=2
    )

    # 返回RabbitMQ连接
    return pika.BlockingConnection(parameters)
