from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.email_parser.api.nlp import router as nlp_router
from app.chatbot.api.chatbot import router as chatbot_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True, # allowed to send cookies 
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=-1,  # Only for the sake of the example. Remove this in your own project.
)


app.include_router(nlp_router, prefix="/automation", tags=["automation"])
app.include_router(chatbot_router, prefix="/chatbot", tags=['chatbot'])