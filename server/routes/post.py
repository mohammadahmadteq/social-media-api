from fastapi import APIRouter

router = APIRouter(
    prefix="/posts", tags=["posts"], responses={404: {"message": "No data found"}}
)


@router.get("/")
async def getPosts():
    return {"Posts": []}
