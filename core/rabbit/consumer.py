import json
import aio_pika
from aio_pika import IncomingMessage
from typing import Callable, Awaitable
from core.config import get_settings


class RabbitConsumer:
    def __init__(self, amqp_url: str):
        self.amqp_url = amqp_url
        self.connection = None
        self.channel = None

    async def connect(self):
        self.connection = await aio_pika.connect_robust(self.amqp_url)
        self.channel = await self.connection.channel()
        await self.channel.set_qos(prefetch_count=10)

    async def consume(self, queue_name: str, handler_func: Callable[[dict], Awaitable[None]]):
        """
        Подписывается на очередь и передает расшифрованные данные в handler_func
        """
        queue = await self.channel.declare_queue(queue_name, durable=True)

        async def _on_message(message: IncomingMessage):
            async with message.process():
                data = json.loads(message.body.decode())
                # Передаем чистый словарь в бизнес-логику
                await handler_func(data)

        await queue.consume(_on_message)

    async def disconnect(self):
        if self.connection and not self.connection.is_closed:
            await self.connection.close()

settings = get_settings()
rabbit_consumer = RabbitConsumer(settings.rabbit_url)