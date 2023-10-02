# llms/agent/agent.py
import logging
from llms.factory import llm_factory

class Agent:
    def __init__(self, llm_identifier: str):
        self.llm = llm_factory(llm_identifier)
        self.logger = logging.getLogger(__name__)

    def __rich__(self) -> str:
        llm_info = str(self.llm)
        return f"Agent Information:\nLLM: {llm_info}"

    def get_response(self, prompt: str) -> str:
        try:
            # Update tokens for the prompt
            self.llm.update_token_dict(prompt)

            # Generate the response; if your LLM has a generate_response method, use it.
            # If not, replace with appropriate code to generate a response.
            response = self.llm.generate_response(prompt) if hasattr(self.llm, 'generate_response') else "Dummy Response"

            # Log the response
            logging.info(f"Generated response: {response}")

            # Update tokens for the generated response
            self.llm.update_token_dict(response)
            
            return response

        except Exception as e:
            self.logger.error(f"Failed to get response: {e}")
            return "Error generating response."
