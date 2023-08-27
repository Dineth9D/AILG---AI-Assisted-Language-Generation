from fastapi.staticfiles import StaticFiles
import torchvision.models as models
import pandas as pd
from torchvision import transforms
import torch.nn as nn
import torch
import matplotlib.pylab as plt
import numpy as np
import os

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_ID = "fine_tuned_gpt2"

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
model = AutoModelForCausalLM.from_pretrained(MODEL_ID, cache_dir='/content', trust_remote_code=True, offload_folder="offload")
tokenizer = AutoTokenizer.from_pretrained("gpt2")
MAX_CHAT_LINES = 10


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse('chat.html', {"request": request})

@app.post("/get")
async def chat(request: Request):
    form_data = await request.form()
    user_input = form_data["msg"]
    return get_chat_response(user_input)

def get_chat_response(user_input):
    chat_history_ids = None

    for step in range(MAX_CHAT_LINES):
        new_user_input_ids = tokenizer.encode(str(user_input), return_tensors='pt')
        chat_history_ids = model.generate(new_user_input_ids, max_length=100, do_sample=True, temperature=0.7, pad_token_id=tokenizer.eos_token_id)
        response = tokenizer.decode(chat_history_ids[0], skip_special_tokens=True)
    return response[len(user_input):].strip()