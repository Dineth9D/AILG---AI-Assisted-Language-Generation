# AI-Assisted Chatbot with GPT-2

This repository contains a AI-assisted chatbot built using the GPT-2 large language model. The chatbot takes user input and generates responses using the GPT-2 model to create a conversational experience.

## Introduction

The AI-assisted chatbot uses the GPT-2 language model to generate responses based on user input. The chatbot's primary purpose is to provide a conversational experience where users can interact with the model-generated responses.

## Requirements

- Python 3.7 or above
- PyTorch 1.9 or above
- Transformers library
- Datasets library
- Other dependencies mentioned in the `requirements.txt` file

## Steup Development Environment

- Clone this repository

```bash
git clone https://github.com/SLTDigitalLab/LLM-ChatBot.git
```

- Create new python environment

```bash
python -m venv venv
```

- Activate the environment
  - For Windows

```bash
.\venv\Scripts\activate
```

- Install the required dependencies

```bash
pip install -r requirements.txt
```

- Run the FastAPI application

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

## Usage

- Open your web browser and navigate to <http://localhost:8000> to access the chatbot interface.

- Enter your message in the input field and press "Send" to receive a model-generated response.

- The response will be displayed in the chat interface.