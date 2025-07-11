from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def auth():
    """ 
    Rota padrão de autenticação de nossa aplicação!
    """
    return {"mensagem": "Rota de autenticação", "autenticado": False}