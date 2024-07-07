from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from dependencies.token import get_token_header


router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

templates = Jinja2Templates(directory="static/templates")

@router.get("/") # 
async def admin(request: Request):
    print("admin request: ", request)
    return templates.TemplateResponse("admin.html", {"request" : request})
