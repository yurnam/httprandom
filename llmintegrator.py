from ollama import Client

class LLMIntegrator:
    def __init__(self):
        self.client = Client(host = "http://192.168.19.128")
        self.model_name = "granite4:latest"

    def generate_response(self, prompt):
        messages = {"role": "user", "content": prompt}
        response = self.client.chat(model=self.model_name, messages=[messages])
        return response ['message'] ['content']


