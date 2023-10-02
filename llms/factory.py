from llms.chatgpt35turbo.chatgpt35turbo import ChatGPT35Turbo
from llms.chatgpt4.chatgpt4 import ChatGPT4

def llm_factory(identifier: str):
    if identifier == 'chatgpt35turbo':
        return ChatGPT35Turbo()
    elif identifier == 'chatgpt4':
        return ChatGPT4()
    else:
        raise ValueError(f"Invalid LLM identifier: {identifier}")
