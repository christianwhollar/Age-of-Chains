from llms.base import LLM
from rich.text import Text
import tiktoken

class ChatGPT4(LLM):

    @property
    def token_file_name(self) -> str:
        return 'chatgpt4/chatgpt4.txt'

    @property
    def cost_per_token(self) -> float:
        return 0.06 / 1000

    def count_tokens(self, text: str) -> int:
        enc = tiktoken.get_encoding("cl100k_base")
        tokenized_text = enc.encode(text)
        return len(tokenized_text)

    def __rich__(self) -> Text:
        return Text(f"ChatGPT4: Token File Name = {self.token_file_name}, Cost Per Token = {self.cost_per_token}")
