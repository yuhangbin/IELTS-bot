from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from .llm import LLMInterface

class IELTSChain:
    def __init__(self):
        self.llm = LLMInterface()

    def create_chain(self, template):
        prompt = PromptTemplate(template=template, input_variables=["question"])
        return LLMChain(llm=self.llm.llm, prompt=prompt)

    def run_chain(self, chain, context):
        return chain.invoke(input=context)  # Pass 'input' argument

    def reading_chain(self):
        template = """
        You are an IELTS tutor specializing in the Reading section. Use the following question to provide a helpful response:

        Question: {question}

        Provide a detailed explanation and guidance for the IELTS Reading task:
        """
        return self.create_chain(template)

    def listening_chain(self):
        template = """
        You are an IELTS tutor specializing in the Listening section. Use the following question to provide a helpful response:

        Question: {question}

        Provide a detailed explanation and guidance for the IELTS Listening task:
        """
        return self.create_chain(template)

    def speaking_chain(self):
        template = """
        You are an IELTS tutor specializing in the Speaking section. Use the following question to provide a helpful response:

        Question: {question}

        Provide a detailed explanation and guidance for the IELTS Speaking task:
        """
        return self.create_chain(template)

    def writing_chain(self):
        template = """
        You are an IELTS tutor specializing in the Writing section. Use the following question to provide a helpful response:

        Question: {question}

        Provide a detailed explanation and guidance for the IELTS Writing task:
        """
        return self.create_chain(template)
