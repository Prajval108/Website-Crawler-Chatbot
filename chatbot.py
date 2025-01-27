from litellm import completion
from environment import get_config
import os

class ChatBot:
    def __init__(self):
        self.config = get_config()
        os.environ['GROQ_API_KEY'] = self.config["api_key"]
        self.context = None
        self.conversation_history = []

    def load_context(self, context):
        self.context = context

    def get_response(self, user_input):
        prompt = f"Context:\n{self.context}\n\nConversation history:\n"
        for history in self.conversation_history:
            prompt += f"User: {history['user']}\nBot: {history['bot']}\n"
        prompt += f"User: {user_input}\nBot:"
        
        response = completion(
            model= self.config["model_id"],
            messages=[{"role": "user", "content": prompt}],
        )
        
        bot_response = response.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
        
        self.conversation_history.append({"user": user_input, "bot": bot_response})
        return bot_response
