from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio

app = FastAPI(title="IvyTech Collaborative IDE Bridge")

@app.websocket("/ws/collaborate/{session_id}")
async def websocket_collaboration_endpoint(websocket: WebSocket, session_id: str):
    await websocket.accept()
    print(f"[IDE-Bridge] Client connected to collaborative session: {session_id}")
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Echo from Omni-Swarm Faculty: Received '{data}'")
    except WebSocketDisconnect:
        print(f"[IDE-Bridge] Client disconnected from session: {session_id}")
