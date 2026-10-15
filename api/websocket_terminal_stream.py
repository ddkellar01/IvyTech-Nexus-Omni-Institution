from fastapi import WebSocket

class WebSocketTerminalStreamer:
    """Streams real-time console outputs from professor node code execution directly to web dashboards."""
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    async def broadcast_terminal_log(self, log_message: str):
        for connection in self.active_connections:
            await connection.send_text(log_message)
