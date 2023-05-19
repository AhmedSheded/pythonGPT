# pythonGPT

ChatGPT Requests Module

The ChatGPT Requests module is a Python package that provides a convenient interface for making requests to the ChatGPT language model. It abstracts away the complexity of interacting with the model's API, allowing developers to easily integrate ChatGPT into their applications.

Key Features:
- Simple API: The module provides a high-level API that simplifies the process of sending messages and receiving responses from the ChatGPT model.
- Stateful Conversations: It supports stateful conversations, enabling users to have multi-turn interactions by maintaining context across messages.
- Customization Options: Developers can customize various aspects, such as the system prompt, temperature, and maximum response length, to fine-tune the behavior of the model.
- Error Handling: The module includes robust error handling to gracefully handle API errors and timeouts, ensuring a reliable integration.

Usage Example:
```python
from pythonGPT import PythonGPT

chatgpt = ChatGPT(api_key='your-api-key')

# Start a conversation
chatgpt.begin_conversation()

# Send a message and receive a response
response = chatgpt.send_message('Hello, how are you?')
print(response['message']['content'])

# Continue the conversation with additional messages
response = chatgpt.send_message('I have a question for you.')
print(response['message']['content'])

# End the conversation
chatgpt.end_conversation()

