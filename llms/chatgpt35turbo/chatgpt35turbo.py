from llms.base import LLM
from rich.text import Text
import tiktoken

class ChatGPT35Turbo(LLM):

    @property
    def token_file_name(self) -> str:
        return 'chatgpt35turbo/chatgpt35turbo.txt'

    @property
    def cost_per_token(self) -> float:
        return 0.002 / 1000

    def count_tokens(self, text: str) -> int:
        enc = tiktoken.get_encoding("cl100k_base")
        tokenized_text = enc.encode(text)
        return len(tokenized_text)

    def __rich__(self) -> Text:
        return Text(f"ChatGPT35Turbo: Token File Name = {self.token_file_name}, Cost Per Token = {self.cost_per_token}")
