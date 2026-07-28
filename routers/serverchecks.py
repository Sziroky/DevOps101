from typing import TypedDict

from fastapi import APIRouter


class Response(TypedDict):
    operation: str
    status: str
    response: dict


router = APIRouter()


@router.get("/health")
async def health() -> Response:
    return {
        "operation": "health",
        "status": "done",
        "response": {"text": "Server Running!"},
    }
