import asyncio
import json

class SwarmMessageBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, topic: str, callback):
        if topic not in self.subscribers:
            self.subscribers[topic] = []
        self.subscribers[topic].append(callback)

    async def publish(self, topic: str, message: dict):
        if topic in self.subscribers:
            payload = json.dumps(message)
            for cb in self.subscribers[topic]:
                await cb(payload)
