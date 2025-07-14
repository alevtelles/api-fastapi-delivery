from fastapi import APIRouter, Depends
from models import Usuario
from dependencies import pegar_sessao

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get("/")
async def auth():
    """
    Rota padrão de autenticação de nossa aplicação!
    """
    return {"mensagem": "Rota de autenticação", "autenticado": False}


@auth_router.post("/criar_conta")
async def criar_conta(email: str, nome: str, senha: str, session=Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if usuario:
        return {"mensagem": "Usuário já cadastrado"}
    else:
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": "Usuário cadastrado com sucesso!"}
