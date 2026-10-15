import json

class DistributedTaskQueue:
    """Manages asynchronous task distribution for heavy GPU rendering and LLM reasoning workloads across swarm workers."""
    def __init__(self, redis_client=None):
        self.redis = redis_client
        self.local_queue = []

    def enqueue_task(self, task_name: str, payload: dict):
        task = {"name": task_name, "payload": payload}
        self.local_queue.append(task)
        print(f"[TaskQueue] Enqueued task: {task_name}")

    def dequeue_task(self) -> dict:
        if self.local_queue:
            return self.local_queue.pop(0)
        return None
