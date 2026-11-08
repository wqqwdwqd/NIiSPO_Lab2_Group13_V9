# Лабораторная работа №2 — Упражнение 2.2

Группа 13. Язык программирования: Python.

## Цель работы

Изучить асинхронный обмен сообщениями с помощью RabbitMQ.

## Архитектура

Брокер RabbitMQ запускается в Docker.
Программы Python выполняются на хост-системе Windows.

## Запуск брокера

docker compose up -d

Административный интерфейс:

http://localhost:15672

Локальные учётные данные находятся в файле .env.

## Установка зависимостей

python -m pip install -r requirements.txt

## Урок 1: Hello World

python -m tutorial1.receive
python -m tutorial1.send

## Урок 2: Work Queues

Запустить в двух терминалах:

python -m tutorial2.worker

В третьем терминале:

python -m tutorial2.new_task "Task one.."

## Урок 3: Publish/Subscribe

Запустить в двух терминалах:

python -m tutorial3.receive_logs

В третьем терминале:

python -m tutorial3.emit_log "Hello subscribers"

## Результаты

Реальные результаты тестирования добавляются после запуска.
