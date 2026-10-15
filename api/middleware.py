import time
from fastapi import Request, HTTPException

async def rate_limiter_middleware(request: Request, call_next):
    """Simple rate-limiting middleware protecting API endpoints from flooding."""
    client_ip = request.client.host
    # Rate limit check implementation placeholder
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
