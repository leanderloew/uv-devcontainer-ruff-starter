from fastapi import FastAPI

from common import validated_dataclass

app = FastAPI(title="Example API", version="1.0.0")


@validated_dataclass
class HealthResponse:
    status: str
    service: str
    version: str


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello, World!"}


@app.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(status="healthy", service="example-api", version="1.0.0")
