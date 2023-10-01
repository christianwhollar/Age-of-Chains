from abc import ABC, abstractmethod

class LLM(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    @property
    def token_file_path(self):

    @abstractmethod
    def count_tokens(self):

    @abstractmethod
    def update_token_file(self):
    
    @abstractmethod
    def update_token_price(self):
    
    def read_token_file(self):

    def update_token_file(self):
        

# class GPT3.5Turbo(LLM):
