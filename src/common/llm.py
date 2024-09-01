from langchain.llms import Ollama

class LLMInterface:
    def __init__(self):
        self.llm = Ollama(model="llama3.1")

    def generate(self, prompt):
        return self.llm(prompt)
