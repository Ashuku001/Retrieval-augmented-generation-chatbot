from fastapi.routing import APIRouter
from app.chatbot.repository.gemini import chat
from dotenv import load_dotenv
import os

router = APIRouter()
load_dotenv()

# @router.post('/llama-3.1-405B')
# async def llama(userPrompt: str):
#     return userPrompt


@router.post('/gemini')
async def gemini(user_prompt: str):
    response = chat(user_prompt, os.getenv("RAG_CONTEXT"))
    
    return response['answer']