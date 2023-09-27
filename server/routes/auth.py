from fastapi import APIRouter

router = APIRouter(
    prefix="/auth", tags=["auth"], responses={404: {"message": "User not found"}}
)


@router.post("/login")
async def login():
    return {"login": "notImplemented"}
