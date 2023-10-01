import tiktoken

def count_tokens(text):
    enc = tiktoken.get_encoding("cl100k_base")
    tokenized_text = enc.encode(text)
    return len(tokenized_text)

if __name__ == "__main__":
    example_text = "your text here"
    num_tokens = count_tokens(example_text)
    print(f"The text has {num_tokens} tokens.")
