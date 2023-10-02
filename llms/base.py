from abc import ABC, abstractmethod
from rich.console import Console
import os
import json
import logging

class LLM(ABC):
    
    @property
    @abstractmethod
    def token_file_name(self) -> str:
        """Abstract property for the token file name."""
        pass

    @property
    def token_file_path(self) -> str:
        """Returns the full path of the token file."""
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), self.token_file_name)

    @property
    @abstractmethod
    def cost_per_token(self) -> float:
        """Abstract property for the cost per token."""
        pass

    @abstractmethod
    def count_tokens(self, text: str) -> int:
        """Abstract method to count tokens in a text."""
        pass

    def update_token_dict(self, prompt: str):
        """Update the token count and total price in a token file."""
        if os.path.exists(self.token_file_path):
            try:
                with open(self.token_file_path, 'r') as token_dict_file:
                    data = json.load(token_dict_file)
                data['total_tokens'] = data.get('total_tokens', 0) + self.count_tokens(prompt)
                data['price'] = data['total_tokens'] * self.cost_per_token
                with open(self.token_file_path, 'w') as token_dict_file:
                    json.dump(data, token_dict_file, indent=4)
            except Exception as e:
                logging.error(f"Error updating token dict: {e}")
        else:
            data = {
                'total_tokens': self.count_tokens(prompt),
                'price': self.cost_per_token
            }
            with open(self.token_file_path, 'w') as token_dict_file:
                json.dump(data, token_dict_file, indent=4)
