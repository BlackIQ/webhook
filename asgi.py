import multiprocessing
import uvicorn

from api.main import app

if __name__ == "__main__":
    num_workers = multiprocessing.cpu_count()
    uvicorn.run("asgi:app", host="0.0.0.0", port=int(8000), workers=num_workers)