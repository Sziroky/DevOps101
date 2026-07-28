from typing import TypedDict

from fastapi import APIRouter


class DataManagerResponse(TypedDict):
    operation: str
    status: str
    response: dict


router = APIRouter()


@router.post("/upload")
async def upload() -> DataManagerResponse:
    return {"operation": "upload", "status": "done", "response": {}}


@router.get("/download")
async def download() -> DataManagerResponse:
    return {"operation": "download", "status": "done", "response": {}}


@router.get("/list")
async def list_data() -> DataManagerResponse:
    return {"operation": "download", "status": "done", "response": {}}
